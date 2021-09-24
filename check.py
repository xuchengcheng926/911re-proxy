import requests
import time

url="http://usa1.chengs.tk:8000/check/911re"
port=5000
t=time.localtime().tm_hour

def report2server(erro_port):
  try:
    res=requests.get(url, params={"erro_port":int(erro_port)})
  except:
    pass
  else:
    return 'ok'
  return "error"

def main():
  print('')
  print("--------------------------------------------------------------")
  if t>5 and t<14:
    print(f"{time.localtime().tm_mon}.{time.localtime().tm_mday} {time.localtime().tm_hour}:{time.localtime().tm_min} don't change")
    print("--------------------------------------------------------------")
    exit(0)
  else:
    print(f"{time.localtime().tm_mon}.{time.localtime().tm_mday} {time.localtime().tm_hour}:{time.localtime().tm_min} can change ")

    for i in range(5):
      proxies = {"http":"socks5://usa1.chengs.tk:"+str(port+i)}
      try:
        requests.get('http://google.com', proxies=proxies)
      except:
        print('faild'+':'+str(proxies)+", report to server: "+report2server(port+i))
      else:
        print('success'+':'+str(proxies)+", don't report")
  print("--------------------------------------------------------------")
main()
