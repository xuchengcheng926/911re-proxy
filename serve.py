from fastapi import FastAPI
import uvicorn as uvicorn
import requests
import os 
import sys
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
import json



area=["-changeproxy/FR/IDF/Paris","-changeproxy/DE/BE/Berlin","-changeproxy/GB/ENG/London"]
error_dict={
    '5000':0,
    '5001':0,
    '5002':0,
    '5003':0,
    '5004':0,
    '5005':0,
    '5006':0,
    '5007':0,
    '5008':0,
    '5009':0,
    '5010':0,
    '5011':0,
    '5012':0,
    '5013':0,
    '5014':0,
    '5015':0,
    '5016':0,
    '5017':0,
    '5018':0,
    '5019':0,
    '5020':0,
    '5021':0,
    '5022':0,
    '5023':0,
    '5024':0,
    '5025':0,
    '5026':0,
    '5027':0,
    '5028':0,
    '5029':0,
    '5030':0,
    'totol':0
}

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

def portchange(port):
    error_dict[port]=error_dict[port]+1
    if error_dict[port] > 10 :
        error_dict['totol']=error_dict['totol']+1
        error_dict[port]=0
        os.system(f"C:\\Users\\Administrator\\Desktop\\create.bat {port}")
        try:
            print("")
            requests.get("http://pushplus.hxtrip.com/send",params={"token":"d4caebf0eac54e39897337ba1679f3d9", "title":"911re port change","content":f"{port}","template":"html"})
        except:
            pass
        
    print(str(port))
    print(error_dict)

@app.get("/check/911re")
async def read_root(erro_port):
    erro_port=str(int(erro_port)-45891)
    portchange(erro_port)
   



if __name__ == '__main__':
    uvicorn.run(app='serve:app', host="des.chengs.tk", port=14856, reload = True)

