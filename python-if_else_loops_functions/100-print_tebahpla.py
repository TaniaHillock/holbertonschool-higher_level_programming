#!/usr/bin/python3
for chara in reversed(range(97, 123)):
    print("{:c}".format(chara if (chara % 2 == 0) else (chara - 32)), end='')
    
