"""Simple application entry point."""
import sys
import logging
from src.utils import greet, format_message

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    name = args[0] if args else "world"
    logger.info("Greeting target: %s", name)
    message = greet(name)
    logger.info("Generated message: %s", message)
    print(format_message(message))
    return 0


if __name__ == "__main__":
    sys.exit(main())
