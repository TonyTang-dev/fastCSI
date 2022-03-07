from dao import userDao

def deleteUserInfor(userName):
    DBdata = True
    for i in userName:
        DBdata = userDao.deleteUserInformation(i)
    if DBdata:
        return {'status':True, 'feedback':"删除成功"}
    return {'status':False, 'feedback':"删除失败"}