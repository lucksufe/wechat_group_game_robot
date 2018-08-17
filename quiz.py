import json
import time
import random
from fake_robot import *

PATH_DICTIONARY = {'test': 'quiz/test.json'}


class Quiz:
    def __init__(self, register, quiz_type="test", quiz_num=5):
        self.register = register
        self.quiz_type = quiz_type
        self.quiz_num = quiz_num
        self.should_continue = True
        self.data = {}
        self.sub = None
        self.quiz_indices = []
        self.champions = []
        self.load_json(PATH_DICTIONARY[self.quiz_type])
        self.generate_quiz_index()        
        self.loop_run()
        print(self.final_score())

    def load_json(self, file):
        with open(file, "r", encoding='UTF-8') as quiz_file:
            data = json.loads(quiz_file.read())
            self.data = data

    def generate_quiz_index(self):
        self.quiz_indices = [random.randint(0, len(self.data)-1) for _ in range(self.quiz_num)]

    def loop_run(self):
        for i in range(self.quiz_num):            
            self.mk_sub_q(self.data[self.quiz_indices[i]])
            self.wait_finish()

    def wait_finish(self):
        while not self.should_continue:
            self.fetch_answer()
            time.sleep(1)

    def mk_sub_q(self, quiz_content):
        self.sub = SubQ(quiz_content, self)
        self.should_continue = False

    def finish_sub_q(self, user):
        self.quiz_num -= 1
        self.should_continue = True
        self.champions.append(user)

    def final_score(self):
        if self.quiz_num > 0:
            return None
        score_map = {}
        for c in self.champions:
            score_map[c] = score_map.get(c, 0) + 1
        return score_map

    def receive(self, answer, user):
        print('{0} guess it is {1}'.format(user, answer))
        self.sub.answer(answer, user)

    def fetch_answer(self):
        ans, user = self.register.spawn()
        self.receive(ans, user)


class SubQ:
    def __init__(self, content, quiz, life_time=60):
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
        self.quiz.finish_sub_q(user)


fake = FakeRobot()
q = Quiz(fake)
# while q.final_score():
#     print('---')
#     time.sleep(3)

# print(q.final_score())

