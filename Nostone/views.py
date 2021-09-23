from django.shortcuts import render , HttpResponse
def one(request):
    return HttpResponse('you will find the stone')



def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
