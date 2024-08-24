from django.shortcuts import render

# Create your views here.
def printing(request):
    d = {'name':'Hareesh Reddy'}
    return render(request,'printing.html',context=d)
