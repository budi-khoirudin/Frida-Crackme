# Create and RPC endpoint which can be used in host and executed by the frida
#
# Run: python rpc.py 

import frida
import sys

def main():
    # Attach on running process
    session = frida.attach("f.exe")

    # Instrumentation script 
    script = session.create_script("""
    'use strict';

    rpc.exports = {
        disassemble(address) {
            return Instruction.parse(ptr(address)).toString();
        }
    };
    """)

    # Load the script
    script.load()

    # Use exported RPC
    api    = script.exports
    result = api.disassemble("0x401570")
    print(result)

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

    