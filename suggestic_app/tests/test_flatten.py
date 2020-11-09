import sys
import os
import unittest
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.getcwd())

from utils.flatten import flatten_list
from models.flatten import Flatten, Base
from app import app as main


class FlattenListTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = [1, 2, [3, 4, [5, 6], 7], 8]
        self.input_list_empty = []

    def test_flatten_list_filled(self):
        response_flatten_list = flatten_list(self.input_list, [])
        self.assertListEqual(response_flatten_list, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(type(response_flatten_list), list)
        self.assertEqual(sum(response_flatten_list), 36)

    def test_flatten_list_empty(self):
        response_flatten_list = flatten_list(self.input_list_empty, [])
        self.assertListEqual(response_flatten_list, [])
        self.assertEqual(type(response_flatten_list), list)
        self.assertEqual(sum(response_flatten_list), 0)


class ORMCreateSchemaTestCase(TestCase):
    def setUp(self) -> None:
        self.engine = create_engine("sqlite:///:memory:")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_create_schema(self):
        Base.metadata.create_all(self.engine)
        self.assertTrue(Base.metadata.tables[Flatten.__tablename__].exists(self.engine))


class ORMCreateExampleDataTestCase(TestCase):
    def setUp(self) -> None:
        self.input_list = [1, 2, [3, 4, [5, 6], 7], 8]
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_create_example(self):
        response_flatten_list = flatten_list(self.input_list, [])
        flatten_saved = Flatten(
            items=str(self.input_list), result=str(response_flatten_list)
        )
        self.session.add(flatten_saved)
        self.session.commit()
        self.assertEqual(flatten_saved.result, "[1, 2, 3, 4, 5, 6, 7, 8]")
        self.assertNotEqual(flatten_saved.items, flatten_saved.result)


class ApiFlattenTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = [1, 2, [3, 4, [5, 6], 7], 8]

    def test_api_saved_data(self):
        tester = main.test_client(self)
        response = tester.post("flatten-list", json={"items": self.input_list})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertIsInstance(response.json.get("result", []), list)
        self.assertEqual(response.json.get("result", []), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(sum(response.json.get("result", [])), 36)


if __name__ == "__main__":
    unittest.main()
