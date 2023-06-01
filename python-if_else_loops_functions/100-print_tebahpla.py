#!/usr/bin/python3
for charac in reversed(range(97, 123)):
    print("{:c}".format(charac if (charac % 2 == 0) else (charac - 32)))
