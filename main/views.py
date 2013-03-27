# Create your views here.
from decimal import Context
from django.http import HttpResponse
from users.models import Users
from main.models import Article
from django.template import Context,loader
from django.contrib.auth import authenticate, login

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("OK login!")
            # Redirect to a success page.
        else:
            return HttpResponse("Disabled account!")
        # Return a 'disabled account' error message
    else:
        return HttpResponse("Invalid login!")
        # Return an 'invalid login' error message.


def home(request):
    articles_list = Article.objects.order_by('-date')[:10]
    template = loader.get_template('main/home.html')
    context = Context({
        'articles_list':articles_list,
    })
    return HttpResponse(template.render(context))


def profile(request,user_id):
    user = Users.objects.get(id=user_id)
    articles_list = Article.objects.filter(user_id = user).order_by('-date')
    template = loader.get_template("main/profile.html")
    context = Context({
        'user':user,
        'articles_list':articles_list,
    })
    return HttpResponse(template.render(context))

def article(request,article_id):
    art = Article.objects.get(id=article_id)
    user = Users.objects.get(id = art.user_id.id)
    template = loader.get_template("main/article.html")
    context = Context({
        'art':art,
        'user':user,
    })
    return HttpResponse(template.render(context))

