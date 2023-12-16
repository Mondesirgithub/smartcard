from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, "web/index.html")


def contacts(request):
    return render(request, "web/contacts.html")

def pricing_plan(request):
    return render(request, "web/pricing-plan.html")


def services(request):
    return render(request, "web/services.html")

def about(request):
    return render(request, "web/about.html")