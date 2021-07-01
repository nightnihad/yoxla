from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def blog(request):
    return HttpResponse('sene ne var')