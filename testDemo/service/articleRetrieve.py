from api import item
from dao import itemDao
from dao import userDao
import json
from util import dataTimeConversion


# 通过用户名查找我的文章
def getArticle(userName):
    DBdata = itemDao.selectArticleByUserName(userName)
    result = []
    if DBdata:
        for i in DBdata:
            if(i[6] == userName):
                result.append({'status':True,'postID':i[0],'postTitle':i[1],'postAudio':i[4],'postTime':json.dumps(i[5],cls=dataTimeConversion.DateEncoder),'userName':userName})
    else:
        result.append({'status':False,'feedback':'您未发布文章'})
    return result


# 获取文章内容
def getArticleText(postID):
    DBdata = itemDao.selectAllArticle()
    result = None
    for i in DBdata:
        if(i[0] == postID):
            result = i[2]
    return {'status':True, 'postText':result}


# 获得所有文章
def getAllArticle(userName):
    result = []
    data = itemDao.getAdminInformation(userName)
    for j in data:
        if(j[1] == userName):
            admin = j[13]
            result.append({'status':True,'admin':admin})
    DBdata = itemDao.selectAllArticle()
    if DBdata:
        for i in DBdata:
            userInfor = userDao.getAllUserInformation()
            for k in userInfor:
                if(k[1] == i[6]):
                    regPhoto = k[6]
            result.append({'postID':i[0],'userName':i[6],'postTitle':i[1],'postAudio':i[4],'postTime':json.dumps(i[5],cls=dataTimeConversion.DateEncoder),'regPhoto':regPhoto})
    else:
        result[0]['status'] = False
        result[0].update({'feedback':'无'})
    return result


# 阅读文章
def readAnArticle(postID,userName):
    DBdata = itemDao.selectAllArticle()
    result = []
    users = userDao.getAllUserInformation()
    admin = '0'
    for k in users:
        if(k[1] == userName):
            # 获取用户权限：是否是管理员
            admin=k[13]
    if DBdata:
        for i in DBdata:
            if(i[0] == postID):
                comments = itemDao.getAllComments()
                comment = []
                for j in comments:
                    if(postID == j[1]):
                            # 评论信息
                            comment.append({'cmID':j[0], 'cmAudio':j[3], 'cmTime':json.dumps(j[4],cls=dataTimeConversion.DateEncoder), 'cmUserID':j[5], 'cmUserName':j[6],'cmUserPhoto':k[6]})
                for m in users:
                    if(m[1] == i[6]):
                    # 获取文章状态、权限信息
                        authorPhoto = m[6]
                # 文章信息
                result.append({'status':True, 'userAdmin':admin})
                result.append({'postID':postID,'postTitle':i[1],'postAudio':i[4],'postTime':json.dumps(i[5],cls=dataTimeConversion.DateEncoder),'authorUserName':i[6],'authorPhoto':authorPhoto})
                result.append(comment)
    else:
        result.append([{'status':False,'feedback':'无'}])
    return result
