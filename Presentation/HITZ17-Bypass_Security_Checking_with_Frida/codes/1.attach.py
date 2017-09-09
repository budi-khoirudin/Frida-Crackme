# Various way to attach to a process.
#
# Run: python call.py 

import frida
import sys

def main():
    # Attach to process on local machine
    session = frida.attach("processname")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        session.close()

    # Attach to process on remote machine (with frida server)
    device  = frida.get_remote_device()
    session = device.attach("processname")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        session.close()

    # Attach to device (with frida server)
    device  = frida.get_usb_device()
    session = device.attach("processname")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        session.close()

    # Attach to the front app (of mobile application)
    device  = frida.get_remote_device()
    session = device.get_frontmost_application()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        session.close()

    # Enumerate devices and attach the app on the last device
    manager = frida.get_device_manager()
    device  = manager.enumerate_devices()[-1]
    session = device.attach("processname")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        session.close()

if __name__ == '__main__':
    main()