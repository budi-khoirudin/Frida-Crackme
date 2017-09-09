var RtlAllocateHeapAddr = Module.findExportByName('ntdll.dll', 'RtlAllocateHeap');
console.log('RtlAllocateHeap   address: ' + RtlAllocateHeapAddr.toString());

var RtlFreeHeapAddr     = Module.findExportByName('ntdll.dll', 'RtlFreeHeap');
console.log('RtlFreeHeap       address: ' + RtlFreeHeapAddr.toString());

var RtlReAllocateHeapAddr = Module.findExportByName('ntdll.dll', 'RtlReAllocateHeap');
console.log('RtlReAllocateHeap address: ' + RtlReAllocateHeapAddr.toString());

Interceptor.attach(RtlAllocateHeapAddr, {
	onEnter(args) {
		console.log('RtlAllocateHeap called from ' + this.returnAddress.sub(6).toString());
		console.log('HeapHandle: ' + args[0].toString());
		console.log('Flags: ' + args[1].toString());
		console.log('Size: ' + args[2].toString());
	}, 
	onLeave(retval) {
		console.log('[+] Returned address: ' + retval.toString());
		console.log('---------------------');
	}
});

Interceptor.attach(RtlFreeHeapAddr, {
	onEnter(args) {
		console.log('RtlFreeHeap called from ' + this.returnAddress.sub(6).toString());
		console.log('HeapHandle: ' + args[0].toString());
		console.log('Flags: ' + args[1].toString());
		console.log('HeapBase: ' + args[2].toString());
	}, 
	onLeave(retval) {
		console.log('---------------------');
	}
});

Interceptor.attach(RtlReAllocateHeapAddr, {
	onEnter(args) {
		console.log('RtlReAllocateHeap called from ' + this.returnAddress.sub(6).toString());
		console.log('HeapHandle: ' + args[0].toString());
		console.log('Flags: ' + args[1].toString());
		console.log('Pointer: ' + args[2].toString());
		console.log('Size: ' + args[3].toString());
	}, 
	onLeave(retval) {
		console.log('[+] Returned address: ' + retval.toString());
		console.log('---------------------');
	}
});