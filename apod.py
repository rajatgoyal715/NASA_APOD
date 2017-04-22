import requests
import urllib.request
import ctypes

def set_wallpaper():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "apod.jpg" , 0)
    print('Wallpaper set')

print('Astronomy Picture Of The Day')

url = 'https://api.nasa.gov/planetary/apod'
key = 'TRUeFmW0K72G8JRKOYfhZymkQUFM9bGxF05QrbNo'

param = {'api_key': key}

try :
    resp = requests.get(url, params=param).json()
    apod_url = resp["hdurl"]

    print(resp["title"])
    print(resp["date"])
    print(resp["explanation"])

    urllib.request.urlretrieve(apod_url, "apod.jpg")
    #set_wallpaper()

except Exception():
    print('An error happened')