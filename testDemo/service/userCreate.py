from dao import userDao
from service import userRetrieve
from util import passwordMD5

# 用户注册
def userRegister(userName,password,regAge,regSex,regEmail,admin):
    print(admin)
    if_exist = userRetrieve.retrieveUserByName(userName)
    if if_exist:
        return {'status':False, 'feedback':"用户名已存在"}
    passwordII = passwordMD5.passwordToMD5(password)
    result = userDao.createUserInformation(userName,passwordII,regAge,regSex,regEmail,admin)
    if result:
        return {'status':True, 'feedback':userName}
    else:
        return {'status':False, 'feedback':'数据库连接失败'}