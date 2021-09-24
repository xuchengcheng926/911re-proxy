from fastapi import FastAPI
import uvicorn as uvicorn
import os
import requests


push_tk=""
host_name=""
app = FastAPI()

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
}

def portchange(port):
    error_dict[port]=error_dict[port]+1
    if error_dict[port] > 6 :
        error_dict[port]=0
        os.system(f"C:\\Users\\Administrator\\Desktop\\create.bat {port}")
        request.get("http://pushplus.hxtrip.com/send", params={"token":push_tk,"title":"911re port change","content":f"{port}","template":"html"})
    print(error_dict)
    

@app.get("/check/911re")
async def read_root(erro_port):
    print(int(erro_port))
    portchange(erro_port)
    return {"message": "Hello World"}



if __name__ == '__main__':
    uvicorn.run(app='serve:app', host=host_name, port=8000, reload = True)