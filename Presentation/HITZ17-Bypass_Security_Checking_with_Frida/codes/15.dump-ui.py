# Launch and spy on iOS app
#
# Run: python dump-ui.py 

import frida
import sys

session = None

def on_message(message):
    print(message.payload['ui'])
    session.detach()
    sys.exit(0)

def main():
    # Connect to device
    device = frida.get_usb_device()

    # Spawn the target and save it as pid
    app    = device.get_frontmost_application()

    # Attach to pid
    session = frida.attach(app.id)

    # Instrumentation script 
    script = session.create_script("""
    'use strict';

    ObjC.schedule(ObjC.mainQueue, () => {
        const window = ObjC.classes.UIWindow.keyWindow();
        const ui     = window.recursiveDescription().toString();
        send( { ui: ui } );
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

    