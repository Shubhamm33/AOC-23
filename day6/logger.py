import logging

logging.basicConfig(filemode='w', filename='dev.log', level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger("--AdventOfCode2023--")