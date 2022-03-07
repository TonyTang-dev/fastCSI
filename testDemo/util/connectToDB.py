import pymysql

def connectToDB():
    # 连接数据库
    connect = pymysql.connect(#host='127.0.0.1',
                        host='192.168.1.106',
                        #host ='192.168.1.10',
                        user='root',  # 数据库用户名
                        passwd='root',  # 密码
                        #passwd='1109an109',
                        db='app',  # 数据库名称
                        port=3306)
    return connect

def userDBName():
    return "userinformation"

def articleDBName():
    return "postinformation"

def commentDBName():
    return "cminformation"