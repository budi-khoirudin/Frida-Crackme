# Trace the execution of memory allocation process.
# 
# Run: python alloc-trace.py 
from __future__ import print_function
import frida
import sys

def on_message(message, data):
    print("[M] {0} ".format(message))
    print("[D] {0} ".format(data))
    print("-----------")

def main():
    # Attach on running process
    session = frida.attach("alloc.exe")
    
    # Instrumentation script 
    # Using Interceptor to attach to a function
    # Here we are inside a function
    with open("18.script.js") as f:
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