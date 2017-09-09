# Attach on running process and call a function with user-defined argument.
# The script is embedded to this python file.
#
# Run: python call.py 

import frida
import sys

def main():
    # Attach on running process
    session = frida.attach("f.exe")

    addr = 0

    # Address is in hex form
    if len(sys.argv) > 1:
        addr = int(sys.argv[1], 16)
    else:
        addr = int(input("Address: "), 16)

    # Instrumentation script 
    # Hook to native function on certain address ex: ptr("0x123456")
    # returning void
    # with list of arguments ['int']
    script = session.create_script("""
    var f = new NativeFunction(ptr("%s"), 'void', ['int']);
    f(1992);
    f(1992);
    f(1992);
    """ % addr)

    # Load the script
    script.load()

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