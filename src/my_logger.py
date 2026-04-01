import logging

logging.basicConfig(
    filename="logs/lab1_test3.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filemode="w"
)

log = logging.getLogger(__name__)
log.info("Logger initialized")
