# Attach on running process and call a function with user-defined argument.
# The argument is a string that is allocated manually before passing.
# The script is embedded to this python file.
#
# Run: python stringhook.py 
from __future__ import print_function
import frida
import sys

def on_message(message, data):
    print(message)

def main():
    # Attach on running process
    session = frida.attach("hi.exe")

    addr = 0

    # Address is in hex form
    if len(sys.argv) > 1:
        addr = int(sys.argv[1], 16)
    else:
        addr = int(input("Address: "), 16)

    # Instrumentation script 
    # Hook to native function on certain address ex: ptr("0x123456")
    # returning int
    # with list of arguments ['pointer']
    script = session.create_script("""
    var st = Memory.allocUtf8String("XATHRYA!");
    var f  = new NativeFunction(ptr("%s"), 'int', ['pointer']);
    f(st);
    """ % addr)

    # Set a callback, when frida is sending a string, we print it out
    script.on('message', on_message)

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