'''This is the HelloWorld plugin.
Can do noting!'''

class HelloWorld:
    def __init__(self):
        pass

    def activate(self, shell):
        print ("Hello World Activated")

    def deactivate(self, shell):
        print ("Hello World Deactivated")
