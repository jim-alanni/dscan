import threading
import time
import requests
import sys


f = open("./DIR.txt","r+")
Dirs = f.readlines()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    , 'referer': 'https://www.baidu.com'
}


def ScanTarGet(TarGet,task):
    try:
        req = requests.get(TarGet + task, verify=False, timeout=3000,headers=header)
        if (req.status_code in [200, 302, 403]):
            print(TarGet + task)
            time.sleep(2)
    except:
        pass

def main():

    print('''
       _____  .__                       .__
      /  _  \ |  | _____    ____   ____ |__|
     /  /_\  \|  | \__  \  /    \ /    \|  |
    /    |    \  |__/ __ \|   |  \   |  \  |
    \____|__  /____(____  /___|  /___|  /__|
            \/          \/     \/     \/
                                  --Ver 2.1
    ''')

    try:
        TarGet = sys.argv[1]
        for task in Dirs:
            task = task.replace("\n", "")
            t = threading.Thread(target=ScanTarGet, args=(TarGet, task))
            t.start()
    except IndexError as e:
        print("Python dscan.py <url>")


if __name__ == '__main__':
    main()