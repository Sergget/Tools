import requests
import traceback
from dns import resolver
from datetime import datetime

conf = {
    "dynUrl":"https://dyn.dns.he.net/nic/update?hostname=",
    "TLD":"sergget.ga",
    "names":[
        {
            "name":"blog",
            "key":"9GuwZ9oS97YSoG8m"
        }
    ]
}

def obCurrentTime():
    return "["+str(datetime.now())+"] "

# obtain public IP address from https://api.ipify.org
def check_ip():
    res = requests.get("https://api.ipify.org")
    if res.status_code==200:
        return res.text
    else:
        raise ConnectionError("cannot obtain IP, response code:"+res.text) 

def update_dns_record(ip,conf):
    for sub in conf["names"]:
        if ip and sub["name"] and sub["key"]:
            # dnsRec=resolver.query(sub["name"]+"."+conf["TLD"],'A')[0].to_text()
            dnsRec = resolver.resolve(sub["name"]+"."+conf["TLD"])[0].to_text()
            if dnsRec !=ip:
                # print(conf["dynUrl"]+sub["name"]+"."+conf["TLD"]+"&password="+sub["key"]+"&myip="+ip)
                r=requests.get(conf["dynUrl"]+sub["name"]+"."+conf["TLD"]+"&password="+sub["key"]+"&myip="+ip)
                if r.text=="badauth":
                    raise ConnectionRefusedError("Auth failed for ["+sub["name"]+"]: "+r.text)
                else:
                    print(obCurrentTime()+r.text)
            else:
                print("No need to change, IP: "+dnsRec)
        elif not ip:
            raise ValueError("Empty IP!")
        else:
            raise ValueError("Invalid config")
try:
    update_dns_record(check_ip(),conf)
except Exception:
    print(obCurrentTime()+"Error detected: "+traceback.format_exc())