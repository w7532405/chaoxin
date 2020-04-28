import time
import pyperclip
import itchat

print('开始运行')
itchat.login()
# itchat.auto_login(hotReload=True)
mps = itchat.search_mps(name='答案聚集地')
userName = mps[0]['UserName']
last_string = pyperclip.paste()
while True:
    time.sleep(0.5)
    string = pyperclip.paste()
    if string != last_string and string != '':
        print('正在运行')
        itchat.send(string,toUserName = userName)
        last_string = string