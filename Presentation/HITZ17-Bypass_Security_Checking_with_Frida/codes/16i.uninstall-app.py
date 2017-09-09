# Launch and spy on iOS app
#
# Run: python uinstall-app.py 

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
    const LSApplicationWorkspace = ObjC.classes.LSApplicationWorkspace;
    const onProgress = new ObjC.Block({
        reType: 'void',
        argTypes: ['object'],
        implementation: (progress) => {
            console.log('onProgress: ' + progress);
        }
    });
    function uninstall(appid) {
        const workspace = LSApplicationWorkspace.defaultWorkspace();
        return workspace.uninstallApplication_with_Options_usingBlock_(appid, null, onProgress);
    }
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

    