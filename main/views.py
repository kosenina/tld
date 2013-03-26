# Create your views here.
from decimal import Context
from lib2to3.fixes.fix_input import context
from re import template
from django import template
from django.http import HttpResponse
from django.shortcuts import render
from main.models import User
from main.models import Article
from django.template import Context,loader

def login(request):
    return render(request, 'main/login.html')

def home(request):
    articles_list = Article.objects.order_by('-date')[:10]
    template = loader.get_template('main/home.html')
    context = Context({
        'articles_list':articles_list,
    })
    return HttpResponse(template.render(context))


def profile(request,user_id):
    user = User.objects.get(id=user_id)
    articles_list = Article.objects.filter(user_id = user).order_by('-date')
    template = loader.get_template("main/profile.html")
    context = Context({
        'user':user,
        'articles_list':articles_list,
    })
    return HttpResponse(template.render(context))

def article(request,article_id):
    art = Article.objects.get(id=article_id)
    user = User.objects.get(id = art.user_id.id)
    template = loader.get_template("main/article.html")
    context = Context({
        'art':art,
        'user':user,
    })
    return HttpResponse(template.render(context))

