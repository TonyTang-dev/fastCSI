from dao import userDao
from util import passwordMD5
import json
from util import dataTimeConversion

# 用户登录
def login(userName, password) :
    if_exist = retrieveUserByName(userName)
    if not if_exist:
        return {'status':False, 'feedback':"用户不存在"}
    passwordII = passwordMD5.passwordToMD5(password)
    DBdata = userDao.selectByUnameAndPwd(userName,passwordII)
    if DBdata:
        for i in DBdata :
            if(i[1] == userName and i[2]==passwordII) :
                #修改登录时间
                userDao.updateLoginT(userName)
                return {'status':True,'id':i[0], 'userName':i[1],'admin':i[13]}
    return {'status':False, 'feedback':"密码错误"}


# 某用户基本信息
def getUserInfor(userName):
    DBdata = userDao.getAllUserInformation()
    result = ()
    if DBdata:
        for i in DBdata:
            if(i[1]==userName):
                result += (i[1],i[3],i[4],i[5],i[6],json.dumps(i[7],cls=dataTimeConversion.DateEncoder))
                return result
    return result


# 用户是否存在。True存在
def retrieveUserByName(userName) :
    DBdata = userDao.selectByUserName(userName)
    if DBdata:
        return True
    return False


# 普通用户列表 JWT验证
def getAllUserInfor(userName):
    DBdata = userDao.getAllUserInformation()
    result = []
    for i in DBdata:
        if(i[1] != userName):
            result.append([i[0],i[1],i[6],json.dumps(i[7],cls=dataTimeConversion.DateEncoder),json.dumps(i[8],cls=dataTimeConversion.DateEncoder),i[13]])
    return result


# 管理员 用户信息
def managerGetUserInfor(userName):
    DBdata = userDao.getAllUserInformation()
    result = []
    if DBdata:
        for i in DBdata:
            if(i[1]==userName):
                result.append((i[1],i[2],i[3],i[4],i[5],i[6],i[13]))
                return result
    return result


# 我的设置
def mySetting(userName):
    DBdata = userDao.getAllUserInformation()
    result = '0'
    for i in DBdata:
        if(i[1] == userName):
            result = i[13]
    return {'admin': result}