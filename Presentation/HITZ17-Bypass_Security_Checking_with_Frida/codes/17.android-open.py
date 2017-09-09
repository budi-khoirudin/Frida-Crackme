# Search current application and load the dex
#
# Run: python android-open.py 
from __future__ import print_function
import frida
import sys
import re

DEX_PATH    = "/data/local/tmp/test.apk"
ENTRY_FUNC  = ""
ENTRY_CLASS = ""
ARG         = ""

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

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
    # Using Interceptor to attach to a function
    # Here we are inside a function
    script = session.create_script("""
    Java.perform(function()
    {
        var currentApp = Java.use("android.app.ActivityThread").currentApplication();
        var context    = currentApplication.getApplicationContext();
        var pkgname    = context.getPackageName();
        var dexPath    = "%s";
        var entryClass = "%s";

        Java.openClassFile(dexPath).load();
        console.log("inject " + dexPath + " to " + pkgName + " successfully!");
        Java.use(entryClass).%s("%s");
        console.log("Call entry successfully!");
    })
    """ % (DEX_PATH, ENTRY_CLASS, ENTRY_FUNC, ARG))

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