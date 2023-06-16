from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':40,'b':20,'c':10}

    return render(request,'condition.html',context=d )
def loop(request):
    d={'name':'bhavi'}
    return render(request,'loop.html',d)
