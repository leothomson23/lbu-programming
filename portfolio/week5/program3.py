#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("No arguments provided")
    else:
        print("The shortest argument is: ", min(sys.argv[1:]))