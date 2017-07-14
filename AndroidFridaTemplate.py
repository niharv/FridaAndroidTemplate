import frida, sys

def on_message(message,data):
    if message['type']=='send':
        print("[*] {0}".format(message['payload']))
    else:
        print (message)

"""Frida nagic goes into jscode"""

jscode = """
Java.perform(function() {
  var target = Java.use('class to target');
  
  //Include params in function if expected like function (param1,param2) 
  target.method.implementation = function () {
    send('We are now in method')
    
    //Modify code as you like
    
    //Include params in this call if it is expected
    this.method()
    };
});
"""

process = frida.get_usb_device().attach('[name of app to attach to]')

"""jscode is the Javascript code we intent to inject"""
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running Frida')
script.load()
sys.stdin.read()