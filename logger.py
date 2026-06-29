import logging
import os

logging.basicConfig(
    filename=os.path.join("output","execution_log.txt"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)