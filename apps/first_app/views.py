from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    return redirect("/")
def show(request, test):
    response = 'placeholder to display blog', test
    return HttpResponse(response)
def edit(request, test):
    response = 'placeholder to edit blog', test
    return HttpResponse(response)
def destroy(request, test):
    return redirect("/")