from util import connectToDB
import datetime


# 通过用户名查找我的文章
def selectArticleByUserName(userName):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.articleDBName()
    cursor.rownumber = 0
    sql = 'select * from {0} where userName=%s'.format(tableName)
    rowNum = cursor.execute(sql, (userName,))
    cursor.rownumber = 0
    if(rowNum != 0):
        result = cursor.fetchall()
        cursor.rownumber = 0
        cursor.close()
        connect.close()
        return result
    cursor.rownumber = 0
    cursor.close()
    connect.close()
    return ()


# 获得所有文章
def selectAllArticle():
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.articleDBName()
    sql = 'select * from {0}'.format(tableName)
    rowNum = cursor.execute(sql)
    if(rowNum != 0):
        result = cursor.fetchall()
        cursor.close()
        connect.close()
        return result
    cursor.close()
    connect.close()
    return ()


# 发表文章
def uploadArticleInformation(userName,postTitle,postText):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.articleDBName()
    postTime = datetime.datetime.now()
    sql = 'insert into {0} (postTitle,postText,postPageviews,postTime,userName) values (%s,%s,%s,%s,%s)'.format(tableName)
    rowNum = cursor.execute(sql,(postTitle,postText,0,postTime,userName))
    connect.commit()
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    else:
        return False


# 文章语音
def uploadArticleAudio(postID,postAudio):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.articleDBName()
    sql = 'update {0} set postAudio=%s where postID=%s'.format(tableName)
    rowNum = cursor.execute(sql,(postAudio,postID))
    connect.commit()
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    else:
        return False


# 语音设置
def setVoiceByUserName(userName, spd, vol, pit, per):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = 'update {0} set auSetVol=%s,auSetSpd=%s,auSetVoiPer=%s,auSetPit=%s where userName=%s'.format(tableName)
    rowNum = cursor.execute(sql,(vol,spd,per,pit,userName))
    connect.commit()
    cursor.close()
    connect.close()
    if(rowNum != 0):
        return True
    return False


# 获取语音设置信息
def getMyVoiceSettingByUname(userName):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = 'select * from {0} where userName=%s'.format(tableName)
    rowNum = cursor.execute(sql, (userName,))
    if (rowNum != 0):
        result = cursor.fetchall()
        cursor.close()
        connect.close()
        return result
    cursor.close()
    connect.close()
    return ()


# 修改文章
def updateArticleByPostID(postID,postText):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.articleDBName()
    sql = 'update {0} set postText=%s where postID=%s'.format(tableName)
    rowNum = cursor.execute(sql,(postText,postID))
    connect.commit()
    cursor.close()
    connect.close()
    if(rowNum != 0):
        return True
    return False


# 删除文章
def deleteArticleByPostID(postID):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.articleDBName()
    sql = 'delete from {0} where postID=%s'.format(tableName)
    rowNum = cursor.execute(sql,(postID,))
    connect.commit()
    cursor.close()
    connect.close()
    if(rowNum != 0):
        return True
    return False


# 查询用户是否是文章作者
def findAuthorNameByPostID(postID):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.articleDBName()
    sql = 'select * from {0} where postID=%s'.format(tableName)
    rowNum = cursor.execute(sql, (postID,))
    if (rowNum != 0):
        result = cursor.fetchall()
        cursor.close()
        connect.close()
        return result
    cursor.close()
    connect.close()
    return ()


# 我的评论
def getMyCommentsByUserID(userID):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.commentDBName()
    sql = 'select * from {0} where userID=%s'.format(tableName)
    rowNum = cursor.execute(sql, (userID,))
    if(rowNum != 0):
        result = cursor.fetchall()
        cursor.close()
        connect.close()
        return result
    cursor.close()
    connect.close()
    return ()


# 发表评论
def createComments(postID,userID,cmText,userName):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.commentDBName()
    cmTime = datetime.datetime.now()
    sql = 'insert into {0} (postID,cmText,cmTime,userID,userName) values (%s,%s,%s,%s,%s)'.format(tableName)
    rowNum = cursor.execute(sql,(postID,cmText,cmTime,userID,userName))
    connect.commit() # 执行insert into后，就fetchall()获取不到数据
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    return False


# 获取用户ID
def getUserIDByUname(userName):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = 'select * from {0} where userName=%s'.format(tableName)
    rowNum = cursor.execute(sql, (userName,))
    result = cursor.fetchall()
    cursor.close()
    connect.close()
    return result


# 获取所有评论
def getAllComments():
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.commentDBName()
    sql = 'select * from {0}'.format(tableName)
    rowNum = cursor.execute(sql)
    if(rowNum != 0):
        result = cursor.fetchall()
        cursor.close()
        connect.close()
        return result
    cursor.close()
    connect.close()
    return ()


# 评论语音
def createCommentsAudio(cmID, cmAudio):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.commentDBName()
    sql = 'update {0} set cmAudio=%s where cmID=%s'.format(tableName)
    rowNum = cursor.execute(sql,(cmAudio,cmID))
    connect.commit()
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    else:
        return False


# 修改评论
def updateComment(cmID,cmText,cmAudio):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.commentDBName()
    sql = 'update {0} set cmText=%s,cmAudio=%s where cmID=%s'.format(tableName)
    rowNum = cursor.execute(sql, (cmText,cmAudio,cmID))
    connect.commit()
    cursor.close()
    connect.close()
    if (rowNum != 0):
        return True
    return False


# 删除评论
def deleteCommentByCmID(cmID):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.commentDBName()
    sql = 'delete from {0} where cmID=%s'.format(tableName)
    rowNum = cursor.execute(sql,(cmID,))
    connect.commit()
    cursor.close()
    connect.close()
    if(rowNum != 0):
        return True
    return False


# 查看权限
def getAdminInformation(userName):
    connect = connectToDB.connectToDB()
    cursor = connect.cursor()
    tableName = connectToDB.userDBName()
    sql = 'select * from {0} where userName=%s'.format(tableName)
    rowNum = cursor.execute(sql, (userName,))
    if (rowNum != 0):
        result = cursor.fetchall()
        cursor.close()
        connect.close()
        return result
    cursor.close()
    connect.close()
    return ()