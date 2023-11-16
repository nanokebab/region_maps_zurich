# code for scraping webcam images

import requests
import shutil
import datetime

WEBCAM_URL = 'https://www.surfclub-uri.ch/webcam/webcam_axenegg.jpg'
# WEBCAM_URL = 'https://www.surfclub-uri.ch/webcam/webcam_bucht.jpg'

now = datetime.datetime.now()

FILEPATH = 'data/raw/'
FILENAME = WEBCAM_URL.split('.')[-2].split('_')[-1] + '_' + str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2) + str(now.hour).zfill(2) + str(now.minute).zfill(2) + '.jpg'
FILENAME = FILEPATH + FILENAME

res = requests.get(WEBCAM_URL, stream = True)

if res.status_code == 200:
    with open(FILENAME,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',FILENAME)
else:
    print('Image Couldn\'t be retrieved')