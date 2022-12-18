from django.shortcuts import render

# Create your views here.
def loki(request):
    return render(request,'loki.html')