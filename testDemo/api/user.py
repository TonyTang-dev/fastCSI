from fastapi import APIRouter, File, UploadFile, Form
from pydantic.networks import EmailStr
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from service import userDelete, userRetrieve, userCreate, userUpdate
from fastapi.staticfiles import StaticFiles
from dao import itemDao
from util.httpStatic import address


# 构建api路由
router = APIRouter()

MANAGER_KEY = "8080"

# 登录
class token(BaseModel):
    userName: str
    password: str

@router.post("/login", tags=["users"])
async def login(text: token):
    userName = text.userName
    password = text.password
    result = userRetrieve.login(userName,password)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"登录",
            'data' : result,
        }
    )


# 注册
class createUser(BaseModel):
    userName:str
    password:str
    regAge:int
    regSex:str
    regEmail:EmailStr
    managerKey:str

@router.post("/createUser", tags=["users"])
async def createUsers(text: createUser):
    userName = text.userName
    password = text.password
    regAge = text.regAge
    regSex = text.regSex
    regEmail = text.regEmail
    managerKey = text.managerKey
    if (managerKey == MANAGER_KEY):
        result = userCreate.userRegister(userName,password,regAge,regSex,regEmail,'1')
    else:
        result = userCreate.userRegister(userName,password,regAge,regSex,regEmail,'0')
    print(result)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"注册",
            'data' : result,
        }
    )


# 忘记密码
class dropPassword(BaseModel):
    userName:str
    regEmail:EmailStr
    newPassword:str

@router.post("/forgetPassword", tags=["users"])
async def forgetPassword(text:dropPassword):
    userName = text.userName
    regEmail = text.regEmail
    newPassword = text.newPassword
    result = userUpdate.updateUserPassword(userName,regEmail,newPassword)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"忘记密码",
            'data' : result,
        }
    )


# 展示用户基本信息
class showUserInformation(BaseModel):
    userName:str

@router.post("/getUserInfor", tags=["users"])
async def showUserInfor(text:showUserInformation):
    userName = text.userName
    result = userRetrieve.getUserInfor(userName)
    return JSONResponse(
        content={
            'code': 200,
            'message': "展示用户基本信息",
            'data': result,
        }
    )


# 修改用户基本信息
class updateUserInformation(BaseModel):
    oldName:str
    newName:str
    regAge:int
    regSex:str
    regEmail:EmailStr

@router.post("/updateUser", tags=["users"])
async def updateUser(text:updateUserInformation):
    oldName = text.oldName
    newName = text.newName
    regAge = text.regAge
    regSex = text.regSex
    regEmail = text.regEmail
    result = userUpdate.updateUserInfor(oldName,newName,regAge,regSex,regEmail)
    return JSONResponse(
        content={
            'code': 200,
            'message': "修改基本信息",
            'data': result,
        }
    )


# 修改密码
class userPassword(BaseModel):
    userName:str
    oldPassword:str
    newPassword:str

@router.post("/updatePassword", tags=["users"])
async def updatePassword(text:userPassword):
    userName = text.userName
    oldPassword = text.oldPassword
    newPassword = text.newPassword
    result = userUpdate.updatePassword(userName,oldPassword,newPassword)
    return JSONResponse(
        content={
            'code':200,
            'message':"修改密码",
            'data':result,
        }
    )


# 用户列表
@router.get("/getAllUserInfor/{userName}", tags=["users"])
async def getAllUser(userName):
    print(userName)
    result = userRetrieve.getAllUserInfor(userName)
    return JSONResponse(
        content={
            'code':200,
            'message':"用户列表",
            'data':result,
        }
    )
    

# 管理员 删除用户
class deleteUsers(BaseModel):
    userName: list

@router.post("/deleteUser", tags=["users"])
async def deleteUser(text: deleteUsers):
    userName = text.userName
    result = userDelete.deleteUserInfor(userName)
    return JSONResponse(
        content={
            'code':200,
            'message':"删除用户",
            'data':result,
        }
    )


# 管理员 展示用户信息
class showUsers(BaseModel):
    userName: str

@router.post("/managerGetUserInfor", tags=["users"])
async def showUserInfor(text:showUsers):
    userName = text.userName
    result = userRetrieve.managerGetUserInfor(userName)
    return JSONResponse(
        content={
            'code': 200,
            'message': "展示用户基本信息",
            'data': result,
        }
    )


# 管理员编辑用户
class editUser(BaseModel):
    newName: str
    regSex: str
    regAge: int
    regEmail: EmailStr
    admin: str
    oldName: str

@router.post("/editUserInfor", tags=["users"])
async def editUsers(text: editUser):
    newName = text.newName
    regSex = text.regSex
    regAge = text.regAge
    regEmail = text.regEmail
    admin = text.admin
    oldName = text.oldName
    if(admin == '普通用户'):
        admin = '0'
    else:
        admin = '1'
    result = userUpdate.managerEditUserInfor(newName, regSex, regAge, regEmail, admin, oldName)
    return JSONResponse(
        content={
            'code':200,
            'message':"删除用户",
            'data':result,
        }
    )


# 我的设置
class mySet(BaseModel):
    userName: str

@router.post("/mySetting", tags=["users"])
async def editUsers(text: mySet):
    userName = text.userName
    result = userRetrieve.mySetting(userName)
    return JSONResponse(
        content={
            'code':200,
            'message':"我的设置",
            'data':result,
        }
    )


# 修改头像
from main import app
# 挂载静态资源，所有语音、图片存在服务器本地
app.mount('/static', StaticFiles(directory='D://VSCodePython/testDemo/statics'), name='a')

@app.post("/api/updatePhoto",tags=["users"])
async def updatePhoto(file:UploadFile=File(...), userName:str=Form(...)):
    DBdata = itemDao.getUserIDByUname(userName)
    userID = None
    for i in DBdata:
        if (i[1] == userName):
            userID = i[0]
    contents = await file.read()
    with open('D://VSCodePython/testDemo/statics/images/'+str(userID)+'.jpg', 'wb') as f:
        f.write(contents)
    photoPath = address +'/static/images/'+str(userID)+'.jpg'
    result = userUpdate.updateUserPhoto(userID,photoPath)
    return JSONResponse(
        content={
            'code':200,
            'message':"修改头像",
            'data':result,
        }
    )