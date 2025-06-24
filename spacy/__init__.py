class DummyDoc:
    def __init__(self):
        self.ents = []

class DummyNLP:
    def __call__(self, text):
        return DummyDoc()

def load(name):
    return DummyNLP()
