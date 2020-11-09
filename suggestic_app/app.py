import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from utils.flatten import flatten_list
from marshmallow import fields, ValidationError
from models.flatten import Flatten

# Init app
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Custom Field
class CustomFlattenField(fields.Field):
    """Custom field that validates input on integers or list."""

    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, list):
            return value
        else:
            raise ValidationError("Field should be list")


# Schema Flattem
class FlattenSchema(ma.Schema):
    items = CustomFlattenField(required=True)
    result = CustomFlattenField(required=False)

    class Meta:
        fields = ("items", "result")


# POST - Create Flatten Object
@app.route("/flatten-list", methods=["POST"])
def add_flatten():
    try:
        response = FlattenSchema().load(request.json)
        items = response["items"]
        result = flatten_list(items, [])
        logger.info(f"input items: {items}")
        logger.info(f"output result: {result}")
        flatten = Flatten(items=str(items), result=str(result))
        db.session.add(flatten)
        db.session.commit()
        return jsonify({"result": result}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400


# Run Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
