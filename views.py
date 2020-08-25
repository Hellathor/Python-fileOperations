from django.shortcuts import render,redirect,HttpResponse  
from django.contrib.auth.decorators import login_required  
from django.views.decorators.csrf import csrf_exemp  

@login_required  
@csrf_exempt  
def text(request):  
    if request.method == "POST":  
        title = request.POST.get('title')  
        print(title)  
        content = request.POST.get('content')  
        print(content)  
    return render(request,'index.html')  

@login_required  
@csrf_exempt  
def instantuploa(request):  
    if request.method == 'POST':  
        content_img = request.FILES['file']  
        if content_img.size/1024/1024 < 2:  
            if content_img.content_type == 'image/jpeg' or content_img.content_type == 'image/jpg' or content_img.content_type == 'image/png':  
                nowtime = datetime.datetime.now().strftime('%Y%m%d%H%S')  
                path = os.path.join(settings.MEDIA_ROOT,nowtime + content_img.name)  
                with open(path, 'wb') as f:  
                    for content in content_img.chunks():  
                        f.write(content)  
                f.close()  
                user_img = '{}'.format(nowtime + content_img.name)  
                response = {  
                    "status": 1,  
                    "message": "OK",  
                    'file': user_img,  
                }  
                return HttpResponse(json.dumps(response))  

            else:  
                response={  
                    "status": 0,  
                    "message": "You images type is not jpeg or jpg or png！",  
                }  
                return HttpResponse(json.dumps(response))  
        else:  
            response = {  
                "status": 0,  
                "message": "image size is 2M！",  
            }  
            return HttpResponse(json.dumps(response))  