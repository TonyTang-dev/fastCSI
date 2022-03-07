from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from service import articleCreate,articleRetrieve,articleDelete,articleUpdate,commentRetrieve,commentCreate,commentDelete, commentUpdate
from typing import Optional


# 构建api路由
router=APIRouter()


# 我的文章
class myArticle(BaseModel):
    userName:str

@router.post("/getMyArticle", tags=["articles"])
async def getMyArticle(text:myArticle):
    userName = text.userName
    result = articleRetrieve.getArticle(userName)
    return JSONResponse(
        content={
            'code':200,
            'message':"我的文章",
            'data':result,
        }
    )


# 所有文章
class allArticle(BaseModel):
    userName:str

@router.post("/getAllArticle", tags=["articles"])
async def getAllArticle(text:allArticle):
    userName = text.userName
    result = articleRetrieve.getAllArticle(userName)
    return JSONResponse(
        content={
            'code':200,
            'message':"所有文章",
            'data':result,
        }
    )


# 文章详情
class article(BaseModel):
    postID:int
    userName:str #当前用户的

@router.post("/readArticle", tags=["articles"])
async def readArticle(text:article):
    postID = text.postID
    userName = text.userName
    result = articleRetrieve.readAnArticle(postID,userName)
    return JSONResponse(
        content={
            'code':200,
            'message':"文章详情",
            'data':result,
        }
    )


# 发布文章
class postArticleInfor(BaseModel):
    userName:str
    postTitle:str
    postText:str

@router.post("/postArticle", tags=["articles"])
async def postArticle(text:postArticleInfor):
    userName = text.userName
    postTitle = text.postTitle
    postText = text.postText
    result = articleCreate.uploadArticle(userName,postTitle,postText)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"发布文章",
            'data' : result,
        }
    )


# 获取文章内容
@router.get("/articleText/{postID}", tags=["articles"])
async def articleText(postID):
    print(postID)
    postID = int(postID)
    print(type(postID))
    result = articleRetrieve.getArticleText(postID)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"文章内容文字",
            'data' : result,
        }
    )


# 修改文章
class updateArticles(BaseModel):
    userName:str
    postID:int
    postText:str

@router.post("/editArticle", tags=["articles"])
async def editArticle(text:updateArticles):
    userName = text.userName
    postID = text.postID
    postText = text.postText
    result = articleUpdate.updateArticle(userName,postID,postText)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"修改文章",
            'data' : result,
        }
    )


# 删除文章
class deleteArticles(BaseModel):
    postID: list

@router.post("/deleteArticle", tags=["articles"])
async def deleteArticle(text:deleteArticles):
    postID = text.postID
    result = articleDelete.deleteArticle(postID)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"删除文章",
            'data' : result,
        }
    )


# 我的评论
class myComment(BaseModel):
    userName:str

@router.post("/getMyComment", tags=["comments"])
async def getMyComment(text:myComment):
    userName = text.userName
    result = commentRetrieve.getMyComments(userName)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"我的评论",
            'data' : result,
        }
    )


# 发表评论
class postComment(BaseModel):
    postID:int
    cmText:str
    userName:str #当前用户的

@router.post("/postComment", tags=["comments"])
async def postcomment(text:postComment):
    postID = text.postID
    cmText = text.cmText
    userName = text.userName
    result = commentCreate.postComment(postID,cmText,userName)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"发表评论",
            'data' : result,
        }
    )


# 获取我的评论文字
@router.get('/commentText/{cmID}', tags=['comments'])
async def commentText(cmID):
    cmID = int(cmID)
    result = commentRetrieve.getCommentText(cmID)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"评论内容",
            'data' : result,
        }
    )


# 修改评论
class changeComment(BaseModel):
    cmID:int
    cmText:str
    userName:str

@router.post("/updateComment", tags=["comments"])
async def updateComment(text:changeComment):
    cmID = text.cmID
    cmText = text.cmText
    userName = text.userName
    result = commentUpdate.updateComments(cmID,cmText,userName)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"修改评论",
            'data' : result,
        }
    )


# 删除评论
class deleteComment(BaseModel):
    cmID:list

@router.post("/deleteComment", tags=["comments"])
async def deleteComments(text:deleteComment):
    cmID = text.cmID
    print(cmID)
    result = commentDelete.deleteComments(cmID)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"删除评论",
            'data' : result,
        }
    )


# 展示语音设置
class showVoiceSetting(BaseModel):
    userName:str

@router.post("/voiceSetting", tags=["comments"])
async def voiceSetting(text:showVoiceSetting):
    userName = text.userName
    result = commentRetrieve.getVoiceSetting(userName)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"展示用户语音设置",
            'data' : result,
        }
    )


# 语音设置
class voice(BaseModel):
    userName:str
    auSetVol:Optional[int] = 9 # 音量 0-15
    auSetSpd:Optional[int] = 4 # 语速 0-9
    auSetVoiPer:Optional[int] = 1 # 音色（男、女。。） 0,1,3,4
    auSetPit:Optional[int] = 4 # 语调 0-9

@router.post("/setVoice", tags=["articles"])
async def voiceSet(text:voice):
    userName = text.userName
    spd = text.auSetSpd
    vol = text.auSetVol
    pit = text.auSetPit
    per = text.auSetVoiPer
    result = commentUpdate.setVoice(userName,spd,vol,pit,per)
    return JSONResponse(
        content={
            'code': 200,
            'message' :"语音设置",
            'data' : result,
        }
    )