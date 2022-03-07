from dao import userDao
from service import userRetrieve
from util import passwordMD5

# 忘记密码
def updateUserPassword(userName,regEmail,newPassword):
    UnameExist = userRetrieve.retrieveUserByName(userName)
    if not UnameExist:
        return {'status':False, 'feedback':"用户名不存在"}
    DBdata = userDao.getAllUserInformation()
    EmailExist = False
    if DBdata:
        for i in DBdata:
            if(i[1]==userName and i[5]==regEmail):
                EmailExist = True
    if not EmailExist:
        return {'status':False, 'feedback':"邮箱地址错误"}
    newPasswordII = passwordMD5.passwordToMD5(newPassword)
    result = userDao.updatePassword(userName, newPasswordII)
    if result:
        return {'status':True, 'feedback':"密码修改成功"}
    else:
        return {'status':False, 'feedback':"密码修改失败"}


# 修改用户基本信息
def updateUserInfor(oldName,newName,regAge,regSex,regEmail):
    if_exist = userRetrieve.retrieveUserByName(newName)
    if if_exist:
        return {'status':False, 'feedback':"该用户名已被使用"}
    result = userDao.updateUserInformation(oldName,newName,regAge,regSex,regEmail)
    if result:
        return {'status':True, 'userName':newName,'regAge':regAge,'regSex':regSex,'regEmail':regEmail}
    else:
        return {'status':False, 'feedback':"数据库连接失败"}


# 修改密码。检验旧密码是否正确
def updatePassword(userName, oldPassword, newPassword):
    DBdata = userDao.getAllUserInformation()
    if_exist = True
    for i in DBdata:
        if(i[1]==userName and i[2]==passwordMD5.passwordToMD5(oldPassword)):
            if_exist = True    
    if not if_exist:
        return {'status':False, 'feedback':"密码错误"}
    newPasswordII = passwordMD5.passwordToMD5(newPassword)
    result = userDao.updatePassword(userName, newPasswordII)
    if result:
        return {'status':True, 'feedback':"密码修改成功"}
    else:
        return {'status':False, 'feedback':"密码修改失败"}
    

# 修改头像
def updateUserPhoto(userID,photoPath):
    result = userDao.updateUserPhoto(userID,photoPath)
    return {'status':True, 'feedback':"头像修改成功", 'regPhoto':photoPath}


# 管理员修改用户信息
def managerEditUserInfor(newName, regSex, regAge, regEmail, admin, oldName):
    result = userDao.ManagerEditUserInformation(newName, regSex, regAge, regEmail, admin, oldName)
    if result:
        return {'status': True, 'feedback': "修改成功"}
    return {'status': False, 'feedback': "修改失败"}