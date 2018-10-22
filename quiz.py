# coding=utf-8
import json
import time
import random
from log import logger
# import sys
# reload(sys)
# sys.setdefualtencoding('utf8')
PATH_DICTIONARY = {'test': 'quiz/test.json',
                   'one_way': 'quiz/one_way.json'}


class Quiz:
    def __init__(self, register, msg_sender, quiz_type="one_way", quiz_num=5):
        self.register = register
        self.quiz_type = quiz_type
        self.quiz_num = quiz_num
        self.should_continue = True
        self.data = {}
        self.sub = None
        self.msg_sender = msg_sender
        self.quiz_indices = []
        self.champions = []
        self.load_json(PATH_DICTIONARY[self.quiz_type])
        self.generate_quiz_index()        
        self.loop_run()
        logger.info(self.final_score())
        self.register.end_activity(self.msg_sender.puid)

    def load_json(self, file):
        with open(file, "r", encoding='UTF-8') as quiz_file:
            data = json.loads(quiz_file.read())
            self.data = data

    def generate_quiz_index(self):
        # self.quiz_indices = [random.randint(0, len(self.data)-1) for _ in range(self.quiz_num)]
        self.quiz_indices = random.sample(range(0, len(self.data)), self.quiz_num)

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
        if user is None:
            self.msg_sender.send('回答超时，遗憾！')
        else:
            self.msg_sender.send('回答正确，你真棒！')

    def final_score(self):
        if self.quiz_num > 0:
            return None
        score_map = {}
        for c in self.champions:
            score_map[c] = score_map.get(c, 0) + 1
        self.msg_sender.send(generate_score(score_map))
        return score_map

    def receive(self, answer, user):
        logger.info('{0} guess it is {1}'.format(user, answer))
        self.sub.answer(answer, user)

    def fetch_answer(self):
        ans, user = self.register.spawn(self.msg_sender.puid)
        self.receive(ans, user)


class SubQ:
    def __init__(self, content, quiz, life_time=60):
        self.born_time = time.time()
        self.hint_idx = 0
        self.data = content
        self.life_time = life_time
        self.quiz = quiz
        self.quiz.msg_sender.send(content="问题: {0}".format(self.data["paragraphs"]))
        logger.info(content)

    def answer(self, text, user):
        if text == self.data["answer"]:
            self.correct(user)
        elif time.time()-self.born_time > self.life_time:
            self.correct(None)
        elif time.time()-self.born_time > 5 * self.hint_idx + 10:
            self.give_hint()        
        # elif self.life_time - (time.time()-self.born_time) <30:
        #     self.count_down()

    def give_hint(self):
        if self.hint_idx >= len(self.data["hint"]):
            return
        self.quiz.msg_sender.send(content="提示: {0}".format(self.data["hint"][self.hint_idx]))
        logger.info(self.data["hint"][self.hint_idx])
        self.hint_idx += 1

    def correct(self, user):
        self.quiz.finish_sub_q(user)

    def count_down(self):
        pass


def generate_quiz(file):
    quiz = []
    with open(file, 'r') as source:
        lines = source.readlines()
        for line in lines:
            remove_rank = line.split('.')
            if len(remove_rank)>1:
                q = line.strip('\n').replace(remove_rank[0]+'.','')
                q = q.split('?')
                if not q[1] == '驯鹿':
                    quiz.append(q)
    return quiz


def mk_quiz(content, file , tp='word'):
    json_arr = []
    for c in content:
        tmp = { 
                "hint":[],
                "answer":"",
                "paragraphs":"",
                "type":""
              }
        tmp["hint"].append('{0}个字'.format(len(c[1])))
        tmp["answer"] = c[1]
        tmp["paragraphs"] = c[0]+'?'
        tmp["type"] = tp
        json_arr.append(tmp)
    f = open(file,'w')
    f.write(json.dumps(json_arr,ensure_ascii=False)) 
    f.close()

    
def generate_score(score_map):
    output = ''
    for (k,v) in score_map.items():
        if k is not None:
            output += '{0}答对了{1}题！恭喜！！คิดถึง'.format(k,v)
    return output
# mk_quiz(generate_quiz('quiz/1'), 'quiz/one_way.json')


