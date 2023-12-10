from django.shortcuts import render, HttpResponse
from .models import Employee


# Create your views here.


# def homepage(request):
    # logger.info("homepage")
#     print(request.method, request.user)
#     return HttpResponse("Helllo")

def homepage(request):
    emps = Employee.objects.all()
    logger.info("fetched all emps")
    return render(request, "home.html", context={"name": ["A", "B", "C", "D"], "all_emps": emps})



def welcome(request):
    '''added by sheetal'''
    pass



# client    -->  server