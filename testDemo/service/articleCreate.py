from dao import itemDao
from util import dataTimeConversion
from service import textToVoice
import json

# 发表文章
def uploadArticle(userName,postTitle,postText):
    DBdata = itemDao.uploadArticleInformation(userName,postTitle,postText)
    if not DBdata:
        return {'status':False, 'feedback':"数据库连接失败"}
    content = itemDao.selectAllArticle()
    postID = 0
    if content:
        for i in content:
            if (i[1]==postTitle and i[2]==postText and i[6]==userName):
                postID = i[0]
                postTime = i[5]
    postAudio = textToVoice.voiceConversion(userName,postID,postText,'article')
    result = itemDao.uploadArticleAudio(postID, postAudio)
    if result:
        return {'status':True,'postID':postID,'postTitle':postTitle,'postTime':json.dumps(postTime,cls=dataTimeConversion.DateEncoder),'postAudio':postAudio}
    return {'status':False, 'feedback':"数据库连接失败"}
