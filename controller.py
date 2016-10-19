from test import test

class controller:
    def __init__(self):
        self.t = test()

        self.setup()

    def setup(self):
        enteredText=raw_input('Please enter some text:\n')

        # print(">>> User Entered: {}").format(enteredText)
        self.t.example()
