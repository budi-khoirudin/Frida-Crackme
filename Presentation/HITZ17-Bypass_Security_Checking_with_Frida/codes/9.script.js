// function should be exported
func_addr = Module.findExportByName("module", "export_func");
console.log("Will hook to " + func_addr);
Interceptor.attach(ptr(func_addr), {
	onEnter: function(args) {
		send("open(" + Memory.readCString(args[0]) + "," + args[1] + ")");
		args[0] = ptr("1337");
	}, 
	onLeave: function(retVal) { }
});