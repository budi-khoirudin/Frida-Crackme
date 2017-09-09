# Send and receive data to and from instrumented process.
#
# Run: python recv.py 

import frida
import sys

def on_message(message, data):
    print(message)

def main():
    # Attach on running process
    session = frida.attach("f.exe")

    # Instrumentation script 
    # Receive message from host and handle it on handleMessage
    script = session.create_script("""
    'use strict';

    var i = 2;

    function handleMessage(message)
    {
        send(message.magic * i);
        i++;
        recv(handleMessage);
    }
    recv(handleMessage);
    """)

    # Set a callback, when frida is sending a string, we print it out
    script.on('message', on_message)

    # Load the script
    script.load()

    script.post( { 'magic' : 135 } );
    script.post( { 'magic' : 135 } );

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