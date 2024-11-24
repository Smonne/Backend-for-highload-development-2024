from rest_framework import viewsets
from .models import SecureModel
from .serializers import SecureModelSerializer
from django.http import JsonResponse
from .forms import DataUploadForm
from .models import DataUpload
from .tasks import process_data_upload
from django.http import JsonResponse


class SecureModelViewSet(viewsets.ModelViewSet):
    queryset = SecureModel.objects.all()
    serializer_class = SecureModelSerializer

    from django.shortcuts import render, redirect

def upload_data(request):
    if request.method == 'POST':
        form = DataUploadForm(request.POST, request.FILES)
        if form.is_valid():
           
            data_upload = form.save(commit=False)
            data_upload.user = request.user
            data_upload.status = 'Processing'
            data_upload.save()

           
            process_data_upload.delay(data_upload.id)

            return JsonResponse({"message": "File is being processed in the background!"})

    else:
        form = DataUploadForm()

    return render(request, 'upload.html', {'form': form})



def check_upload_status(request, upload_id):
    data_upload = DataUpload.objects.get(id=upload_id)
    return JsonResponse({'status': data_upload.status})

import clamd

def scan_file(file):
    cd = clamd.ClamdUnixSocket()
    result = cd.scan(file)
    if result and result['file'][0] != 'OK':
        raise ValidationError("Malware detected in the file!")
    return file


from django.core.cache import cache
from .models import DataUpload

def get_data():
    data = cache.get('my_data')
    
    if not data:
        data = DataUpload.objects.all()
        
        cache.set('my_data', data, timeout=60*15)
        
    return data

def get_uploads():
   
    uploads = DataUpload.objects.select_related('user').all()
    return uploads
