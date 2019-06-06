import json

ANSWER = []
RESERVED = ['耨', '套', '糗', '卯', '润', '轴', '髓', '衰', '馁', '胎', '俗', '耶', '跬', '扃', '店', '短', '湃', '翁', '纂', '腿', '拷', '崩', '汝', '奈', '薪', '瓢', '悛', '孩', '伞', '宗', '母', '跄', '踪', '愿', '子', '赅', '然', '场', '虐', '涯', '牙', '怨', '铆', '磷', '种', '伦', '赖', '痒', '睐', '恨', '贴', '镫', '鳖', '忾', '葩', '裤', '定', '算', '纶', '冗', '乖', '盹', '散', '歹', '蜡', '乱', '色', '踵', '灾', '溃', '派', '薄', '腕', '邦', '卵', '紫', '酥', '鞅', '约', '户', '样', '脑', '痕', '妈', '磒', '命', '怪', '壮', '闩', '地', '照', '组', '该', '垢', '聩', '辣', '暖', '之', '躥', '屩', '里', '者', '虑', '爪', '腮', '丑', '税', '郭', '蒂', '李', '理', '哉', '帖', '状', '业', '佩', '珮', '私', '盟', '达', '它', '钉', '弟', '股', '俎', '燃', '灭', '递', '篡', '卉', '测', '琢', '疵', '棱', '逮', '祖', '猴', '舌', '听', '眺', '晒', '考', '策', '媚', '蘖', '檗', '梓', '俏', '幸', '影', '敌', '跳', '措', '思', '匮', '吼', '邻', '性', '鬓', '凫', '撞', '端', '盆', '丈', '骸', '仗', '杖', '姓', '苑', '律', '央', '肉', '鼐', '祥', '丝', '火', '颤', '蛇', '赵', '礼', '掌', '萌', '嶂', '轮', '辏', '缺', '堕', '下', '领', '篑', '序', '蝼', '蹙', '外', '戟', '息', '愧', '伙', '噎', '几', '答', '远', '体', '牡', '簇', '亩', '己', '法', '券', '辔', '偶', '源', '挫']


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
