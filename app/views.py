from django.shortcuts import render

# Create your views here.
def mouni(request):
    d={'a':10,'b':70,'c':30}
    return render(request,'mouni.html',d)