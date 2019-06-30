from urllib import request  # 从urllib包中引入request模块
import time  # 引入time模块
import os
import pygame

kill_desktop = True

pygame.mixer.init()
i=0
b=0
blist = []
while True:
    try:
        # 调用接口获取微信端最近发送的一条消息，接口地址为http://api.itmojun.com/pc/cmd/get，该接口带有一个参数id，表示当前电脑ID
        # 微信端通过这个电脑ID区分不同电脑
        # urlopen函数的返回值为一个文件对象，可以调用其read方法获取接口的返回数据（bytes类型）
        r = request.urlopen("http://api.itmojun.com/pc/cmd/get?id=liuhui").read()

        # 将bytes类型数据转换为str类型
        msg = r.decode("gbk")

        # 如果接收到一条消息，msg将不是空字符串，否则为空字符串
        if msg != "":
            print(msg)
            if "亚索" in msg:
                # 强制结束LOL
                os.system("taskkill -f -im chrome.exe")
            elif '关机' in msg:
                # 关机
                # os.system("shutdown -s -t 0")
                pass
            elif '重启' in msg:
                # 重启
                # os.system("shutdown -r -t 0")
                pass
            elif '骚扰' in msg:
                os.system("explorer http://www.pangshe.com")  # 强制弹出网站
            elif '桌面' in msg:
                if kill_desktop:
                    os.system("taskkill -f -im explorer.exe")  # 强制结束桌面进程
                else:
                    os.system(r"C:\Windows\explorer.exe")  # 恢复桌面

                kill_desktop = not kill_desktop
            #elif '播放' in msg:
                # 播放一首歌
                # 打开指定的音乐文件，并取个名字代表它
                # ctypes.windll.winmm.mciSendStringW("open D:\\dj.mp3 alias sdj", None, 0, None)
                # 播放打开的音乐
                # ctypes.windll.winmm.mciSendStringW("play sdj", None, 0, None)
                # disk = msg.split(" ")
                # print(len(disk))
                # print(msg)
                # for b in range(len(disk)-1):
                #     blist.insert(b,disk[b+1])
                # print(blist)
                # pygame.mixer.music.load(r"D:\Music\%s.mp3"%(blist[0]))
                # pygame.mixer.music.play()
                # blist.pop(0)
            elif '播放' == msg[0:2]:
                music_name = msg[2:]
                try:
                    pygame.mixer.music.load(r"D:\Music\%s.mp3" % music_name)
                    pygame.mixer.music.play()
                except:
                    print("not find")

            elif '切歌' in msg:
                # 播放一首歌
                # 打开指定的音乐文件，并取个名字代表它
                # ctypes.windll.winmm.mciSendStringW("open D:\\dj.mp3 alias sdj", None, 0, None)
                # 播放打开的音乐
                # ctypes.windll.winmm.mciSendStringW("play sdj", None, 0, None)
                # print(blist)
                # print(blist[0])
                # pygame.mixer.music.load(r"D:\Music\%s.mp3"%(blist[0]))
                # blist.pop(0)
                # pygame.mixer.music.play()
                pass
            elif '暂停' in msg:
                ctypes.windll.winmm.mciSendStringW(r"pause s", None, 0, None)
                pygame.mixer.music.pause()
            elif "继续" in msg:
                pygame.mixer.music.unpause()
            elif '停止' in msg:
                ctypes.windll.winmm.mciSendStringW(r"close s", None, 0, None)
                pygame.mixer.music.stop()

                
            time.sleep(3)  # 休眠3秒，避免接收到重复的消息，因为微信端发送的每条消息都会在服务器上暂存3秒
        else:
            time.sleep(1)  # 如果没有接收到消息，就休眠1秒，避免快速频繁调用接口导致服务器压力太大
    except Exception as e:
        print(e)
    except:  # 捕获处理try块中的代码产生的任何异常
        pass  # 空语句，啥也不干，为了满足Python语法规则
        time.sleep(1)
        
