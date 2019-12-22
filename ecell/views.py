from django.shortcuts import render

def mainPage(request):
    return render(request,"index.html")

def sip(request):
    return render(request,"sip.html")

def company(request):
    return render(request,"registration_Company.html")


def student(request):
    return render(request,"registration_Student.html")
