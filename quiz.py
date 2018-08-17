import json
import time

PATH_DICTIONARY = {'test':'quiz/test.json'}

class Quiz:
    def __init__(self, quiz_type = "test"):
        self.quiz_type = quiz_type
        self.load_json(PATH_DICTIONARY[self.quiz_type])

    def load_json(self, filepath):
        with open(filepath, "r") as quiz_file:
            data = json.loads(quiz_file.read())
            self.data = data

    def generate_quiz_index(self):
        pass

    def loop_run(self, quiz_num = 5):
        pass

    def mk_subQ(self):
        # SubQ(self, )
        pass

    def finish_subQ(self, user):
        pass

class SubQ:
    def __init__(self, content, quiz, life_time = 60):
        self.data = content
        self.life_time = life_time
        self.quiz = quiz

    def answer(self, text, user):
        if text == self.data["answer"]:
            self.correct(user)

    def give_hint(self):
        print(self.data["hint"][0])

    def correct(self, user):
        self.quiz.finish_subQ(user)

q = Quiz()


