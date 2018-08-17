from wxpy import *
import requests
import quiz
import message

USER_NAME = ''
USER_NAME_SELF = '孙斐'
MSG_OUTPUT = []
bot = Bot()
my_group = bot.groups().search('诗两行')[0]
my_friend = bot.friends().search('')[0]
tuling = Tuling(api_key='5c2d164575d249a0afc0c4e8da744132')
# print(my_friend)
# my_friend.send('测试一下')


@bot.register(my_group)
def reply_group(msg):
    # if "@" in msg.text or "非瑞克西亚" in msg.text:
    if '天气' in msg.text or '笑话' in msg.text:
        tuling.do_reply(msg)
    if USER_NAME in msg.member.name:
        MSG_OUTPUT.append(msg.text)
    print(msg)


@bot.register(my_friend)
def reply_friend(msg):
    if "笑话" in msg.text:
        tuling.do_reply(msg)
    elif "?" in msg.text or "？" in msg.text:
        tuling.do_reply(msg)
    print(msg)
        # return "received:{0}({1})".format(msg.text, msg.type)


@bot.register(bot.self, except_self=False)
def message_self(msg):
    # print(dir(msg.sender))
    # print(msg.sender.user_name, msg.sender.wxid)
    if USER_NAME_SELF in msg.sender.name:
        print('self')
    if "show" in msg.text:
        return MSG_OUTPUT
    if "@" in msg.text:
        tuling.do_reply(msg)
    return '你好'


bot.join()


