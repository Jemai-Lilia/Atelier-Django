from django.http import HttpResponse

def homepage(request):
    return HttpResponse('hello, Iam Lilia Jemai')

def about(request):
    return HttpResponse('Hello, we are at about as')