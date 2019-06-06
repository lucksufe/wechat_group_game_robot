import json

ANSWER = []
# RESERVED = ['耨', '套', '糗', '卯', '润', '轴', '髓', '遗', '胎']
RESERVED = []


def not_in_answer(idiom_hint):
    if type(idiom_hint) == str:
        return True
    for idiom in ANSWER:
        if idiom['word'] == idiom_hint['word'] or idiom_hint['word'][-1:] in RESERVED:
            return False
    return True


def find_key(idiom_hint):
    if type(idiom_hint) == str:
        return idiom_hint[-1:]
    return idiom_hint['word'][-1:]


def find_pinyin(idiom_hint, is_first):
    if type(idiom_hint) == str:
        return
    py_arr = idiom_hint['pinyin'].split(' ')
    if is_first:
        return py_arr[0]
    else:
        return py_arr[len(py_arr)-1]


def next_idiom(idiom_dictionary, idiom_word):
    for idiom_single in idiom_dictionary:
        if idiom_single['word'][:1] == find_key(idiom_word) and not_in_answer(idiom_single):
            print(idiom_single['word'])
            # print(idiom_single)
            return idiom_single
    for idiom_single in idiom_dictionary:
        if find_pinyin(idiom_single, True) == find_pinyin(idiom_word, False) and not_in_answer(idiom_single):
            print(idiom_single['word'])
            # print(idiom_single)
            return idiom_single


def loop(idiom_dictionary, idiom_word, num=10):
    while num > 0:
        if idiom_word is None:
            del ANSWER[-1:]
            RESERVED.append(ANSWER[len(ANSWER)-1]['word'][-1:])
            idiom_word = ANSWER[len(ANSWER)-2]
            del ANSWER[-1:]
        idiom_word = next_idiom(idiom_dictionary, idiom_word)
        ANSWER.append(idiom_word)
        num -= 1
        print(num)


def start(idiom_word):
    with open('idiom.json', 'rb') as idiom_file:
        idiom_content = json.load(idiom_file)
        loop(idiom_content, idiom_word, 10000)
        print(len(ANSWER))
        print(RESERVED)


if __name__ == '__main__':
    start('星')
    # print(ANSWER)
