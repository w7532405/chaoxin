# chaoxin
学习通等软件自动获取题目答案 超安全 python脚本
## 理论上来说，这个方法只要公众号不倒，永远可以用。
## 就算公众号倒了，换个公众号就行了。而且绝无学习通不良问题
## 你明白原理就知道为什么了~
# 程序说明
这几天发现学习通课快截至了，就抓紧时间刷视频答题，但是答题每次还得 手动复制百度，用脚本或者软件的话在现在的学习通还是不要用了，以免有不良记录。所以自己写了个小python脚本
# 程序原理
使用`pyperclip` `itchat` `time`这三个包
原理是先使用`pyperclip`包获取剪切板内容
之后用`itchat`包将获取内容导入微信获取答案公众号
# 程序步骤
### 1.关注公众号 **答案聚集地**!
### 2.python安装`pyperclip` `itchat`包
打开cmd，之后使用```pip install xxx```命令安装
因为默认源太慢了，我这里使用了换豆瓣源安装
```python
pip install pyperclip -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install itchat -i https://pypi.tuna.tsinghua.edu.cn/simple/
```
### 3.使用以下代码运行程序(或下载项目中的run.py运行)
注：如果是第一次运行，用图片中即可，如果第二次运行，将注释代码替换上一行代码就行
```python
import time
import pyperclip
import itchat

print('开始运行')
itchat.login()
#itchat.auto_login(hotReload=True)
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
```
### 4.使用结果
运行run.py程序，会弹出一个图片二维码，用你的微信扫一下，之后就可以开始答题了~，我录了个演示视频
你只需复制题目，你的手机微信里面就能收到答案~

b站视频演示：https://www.bilibili.com/video/BV1Ma4y147df/

csdn带图片说明：https://blog.csdn.net/sinat_21560581/article/details/105803513
