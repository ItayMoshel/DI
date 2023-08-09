from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Post

person = Person.objects.filter(first_name="Maria",
                               last_name="Fez").first()


def about(request):
    return HttpResponse('<h1> Welcome Users<h1>')


def index(request):
    context = {
        'page_title': "Homepage",
        'user': person
    }
    return render(request, 'posts/homepage.html', context)


def posts(request):
    context = {
        'page_title': "Posts",
        'posts': Post.objects.filter(
            author__first_name=person.first_name,
            author__last_name=person.last_name)
    }
    return render(request, 'posts/posts.html', context)
