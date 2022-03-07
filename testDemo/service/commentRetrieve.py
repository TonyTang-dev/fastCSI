from dao import itemDao
import json
from util import dataTimeConversion

# 我的评论
def getMyComments(userName):
    userID = getUserID(userName)
    DBdata = itemDao.getMyCommentsByUserID(userID)
    result = []
    postTitle = ''
    if DBdata:
        for i in DBdata:
            if(i[6] == userName):
                titles = itemDao.selectAllArticle()
                for j in titles:
                    if(j[0] == i[1]):
                        postTitle = j[1]
                result.append({'status':True,'cmID':i[0],'postID':i[1],'cmText':i[2],'cmAudio':i[3],'cmTime':json.dumps(i[4],cls=dataTimeConversion.DateEncoder),'postTitle':postTitle})
    else:
        result.append({'status':False,'feedback':'您未发表评论'})
    return result
    

# 展示用户语音设置
def getVoiceSetting(userName):
    DBdata = itemDao.getMyVoiceSettingByUname(userName)
    if DBdata:
        for i in DBdata:
            if(i[1] == userName):
                return {'status':True,'auSetVol':i[9],'auSetSpd':i[10],'auSetVoiPer':i[11],'auSetPit':i[12]}
    return {'status':False, 'feedback':'数据库连接失败'}


# 获取用户ID
def getUserID(userName):
    DBdata = itemDao.getUserIDByUname(userName)
    for i in DBdata:
        if(i[1] == userName):
            return i[0]
    return None


# 通过评论ID获取评论文字
def getCommentText(cmID):
    DBdata = itemDao.getAllComments()
    cmText = ''
    for i in DBdata:
        if(cmID == i[0]):
            cmText = i[2]
    return cmText
