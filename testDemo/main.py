import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api import user,item

app = FastAPI()


#配置跨域
origins = ["*"]  


app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"])  

# 注册api路由
# prefix:前缀,请求的URL；在后面使用user.router接口时就要在URL后面加上/api
app.include_router(user.router,prefix="/api")
app.include_router(item.router,prefix="/api")



if __name__ == '__main__':

    uvicorn.run(app='main:app', host='192.168.1.112', port=8000, reload=True)
    
    
