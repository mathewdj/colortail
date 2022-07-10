#!/usr/bin/env python3
import sys
k = 0
try:
    for line in sys.stdin:
        print(line)
except KeyboardInterrupt:
   sys.stdout.flush()
   pass
