from dao import itemDao
from util import deleteLocalFile
from util.httpStatic import localFile

# 删除评论
def deleteComments(cmID):
    print(cmID)
    for i in cmID:
        deleteLocalFile.deleteLocalFiles(localFile+'audio/cm'+str(i)+'.mp3')
        DBdata = itemDao.deleteCommentByCmID(i)
    if DBdata:
        return {'status':True, 'feedback':"删除成功"}
    return {'status':False, 'feedback':"删除失败"}