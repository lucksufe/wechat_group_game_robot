from wxpy import *
from idiom import start

USER_NAME = ''
USER_NAME_SELF = ''
MSG_OUTPUT = []
bot = Bot()
bot.enable_puid()
my_group = bot.groups().search('久别无恙')[0]
# my_friend = bot.friends().search('')[0]
dog = ensure_one(my_group.search('王二狗'))


@bot.register(my_group)
def reply_group(msg):
    print(msg.text)
    if msg.member == dog and '第1条' in msg.text:
        results = start(msg.text[-2:-1])
        for res in results:
            msg.sender.send(res['word'])


bot.join()


