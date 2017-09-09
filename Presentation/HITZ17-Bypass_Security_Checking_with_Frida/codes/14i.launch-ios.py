# Launch and spy on iOS app
#
# Run: python launch-ios.py 
# or use "frida-trace -U -f com.android.vending -I libcommonCrypto.dylib"

import frida
import sys

device = None
pid    = None

def on_message(message):
    if message.type == 'send' and message.payload['event'] == 'ready':
        device.resume(pid)
    else:
        print(message)

def main():
    # Connect to device
    device = frida.get_usb_device()

    # Spawn the target and save it as pid
    pid    = device.spawn(['com.apple.Appstore'])

    # Attach to pid
    session = frida.attach(pid)

    # Instrumentation script 
    script = session.create_script("""
    Module.enumerateExports('libcommonCrypto.dylib', {
        onMatch(e) {
            if (e.type === 'function') {
                try {
                    Interceptor.attach(e.address, {
                        onEnter(args) {
                            send( { event: 'call', name: e.name } )
                        }
                    })
                } catch (error) {
                    console.log('Ignoring ' + e.name + ': ' + error.message);
                }
            }
        },
        onComplete() {
            send( { event: 'ready' } );
        }
    });
    """)

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

    