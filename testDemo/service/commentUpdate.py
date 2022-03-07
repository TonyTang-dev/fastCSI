from dao import itemDao
from util import deleteLocalFile
from util.httpStatic import localFile
from service import textToVoice

# 修改评论
def updateComments(cmID,cmText,userName):
    deleteLocalFile.deleteLocalFiles(localFile+'audio/cm'+str(cmID)+'.mp3')
    cmAudio = textToVoice.voiceConversion(userName,cmID,cmText,'cm')
    result = itemDao.updateComment(cmID,cmText,cmAudio)
    if result:
        return {'status':True,'cmID':cmID,'cmText':cmText,'cmAudio':cmAudio}
    return {'status':False, 'feedback':"数据库连接失败"}


# 语音设置：语速、音量、音调、男女
# spd:语速  vol:音量(0-15,0最小音)  pit:音调  per:男女声(0女，1男)
def setVoice(userName,spd, vol, pit, per):
    result = itemDao.setVoiceByUserName(userName,spd,vol,pit,per)
    if result:
        return {'status':True,'spd':spd,'vol':vol,'pit':pit,'per':per}
    return {'status':False, 'feedback':"设置失败"}