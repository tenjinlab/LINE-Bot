# -*-coding: utf-8 -*-
from akad.SquareService import sendMessage_args
from linepy import *
#from numba import jit
from datetime import datetime
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse, timeit, _thread
import atexit
#==============================================================================#
#f = open('bot/run.txt','r')
#ttoken = f.read()
#f.close()
#cl = LINE(ttoken) 
botStart = time.time()
cl = LINE("E-mail","Password")
print("Auth Token : " + str(cl.authToken))
#f = open('bot/token.txt','w')
#f.write(str(cl.authToken))
#f.close()
clMID = cl.profile.mid
#botStart = time.time()
oepoll = OEPoll(cl)
ban = json.load(codecs.open("bot/ban.json","r","utf-8"))
pic = json.load(codecs.open("bot/picture.json","r","utf-8"))
settings = json.load(codecs.open("bot/temp.json","r","utf-8"))
msg_dict = {}
msg_dictt = {}
restart = False
profile = cl.getProfile()
status = str(profile.statusMessage)
lock = _name = "Dorothy OS 66.3 Startup !!\n\nGlynda Module is running !!"
if lock not in status:
    profile.statusMessage = lock + status
    cl.updateProfile(profile)
else:
    pass

def restartBot():
    print ("[ INFO ] BOT RESETTED {}".format(datetime.today().strftime('%Y/%m/%d|%H/%M/%S|')))
    backupData()
    t = open('bot/run.txt','w')
    t.write(str(cl.authToken))
    t.close()
    for x in msg_dictt:
        cl.deleteFile(msg_dictt[x]["object"])
        del msg_dict[x]
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        json.dump(settings,codecs.open('bot/temp.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(pic,codecs.open('bot/picture.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    with open("bot/errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invaliod mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
            textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def helpmessage():
    helpMessage = """〘 Onwer-Only 〙
💮〘 Help 〙💮
☞ Help 查看指令
💮〘 Status 〙 💮
☞ Restart 重新啟動
☞ Save 儲存設定
☞ Runtime 運作時間
☞ Speed 速度
☞ Set 設定
☞ About 關於發送者
💮〘 Set Up 〙💮
☞ AutoAdd On/Off 自動加入
☞ AutoLeave On/Off 離開副本
☞ AutoRead On/Off 自動已讀
☞ Prompt On/Off 群組狀況提示
☞ ReRead On/Off 查詢收回
☞ Pro On/Off 所有保護
☞ Protect On/Off 踢人保護
☞ QrProtect On/Off 網址保護
☞ Invprotect On/Off 邀請保護
☞ Getinfo On/Off 取得友資詳情
☞ Detect On/Off 標註偵測
☞ Savelolipic On/Off 帥哥圖儲存
☞ Savepic On/Off 妹子圖儲存
☞ Savewallpic On/off 桌布儲存
☞ Timeline On/Off 文章預覽
💮〘 Self / Friend 〙💮
☞ Me 我的連結
☞ Mymid 我的mid
☞ Name @ 名字[發訊者/Tag]
☞ Bio @ 個簽[發訊者/Tag]
☞ Picture @ 頭貼[發訊者/Tag]
☞ Cover @ 封面[發訊者/Tag]
☞ Mid @ 查mid[友資/Tag]
☞ Contact: 以mid查友資
☞ Info @ 查看資料
💮〘 Blacklist 〙💮
☞ Ban [@/:] 加入黑單[友資/Tag/MID]
☞ Unban [@/:] 取消黑單[友資/Tag/MID]
☞ Keepban [times] 連續加入黑單
☞ Keepunban [times] 連續取消黑單
☞ Banlist 查看黑單
☞ Gbanlist 查看本群黑單
☞ CleanBan 清空黑單
☞ Kickban 踢除黑單
💮〘 Group Related 〙💮
☞ Link On/Off 網址開啟/關閉
☞ Link 查看群組網址
☞ GroupList 所有群組列表
☞ GroupMemberList 成員名單
☞ GroupInfo 群組資料
☞ Cg: 以群組ID查詢資料
☞ Gn [text] 更改群名
☞ Tk @ 標註踢人
☞ Zk 踢出0字元
☞ Inv (mid) 透過mid邀請
☞ Cancel 取消所有邀請
☞ Ri @ 來回機票
☞ Tagall 標註全體
☞ Zc 發送0字元友資
☞ Zt 標注0字元
☞ Setread 已讀點設置
☞ Cancelread 取消偵測
☞ Checkread 已讀偵測
☞ Gbc: 群組廣播(可限制人數)
☞ Fbc: 好友廣播
☞ Bye 機器退群(確認請打Y)
💮〘 Administraor 〙💮
☞ Adminadd @ 新增權限
☞ Admindel @ 刪除權限
☞ Adminlist 查看權限表
💮〘 Other 〙💮
☞ Ver 當前版本查詢
☞ Say [text times] 重複講話
☞ Tag @ [times] 重複標人
☞ Rls 本日運勢
☞ bomb 彩蛋
☞ Rlb 拉霸一次
☞ 帥哥 抽帥哥
☞ 妹子 抽妹子
☞ wall 抽桌布
☞ Kernel 核心版本查詢"""
    return helpMessage
def helpm():
    helpM = """〘 Administrator only 〙
💮〘 Help 〙💮
☞ Help 查看指令
☞ Runtime 運作時間
☞ Speed 速度
☞ Set 設定
☞ About 關於發送者
☞ Save 儲存設定
💮〘 Self / Friend 〙💮
☞ Me 我的連結
☞ Mymid 我的mid
☞ Name @ 名字[發訊者/Tag]
☞ Bio @ 個簽[發訊者/Tag]
☞ Picture @ 頭貼[發訊者/Tag]
☞ Cover @ 封面[發訊者/Tag]
☞ Mid @ 查mid[友資/Tag]
☞ Contact: 以mid查友資
☞ Info @ 查看資料
💮〘 Group Related 〙💮
☞ Link On/Off 網址開啟/關閉
☞ Link 查看群組網址
☞ GroupList 所有群組列表
☞ GroupMemberList 成員名單
☞ GroupInfo 群組資料
☞ Gn (文字) 更改群名
☞ Tagall 標註全體
☞ Zc 發送0字元友資
☞ Zt 標注0字元
☞ Setread 已讀點設置
☞ Cancelread 取消偵測
☞ Checkread 已讀偵測
☞ Bye 機器退群(確認請打Y)
💮〘 Other 〙💮
☞ Ver 當前版本查詢
☞ Say [內容 次數] 重複講話
☞ Tag @ [次數] 重複標人
☞ Adminlist 查看權限表
☞ Banlist 查看黑單
☞ Banmidlist 查看黑單者mid
☞ bomb 彩蛋
☞ Rls 本日運勢
☞ Rlb 拉霸一次
☞ 帥哥 抽帥哥
☞ 妹子 抽妹子
☞ wall 抽桌布
☞ Kernel 核心版本查詢"""
    return helpM
wait = {
    "ban":False,
    "unban":False,
    "getmid":False,
    "pic":False,
    "monmonpic":False,
    "wallpic":False,
    "keepban":0,
    "keepunban":0,
    'rapidFire':{},
    'bye':{}
}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']

if clMID not in ban["owners"]:
    ban["owners"].append(clMID)
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION {}".format(datetime.today().strftime('%Y/%m/%d|%H：%M：%S|')))
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                sendMention(op.param1, " @! 感謝你加我為好友",[op.param1])
        if op.type == 11:
            print ("[ 11 ] Change Group settings")
            G = cl.getGroup(op.param1)
            if op.param1 in settings["mention"]:
                sendMention(op.param1, " @! 更改群組設置",[op.param2])
            if op.param1 in settings["qrprotect"]:
                if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    ban["blacklist"][op.param2] = True
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
        if op.type == 13:
            print ("[ 13 ] invite Group {}".format(datetime.today().strftime('%Y/%m/%d|%H：%M:%S|')))
            if clMID in op.param3:
                group = cl.getGroup(op.param1)
                if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                    cl.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "感謝 @! 邀請加入",[op.param2])
                else:
                    cl.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "@! 你不是管理員!",[op.param2])
                    cl.leaveGroup(op.param1)
            elif op.param1 in settings["invprotect"]:
                if op.param2 in ban["admin"] or op.param2 in ban["bots"] or op.param2 in ban["owners"]:
                    pass
                else:
                    ban["blacklist"][op.param2] = True
                    if len(op.param3) < 6:
                        for x in op.param3:
                            try:
                                cl.cancelGroupInvitation(op.param1,[x.mid])
                            except:
                                sleep(0.2)
                                cl.kickoutFromGroup(op.param1,[op.param3])
                    else:
                        sendMention(op.param1, "警告! @! 嘗試邀請多人ಠωಠ",[op.param2])
            else:
                gInviMids = []
                for z in op.param3:
                    if z in ban["blacklist"]:
                        gInviMids.append(z.mid)
                if gInviMids == []:
                    pass
                else:
                    for mid in gInviMids:
                        cl.cancelGroupInvitation(op.param1, [mid])
                    cl.sendMessage(op.param1,"請勿邀請黑單成員 ! ! !")
        if op.type == 17:
            print ("[ 17 ] Welcome Info {}".format(datetime.today().strftime('%Y/%m/%d|%H:%M:%S|')))
            if op.param1 in ban["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param1])
                cl.sendMessage(op.param1,"黑單成員加入 ! ! !")
            if op.param1 in settings["mention"]:
                name = str(cl.getGroup(op.param1).name)
                sendMention(op.param1, "嗨! @! 歡迎加入"+name,[op.param2])
        if op.type == 19:
            print ("[ 19 ] Leave Info")
            if op.param1 in settings["mention"]:
                chiya=[op.param2]
                chiya.append(op.param3)
                sendMention(op.param1,"警告!! @! 踢出 @! ", chiya)
            if op.param2 in ban["admin"] or op.param2 in ban["bots"] or op.param2 in ban["owners"]:
                pass
            elif op.param3 in ban["owners"]:
                ban["blacklist"][op.param2] = True
                json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                cl.kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
            elif op.param1 in settings["protect"]:
                ban["blacklist"][op.param2] = True
                cl.kickoutFromGroup(op.param1,[op.param2])
                json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        if op.type == 24 or op.type == 21 or op.type ==22:
            print ("[ 21 or 22 or 24 ] autoLeave")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if (op.type == 25 or op.type == 26) and op.message.contentType == 0:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            elif msg.toType == 2:
                to = receiver
            if text is None:
                return
            if sender in ban["blacklist"]:
                return
#                cl.kickoutFromGroup(to,[sender])  when black list user speek
            if text.lower() == 'help':
                if sender in ban["owners"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif sender in ban["admin"]:
                    helpM = helpm()
                    cl.sendMessage(to, str(helpM))
                else:
                    cl.sendMessage(to,"你可以輸入帥哥以獲得更多的帥哥~")
            if sender not in ban["blacklist"]:
                if text.lower() in ['抽妹子','妹子','Beauty'] :
                    cl.sendImage(to, "bot/linepy/loli/{}-monmon.png".format(str(random.randint(0,int(settings["monmonpic"]-1)))))
                elif text.lower() in ['loli','帥哥','Handsome'] :
                    cl.sendImage(to, "bot/linepy/loli/{}-image.png".format(str(random.randint(0,int(settings["pic"]-1)))))
                elif text.lower() in ['wall','桌布','wallpaper'] :
                    cl.sendImage(to, "bot/linepy/loli/{}-wall.png".format(str(random.randint(0,int(settings["wallpic"]-1)))))
            if sender in ban["admin"] or sender in ban["owners"]:
                if text.lower() in ['speed','sp']:
                    cl.sendMessage(to,"Testing. . .")
                if text.lower() in ['speed','sp']:
                    cl.sendMessage(to,"The response speed is "+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=1000)) + " seconds")
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to,"Save settings successfully !")
                if text.lower() in ['osversion','osver','version','botversion','ver']:
                    cl.sendMessage(to,"Detecting. . .")
                if text.lower() in ['osversion','osver','version','botversion','ver']:
                    cl.sendMessage(to,"Bot Version :  7  .  0  .  1  ")
                elif text.lower() == 'runtime':
                    cl.sendMessage(to, "The system has been operating for {}".format(str(format_timespan(time.time() - botStart))))
                elif text.lower() == 'about':
                    ret_ = "╔══[ About Users ]"
                    ret_ += "\n╠ 使用者名稱 : {}".format(cl.getContact(sender).displayName)
                    if sender in cl.getAllContactIds():ret_ += "\n╠ 與本帳關係 : 好友"
                    else:ret_ += "\n╠ 與本帳關係 : 普通"
                    if sender in ban["owners"]:ret_ += "\n╠ 使用者權限 : 最高(擁有者)"
                    elif sender in ban["admin"]:ret_ += "\n╠ 使用者權限 : 部分(權限者)"
                    elif sender in ban["blacklist"]:ret_ += "\n╠ 使用者權限 : 無(黑單者)"
                    else:ret_ += "\n╠ 使用者權限 : 基本(抽圖片)"
                    ret_ += "\n╠ 詳細功能請打help"
                    ret_ += "\n╠ 當前版本：V7.0.1"
                    ret_ += "\n╠ 擁有者 :{}".format(cl.getContact("uccbf1a060985c3cad6afee0741edd155").displayName)
                    ret_ += "\n╠ 查詢時間 :\n╠{}".format(datetime.today().strftime('%Y/%m/%d|-%H:%M:%S-|'))
                    ret_ += "\n╚══[ Over ]"
                    cl.sendMessage(to, str(ret_))
                    try:
                        ret_ = "╔══[ Local Settings ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠ 自動加入好友 🎉"
                        else: ret_ += "\n╠ 自動加入好友 ✨"
                        if settings["autoLeave"] == True: ret_ += "\n╠ 自動退出副本 🎉"
                        else: ret_ += "\n╠ 自動退出副本 ✨"
                        if settings["autoRead"] == True: ret_ += "\n╠ 自動已讀 🎉"
                        else: ret_ += "\n╠ 自動已讀 ✨"
                        if settings["getmid"] == True: ret_ += "\n╠ 獲取友資詳情 🎉"
                        else: ret_ += "\n╠ 獲取友資詳情 ✨"
                        if settings["timeline"] == True: ret_ += "\n╠ 文章預覽 🎉"
                        else: ret_ += "\n╠ 文章預覽 ✨"
                        if settings["detectMention"] ==True: ret_+="\n╠ 標註偵測 🎉"
                        else: ret_ += "\n╠ 標註偵測 ✨"
                        if msg.toType==2:
                            ret_ += "\n╠══[ Simple Group Setting ]"
                            G = cl.getGroup(msg.to)
                            ret_ += "\n╠ 群組名稱 : {}".format(str(G.name))
                            if G.id in settings["protect"] : ret_+="\n╠ 踢人保護 🎉"
                            else: ret_ += "\n╠ 踢人保護 ✨"
                            if G.id in settings["qrprotect"] : ret_+="\n╠ 網址保護 🎉"
                            else: ret_ += "\n╠ 網址保護 ✨"
                            if G.id in settings["invprotect"] : ret_+="\n╠ 邀請保護 🎉"
                            else: ret_ += "\n╠ 邀請保護 ✨"
                            if G.id in settings["mention"] : ret_ += "\n╠ 群組狀況提示 🎉"
                            else: ret_ += "\n╠ 群組狀況提示 ✨"
                            if G.id in settings["reread"]: ret_+="\n╠ 復讀 🎉"
                            else: ret_ += "\n╠ 復讀 ✨"
                        ret_ += "\n╚[ Over ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() in ['adminlist','admin']:
                    if ban["admin"] == []:
                        cl.sendMessage(to,"No person with permission !")
                    else:
                        mc = "╔[ Authority ]"
                        for mi_d in ban["admin"]:
                            try:
                                mc += "\n╠ "+cl.getContact(mi_d).displayName
                            except:
                                pass
                        cl.sendMessage(to,mc + "\n╚[ Over ]")
                elif text.lower().startswith("say "):
                    x = text.split(' ')
                    if len(x) == 2:
                        cl.sendMessage(to,x[1])
                    elif len(x) == 3:
                        try:
                            c = int(x[2])
                            for c in range(c):
                                cl.sendMessage(to,x[1])
                        except:
                            cl.sendMessage(to,"錯誤指令")
                elif msg.text.lower().startswith("tag "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = text.split(' ')
                    if len(x) == 2:
                        cl.sendMessage(to,x[1])
                    elif len(x) == 3:
                        c = int(x[2])
                        for c in range(c):
                            sendMessageWithMention(to, inkey)
                elif text.lower().startswith("text "):
                    a = text.split(" ",2)
                    textnya = a[1]
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    cl.sendImageWithURL(msg.to, urlnya)
#==============================================================================#
                elif text.lower() == 'me':
                    if msg.toType == 0:
                        cl.sendContact(to, sender)
                    else:
                        sendMessageWithMention(to, sender)
                        cl.sendContact(to,sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'name':
                    cl.sendMessage(msg.to,"[Name]\n" + cl.getContact(sender).displayName)
                elif text.lower() == 'bio':
                    cl.sendMessage(msg.to,"[StatusMessage]\n" + cl.getContact(sender).statusMessage)
                elif text.lower() == 'picture':
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + cl.getContact(sender).pictureStatus)
                elif text.lower() == 'videoprofile':
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + cl.getContact(sender).pictureStatus + "/vp")
                elif text.lower() == 'cover':
                    cl.sendImageWithURL(msg.to, cl.getProfileCoverURL(sender))
                elif msg.text.lower().startswith("contact:"):
                    y = text[8:].split( )
                    for mid in y:
                        cl.sendContact(msg.to,mid)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif text.lower() == 'mid':
                    wait["getmid"]=True
                    cl.sendMessage(to,"Please send a contact")
                elif msg.text.lower().startswith("name ") :
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendMessage(msg.to,"[Name]\n" + cl.getContact(inkey).displayName)
                elif msg.text.lower().startswith("bio ") :
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendMessage(msg.to,"[StatusMessage]\n" + cl.getContact(inkey).statusMessage)
                elif msg.text.lower().startswith("cover ") :
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendImageWithURL(msg.to, cl.getProfileCoverURL(inkey))
                elif msg.text.lower().startswith("picture ") :
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + cl.getContact(inkey).pictureStatus)
                elif msg.text.lower().startswith("videoprofile ") :
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + cl.getContact(inkey).pictureStatus + "/vp")
                elif msg.text.lower().startswith("info "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ Name ]\n" + contact.displayName +"\n[ Sign ]\n" + contact.statusMessage +"\n[ MID ]\n" + contact.mid)
                            cl.sendImageWithURL(msg.to, str("http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus)) 
                            cl.sendImageWithURL(msg.to, str(cl.getProfileCoverURL(ls)))
#==============================================================================#
                elif text.lower() in ['link on',"招待URL許可"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "它已被允許。")
                        else:
                            if group.id in settings["qrprotect"]:
                                cl.sendMessage(to,"無法創建邀請URL，因為禁止更改設置。")
                            else:
                                group.preventedJoinByTicket = False
                                cl.updateGroup(group)
                                cl.sendMessage(to, "允許訪問URL")
                elif text.lower() in ["招待URL拒否",'link off']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "它已被拒絕")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to,  "我拒絕了網址邀請。")
            if sender in ban["owners"]:
                if text.lower() in ['魔刻結晶','time']:
                    cl.sendMessage(to, "現在時間:{}".format(datetime.today().strftime('%Y/%m/%d|%H/%M/%S|')))
                elif text.lower() == 'join':
                    group = cl.getGroup(to)
                    if group.preventedJoinByTicket == False:
                        for m_id in ban["bots"]:
                            cl.sendMessage(m_id,"https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id))))
                    else:
                        group.preventedJoinByTicket = False
                        cl.updateGroup(group)
                        for m_id in ban["bots"]:
                            cl.sendMessage(m_id,"https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id))))
                elif text.lower() in ['gurl_get','gurl','link','grouplink',"招待URL生成"]:
                    if msg.toType==2:
                        group=cl.getGroup(to)
                        if group.id in wait["qrprotect"]:
                            cl.sendMessage(to, "無法創建邀請URL，因為禁止更改設置。")
                        else:
                            cl.sendMessage(to,"https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id))))
                elif text.lower() in ['groupinfo','ginfo']:
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "無"
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔═[ Group data ]"
                    ret_ += "\n╠ 群組名稱 : {}".format(str(group.name))
                    ret_ += "\n╠ 群組 Id : {}".format(group.id)
                    ret_ += "\n╠ 創建者 : {}".format(str(gCreator))
                    ret_ += "\n╠ 群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請中 : {}".format(gPending)
                    ret_ += "\n╠ 網址狀態 : {}".format(gQr)
                    ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ Over ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower().startswith('cg:'):
                    group = cl.getGroup(text[3:])
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "無"
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔═[ Group data ]"
                    ret_ += "\n╠ 群組名稱 : {}".format(str(group.name))
                    ret_ += "\n╠ 群組 Id : {}".format(group.id)
                    ret_ += "\n╠ 創建者 : {}".format(str(gCreator))
                    ret_ += "\n╠ 群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請中 : {}".format(gPending)
                    ret_ += "\n╠ 網址狀態 : {}".format(gQr)
                    ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ Over ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() in ['groupmemberlist','gmember','member']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "╔═[ List of members ]"
                        no = 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚═[ All members are {} people]".format(str(no-1))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() in ['grouplist','glist','lg']:
                        groups = cl.groups
                        ret_ = "╔══[ Group list ]"
                        no = 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚═[ Total {} group ]".format(str(no))
                        cl.sendMessage(to, str(ret_))
#==============================================================================#
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "Total {} people".format(str(len(nama))))
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower() == 'zc':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for mi_d in targets:
                           cl.sendContact(to,mi_d)
                elif text.lower().startswith("gn "):
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"It can't be used besides the group.")
                elif text.lower() in ['setread','sr','既読ポイント設定']:
                    cl.sendMessage(msg.to, "讀取點已設置")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                elif text.lower() in ['cancelread','cr']:
                    cl.sendMessage(to, "已讀點已刪除")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif text.lower() in ['checkread','lookread','lr','既読確認','sn']:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[已讀的人]:\n%s\n查詢時間:[%s]" % (chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "讀取點未設置 !!")
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"No black singel members !")
                    else:
                        mc = "╔═[ Blacklisted members ]"
                        for mi_d in ban["blacklist"]:
                            try:
                                mc += "\n╠ "+cl.getContact(mi_d).displayName
                            except:
                                pass
                        cl.sendMessage(msg.to,mc + "\n╚══[ Over ]")
                elif text.lower() in ['groupbanmidlist','gban','gbanlist']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                    for tag in ban["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendMessage(msg.to,"無本群黑單成員 !")
                        return
                    for jj in matched_list:
                        mc = "╔══[ 本群黑單成員 ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n╠ "+mi_d
                        cl.sendMessage(to,mc + "\n╚[ Over ]")
                elif text.lower() == 'banmidlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"No black singel members !")
                    else:
                        mc = "╔══[ Blacklisted members ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n╠ "+mi_d
                        cl.sendMessage(to,mc + "\n╚[ Over ]")
                elif text.lower().startswith("nt "):
                    if msg.toType == 2:
                        _name = msg.text.replace("Nt ","")
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendMessage(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    sendMessageWithMention(to, target)
                                except:
                                    pass
                elif text.lower() == 'bomb':
                    cl.sendMessage(msg.to,"( ´-ω･)︻┻┳══━一")
                elif text.lower() in ["さようなら",'bye']:
                    cl.sendMessage(msg.to, "Are sure to leave ?\n（Yes / No ）")
                    wait['bye'][msg.to] = sender
                elif text.lower() in ["Y","y","退出","N","n","掰掰"]:
                    if msg._from== wait['bye'][msg.to]:
                        if text.lower() in ["掰掰",'y']:
                            cl.sendMessage(msg.to, "Execute leave ! ! !")
                            cl.leaveGroup(msg.to)
                            del wait['bye'][msg.to]
                        elif text.lower() in ['n',"取消"]:
                            cl.sendMessage(msg.to, "Cancel leave !")
                            del wait['bye'][msg.to]
                    else:
                        pass
                elif text.lower().startswith("sendto"):
                    x =text.split(' ')
                    if len(x)==2:
                        try:
                            cl.sendMessage(x[1],x[2])
                        except:
                            cl.sendMessage(to,"Can't find")
#==============================================================================#   
            if sender in ban["owners"]:
                if text.lower() == 'restart':
                    cl.sendMessage(to, "Stop running ! !")
                    time.sleep(1)
                    cl.sendMessage(to, "請稍後 15秒 進行重啟 !")
                    time.sleep(5)
                    cl.sendMessage(to, "重新啟動成功 ! !")
                    time.sleep(4)
                    cl.sendMessage(to, "Restart Version《Alpha2-V7》")
                    restartBot()
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入好友開啟")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入好友關閉")
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本開啟")
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本關閉")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀開啟")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀關閉")
                elif text.lower() == 'autolike on':
                    settings["autolike"] = True
                    cl.sendMessage(to, "自動按讚貼文開啟")
                elif text.lower() == 'autolike off':
                    settings["autolike"] = False
                    cl.sendMessage(to, "自動按讚貼文關閉")
                elif text.lower() == 'prompt on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["mention"][G.id] = True
                        cl.sendMessage(to, "群組狀況提示開啟")
                elif text.lower() == 'prompt off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["mention"][G.id]
                            cl.sendMessage(to, "群組狀況提示關閉")
                        except:
                            cl.sendMessage(to, "目前功能是關閉的")
                elif text.lower() == 'reread on':
                    settings["reread"][to] = True
                    cl.sendMessage(to,"復讀開啟")
                elif text.lower() == 'reread off':
                    try:
                        del settings["reread"][to]
                        cl.sendMessage(to,"復讀關閉")
                    except:
                        pass
                elif text.lower() == 'protect on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["protect"][G.id] = True
                        cl.sendMessage(to, "踢人保護開啟")
                elif text.lower() == 'protect off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["protect"][G.id]
                            cl.sendMessage(to, "踢人保護關閉")
                        except:
                            cl.sendMessage(to, "目前功能是關閉的")
                elif text.lower() == 'detect on':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "已開啟標註偵測")
                elif text.lower() == 'detect off':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "已關閉標註偵測")
                elif text.lower() == 'ban':
                    wait["ban"]=True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'unban':
                    wait["unban"]=True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower().startswith("keepban "):
                    times = text.split(' ')
                    wait["keepban"]=int(times[1])
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower().startswith("keepunban "):
                    times = text.split(' ')
                    wait["keepunban"]=int(times[1])
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'qrprotect on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["qrprotect"][G.id] = True
                        cl.sendMessage(to, "網址保護開啟")
                elif text.lower() == 'qrprotect off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["qrprotect"][G.id]
                            cl.sendMessage(to, "網址保護關閉")
                        except:
                            cl.sendMessage(to, "目前功能是關閉的")
                elif text.lower() == 'invprotect on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["invprotect"][G.id] = True
                        cl.sendMessage(to, "邀請保護開啟")
                elif text.lower() == 'invprotect off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["invprotect"][G.id]
                            cl.sendMessage(to, "邀請保護關閉")
                        except:
                            cl.sendMessage(to, "目前功能是關閉的")
                elif text.lower() == 'getinfo on':
                    settings["getmid"] = True
                    cl.sendMessage(to, "友資詳情獲取開啟")
                elif text.lower() == 'getinfo off':
                    settings["getmid"] = False
                    cl.sendMessage(to, "友資詳情獲取關閉")
                elif text.lower() == 'timeline on':
                    settings["timeline"] = True
                    cl.sendMessage(to, "文章預覽開啟")
                elif text.lower() == 'timeline off':
                    settings["timeline"] = False
                    cl.sendMessage(to, "文章預覽關閉")
                elif text.lower() == 'savelolipic on':
                    wait["pic"] = True
                    cl.sendMessage(to,"Send some picture to saving ~")
                elif text.lower() == 'savelolipic off':
                    wait["pic"] = False
                    backupData()
                    cl.sendMessage(to, "Saved !")
                elif text.lower() == 'savepic on':
                    wait["monmonpic"] = True
                    cl.sendMessage(to,"Send some picture to saving ~")
                elif text.lower() == 'savepic off':
                    wait["monmonpic"] = False
                    backupData()
                    cl.sendMessage(to, "Saved !")
                elif text.lower() == 'savewallpic on':
                    wait["wallpic"] = True
                    cl.sendMessage(to,"Send some picture to saving ~")
                elif text.lower() == 'savewallpic off':
                    wait["wallpic"] = False
                    backupData()
                    cl.sendMessage(to, "Saved !")
                elif text.lower() == 'pro on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["protect"][G.id] = True
                        settings["qrprotect"][G.id] = True
                        settings["invprotect"][G.id] = True
                        cl.sendMessage(to, "踢人保護開啟")
                        cl.sendMessage(to, "網址保護開啟")
                        cl.sendMessage(to, "邀請保護開啟")
                elif text.lower() == 'pro off':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["protect"][G.id]
                            cl.sendMessage(to, "踢人保護關閉")
                        except:
                            pass
                        try:
                            del settings["qrprotect"][G.id]
                            cl.sendMessage(to, "網址保護關閉")
                        except:
                            pass
                        try:
                            del settings["invprotect"][G.id]
                            cl.sendMessage(to, "邀請保護關閉")
                        except:
                            pass
                elif msg.text.lower().startswith("adminadd ") or msg.text.lower().startswith("add "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["admin"] and inkey not in ban["blacklist"] and inkey not in ban["owners"]: 
                        ban["admin"].append(str(inkey))
                        cl.sendMessage(to, "Permission granted !")
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                elif msg.text.lower().startswith("admindel ") or msg.text.lower().startswith("del "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["admin"]:
                        ban["admin"].remove(str(inkey))
                        cl.sendMessage(to, "Permission cancelled !")
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                
                elif msg.text.lower().startswith("botsadd "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["bots"].append(str(inkey))
                    cl.sendMessage(to, "已加入分機！")
                elif msg.text.lower().startswith("botsdel "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["bots"].remove(str(inkey))
                    cl.sendMessage(to, "已取消分機！")
                elif text.lower() == 'botslist':
                    if ban["bots"] == []:
                        cl.sendMessage(to,"無分機!")
                    else:
                        mc = "╔══[ Inviter List ]"
                        for mi_d in ban["bots"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Over ]")
                elif msg.text.lower().startswith("ii "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    s = text.split(' ')
                    try:
                        for a in range(int(s[2])):
                            cl.createGroup("fuck",[inkey])
                    except:
                        pass
                    c =cl.getGroupIdsByName("fuck")
                    for gid in c:
                        cl.leaveGroup(gid)
                elif msg.text.lower().startswith("tk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.sendMessage(to,"Never see you again !!")
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendMessage(to,"Error")
                elif msg.text.lower().startswith("zk "):
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in ban["admin"]:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif msg.text.lower().startswith("ri "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.sendMessage(to,"來回一次")
                            cl.findAndAddContactsByMid(target)
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.sendMessage(to,"Error")
                elif text.lower().startswith("nk "):
                    if msg.toType == 2:
                        _name = msg.text.replace("Nk ","")
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendMessage(msg.to,"Non found")
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                elif text.lower() in ['byeall','.kickall','kickall']:
                    if msg.toType == 2:
                        gs = cl.getGroup(msg.to)
                        for g in gs.members:
                            try:
                                cl.kickoutFromGroup(msg.to,[g.mid])
                                sleep(1)
                            except:
                                pass
                elif text.lower() == 'cancel':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                        sleep(2)
                    cl.sendMessage(msg.to,"已取消所有邀請!")
                elif text.lower() in ["取消"]:
                    group = cl.getGroup(to)
                    if group.invitee is None:
                        cl.sendMessage(to, "沒有人邀請你")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(to, gInviMids)
                        cl.sendMessage(to, str(len(group.invitee)) + "你取消了這個人的邀請。")
                elif text.lower().startswith("inv "):
                    if msg.toType == 2:
                        midd = text.split(' ')
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(to,[midd])

#==============================================================================#
            if sender in ban["owners"]:
                    if text.lower() == 'kernel':
                        cl.sendMessage(to, "Kernel Version:V7.0.1\n{}".format(datetime.today().strftime('%Y/%m/%d|%H：%M：%S|')))
            if sender in ban["owners"]:
                    if text.lower() == '오':
                        cl.sendMessage(to, """🥀更新日誌🥀\n1.系統優化\n2.修復部分錯誤\n\nVersion:V7.0.1\n如有問題請找:""")
                        time.sleep(1)
                        cl.sendContact(to, "ucbbd21e79a63b5486a47101ef73451b7")
            if sender in ban["owners"]:
                    if text.lower() == '네':
                        cl.sendMessage(to, "한글은 지원하지 않습니다!!")
            
            if sender in ban["admin"]:
                    if text.lower() == 'kernel':
                        cl.sendMessage(to, "Kernel Version:V7.0.1\n{}".format(datetime.today().strftime('%Y/%m/%d|%H：%M：%S|')))
            if sender in ban["owners"]:
                if text.lower() == 'rlb':
                    a = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    b = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    c = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    d = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    e = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    f = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    g = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    h = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    i = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    j = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    k = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    l = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    m = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    n = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    o = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    slot = "拉霸一次\n第一行==>{}  {}  {}<==\n第二行==>{}  {}  {}<==\n第三行==>{}  {}  {}<==\n第四行==>{}  {}  {}<==\n第五行==>{}  {}  {}<==\n以上是你的抽獎結果".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
                    cl.sendMessage(to,slot)
                    if a == e == i == j == o:
                        cl.sendMessage(to,"恭喜獲勝 !！")
                        return
                    cl.sendMessage(to,"再試一次")                            
                elif text.lower() == '本日運勢':
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "你的運勢為\n{}<==\n以上是你的抽獎結果".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == '抽':
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "你的運勢為\n{}<==\n以上是你的抽獎結果".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == 'rls':
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "你的運勢為\n{}<==\n以上是你的抽獎結果".format(a)
                    cl.sendMessage(to,slot)

            if sender in ban["admin"]:
                if text.lower() == 'rlb':
                    a = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    b = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    c = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    d = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    e = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    f = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    g = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    h = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    i = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    j = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    k = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    l = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    m = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    n = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    o = random.choice(["0","9","8","7","6","5","4","3","2","1"])
                    slot = "拉霸一次\n第一行==>{}  {}  {}<==\n第二行==>{}  {}  {}<==\n第三行==>{}  {}  {}<==\n第四行==>{}  {}  {}<==\n第五行==>{}  {}  {}<==\n以上是你的抽獎結果".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
                    cl.sendMessage(to,slot)
                    if a == e == i == j == o:
                        cl.sendMessage(to,"恭喜獲勝 !")
                        return                      
                elif text.lower() == '本日運勢':
                    a = random.choice(["大吉！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "你的運勢為\n{}<==\n以上是你的抽獎結果".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == '抽':
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "你的運勢為\n{}<==\n以上是你的抽獎結果".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == 'rls':
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "你的運勢為\n{}<==\n以上是你的抽獎結果".format(a)
                    cl.sendMessage(to,slot)
#==============================================================================#
                elif msg.text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target not in ban["owners"] :
                            try:
                                ban["blacklist"][target] = True
                                cl.sendMessage(msg.to,"Blacklist has been added !")
                                json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                            except:
                                cl.sendMessage(msg.to,"Add failed !")
                elif text.lower().startswith("ban :"):
                    txt = text.replace("Ban :","")
                    if txt not in ban["owners"] and len(txt) ==33 and txt.lower.startswith("u"):
                        ban["blacklist"][txt] = True
                        cl.sendMessage(msg.to,"Blacklist has been added !")
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                    else:
                        cl.sendMessage(msg.to,"Add failed !")
                elif text.lower().startswith("unban :"):
                    txt = text.replace("Unban :","")
                    if txt in ban["blacklist"] :
                        del ban["blacklist"][txt]
                        cl.sendMessage(msg.to,"Blacklist deleted .")
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                    else:
                        cl.sendMessage(msg.to,"This person is not in the blacklist !")
                elif msg.text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["blacklist"][target]
                            cl.sendMessage(msg.to,"Successfully deleted !")
                            json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                        except:
                            cl.sendMessage(msg.to,"Failed to delete !")
                elif text.lower() in ['kickban','killban']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                    for tag in ban["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendMessage(msg.to,"There was no blacklist user .")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendMessage(msg.to,"Blacklist kicked out .")
                elif text.lower() == 'cleanban':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendMessage(to, "Blackelist cleared .")
#==============================================================================#
                elif text.lower().startswith("fbc:"):
                    bctxt = text.split(':')
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,bctxt[1])
                elif text.lower().startswith("gbc:"):
                    bctxt = text.split(':')
                    n = cl.getGroupIdsJoined()
                    if len(bctxt)==3:
                        for manusia in n:
                            group = cl.getGroup(manusia)
                            nama =[contact.mid for contact in group.members]
                            if len(nama) >int(bctxt[2]):
                                cl.sendMessage(manusia,bctxt[1])
                            else:
                                pass
                    elif len(bctxt)==2:
                        for g in n:
                            cl.sendMessage(g,bctxt[1])
                elif text.lower().startswith("copy "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    contact = cl.getContact(inkey)
                    p = cl.profile
                    home = cl.getProfileDetail(inkey)
                    objectId = home["result"]["objectId"]
                    cl.updateProfileCoverById(objectId)
                    p.displayName = contact.displayName
                    p.statusMessage = contact.statusMessage
                    cl.updateProfile(p)
                    cl.updateProfileCoverById(cl.getProfileCoverId(inkey))
                    p.pictureStatus = contact.pictureStatus
                    cl.updateProfilePicture(contact.pictureStatus)
            if text.lower() == 'cc9487':
                if sender in ['ua10c2ad470b4b6e972954e1140ad1891']:
                    sys.exit()
                else:
                    pass
#==============================================================================# 
        if op.type == 26:
            msg=op.message
            sender = msg._from
            receiver = msg.to
            text = msg.text
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if text is None:
                return
            if msg.contentType == 1:
                if wait["pic"] == True:
                    if msg._from in ban["owners"]:
                        image = cl.downloadObjectMsg(msg.id, saveAs="bot/linepy/loli/{}-image.png".format(settings["pic"]))
                        settings["pic"] +=1
                        cl.sendMessage(to,"OK")
                if wait["monmonpic"] == True:
                    if msg._from in ban["owners"]:
                        image = cl.downloadObjectMsg(msg.id, saveAs="bot/linepy/loli/{}-monmon.png".format(settings["monmonpic"]))
                        settings["monmonpic"] +=1
                        cl.sendMessage(to,"OK")
                if wait["wallpic"] == True:
                    if msg._from in ban["owners"]:
                        image = cl.downloadObjectMsg(msg.id, saveAs="bot/linepy/loli/{}-wall.png".format(settings["wallpic"]))
                        settings["wallpic"] +=1
                        cl.sendMessage(to,"OK")
            if msg.contentType == 13:
                if settings["getmid"] == True:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    cl.sendMessage(to, "[ Name ]\n" + contact.displayName +"\n[ Sign ]\n" + contact.statusMessage +"\n[ MID ]\n" + contact.mid)
                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    cl.sendImageWithURL(to, str(path))
                    path = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                    cl.sendImageWithURL(to, str(path))
                if wait["ban"] ==True:
                    if msg._from in ban["owners"]:
                        ban["blacklist"][msg.contentMetadata["mid"]]=True
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(to,"OK")
                        wait["ban"] =False
                if wait["unban"] ==True:
                    if msg._from in ban["owners"]:
                        del ban["blacklist"][msg.contentMetadata["mid"]]
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(to,"OK")
                        wait["unban"] =False
                if wait["getmid"] ==True:
                    if msg._from in ban["owners"] or msg._from in ban["admin"]:
                        cl.sendMessage(to,msg.contentMetadata["mid"])
                        wait["getmid"] =False
                if wait["keepban"] >0:
                    if msg._from in ban["owners"]:
                        ban["blacklist"][msg.contentMetadata["mid"]]=True
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(to,"OK")
                        wait["keepban"] -=1
                if wait["keepunban"] >0:
                    if msg._from in ban["owners"]:
                        del ban["blacklist"][msg.contentMetadata["mid"]]
                        json.dump(ban, codecs.open('bot/ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(to,"OK")
                        wait["keepunban"] -=1
            if msg.contentType == 16:
#                if settings["autolike"] == True:
#                    url = msg.contentMetadata("postEndUrl")
#                    cl.likePost(url[25:58], url[66:], likeType=1001)    autolike can't be use in normal API
                if settings["timeline"] == True:
                    try:
                        ret_ = "═══Article perview═══"
                        ret_ += "\n[Article author ]\n @!"
                        if "text" in msg.contentMetadata:
                            ret_ += "\n[ Article details ]\n"+msg.contentMetadata["text"]
                        ret_ += "\n[ URL ]\n {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                        if "mediaOid" in msg.contentMetadata:
                            object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                            if msg.contentMetadata["mediaType"] == "V":
                                if msg.contentMetadata["serviceType"] == "GB":
                                    ourl = "\n[ Objek URL ]\n https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    murl = "\n[ Media URL ]\n https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                else:
                                    ourl = "\n[ Objek URL ]\n https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    murl = "\n[ Media URL ]\n https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                ret_ += murl
                            else:
                                if msg.contentMetadata["serviceType"] == "GB":
                                    ourl = "\n[ Objek URL ]\n https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                else:
                                    ourl = "\n[ Objek URL ]\n https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                            ret_ += ourl
                        if "stickerId" in msg.contentMetadata:
                            ret_ += "\n[ 貼圖訊息 ]\n https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                        f = msg.contentMetadata["postEndUrl"].split('userMid=')
                        s = f[1].split('&')
                        sendMention(msg.to, ret_,[s[0]])
                    except:
                        txt = msg.contentMetadata["text"]
                        txt += "\n[Article URL]\n" + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(to,"[Article details]\n"+txt)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if text is None:
                return
            if settings["autoRead"] == True:
                cl.sendChatChecked(to, msg_id)
            if msg.contentType == 0 and sender not in ban["owners"] and msg.toType == 2:
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    lists = []
                    for mention in mentionees:
                        if clMID in mention["M"]:
                            if settings["detectMention"] == True:
                                contact = cl.getContact(sender)
                                sendMention(to,"@! 有事直接私訊我", [contact.mid])
                            break
            try:
                if to in settings["reread"]:
                    if msg.contentType == 0:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                lists.append(mention["M"])
                            list=""
                            x = msg.text
                            for mid in lists:
                                x=x.replace("@"+str(cl.getContact(mid).displayName),"@!")
                                list+=mid+","
                            listt=list[:-1]
                            msg_dict[msg.id] = {"mtext":"[Recaller]\n @! \n[Message content]\n"+x,"from":msg._from,"createdTime":time.time(),"mentionee":listt}
                        else:
                            msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":time.time()}
            except Exception as e:
                print(e)
            if msg.contentType == 1:
                if to in settings["reread"]:
                    if 'gif' in msg.contentMetadata.keys()!= None:
                        gif = cl.downloadObjectMsg(msg_id, saveAs="bot/linepy/tmp/{}-image.gif".format(time.time()))
                        msg_dictt[msg.id] = {"from":msg._from,"gif":0,"object":gif,"createdTime":time.time()}
                    else:
                        image = cl.downloadObjectMsg(msg_id, saveAs="bot/linepy/tmp/{}-image.bin".format(time.time()))
                        msg_dictt[msg.id] = {"from":msg._from,"image":0,"object":image,"createdTime":time.time()}
            elif msg.contentType == 3:
                if to in settings["reread"] :
                    sound = cl.downloadObjectMsg(msg_id, saveAs="bot/linepy/tmp/{}-sound.mp3".format(time.time()))
                    msg_dictt[msg.id] = {"from":msg._from,"sound":0,"object":sound,"createdTime":time.time()}
            elif msg.contentType == 7:
                if to in settings["reread"]:
                    stk_id = msg.contentMetadata['STKID']
                    msg_dict[msg.id] = {"from":msg._from,"stkid": stk_id ,"createdTime":time.time()}
            elif msg.contentType == 13:
                if to in settings["reread"]:
                    mid = msg.contentMetadata["mid"]
                    msg_dict[msg.id] = {"from":msg._from,"mid": mid ,"createdTime":time.time()}
            elif msg.contentType == 14:
                if to in settings["reread"]:
                    file = cl.downloadObjectMsg(msg_id, saveAs="bot/linepy/tmp/{}-".format(msg_id)+msg.contentMetadata['FILE_NAME'])
                    msg_dictt[msg.id] = {"from":msg._from,"file":0,"object":file,"createdTime":time.time()}
            try:
                if len(msg_dictt)>=100:
                    for x in msg_dictt:
                        cl.deleteFile(msg_dictt[x]["object"])
                        del msg_dictt[x]
            except:
                pass
#==============================================================================#
        if op.type == 65:
            try:
                msg = op.message
                at = op.param1
                msg_id = op.param2
                if op.param1 in settings["reread"]:
                    if msg_id in msg_dict:
                        timeNow = time.time()
                        opi=[]
                        opi.append(msg_dict[msg_id]["from"])
                        if "mtext" in msg_dict[msg_id]:
                            x =msg_dict[msg_id]["mentionee"].split(',')
                            for ic in x:
                                opi.append(ic)
#                            cl.sendMessage(at,msg_dict[msg_id]["mentionee"]+"||"+str(msg_dict[msg_id]["mtext"]))
                            sendMention(at,msg_dict[msg_id]["mtext"],opi)
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        elif "text" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n"+str(msg_dict[msg_id]["text"]),opi)
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        elif "stkid" in msg_dict[msg_id]:
                            path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(msg_dict[msg_id]["stkid"])
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一張貼圖",opi)
                            cl.sendImageWithURL(at,path)
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        elif "mid" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一則友資",opi)
                            cl.sendContact(at,msg_dict[msg_id]["mid"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                    elif msg_id in msg_dictt:
                        timeNow = time.time()
                        opi=[msg_dictt[msg_id]["from"]]
                        if "image" in msg_dictt[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一張圖片",opi)
                            cl.sendImage(at, msg_dictt[msg_id]["object"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dictt[msg_id]["createdTime"])+"秒之前")
                            cl.deleteFile(msg_dictt[msg_id]["object"])
                            del msg_dictt[msg_id]
                        elif "gif" in msg_dictt[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一張圖片",opi)
                            cl.sendGIF(at, msg_dictt[msg_id]["object"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dictt[msg_id]["createdTime"])+"秒之前")
                            cl.deleteFile(msg_dictt[msg_id]["object"])
                            del msg_dictt[msg_id]
                        elif "sound" in msg_dictt[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一份音檔",opi)
                            cl.sendAudio(at, msg_dictt[msg_id]["object"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dictt[msg_id]["createdTime"])+"秒之前")
                            cl.deleteFile(msg_dictt[msg_id]["object"])
                            del msg_dictt[msg_id]
                        elif "file" in msg_dictt[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一個檔案",opi)
                            cl.sendFile(at, msg_dictt[msg_id]["object"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dictt[msg_id]["createdTime"])+"秒之前")
                            cl.deleteFile(msg_dictt[msg_id]["object"])
                            del msg_dictt[msg_id]
                else:
                    pass
            except Exception as e:
                print (e)
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[𓂀]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[𓂀]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:

        logError(error)
#==============================================================================#
while 1:
    if time.time() -botStart > 10000 :
        
        restartBot()
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
#                _thread.start_new_thread( lineBot, (op, ) )
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
# ==============================================================================#


