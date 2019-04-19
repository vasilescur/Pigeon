from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

import json

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


def drafts(request):
    if request.method == 'GET':
        drafts = Article.objects.filter(is_published = False, is_draft = True)

        return render(request, 'app/drafts.html', context = {
            'drafts': drafts,
            'user': request.user,
        })


def edit(request):
    article_id = request.GET.get('id')
    article = Article.objects.get(pk = article_id)

    return render(request, 'app/edit.html', context = {
        'article': article,
        'user': request.user,
    })


@csrf_exempt
def article(request):
    article_id = request.GET.get('id')
    article = Article.objects.get(pk = article_id)

    return render(request, 'app/article.html', context = {
        'article': article,
    })


@csrf_exempt
def article_newtext(request):
    if request.method != 'POST':
        return HttpResponse("Error: Use a POST request only.")

    request_parsed = json.loads(request.body)

    article_id = request_parsed['id']
    article = Article.objects.get(pk = article_id)

    new_content = request_parsed['newtext']

    article.text = new_content
    article.save()

    return HttpResponse(200)