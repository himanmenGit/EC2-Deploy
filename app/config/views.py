import mimetypes
import os

from django.conf import settings


def serve_media(request, path):
    # path에는 미디어 파일(User-uploaded fiels)의 경로가 주어짐
    # 주어진 미디어 파일의 경로를 settings.MEDIA_ROOT를 기준으로 해서
    # 해당 파일을 리턴해주는 view 함수 작성
    print('asdasdasd', path)
    media_path = os.path.join(settings.MEDIA_ROOT, path)
    content_type = mimetypes.guess_type(path)
    from django.http import FileResponse

    return FileResponse(open(media_path, 'rb'), content_type=content_type)
