from dao import itemDao
from util import deleteLocalFile
from util.httpStatic import localFile

# 删除文章
def deleteArticle(postID):
    result = True
    for i in postID:
        deleteLocalFile.deleteLocalFiles(localFile+'audio/article'+str(i)+'.mp3')
        result = itemDao.deleteArticleByPostID(i) & itemDao.deleteArticleAudioByPostID(i)
    if result:
        return {'status':True, 'feedback':"删除成功"}
    return {'status':False, 'feedback':"删除失败"}
