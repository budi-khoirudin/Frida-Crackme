import frida
import sys

def main():
    # Attach on running process
    session = frida.attach("encrypt_file.exe")

    addr = 0

    # Address is in hex form
    if len(sys.argv) > 1:
        addr = int(sys.argv[1], 16)
    else:
        addr = int(input("Address: "), 16)

    # Instrumentation script (0x401570)
    # Hook to native function on certain address ex: ptr("0x123456")
    # returning void
    # with list of arguments ['int']
    script_src = """
    Interceptor.attach(ptr("%s"), {
        onEnter: function(args) {
            var buffer = Memory.readUtf8String(args[0]);
            console.log(buffer);
        }
    });
    """
    script = session.create_script(script_src % addr)

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