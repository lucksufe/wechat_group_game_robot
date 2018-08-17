import json
import time
import random

PATH_DICTIONARY = {'test':'quiz/test.json'}

class Quiz:
    def __init__(self, quiz_type = "test", quiz_num = 5):
        self.quiz_type = quiz_type
        self.quiz_num = quiz_num
        self.load_json(PATH_DICTIONARY[self.quiz_type])
        self.generate_quiz_index()        
        self.loop_run()

    def load_json(self, filepath):
        with open(filepath, "r") as quiz_file:
            data = json.loads(quiz_file.read())
            self.data = data

    def generate_quiz_index(self):
        self.quiz_indices = [random.randint(0, len(self.data)-1) for i in range(self.quiz_num)]

    def loop_run(self):
        for i in range(self.quiz_num):            
            self.mk_subQ(self.data[self.quiz_indices[i]])

    def mk_subQ(self, quiz_content):
        SubQ(quiz_content, self)

    def finish_subQ(self, user):
        pass

class SubQ:
    def __init__(self, content, quiz, life_time = 60):
        self.data = content
        self.life_time = life_time
        self.quiz = quiz
        print(content)

    def answer(self, text, user):
        if text == self.data["answer"]:
            self.correct(user)

    def give_hint(self):
        print(self.data["hint"][0])

    def correct(self, user):
        self.quiz.finish_subQ(user)

q = Quiz()


