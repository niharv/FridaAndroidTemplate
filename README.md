# FridaAndroidTemplate
Python template for injecting into Android apps using Frida

## For native:

jscode = """
Interceptor.attach(Module.findExportByName('native-lib.so','x'), {
    onEnter: function(args) {
        send(Memory.readUtf8String (args [1]));
    },
    onLeave: function(retval){
    }
});
"""

## Frida without root
See https://www.frida.re/docs/modes/#embedded

1. Get the apk
2. Disassemble the code and add frida-gadget into the library folder (/lib, or /lib/armeabi)
3. Inject a System.loadLibrary("frida-gadget") call into the bytecode of the app before any other code is loaded. A suitable place is
   is the main application Activity initializer. Smali code to do achieve this:
   <code>const-string v0, "frida-gadget" <br>
   invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V </code>
4. Add <uses-permission android:name="android.permission.INTERNET" /> to the manifest if the app doesn't already have the INTERNET
   permission (since firda needs to use a socket communicate between server and CLI)
5. Repackage with apktool, and sign the apk. Change settings on phone to install from untrusted sources. 
