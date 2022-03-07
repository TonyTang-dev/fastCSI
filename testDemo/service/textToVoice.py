from aip import AipSpeech
from dao import itemDao
from util.httpStatic import address

# dao的user.py已经挂载了静态资源，不必再次挂载
#from main import app   
#app.mount('/static', StaticFiles(directory='D://VSCodePython/testDemo/statics'), name='a')

# 文本转语音
def voiceConversion(userName,ID,Text,sign):
    APP_ID = '24538239'
    API_KEY = 'Ft1XhuuvEnSLmFtANGB5SAuO'
    SECRET_KEY = 'siYBfD8wu3QTGPpfeSW6epbkWaqFquBZ'
    client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
    arguments = itemDao.getMyVoiceSettingByUname(userName)
    voice = None
    for i in arguments:
        if(i[1] == userName):
            voice = i
    # 'zh':中文  1:固定参数,web端为1 
    result = client.synthesis(Text,'zh',1,{'spd':voice[10],'vol':voice[9],'per':voice[11],'pit':voice[12]})
    fileName = 'D://VSCodePython/testDemo/statics/audio/'+sign+str(ID)+'.mp3'
    if not isinstance(result, dict):
        with open(fileName, 'wb') as f:
            f.write(result)
    audioPath = address+'/static/audio/'+sign+str(ID)+'.mp3'
    return audioPath