import os
from EduCRM import settings


def uploadfile(img):
    f = open(os.path.join(settings.UPLOAD_ROOT, '', img.name), 'wb')
    for chunk in img.chunks():
        f.write(chunk)
    f.close()