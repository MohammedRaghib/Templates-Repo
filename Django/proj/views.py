import mimetypes
import os
from django.http import FileResponse, Http404
from django.conf import settings

def serve_media_secure(request, filepath):
    full_path = os.path.join(settings.MEDIA_ROOT, filepath)
    
    media_root_real = os.path.realpath(settings.MEDIA_ROOT)
    full_path_real = os.path.realpath(full_path) 
    
    if not full_path_real.startswith(media_root_real):
        raise Http404("Invalid file path: Security violation (Attempt to traverse outside MEDIA_ROOT).")

    if os.path.exists(full_path_real): 
        mime_type, _ = mimetypes.guess_type(full_path_real)
        
        return FileResponse(open(full_path_real, 'rb'), content_type=mime_type or 'application/octet-stream')
    else:
        raise Http404("File not found")