#!/usr/bin/python3
import sys
if __name__ == "__main__":
    answer = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            answer += int(arg)
    print(answer)
