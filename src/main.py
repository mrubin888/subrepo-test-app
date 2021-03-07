from src.some_other import SOME_OTHER_CONSTANT
from subrepo_test_lib.src.test_lib import SOME_CONSTANT


def do_something():
    print("Hello world!")
    print(f"Some constant: {SOME_CONSTANT}")
    print(f"Some other constant: {SOME_OTHER_CONSTANT}")


if __name__ == "__main__":
    do_something()
