import requests
import time

url="http://des.chengs.tk:14856/check/911re"
port=5000
t=time.localtime().tm_hour

def report2server(erro_port):
  erro_port=int(erro_port)+45891
  try:
    res=requests.get(url, params={"erro_port":erro_port},timeout=5)
  except:
    pass
  else:
    return 'ok'
  return "error"

def main():
  print('')
  print("--------------------------------------------------------------")
  if t>50 and t<12:
    print(f"{time.localtime().tm_mon}.{time.localtime().tm_mday} {time.localtime().tm_hour}:{time.localtime().tm_min} don't change")
    print("--------------------------------------------------------------")
    exit(0)
  else:
    print(f"{time.localtime().tm_mon}.{time.localtime().tm_mday} {time.localtime().tm_hour}:{time.localtime().tm_min} can change ")

    for i in range(10):
      proxies = {"http":"socks5://des.chengs.tk:"+str(port+i)}
      try:
        requests.get('http://google.com', proxies=proxies,timeout=10)
      except:
        print('faild'+':'+str(proxies)+", report to server: "+report2server(port+i))
      else:
        print('success'+':'+str(proxies)+", don't report")
  print("--------------------------------------------------------------")
main()
#requests.get(url, params={"erro_port":5004+45891})
#requests.get("http://pushplus.hxtrip.com/send",params={"token":"d4caebf0eac54e39897337ba1679f3d9", "title":"911re port change","content":f"{port}","template":"html"})
