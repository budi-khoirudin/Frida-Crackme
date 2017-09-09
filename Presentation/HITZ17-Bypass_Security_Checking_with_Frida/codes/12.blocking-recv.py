# Send and receive data to and from instrumented process.
#
# Run: python blocking-recv.py 

import frida
import sys

script = None

def on_message(message, data):
    print(message)
    val = int(message['payload'])
    script.post( { 'type':'input', 'payload':str(val * 2) } )

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
    Interceptor.attach(ptr("%s"), {
        onEnter: function(args) {
            send(args[0].toInt32());
            var op = recv('input', function(value) {
                args[0] = ptr(value.payload);
            });
            op.wait();
        }
    });
    """ % addr)

    # Set a callback, when frida is sending a string, we print it out
    script.on('message', on_message)

    # Load the script
    script.load()

    script.post( { 'magic' : 135 } )
    script.post( { 'magic' : 135 } )

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

    