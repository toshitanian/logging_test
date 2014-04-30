from test1 import a
from test2 import b
from log import setup_logging

def main():
    setup_logging()
    a()
    b()

if __name__ == "__main__":
    main()
