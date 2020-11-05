import logging
from utils.flatten import flatten_list

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

input_list = [1, 2, [3, 4, [5, 6], 7], 8]

r = flatten_list(input_list)
logger.info(r)
