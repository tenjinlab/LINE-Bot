cl = LINE(ttoken) 
cl.log("Auth Token : " + str(cl.authToken))
clMID = cl.profile.mid
botStart = time.time()
oepoll = OEPoll(cl)
ban = json.load(codecs.open("ban.json","r","utf-8"))
read = json.load(codecs.open("read.json","r","utf-8"))
settings = json.load(codecs.open("temp.json","r","utf-8"))
msg_dict = {}

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        json.dump(settings,codecs.open('temp.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(read,codecs.open('read.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    with open("errorLog.txt","a") as error:
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
    helpMessage = """╔═══════════
╠♥ ✿✿✿ 喵の單體半垢 ✿✿✿ ♥
╠═✪〘 owners專用 〙✪═
╠✪〘 Help 〙✪═════
╠➥ Help 查看指令
╠✪〘 Status 〙✪════
╠➥ Restart 重新啟動
╠➥ Save 儲存設定
╠➥ Runtime 運作時間
╠➥ Speed 速度
╠➥ Set 設定
╠➥ About關於本帳
╠✪〘 Settings 〙✪═══
╠➥ AutoAdd On/Off 自動加入
╠➥ AutoLeave On/Off 離開副本
╠➥ AutoRead On/Off 自動已讀
╠➥ Prompt On/Off 群組狀況提示
╠➥ ReRead On/Off 查詢收回
╠➥ Pro On/Off 所有保護
╠➥ Protect On/Off 踢人保護
╠➥ QrProtect On/Off 網址保護
╠➥ Invprotect On/Off 邀請保護
╠➥ Getinfo On/Off 取得友資詳情
╠➥ Detect On/Off 標註偵測
╠➥ Timeline On/Off 文章網址預覽
╠✪〘 Self 〙✪═════
╠➥ Me 我的連結
╠➥ Mymid 我的mid
╠➥ Name @ 名字[發訊者/Tag]
╠➥ Bio @ 個簽[發訊者/Tag]
╠➥ Picture @ 頭貼[發訊者/Tag]
╠➥ Cover @ 封面[發訊者/Tag]
╠➥ Mid @ 查mid[友資/Tag]
╠➥ Contact: 以mid查友資
╠➥ Info @ 查看資料
╠✪〘 Blacklist 〙✪═══
╠➥ Ban [@/:] 加入黑單[友資/Tag/MID]
╠➥ Unban [@/:] 取消黑單[友資/Tag/MID]
╠➥ Ban on/off 連續加入黑單
╠➥ Unban on/off 連續取消黑單
╠➥ Banlist 查看黑單
╠➥ CleanBan 清空黑單
╠➥ Kickban 踢除黑單
╠✪〘 Group 〙✪════
╠➥ Link「On/Off」網址開啟/關閉
╠➥ GroupList所有群組列表
╠➥ GroupMemberList 成員名單
╠➥ GroupInfo 群組資料
╠➥ Gn (文字) 更改群名
╠➥ Tk @ 標註踢人
╠➥ Zk 踢出0字元
╠➥ Nk 名字踢人
╠➥ Inv (mid) 透過mid邀請
╠➥ Inv @ 標註多邀
╠➥ Cancel 取消所有邀請
╠➥ Ri @ 來回機票
╠➥ Tagall 標註全體
╠➥ Zc 發送0字元友資
╠➥ Setread 已讀點設置
╠➥ Cancelread 取消偵測
╠➥ Checkread 已讀偵測
╠➥ Gbc: 群組廣播
╠➥ Fbc: 好友廣播
╠✪〘 Admin 〙✪════
╠➥ Adminadd @ 新增權限
╠➥ Admindel @ 刪除權限
╠➥ Adminlist 查看權限表
╚═〘 Created By: 喵喵™ 〙"""
    return helpMessage
def helpm():
    helpM = """╔═══════════
╠♥ ✿✿✿ 喵の單體半垢 ✿✿✿ ♥
╠═✪〘 admin專用 〙✪═
╠✪〘 Help 〙✪═════
╠➥ Help 查看指令
╠➥ Runtime 運作時間
╠➥ Speed 速度
╠➥ Set 設定
╠➥ About關於本帳
╠➥ Save 儲存設定
╠✪〘 Self 〙✪═════
╠➥ Me 我的連結
╠➥ Mymid 我的mid
╠➥ Name @ 名字[發訊者/Tag]
╠➥ Bio @ 個簽[發訊者/Tag]
╠➥ Picture @ 頭貼[發訊者/Tag]
╠➥ Cover @ 封面[發訊者/Tag]
╠➥ Mid @ 查mid[友資/Tag]
╠➥ Contact: 以mid查友資
╠➥ Info @ 查看資料
╠✪〘 Group 〙✪════
╠➥ Link「On/Off」網址開啟/關閉
╠➥ GroupList所有群組列表
╠➥ GroupMemberList 成員名單
╠➥ GroupInfo 群組資料
╠➥ Gn (文字) 更改群名
╠➥ Inv @ 標註多邀
╠➥ Tagall 標註全體
╠➥ Zc 發送0字元友資
╠➥ Setread 已讀點設置
╠➥ Cancelread 取消偵測
╠➥ Checkread 已讀偵測
╠✪〘 Other 〙✪════
╠➥ Say 重複講話[內容 次數]
╠➥ Tag @ 重複標人[目標 次數]
╠➥ Adminlist 查看權限表
╠➥ Banlist 查看黑單
╚═〘 Created By: 喵喵™ 〙"""
    return helpM
wait = {
    "ban":False,
    "unban":False,
    "getmid":False,
    "keepban":False,
    "keepunban":False
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
#if clMID not in ban["owners"]:
#    python = sys.executable
#    os.execl(python, python, *sys.argv)
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                sendMention(op.param1, " @! 感謝您加我為好友",[op.param1])
        if op.type == 11:
            G = cl.getGroup(op.param1)
            if settings["mention"] == True:
                sendMention(op.param1, " @! 更改群組設定",[op.param2])
            if op.param1 in settings["qrprotect"]:
                if op.param2 in ban["admin"] or op.param2 in ban["bots"] or op.param2 in ban["owners"]:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
        if op.type == 13:
            if clMID in op.param3:
                group = cl.getGroup(op.param1)
                if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                    cl.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "權限者 @! 邀請入群",[op.param2])
                else:
                    cl.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "@! 你不是管理員",[op.param2])
                    cl.leaveGroup(op.param1)
            elif op.param1 in settings["invprotect"]:
                if op.param2 in ban["admin"] or op.param2 in ban["bots"] or op.param2 in ban["owners"]:
                    pass
                else:
                    if len(op.param3) < 11:
                        for x in op.param3:
                            cl.cancelGroupInvitation(op.param1,[x.mid])
                    else:
                        sendMention(op.param1, "@! 試圖邀請多個人",[op.param2])
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
                    cl.sendMessage(op.param1,"Do not invite blacklist user...")
        if op.type == 17:
            if settings["mention"] == True:
                name = str(cl.getGroup(op.param1).name)
                sendMention(op.param1, "你好 @! 歡迎加入"+name,[op.param2])
        if op.type == 19:
            if settings["mention"] == True:
                chiya=[op.param2]
                chiya.append(op.param3)
                sendMention(op.param1,"警告!! @! 踢了 @! ", chiya)
            if op.param2 in ban["admin"] or op.param2 in ban["bots"] or op.param2 in ban["owners"]:
                pass
            if op.param3 in ban["owners"]:
                cl.inviteIntoGroup(op.param1,[op.param3])
            elif op.param1 in settings["protect"]:
                ban["blacklist"][op.param2] = True
                cl.kickoutFromGroup(op.param1,[op.param2])
#                cl.findAndAddContactsByMid(op.param3)
#                cl.inviteIntoGroup(op.param1,[op.param3])
        if op.type == 24 or op.type == 21:
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if (op.type == 26 or op.type == 25) and op.message.contentType == 0:
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
            if text.lower() == 'help':
                if sender in ban["owners"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif sender in ban["admin"]:
                    helpM = helpm()
                    cl.sendMessage(to, str(helpM))
            if sender in ban["admin"] or sender in ban["owners"]:
                if text.lower() in ['speed','sp']:
                    start = time.time()
                    cl.sendMessage(to, "檢查中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to,"儲存設定成功!")
                elif text.lower() == 'runtime':
                    cl.sendMessage(to, "系統已運作 {}".format(str(format_timespan(time.time() - botStart))))
                elif text.lower() == 'about':
                    try:
                        owner ="u29a4c850447c164474d6826c5b74b990"
                        creator = cl.getContact(owner)
                        ret_ = "╔══[ 關於使用者 ]"
                        ret_ += "\n╠ 使用者名稱 : {}".format(cl.getContact(clMID).displayName)
                        ret_ += "\n╠ 群組數 : {}".format(str(len(cl.getGroupIdsJoined())))
                        ret_ += "\n╠ 好友數 : {}".format(str(len(cl.getAllContactIds())))
                        ret_ += "\n╠ 已封鎖 : {}".format(str(len(cl.getBlockedContactIds())))
                        ret_ += "\n╠══[ 關於本bot ]"
                        ret_ += "\n╠ 版本 : test"
                        ret_ += "\n╠ 製作者 : ꧁༺檸檬𓂀紅茶༻᭄ꦿ࿐Ŧ神氏"
                        ret_ += "\n╚══[ 感謝您的使用 ]"
                        cl.sendMessage(to, str(ret_))
                        cl.sendContact(to,"ua10c2ad470b4b6e972954e1140ad1891")
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔══[ 狀態 ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠ 自動加入好友 ✅"
                        else: ret_ += "\n╠ 自動加入好友 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ 自動退出副本 ✅"
                        else: ret_ += "\n╠ 自動退出副本 ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ 自動已讀 ✅"
                        else: ret_ += "\n╠ 自動已讀 ❌"
                        if settings["mention"] == True: ret_ += "\n╠ 群組狀況提示 ✅"
                        else: ret_ += "\n╠ 群組狀況提示 ❌"
                        if msg.toType==2:
                            G = cl.getGroup(msg.to)
                            if G.id in settings["protect"] : ret_+="\n╠ 踢人保護 ✅"
                            else: ret_ += "\n╠ 踢人保護 ❌"
                            if G.id in settings["qrprotect"] : ret_+="\n╠ 網址保護 ✅"
                            else: ret_ += "\n╠ 網址保護 ❌"
                            if G.id in settings["invprotect"] : ret_+="\n╠ 邀請保護 ✅"
                            else: ret_ += "\n╠ 邀請保護 ❌"
                        if settings["detectMention"] ==True: ret_+="\n╠ 標註偵測 ✅"
                        else: ret_ += "\n╠ 標註偵測 ❌"
                        if settings["reread"] ==True: ret_+="\n╠ 復讀 ✅"
                        else: ret_ += "\n╠ 復讀 ❌"
                        ret_ += "\n╚[ 你以為還有嗎 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() in ['adminlist','admin']:
                    if ban["admin"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ 權限者 ]"
                        for mi_d in ban["admin"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚[ 想要權限請私作者 ]")
                elif text.lower().startswith("say "):
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        cl.sendMessage(to,x[1])
                elif msg.text.lower().startswith("tag "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = text.split(' ')
                    c = int(x[2])
                    for c in range(c):
                        sendMessageWithMention(to, inkey)
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
                    cl.sendMessage(to,"please send a contact")
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
                            cl.sendMessage(msg.to, "[ 名字 ]\n" + contact.displayName +"\n[ 個簽 ]\n" + contact.statusMessage +"\n[ MID ]\n" + contact.mid)
                            cl.sendImageWithURL(msg.to, str("http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus)) 
                            cl.sendImageWithURL(msg.to, str(cl.getProfileCoverURL(ls)))
#==============================================================================#
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "開啟成功")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "關閉成功")
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
                    ret_ = "╔══[ 群組資料 ]"
                    ret_ += "\n╠ 群組名稱 : {}".format(str(group.name))
                    ret_ += "\n╠ 群組 Id : {}".format(group.id)
                    ret_ += "\n╠ 創建者 : {}".format(str(gCreator))
                    ret_ += "\n╠ 群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請中 : {}".format(gPending)
                    ret_ += "\n╠ 網址狀態 : {}".format(gQr)
                    ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ 完 ]"
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
                    ret_ = "╔══[ 群組資料 ]"
                    ret_ += "\n╠ 群組名稱 : {}".format(str(group.name))
                    ret_ += "\n╠ 群組 Id : {}".format(group.id)
                    ret_ += "\n╠ 創建者 : {}".format(str(gCreator))
                    ret_ += "\n╠ 群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請中 : {}".format(gPending)
                    ret_ += "\n╠ 網址狀態 : {}".format(gQr)
                    ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() in ['groupmemberlist','gmember','member']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "╔══[ 成員名單 ]"
                        no = 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ 全部成員共 {} 人]".format(str(no-1))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() in ['grouplist','glist','lg']:
                        groups = cl.groups
                        ret_ = "╔══[ 群組一覽 ]"
                        no = 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ 共 {} 群 ]".format(str(no))
                        cl.sendMessage(to, str(ret_))
#==============================================================================#
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "總共 {} 人".format(str(len(nama))))
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
                elif text.lower() in ['setread','sr']:
                    cl.sendMessage(msg.to, "已讀點設置成功")
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
                elif text.lower() in ['checkread','lookread','lr']:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[已讀的人]:\n%s\n查詢時間:[%s]" % (chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "尚未開啟偵測")
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "╔══[ 黑單成員 ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n╚══[ 完 ]")
                elif text.lower() == 'banmidlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "╔══[ 黑單成員 ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n╠ "+mi_d
                        cl.sendMessage(to,mc + "\n╚[ 完 ]")
                elif text.lower().startswith("nt "):
                    if msg.toType == 2:
                        _name = msg.text.replace("Nt ","")
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendMessage(msg.to,"Not Found")
                        else:
                            for target in targets:
                                try:
                                    sendMessageWithMention(to, target)
                                except:
                                    pass
                elif text.lower() == 'by':
                    cl.sendImageWithURL(to,"https://drive.google.com/drive/folders/1uXYE7_seRZS-Wmzvtpfp-BB3FUB8sDbI?usp=sharing")
                    helpMessage = helpmessage()
                    cl.sendContact(to,helpMessage)
#==============================================================================#
            if sender in ban["owners"]:
                if text.lower() == 'bye':
                    cl.sendMessage(to,"QQ")
                    cl.leaveGroup(msg.to)
                elif text.lower() == 'restart':
                    cl.sendMessage(to, "重啟成功，請重新登入")
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
                elif text.lower() == 'autojoin off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本關閉")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀開啟")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀關閉")
                elif text.lower() == 'prompt on':
                    settings["mention"] = True
                    cl.sendMessage(to,"群組狀況提示開啟")
                elif text.lower() == 'prompt off':
                    settings["mention"] = False
                    cl.sendMessage(to, "群組狀況提示關閉")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to,"復讀開啟")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to,"復讀關閉")
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
                        except:
                            pass
                        cl.sendMessage(to, "踢人保護關閉")
                elif text.lower() == 'detect on':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "已開啟標註偵測")
                elif text.lower() == 'detect off':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "已關閉標註偵測")
                elif text.lower() == 'ban':
                    wait["ban"]=True
                    cl.sendMessage(to,"please send a contact")
                elif text.lower() == 'unban':
                    wait["unban"]=True
                    cl.sendMessage(to,"please send a contact")
                elif text.lower() == 'ban on':
                    wait["keepban"]=True
                    cl.sendMessage(to,"please send contacts")
                elif text.lower() == 'ban off':
                    wait["keepban"]=False
                    cl.sendMessage(to,"stoped ban contacts")
                elif text.lower() == 'unban on':
                    wait["keepunban"]=True
                    cl.sendMessage(to,"please send contacts")
                elif text.lower() == 'unban off':
                    wait["keepunban"]=False
                    cl.sendMessage(to,"stoped unban contacts")
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
                        except:
                            pass
                        cl.sendMessage(to, "網址保護關閉")
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
                        except:
                            pass
                        cl.sendMessage(to, "邀請保護關閉")
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
                    ban["admin"].append(str(inkey))
                    cl.sendMessage(to, "已獲得權限！")
                elif msg.text.lower().startswith("admindel ") or msg.text.lower().startswith("del "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["admin"].remove(str(inkey))
                    cl.sendMessage(to, "已取消權限！")
                elif msg.text.lower().startswith("ii "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    a = 0
                    while(a<10):
                        cl.createGroup("fuck",[inkey])
                        a+=1
                    c = []
                    c =cl.getGroupIdByName("fuck")
                    for gid in c:
                        cl.leaveGroup(gid)
                elif text.startswith("imagetext "):
                                sep = text.split(" ")
                                textnya = text.replace(sep[0] + " ","")   
                                urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                                cl.sendImageWithURL(msg.to, urlnya)
                elif text.lower() == 'loli' :
                            url = "http://rahandiapi.herokuapp.com/imageapi?key=betakey&q=loli"
                            with requests.session() as web:                                    
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("tk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.sendMessage(to,"Fuck you")
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
                            cl.sendMessage(msg.to,"Not Found")
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
                elif text.lower().startswith("inv "):
                    if msg.toType == 2:
                        midd = text.split(' ')
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(to,[midd])
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
                                cl.sendMessage(msg.to,"已加入黑單!")
                            except:
                                cl.sendMessage(msg.to,"添加失敗 !")
                elif text.lower().startswith("ban :"):
                    txt = text.replace("Ban :","")
                    if txt not in ban["owners"] and len(txt) ==33 and txt.startswith("u"):
                        ban["blacklist"][txt] = True
                        cl.sendMessage(msg.to,"已加入黑單!")
                    else:
                        cl.sendMessage(msg.to,"添加失敗 !")
                elif text.lower().startswith("unban :"):
                    txt = text.replace("Unban :","")
                    if txt in ban["blacklist"] :
                        del ban["blacklist"][txt]
                        cl.sendMessage(msg.to,"已刪除黑單!")
                    else:
                        cl.sendMessage(msg.to,"刪除失敗 !")
                elif msg.text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["blacklist"][target]
                            cl.sendMessage(msg.to,"刪除成功 !")
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                elif text.lower() in ['kickban','killban']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                    for tag in ban["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendMessage(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendMessage(msg.to,"Blacklist kicked out")
                elif text.lower() == 'cleanban':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
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
                    p.displayName = contact.displayName
                    p.statusMessage = contact.statusMessage
                    cl.updateProfile(p)
                    cl.updateProfileCoverById(cl.getProfileCoverId(inkey))
                    p.pictureStatus = contact.pictureStatus
                    cl.updateProfileAttribute(8, p.pictureStatus)
                    cl.updateProfilePicture(contact.pictureStatus)
            if text.lower() == 'cc9487':
                if sender in ['ua10c2ad470b4b6e972954e1140ad1891']:
                    sys.exit
                else:
                    pass
#==============================================================================#
        if op.type == 26:
            msg=op.message
            if msg.contentType == 13:
                if settings["getmid"] == True:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    cl.sendMessage(msg.to, "[ 名字 ]\n" + contact.displayName +"\n[ 個簽 ]\n" + contact.statusMessage +"\n[ MID ]\n" + contact.mid)
                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    cl.sendImageWithURL(msg.to, str(path))
                    path = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                    cl.sendImageWithURL(msg.to, str(path))
                if wait["ban"] ==True:
                    if msg._from in ban["owners"]:
                        ban["blacklist"][msg.contentMetadata["mid"]]=True
                        cl.sendMessage(msg.to,"OK")
                        wait["ban"] =False
                if wait["unban"] ==True:
                    if msg._from in ban["owners"]:
                        del ban["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"OK")
                        wait["unban"] =False
                if wait["getmid"] ==True:
                    if msg._from in ban["owners"] or msg._from in ban["admin"]:
                        cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                        wait["getmid"] =False
                if wait["keepban"] ==True:
                    if msg._from in ban["owners"]:
                        ban["blacklist"][msg.contentMetadata["mid"]]=True
                        cl.sendMessage(msg.to,"OK")
                if wait["keepunban"] ==True:
                    if msg._from in ban["owners"]:
                        del ban["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"OK")
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
                if settings["timeline"] == True:
                    try:
                        f = msg.contentMetadata["postEndUrl"].split('userMid=')
                        s = f[1].split('&')
                        txt = msg.contentMetadata["text"]
                        txt += "\n[文章網址]\n" + msg.contentMetadata["postEndUrl"]
                        list=[]
                        list.append(str(msg._from))
                        list.append(str(s[0]))
                        sendMention(msg.to, "[文章分享者]\n @! \n[文章作者]\n @! \n[文章詳情]\n"+txt,list)
                    except:
                        txt = msg.contentMetadata["text"]
                        txt += "\n[文章網址]\n" + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(msg.to,"[文章詳情]\n"+txt)
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
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    sendMention(to,"@! 標毛?", [contact.mid])
                                break
            try:
                msg = op.message
                if settings["reread"] == True:
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
                            msg_dict[msg.id] = {"mtext":"[收回訊息者]\n @! \n[訊息內容]\n"+x,"from":msg._from,"createdTime":time.time(),"mentionee":listt}
                        else:
                            msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":time.time()}
            except Exception as e:
                print(e)
            if msg.contentType == 1:
                if settings["reread"] == True:
                    if 'gif' in msg.contentMetadata.keys()!= None:
                        gif = cl.downloadObjectMsg(msg_id, saveAs="linepy/tmp/{}-image.gif".format(time.time()))
                        msg_dict[msg.id] = {"from":msg._from,"gif":gif,"createdTime":time.time()}
                    else:
                        image = cl.downloadObjectMsg(msg_id, saveAs="linepy/tmp/{}-image.bin".format(time.time()))
                        msg_dict[msg.id] = {"from":msg._from,"image":image,"createdTime":time.time()}
            if msg.contentType == 3:
                if settings["reread"] == True:
                    sound = cl.downloadObjectMsg(msg_id, saveAs="linepy/tmp/{}-sound.mp3".format(time.time()))
                    msg_dict[msg.id] = {"from":msg._from,"sound":sound,"createdTime":time.time()}
            if msg.contentType == 7:
                if settings["reread"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    msg_dict[msg.id] = {"from":msg._from,"stkid": stk_id ,"createdTime":time.time()}
            if msg.contentType == 13:
                if settings["reread"] == True:
                    mid = msg.contentMetadata["mid"]
                    msg_dict[msg.id] = {"from":msg._from,"mid": mid ,"createdTime":time.time()}
            if msg.contentType == 14:
                if settings["reread"] == True:
                    file = cl.downloadObjectMsg(msg_id, saveAs="linepy/tmp/{}-".format(time.time())+msg.contentMetadata['FILE_NAME'])
                    msg_dict[msg.id] = {"from":msg._from,"file":file,"createdTime":time.time()}
#==============================================================================#
        if op.type == 65:
            print ("[ 65 ] REREAD")
            try:
                msg = op.message
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        timeNow = time.time()
                        opi=[]
                        opi.append(msg_dict[msg_id]["from"])
                        if "mtext" in msg_dict[msg_id]:
                            x =msg_dict[msg_id]["mentionee"].split(',')
                            for ic in x:
                                opi.append(ic)
                            cl.sendMessage(at,msg_dict[msg_id]["mentionee"]+"||"+str(msg_dict[msg_id]["mtext"]))
                            sendMention(at,msg_dict[msg_id]["mtext"],opi)
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "text" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n"+str(msg_dict[msg_id]["text"]),opi)
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "image" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一張圖片",opi)
                            cl.sendImage(at, msg_dict[msg_id]["image"])
                            cl.deleteFile(msg_dict[msg_id]["image"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                        if "gif" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一張圖片",opi)
                            cl.sendGIF(at, msg_dict[msg_id]["gif"])
                            cl.deleteFile(msg_dict[msg_id]["gif"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                        if "sound" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一份音檔",opi)
                            cl.sendAudio(at, msg_dict[msg_id]["sound"])
                            cl.deleteFile(msg_dict[msg_id]["sound"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "file" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一個檔案",opi)
                            cl.sendFile(at, msg_dict[msg_id]["file"])
                            cl.deleteFile(msg_dict[msg_id]["file"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "stkid" in msg_dict[msg_id]:
                            path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(msg_dict[msg_id]["stkid"])
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一張貼圖",opi)
                            cl.sendImageWithURL(at,path)
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                        if "mid" in msg_dict[msg_id]:
                            sendMention(at,"[收回訊息者]\n @! \n[訊息內容]\n一則友資",opi)
                            cl.sendContact(at,msg_dict[msg_id]["mid"])
                            cl.sendMessage(at,"收回時間"+str(timeNow - msg_dict[msg_id]["createdTime"])+"秒之前")
                            del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print (e)
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[※]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[※]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
def botRun():
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)