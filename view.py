from django.http import HttpResponse


def index(request):
    return HttpResponse("hello word")

def login(request):
    return redirect("/index")
