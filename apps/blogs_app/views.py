from django.shortcuts import HttpResponse, redirect

def home(request):
    return HttpResponse("HOME PAGE")

def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    print "reached create"
    return redirect("/")
def show(request, blog_id):
    print blog_id
    return HttpResponse("placeholder to display blog {}".format(blog_id))

def edit(request, blog_id):
    return HttpResponse("placeholder to edit blog {}".format(blog_id))
    
def delete(request, blog_id):
    return HttpResponse(blog_id)