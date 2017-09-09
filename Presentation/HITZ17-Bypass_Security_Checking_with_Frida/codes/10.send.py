# Send and receive data to and from instrumented process.
#
# Run: python send.py 

import frida
import sys

def on_message(message, data):
    print(message)

def main():
    # Attach on running process
    session = frida.attach("f.exe")

    # Instrumentation script 
    # Send message to host
    # Two events generated: send event, error event.
    script = session.create_script("""
    send({
        user: {
            name: 'Xathrya.ReversingID'
        },
        key: '1234'
    });

    oops;
    """)

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