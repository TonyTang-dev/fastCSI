from dao import itemDao
from service import textToVoice
from util import deleteLocalFile
from util.httpStatic import localFile

# 修改文章
def updateArticle(userName,postID,postText):
    DBdata = itemDao.updateArticleByPostID(postID,postText)
    if not DBdata:
        return {'status':False, 'feedback':'数据库连接失败'}
    deleteLocalFile.deleteLocalFiles(localFile+'audio/article'+str(postID)+'.mp3')
    postAudio = textToVoice.voiceConversion(userName,postID,postText,'article')
    result = itemDao.uploadArticleAudio(postID, postAudio)
    if result:
        return {'status':True, 'postID':postID, 'postAudio':postAudio}
    return {'status':False, 'feedback':'数据库连接失败'}