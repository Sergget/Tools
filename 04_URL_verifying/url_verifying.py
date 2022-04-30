import requests
import threading

def url_detect():
    src_path = "input.txt"
    dst_path = "export.txt"
    error_path = "error.txt"

    export = open(dst_path,'w',encoding="utf-8")
    error = open(error_path,'w',encoding="utf-8")
    with open(src_path,'r',encoding="utf-8") as f:
        while True:
            url=f.readline().replace("\n","")
            if url == "":
                break
            else:
                print("Verifying "+url)
                try:
                    r = requests.get(url,timeout=5)
                    if r.status_code == 200:
                        export.write(url+"\n")
                    else:
                        error.write("Status code: %s, url: %s\n" % (r.status_code,url))
                except:
                    error.write("Unreachable: %s\n" % url)
    export.close()
    error.close()

if __name__ == '__main__':
    # 多线程操作
    t1 = threading.Thread(target=url_detect,args=())
    t1.start()