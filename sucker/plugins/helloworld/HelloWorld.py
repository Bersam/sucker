'''HelloWorld plugin for testing
sucker plugin engine'''

class HelloWorld:
    def __init__(self):
        pass

    def activate(self, shell):
        print ("Fuck World!")

    def deactivate(self, shell):
        print ("Hello World Deactivated")
