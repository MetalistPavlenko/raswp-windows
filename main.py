import requests, re, random, os, ctypes, time

def start():
    try:
        i = re.findall('<a class="preview" href="(.+?)"', requests.get('https://wallhaven.cc/search?q=id%3A1&categories=111&purity=110&atleast=1920x1080&ratios=16x9&sorting=random').text)
        i = re.findall('<img id="wallpaper" src="(.+?)"', requests.get(i[random.randint(0, len(i)-1)]).text)[0]
        p = os.environ['TEMP'] + '\\' + re.split('wallhaven-', i)[1]; open(p, 'wb').write(requests.get(i).content)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, p, 0)
        os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP" /f')
        os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP" /v LockScreenImagePath /t REG_SZ /d "'+p+'" /f')
    except:
        time.sleep(5)
        start()
start()
