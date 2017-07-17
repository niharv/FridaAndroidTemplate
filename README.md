# FridaAndroidTemplate
Python template for injecting into Android apps using Frida

For native:

jscode = """
Interceptor.attach(Module.findExportByName('native-lib.so','x'), {
    onEnter: function(args) {
        send(Memory.readUtf8String (args [1]));
    },
    onLeave: function(retval){
    }
});
"""
