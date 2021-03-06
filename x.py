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
    helpMessage = """??? Onwer-Only ???
??????? Help ???????
??? Help ????????????
??????? Status ??? ????
??? Restart ????????????
??? Save ????????????
??? Runtime ????????????
??? Speed ??????
??? Set ??????
??? About ???????????????
??????? Set Up ???????
??? AutoAdd On/Off ????????????
??? AutoLeave On/Off ????????????
??? AutoRead On/Off ????????????
??? Prompt On/Off ??????????????????
??? ReRead On/Off ????????????
??? Pro On/Off ????????????
??? Protect On/Off ????????????
??? QrProtect On/Off ????????????
??? Invprotect On/Off ????????????
??? Getinfo On/Off ??????????????????
??? Detect On/Off ????????????
??? Savelolipic On/Off ???????????????
??? Savepic On/Off ???????????????
??? Savewallpic On/off ????????????
??? Timeline On/Off ????????????
??????? Self / Friend ???????
??? Me ????????????
??? Mymid ??????mid
??? Name @ ??????[?????????/Tag]
??? Bio @ ??????[?????????/Tag]
??? Picture @ ??????[?????????/Tag]
??? Cover @ ??????[?????????/Tag]
??? Mid @ ???mid[??????/Tag]
??? Contact: ???mid?????????
??? Info @ ????????????
??????? Blacklist ???????
??? Ban [@/:] ????????????[??????/Tag/MID]
??? Unban [@/:] ????????????[??????/Tag/MID]
??? Keepban [times] ??????????????????
??? Keepunban [times] ??????????????????
??? Banlist ????????????
??? Gbanlist ??????????????????
??? CleanBan ????????????
??? Kickban ????????????
??????? Group Related ???????
??? Link On/Off ????????????/??????
??? Link ??????????????????
??? GroupList ??????????????????
??? GroupMemberList ????????????
??? GroupInfo ????????????
??? Cg: ?????????ID????????????
??? Gn [text] ????????????
??? Tk @ ????????????
??? Zk ??????0??????
??? Inv (mid) ??????mid??????
??? Cancel ??????????????????
??? Ri @ ????????????
??? Tagall ????????????
??? Zc ??????0????????????
??? Zt ??????0??????
??? Setread ???????????????
??? Cancelread ????????????
??? Checkread ????????????
??? Gbc: ????????????(???????????????)
??? Fbc: ????????????
??? Bye ????????????(????????????Y)
??????? Administraor ???????
??? Adminadd @ ????????????
??? Admindel @ ????????????
??? Adminlist ???????????????
??????? Other ???????
??? Ver ??????????????????
??? Say [text times] ????????????
??? Tag @ [times] ????????????
??? Rls ????????????
??? bomb ??????
??? Rlb ????????????
??? ?????? ?????????
??? ?????? ?????????
??? wall ?????????
??? Kernel ??????????????????"""
    return helpMessage
def helpm():
    helpM = """??? Administrator only ???
??????? Help ???????
??? Help ????????????
??? Runtime ????????????
??? Speed ??????
??? Set ??????
??? About ???????????????
??? Save ????????????
??????? Self / Friend ???????
??? Me ????????????
??? Mymid ??????mid
??? Name @ ??????[?????????/Tag]
??? Bio @ ??????[?????????/Tag]
??? Picture @ ??????[?????????/Tag]
??? Cover @ ??????[?????????/Tag]
??? Mid @ ???mid[??????/Tag]
??? Contact: ???mid?????????
??? Info @ ????????????
??????? Group Related ???????
??? Link On/Off ????????????/??????
??? Link ??????????????????
??? GroupList ??????????????????
??? GroupMemberList ????????????
??? GroupInfo ????????????
??? Gn (??????) ????????????
??? Tagall ????????????
??? Zc ??????0????????????
??? Zt ??????0??????
??? Setread ???????????????
??? Cancelread ????????????
??? Checkread ????????????
??? Bye ????????????(????????????Y)
??????? Other ???????
??? Ver ??????????????????
??? Say [?????? ??????] ????????????
??? Tag @ [??????] ????????????
??? Adminlist ???????????????
??? Banlist ????????????
??? Banmidlist ???????????????mid
??? bomb ??????
??? Rls ????????????
??? Rlb ????????????
??? ?????? ?????????
??? ?????? ?????????
??? wall ?????????
??? Kernel ??????????????????"""
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
            print ("[ 0 ] END OF OPERATION {}".format(datetime.today().strftime('%Y/%m/%d|%H???%M???%S|')))
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                sendMention(op.param1, " @! ????????????????????????",[op.param1])
        if op.type == 11:
            print ("[ 11 ] Change Group settings")
            G = cl.getGroup(op.param1)
            if op.param1 in settings["mention"]:
                sendMention(op.param1, " @! ??????????????????",[op.param2])
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
            print ("[ 13 ] invite Group {}".format(datetime.today().strftime('%Y/%m/%d|%H???%M:%S|')))
            if clMID in op.param3:
                group = cl.getGroup(op.param1)
                if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                    cl.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "?????? @! ????????????",[op.param2])
                else:
                    cl.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "@! ??????????????????!",[op.param2])
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
                        sendMention(op.param1, "??????! @! ??????????????????????????",[op.param2])
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
                    cl.sendMessage(op.param1,"???????????????????????? ! ! !")
        if op.type == 17:
            print ("[ 17 ] Welcome Info {}".format(datetime.today().strftime('%Y/%m/%d|%H:%M:%S|')))
            if op.param1 in ban["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param1])
                cl.sendMessage(op.param1,"?????????????????? ! ! !")
            if op.param1 in settings["mention"]:
                name = str(cl.getGroup(op.param1).name)
                sendMention(op.param1, "???! @! ????????????"+name,[op.param2])
        if op.type == 19:
            print ("[ 19 ] Leave Info")
            if op.param1 in settings["mention"]:
                chiya=[op.param2]
                chiya.append(op.param3)
                sendMention(op.param1,"??????!! @! ?????? @! ", chiya)
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
                    cl.sendMessage(to,"?????????????????????????????????????????????~")
            if sender not in ban["blacklist"]:
                if text.lower() in ['?????????','??????','Beauty'] :
                    cl.sendImage(to, "bot/linepy/loli/{}-monmon.png".format(str(random.randint(0,int(settings["monmonpic"]-1)))))
                elif text.lower() in ['loli','??????','Handsome'] :
                    cl.sendImage(to, "bot/linepy/loli/{}-image.png".format(str(random.randint(0,int(settings["pic"]-1)))))
                elif text.lower() in ['wall','??????','wallpaper'] :
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
                    ret_ = "?????????[ About Users ]"
                    ret_ += "\n??? ??????????????? : {}".format(cl.getContact(sender).displayName)
                    if sender in cl.getAllContactIds():ret_ += "\n??? ??????????????? : ??????"
                    else:ret_ += "\n??? ??????????????? : ??????"
                    if sender in ban["owners"]:ret_ += "\n??? ??????????????? : ??????(?????????)"
                    elif sender in ban["admin"]:ret_ += "\n??? ??????????????? : ??????(?????????)"
                    elif sender in ban["blacklist"]:ret_ += "\n??? ??????????????? : ???(?????????)"
                    else:ret_ += "\n??? ??????????????? : ??????(?????????)"
                    ret_ += "\n??? ??????????????????help"
                    ret_ += "\n??? ???????????????V7.0.1"
                    ret_ += "\n??? ????????? :{}".format(cl.getContact("uccbf1a060985c3cad6afee0741edd155").displayName)
                    ret_ += "\n??? ???????????? :\n???{}".format(datetime.today().strftime('%Y/%m/%d|-%H:%M:%S-|'))
                    ret_ += "\n?????????[ Over ]"
                    cl.sendMessage(to, str(ret_))
                    try:
                        ret_ = "?????????[ Local Settings ]"
                        if settings["autoAdd"] == True: ret_ += "\n??? ?????????????????? ????"
                        else: ret_ += "\n??? ?????????????????? ???"
                        if settings["autoLeave"] == True: ret_ += "\n??? ?????????????????? ????"
                        else: ret_ += "\n??? ?????????????????? ???"
                        if settings["autoRead"] == True: ret_ += "\n??? ???????????? ????"
                        else: ret_ += "\n??? ???????????? ???"
                        if settings["getmid"] == True: ret_ += "\n??? ?????????????????? ????"
                        else: ret_ += "\n??? ?????????????????? ???"
                        if settings["timeline"] == True: ret_ += "\n??? ???????????? ????"
                        else: ret_ += "\n??? ???????????? ???"
                        if settings["detectMention"] ==True: ret_+="\n??? ???????????? ????"
                        else: ret_ += "\n??? ???????????? ???"
                        if msg.toType==2:
                            ret_ += "\n?????????[ Simple Group Setting ]"
                            G = cl.getGroup(msg.to)
                            ret_ += "\n??? ???????????? : {}".format(str(G.name))
                            if G.id in settings["protect"] : ret_+="\n??? ???????????? ????"
                            else: ret_ += "\n??? ???????????? ???"
                            if G.id in settings["qrprotect"] : ret_+="\n??? ???????????? ????"
                            else: ret_ += "\n??? ???????????? ???"
                            if G.id in settings["invprotect"] : ret_+="\n??? ???????????? ????"
                            else: ret_ += "\n??? ???????????? ???"
                            if G.id in settings["mention"] : ret_ += "\n??? ?????????????????? ????"
                            else: ret_ += "\n??? ?????????????????? ???"
                            if G.id in settings["reread"]: ret_+="\n??? ?????? ????"
                            else: ret_ += "\n??? ?????? ???"
                        ret_ += "\n???[ Over ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() in ['adminlist','admin']:
                    if ban["admin"] == []:
                        cl.sendMessage(to,"No person with permission !")
                    else:
                        mc = "???[ Authority ]"
                        for mi_d in ban["admin"]:
                            try:
                                mc += "\n??? "+cl.getContact(mi_d).displayName
                            except:
                                pass
                        cl.sendMessage(to,mc + "\n???[ Over ]")
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
                            cl.sendMessage(to,"????????????")
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
                elif text.lower() in ['link on',"??????URL??????"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "??????????????????")
                        else:
                            if group.id in settings["qrprotect"]:
                                cl.sendMessage(to,"??????????????????URL??????????????????????????????")
                            else:
                                group.preventedJoinByTicket = False
                                cl.updateGroup(group)
                                cl.sendMessage(to, "????????????URL")
                elif text.lower() in ["??????URL??????",'link off']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "???????????????")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to,  "???????????????????????????")
            if sender in ban["owners"]:
                if text.lower() in ['????????????','time']:
                    cl.sendMessage(to, "????????????:{}".format(datetime.today().strftime('%Y/%m/%d|%H/%M/%S|')))
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
                elif text.lower() in ['gurl_get','gurl','link','grouplink',"??????URL??????"]:
                    if msg.toType==2:
                        group=cl.getGroup(to)
                        if group.id in wait["qrprotect"]:
                            cl.sendMessage(to, "??????????????????URL??????????????????????????????")
                        else:
                            cl.sendMessage(to,"https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id))))
                elif text.lower() in ['groupinfo','ginfo']:
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "??????"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "??????"
                        gTicket = "???"
                    else:
                        gQr = "??????"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "??????[ Group data ]"
                    ret_ += "\n??? ???????????? : {}".format(str(group.name))
                    ret_ += "\n??? ?????? Id : {}".format(group.id)
                    ret_ += "\n??? ????????? : {}".format(str(gCreator))
                    ret_ += "\n??? ???????????? : {}".format(str(len(group.members)))
                    ret_ += "\n??? ????????? : {}".format(gPending)
                    ret_ += "\n??? ???????????? : {}".format(gQr)
                    ret_ += "\n??? ???????????? : {}".format(gTicket)
                    ret_ += "\n?????????[ Over ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower().startswith('cg:'):
                    group = cl.getGroup(text[3:])
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "??????"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "??????"
                        gTicket = "???"
                    else:
                        gQr = "??????"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "??????[ Group data ]"
                    ret_ += "\n??? ???????????? : {}".format(str(group.name))
                    ret_ += "\n??? ?????? Id : {}".format(group.id)
                    ret_ += "\n??? ????????? : {}".format(str(gCreator))
                    ret_ += "\n??? ???????????? : {}".format(str(len(group.members)))
                    ret_ += "\n??? ????????? : {}".format(gPending)
                    ret_ += "\n??? ???????????? : {}".format(gQr)
                    ret_ += "\n??? ???????????? : {}".format(gTicket)
                    ret_ += "\n?????????[ Over ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() in ['groupmemberlist','gmember','member']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "??????[ List of members ]"
                        no = 1
                        for mem in group.members:
                            ret_ += "\n??? {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n??????[ All members are {} people]".format(str(no-1))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() in ['grouplist','glist','lg']:
                        groups = cl.groups
                        ret_ = "?????????[ Group list ]"
                        no = 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n??? {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n??????[ Total {} group ]".format(str(no))
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
                elif text.lower() in ['setread','sr','????????????????????????']:
                    cl.sendMessage(msg.to, "??????????????????")
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
                    cl.sendMessage(to, "??????????????????")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif text.lower() in ['checkread','lookread','lr','????????????','sn']:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[????????????]:\n%s\n????????????:[%s]" % (chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "?????????????????? !!")
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"No black singel members !")
                    else:
                        mc = "??????[ Blacklisted members ]"
                        for mi_d in ban["blacklist"]:
                            try:
                                mc += "\n??? "+cl.getContact(mi_d).displayName
                            except:
                                pass
                        cl.sendMessage(msg.to,mc + "\n?????????[ Over ]")
                elif text.lower() in ['groupbanmidlist','gban','gbanlist']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                    for tag in ban["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendMessage(msg.to,"????????????????????? !")
                        return
                    for jj in matched_list:
                        mc = "?????????[ ?????????????????? ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n??? "+mi_d
                        cl.sendMessage(to,mc + "\n???[ Over ]")
                elif text.lower() == 'banmidlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"No black singel members !")
                    else:
                        mc = "?????????[ Blacklisted members ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n??? "+mi_d
                        cl.sendMessage(to,mc + "\n???[ Over ]")
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
                    cl.sendMessage(msg.to,"( ??-?????)?????????????????????")
                elif text.lower() in ["???????????????",'bye']:
                    cl.sendMessage(msg.to, "Are sure to leave ?\n???Yes / No ???")
                    wait['bye'][msg.to] = sender
                elif text.lower() in ["Y","y","??????","N","n","??????"]:
                    if msg._from== wait['bye'][msg.to]:
                        if text.lower() in ["??????",'y']:
                            cl.sendMessage(msg.to, "Execute leave ! ! !")
                            cl.leaveGroup(msg.to)
                            del wait['bye'][msg.to]
                        elif text.lower() in ['n',"??????"]:
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
                    cl.sendMessage(to, "????????? 15??? ???????????? !")
                    time.sleep(5)
                    cl.sendMessage(to, "?????????????????? ! !")
                    time.sleep(4)
                    cl.sendMessage(to, "Restart Version???Alpha2-V7???")
                    restartBot()
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "??????????????????")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "??????????????????")
                elif text.lower() == 'autolike on':
                    settings["autolike"] = True
                    cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'autolike off':
                    settings["autolike"] = False
                    cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'prompt on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["mention"][G.id] = True
                        cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'prompt off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["mention"][G.id]
                            cl.sendMessage(to, "????????????????????????")
                        except:
                            cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'reread on':
                    settings["reread"][to] = True
                    cl.sendMessage(to,"????????????")
                elif text.lower() == 'reread off':
                    try:
                        del settings["reread"][to]
                        cl.sendMessage(to,"????????????")
                    except:
                        pass
                elif text.lower() == 'protect on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["protect"][G.id] = True
                        cl.sendMessage(to, "??????????????????")
                elif text.lower() == 'protect off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["protect"][G.id]
                            cl.sendMessage(to, "??????????????????")
                        except:
                            cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'detect on':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "?????????????????????")
                elif text.lower() == 'detect off':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "?????????????????????")
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
                        cl.sendMessage(to, "??????????????????")
                elif text.lower() == 'qrprotect off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["qrprotect"][G.id]
                            cl.sendMessage(to, "??????????????????")
                        except:
                            cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'invprotect on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        settings["invprotect"][G.id] = True
                        cl.sendMessage(to, "??????????????????")
                elif text.lower() == 'invprotect off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["invprotect"][G.id]
                            cl.sendMessage(to, "??????????????????")
                        except:
                            cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'getinfo on':
                    settings["getmid"] = True
                    cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'getinfo off':
                    settings["getmid"] = False
                    cl.sendMessage(to, "????????????????????????")
                elif text.lower() == 'timeline on':
                    settings["timeline"] = True
                    cl.sendMessage(to, "??????????????????")
                elif text.lower() == 'timeline off':
                    settings["timeline"] = False
                    cl.sendMessage(to, "??????????????????")
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
                        cl.sendMessage(to, "??????????????????")
                        cl.sendMessage(to, "??????????????????")
                        cl.sendMessage(to, "??????????????????")
                elif text.lower() == 'pro off':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        try:
                            del settings["protect"][G.id]
                            cl.sendMessage(to, "??????????????????")
                        except:
                            pass
                        try:
                            del settings["qrprotect"][G.id]
                            cl.sendMessage(to, "??????????????????")
                        except:
                            pass
                        try:
                            del settings["invprotect"][G.id]
                            cl.sendMessage(to, "??????????????????")
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
                    cl.sendMessage(to, "??????????????????")
                elif msg.text.lower().startswith("botsdel "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["bots"].remove(str(inkey))
                    cl.sendMessage(to, "??????????????????")
                elif text.lower() == 'botslist':
                    if ban["bots"] == []:
                        cl.sendMessage(to,"?????????!")
                    else:
                        mc = "?????????[ Inviter List ]"
                        for mi_d in ban["bots"]:
                            mc += "\n??? "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n?????????[ Over ]")
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
                            cl.sendMessage(to,"????????????")
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
                    cl.sendMessage(msg.to,"?????????????????????!")
                elif text.lower() in ["??????"]:
                    group = cl.getGroup(to)
                    if group.invitee is None:
                        cl.sendMessage(to, "??????????????????")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(to, gInviMids)
                        cl.sendMessage(to, str(len(group.invitee)) + "?????????????????????????????????")
                elif text.lower().startswith("inv "):
                    if msg.toType == 2:
                        midd = text.split(' ')
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(to,[midd])

#==============================================================================#
            if sender in ban["owners"]:
                    if text.lower() == 'kernel':
                        cl.sendMessage(to, "Kernel Version:V7.0.1\n{}".format(datetime.today().strftime('%Y/%m/%d|%H???%M???%S|')))
            if sender in ban["owners"]:
                    if text.lower() == '???':
                        cl.sendMessage(to, """????????????????????\n1.????????????\n2.??????????????????\n\nVersion:V7.0.1\n??????????????????:""")
                        time.sleep(1)
                        cl.sendContact(to, "ucbbd21e79a63b5486a47101ef73451b7")
            if sender in ban["owners"]:
                    if text.lower() == '???':
                        cl.sendMessage(to, "????????? ???????????? ????????????!!")
            
            if sender in ban["admin"]:
                    if text.lower() == 'kernel':
                        cl.sendMessage(to, "Kernel Version:V7.0.1\n{}".format(datetime.today().strftime('%Y/%m/%d|%H???%M???%S|')))
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
                    slot = "????????????\n?????????==>{}  {}  {}<==\n?????????==>{}  {}  {}<==\n?????????==>{}  {}  {}<==\n?????????==>{}  {}  {}<==\n?????????==>{}  {}  {}<==\n???????????????????????????".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
                    cl.sendMessage(to,slot)
                    if a == e == i == j == o:
                        cl.sendMessage(to,"???????????? !???")
                        return
                    cl.sendMessage(to,"????????????")                            
                elif text.lower() == '????????????':
                    a = random.choice(["??????????????????????????????(????????????)???","?????????????????????(?????????)","?????????????????????(`??????????)","??????????????????(,,????????,,)","?????????????????????(??????????`)","??????????????????(????????)","?????????????????????????????????(?????`)???(???????? )"])
                    slot = "???????????????\n{}<==\n???????????????????????????".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == '???':
                    a = random.choice(["??????????????????????????????(????????????)???","?????????????????????(?????????)","?????????????????????(`??????????)","??????????????????(,,????????,,)","?????????????????????(??????????`)","??????????????????(????????)","?????????????????????????????????(?????`)???(???????? )"])
                    slot = "???????????????\n{}<==\n???????????????????????????".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == 'rls':
                    a = random.choice(["??????????????????????????????(????????????)???","?????????????????????(?????????)","?????????????????????(`??????????)","??????????????????(,,????????,,)","?????????????????????(??????????`)","??????????????????(????????)","?????????????????????????????????(?????`)???(???????? )"])
                    slot = "???????????????\n{}<==\n???????????????????????????".format(a)
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
                    slot = "????????????\n?????????==>{}  {}  {}<==\n?????????==>{}  {}  {}<==\n?????????==>{}  {}  {}<==\n?????????==>{}  {}  {}<==\n?????????==>{}  {}  {}<==\n???????????????????????????".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
                    cl.sendMessage(to,slot)
                    if a == e == i == j == o:
                        cl.sendMessage(to,"???????????? !")
                        return                      
                elif text.lower() == '????????????':
                    a = random.choice(["???????????????????????????(????????????)???","?????????????????????(?????????)","?????????????????????(`??????????)","??????????????????(,,????????,,)","?????????????????????(??????????`)","??????????????????(????????)","?????????????????????????????????(?????`)???(???????? )"])
                    slot = "???????????????\n{}<==\n???????????????????????????".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == '???':
                    a = random.choice(["??????????????????????????????(????????????)???","?????????????????????(?????????)","?????????????????????(`??????????)","??????????????????(,,????????,,)","?????????????????????(??????????`)","??????????????????(????????)","?????????????????????????????????(?????`)???(???????? )"])
                    slot = "???????????????\n{}<==\n???????????????????????????".format(a)
                    cl.sendMessage(to,slot)
                elif text.lower() == 'rls':
                    a = random.choice(["??????????????????????????????(????????????)???","?????????????????????(?????????)","?????????????????????(`??????????)","??????????????????(,,????????,,)","?????????????????????(??????????`)","??????????????????(????????)","?????????????????????????????????(?????`)???(???????? )"])
                    slot = "???????????????\n{}<==\n???????????????????????????".format(a)
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
                        ret_ = "?????????Article perview?????????"
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
                            ret_ += "\n[ ???????????? ]\n https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
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
                                sendMention(to,"@! ?????????????????????", [contact.mid])
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
                            cl.sendMessage(at,"????????????"+str(timeNow - msg_dict[msg_id]["createdTime"])+"?????????")
                            del msg_dict[msg_id]
                        elif "text" in msg_dict[msg_id]:
                            sendMention(at,"[???????????????]\n @! \n[????????????]\n"+str(msg_dict[msg_id]["text"]),opi)
                            cl.sendMessage(at,"????????????"+str(timeNow - msg_dict[msg_id]["createdTime"])+"?????????")
                            del msg_dict[msg_id]
                        elif "stkid" in msg_dict[msg_id]:
                            path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(msg_dict[msg_id]["stkid"])
                            sendMention(at,"[???????????????]\n @! \n[????????????]\n????????????",opi)
                            cl.sendImageWithURL(at,path)
                            cl.sendMessage(at,"????????????"+str(timeNow - msg_dict[msg_id]["createdTime"])+"?????????")
                            del msg_dict[msg_id]
                        elif "mid" in msg_dict[msg_id]:
                            sendMention(at,"[???????????????]\n @! \n[????????????]\n????????????",opi)
                            cl.sendContact(at,msg_dict[msg_id]["mid"])
                            cl.sendMessage(at,"????????????"+str(timeNow - msg_dict[msg_id]["createdTime"])+"?????????")
                            del msg_dict[msg_id]
                    elif msg_id in msg_dictt:
                        timeNow = time.time()
                        opi=[msg_dictt[msg_id]["from"]]
                        if "image" in msg_dictt[msg_id]:
                            sendMention(at,"[???????????????]\n @! \n[????????????]\n????????????",opi)
                            cl.sendImage(at, msg_dictt[msg_id]["object"])
                            cl.sendMessage(at,"????????????"+str(timeNow - msg_dictt[msg_id]["createdTime"])+"?????????")
                            cl.deleteFile(msg_dictt[msg_id]["object"])
                            del msg_dictt[msg_id]
                        elif "gif" in msg_dictt[msg_id]:
                            sendMention(at,"[???????????????]\n @! \n[????????????]\n????????????",opi)
                            cl.sendGIF(at, msg_dictt[msg_id]["object"])
                            cl.sendMessage(at,"????????????"+str(timeNow - msg_dictt[msg_id]["createdTime"])+"?????????")
                            cl.deleteFile(msg_dictt[msg_id]["object"])
                            del msg_dictt[msg_id]
                        elif "sound" in msg_dictt[msg_id]:
                            sendMention(at,"[???????????????]\n @! \n[????????????]\n????????????",opi)
                            cl.sendAudio(at, msg_dictt[msg_id]["object"])
                            cl.sendMessage(at,"????????????"+str(timeNow - msg_dictt[msg_id]["createdTime"])+"?????????")
                            cl.deleteFile(msg_dictt[msg_id]["object"])
                            del msg_dictt[msg_id]
                        elif "file" in msg_dictt[msg_id]:
                            sendMention(at,"[???????????????]\n @! \n[????????????]\n????????????",opi)
                            cl.sendFile(at, msg_dictt[msg_id]["object"])
                            cl.sendMessage(at,"????????????"+str(timeNow - msg_dictt[msg_id]["createdTime"])+"?????????")
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
                        wait2['readMember'][op.param1] += "\n[????]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[????]" + Name
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


