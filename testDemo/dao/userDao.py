from util import connectToDB
import datetime

# 修改用户登录时间
def updateLoginT(userName):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    loginTime = datetime.datetime.now()
    print('longinTime:',loginTime)
    sql = 'update {0} set loginTime=%s where userName=%s'.format(tableName)
    rowNum = cursor.execute(sql, (loginTime, userName))
    connect.commit()
    print(rowNum)
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    return False


# 用户登录
def selectByUnameAndPwd(userName,password):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    print(type(tableName))
    # 执行sql语句。表名不能用参数传递%s,用{0}
    sql = "select * from {0} where userName=%s and password=%s".format(tableName)
    rowNum = cursor.execute(sql,(userName,password))
    print("结果：",rowNum)
    if (rowNum != 0):
        # fetchall()返回tuple
        result = cursor.fetchall()
        cursor.close()
        connect.close()
        return result
    cursor.close()
    connect.close()
    return ()


# 用户注册
def createUserInformation(userName,password,regAge,regSex,regEmail,admin):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    regTime = datetime.datetime.now()
    sql = "INSERT INTO {0} (userName,password,regAge,regSex,regEmail,regTime,auSetVol,auSetSpd,auSetVoiPer,auSetPit,admin) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(tableName)
    rowNum = cursor.execute(sql, (userName,password,regAge,regSex,regEmail,regTime,9,4,1,4,admin))
    connect.commit()
    print("注册:",rowNum)
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    return False


# 修改用户基本信息
def updateUserInformation(oldName,newName,regAge,regSex,regEmail):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = "update {0} set userName=%s,regAge=%s,regSex=%s,regEmail=%s where userName=%s".format(tableName)
    rowNum = cursor.execute(sql, (newName,regAge,regSex,regEmail,oldName))
    connect.commit()
    print("修改基本信息：",rowNum)
    cursor.close()
    connect.close()
    if rowNum:
        return True
    return False


# 修改密码
def updatePassword(userName, newPassword):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = "update {0} set password=%s where userName=%s".format(tableName)
    rowNum = cursor.execute(sql, (newPassword,userName))
    connect.commit()
    print(rowNum)
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    return False


# 修改头像
def updateUserPhoto(userID, photoPath):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = 'update {0} set regPhoto=%s where userID=%s'.format(tableName)
    rowNum = cursor.execute(sql, (photoPath,userID))
    connect.commit()
    print(rowNum)
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    return False


# 通过用户名查询用户是否存在。True存在
def selectByUserName(userName):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = 'select * from {0} where userName=%s'.format(tableName)
    rowNum = cursor.execute(sql,(userName,))
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    return False


# 获取用户信息
def getAllUserInformation():
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = 'select * from {0}'.format(tableName)
    rowNum = cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connect.close()
    return result


# 删除用户
def deleteUserInformation(userName):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = "DELETE from {0} where userName=%s".format(tableName)
    rowNum = cursor.execute(sql, (userName,))
    connect.commit()
    if(rowNum != 0):
        return True
    return False


# 管理员修改用户信息
def ManagerEditUserInformation(newName, regSex, regAge, regEmail, admin, oldName):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = "update {0} set userName=%s,regSex=%s,regAge=%s,regEmail=%s,admin=%s where userName=%s".format(tableName)
    rowNum = cursor.execute(sql, (newName,regSex,regAge,regEmail,admin,oldName))
    connect.commit()
    print("管理员修改用户：",rowNum)
    cursor.close()
    connect.close()
    if rowNum:
        return True
    return False


