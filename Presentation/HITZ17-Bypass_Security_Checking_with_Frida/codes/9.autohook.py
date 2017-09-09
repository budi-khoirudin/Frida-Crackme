# Attach on running process, find the address of a symbol and then hook it.
#
# Run: python autohook.py 
from __future__ import print_function
import frida
import sys

def on_message(message, data):
    print(message)

def main():
    # Attach on running process
    session = frida.attach("f.exe")

    # Instrumentation script 
    with open("9.script.js") as f:
        source = f.read()
    script = session.create_script(source)

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