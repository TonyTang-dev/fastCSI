from dao import itemDao
import json
from util import dataTimeConversion
from service import commentRetrieve, textToVoice

# 发表评论
def postComment(postID,cmText,userName):
    userID = commentRetrieve.getUserID(userName)
    DBdata = itemDao.createComments(postID,userID,cmText,userName)
    if not DBdata:
        return {'status':False, 'feedback':"1数据库连接失败"}
    content = itemDao.getAllComments()
    cmID = 0
    if content:
        for i in content:
            if (i[1]==postID and i[2]==cmText and i[5]==userID and i[6]==userName):
                cmID = i[0]
                cmTime = i[4]
    cmAudio = textToVoice.voiceConversion(userName,cmID,cmText,'cm')
    result = itemDao.createCommentsAudio(cmID,cmAudio)
    if result:
        return {'status':True,'cmID':cmID,'cmText':cmText,'cmAudio':cmAudio,'cmTime':json.dumps(cmTime,cls=dataTimeConversion.DateEncoder),'userID':userID,'userName':userName}
    return {'status':False, 'feedback':"数据库连接失败"}



