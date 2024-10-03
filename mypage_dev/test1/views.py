from django.shortcuts import render
from .models import test_file
# Create your views here.

def file_give(request):
    test = None
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        file = request.FILES.get('file')
        
        test = test_file.objects.create(
            title = title, content = content, image = image, file = file
        )
 
    return render(
        request,
        'test1/test1_file.html',
        {
            'test' : test,
        }
    )


def file_show(request):
    test = None
    files = test_file.objects.all()
    return render(
        request, 
        'test1/file_show.html',
        {
           'files' : files
        })