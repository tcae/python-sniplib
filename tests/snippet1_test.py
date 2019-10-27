import sys
from sniplib import snip1


def snippet1_test():
    snip1("snippet1_test - snip1")


if __name__ == "__main__":
    print(f"snippet1_test sys.path: {sys.path}")
    snip1("main snippet1_test - snip1")
    snippet1_test()
