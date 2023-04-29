from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def Search(request):
    key = request.POST["key"]
    return render(request, 'result.html', {'result': key})