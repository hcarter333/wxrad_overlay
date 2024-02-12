import requests
import shutil
import datetime
path = "wx_2024_02_10_"
time_hour = 7
time_minute = 5

wx_time = datetime.datetime.strptime("2024/02/10 07:00", "%Y/%m/%d %H:%M")

img_url_strt = "https://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r-t.cgi?&REQUEST=GetMap&TRANSPARENT=true&FORMAT=image/png&BGCOLOR=0x000000&VERSION=1.1.1&LAYERS=nexrad-n0r-wmst&STYLES=default&CRS=EPSG:102100&SRS=EPSG:102100&TIME=2024-02-10T"
#img_url_date = f'{time_hour:0>2d}'+":"+f'{time_minute:0>2d}'
img_url_date = wx_time.strftime("%H:%M")
img_url_end =  ":00Z&WIDTH=1286&HEIGHT=641&BBOX=-11854636.438282276,4105748.8334824615,-11842349.185985452,4111873.350373803"
path_full = f'{path}{time_hour:0>2d}'+"_"+f'{time_minute:0>2d}'+".png"
img_url = img_url_strt+img_url_date+img_url_end
print(img_url)


#Get the weather every five minutes till noon
for x in range(144):
    img_url_date = wx_time.strftime("%H:%M")
    img_url = img_url_strt+img_url_date+img_url_end
    path_full = path+str(x)+".png"
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        with open(path_full, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    wx_time = wx_time + datetime.timedelta(minutes=5)
