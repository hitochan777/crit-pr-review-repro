"""Simple application entry point."""
import sys
from src.utils import greet, format_message


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    name = args[0] if args else "world"
    message = greet(name)
    print(format_message(message))
    return 0


if __name__ == "__main__":
    sys.exit(main())
