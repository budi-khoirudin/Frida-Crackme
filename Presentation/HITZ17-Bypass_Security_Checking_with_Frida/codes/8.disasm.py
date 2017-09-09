# Attach on running process then read some bytes of a functions
# This byte array will be disassembled by capstone
#
# Run: python disasm.py 
from __future__ import print_function
from capstone import *
from capstone.x86_const import *
import frida

INSTR_LEN  = 30
INSTR_ADDR = 0x401570

def on_message(message, data):
    print(message)

def main():
    # Attach on running process
    session = frida.attach("f.exe")

    # Read some bytes from function f
    code = session.read_bytes(INSTR_ADDR, INSTR_LEN)

    # Initialize capstone
    cs = Cs(CS_ARCH_X86, CS_MODE_32)

    for instr in cs.disasm(code, INSTR_ADDR):
        print("%d\t%s\t%s" % (instr.address, instr.mnemonic, instr.op_str))

    # Delay
    # Execution is happened on other process so we need to make our script 
    # running all the way to the end
    try:
        while True:
            pass
    except KeyboardInterrupt:
        session.detach()
        sys.exit(0)

if __name__ == '__main__':
    main()