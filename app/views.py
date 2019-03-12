from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import Article

# Front Page!
def index(request):
    # Get local articles
    local_articles = Article.objects.filter(is_published=True)[:8]

    # Get featured articles
    featured_articles = Article.objects.filter(is_published=True, is_featured=True)

    return render(request, 'app/index.html', context = {
        'articles': local_articles,
        'featured': featured_articles,
    })

def redirect_index(request):
    # Redirect to the index view
    return redirect('/')


# Creation Dashboard
def create(request):
    user = request.user

    return render(request, 'app/create.html', context = {
        'user': request.user,
    })


@csrf_exempt
def create_article(request):
    if request.method == 'POST':
        article = Article()
        article.creator = request.user
        article.headline = request.POST['headline']
        article.save()

        return redirect('/create/')
    else:
        return HttpResponse('Error: Use POST')
