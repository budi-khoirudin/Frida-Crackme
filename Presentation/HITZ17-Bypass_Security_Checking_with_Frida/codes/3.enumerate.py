# Attach on running process then enumerate the modules and exported functions
#
# Run: python enumerate.py 
from __future__ import print_function
import frida

def on_message(message, data):
    print(message)

def main():
    # Attach on running process
    session = frida.attach("f.exe")

    # Modules can be enumerated from the session, or from javascript
    modules = session.enumerate_modules()
    for module in modules:
        print('module name: %s' % (module.name))
        export_funcs = module.enumerate_exports()
        print("\tfunc_name\tRVA")
        
        for export_func in export_funcs:
            print("\t%s\t%s" % (export_func.name, hex(export_func.relative_address)))

if __name__ == '__main__':
    main()