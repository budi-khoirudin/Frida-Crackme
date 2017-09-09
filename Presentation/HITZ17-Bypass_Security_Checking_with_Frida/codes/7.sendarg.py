# Attach on running process and send the arguments passed to the function
#
# Run: python sendarg.py 
from __future__ import print_function
import frida
import sys

def on_message(message, data):
    print(message)

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
    # Using Interceptor to attach to a function
    # Here we are inside a function
    # send the arguments to our host
    script = session.create_script("""
    Interceptor.attach(ptr("%s"), {
        onEnter: function(args) {
            send(args[0].toInt32());
        }
    });
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