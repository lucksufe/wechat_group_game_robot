import json

PATH_DICTIONARY = {'test':'quiz/test.json'}

class Quiz:
    def __init__(self, quiz_type = "test"):
        self.quiz_type = quiz_type
        self.load_json(PATH_DICTIONARY[self.quiz_type])

    def load_json(self, filepath):
        with open(filepath, "r") as quiz_file:
            data = json.loads(quiz_file.read())
            self.data = data
            
    def mk_subQ(self, answer):
        pass

class SubQ:
    def __init__(self, content):
                
q = Quiz()


