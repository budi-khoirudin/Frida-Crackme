# Attach on running process then enumerate the modules
#
# Run: python enumproc.py 
from __future__ import print_function
import frida

def on_message(message, data):
    print(message)

def main():
    # Get device
    device  = frida.get_remote_device()

    # Enumerate all process on current device
    processes = device.enumerate_processes()
    for process in processes:
        print(process)
    
if __name__ == '__main__':
    main()