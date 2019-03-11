from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

# Front Page!
def index(request):
    # Get local articles
    local_articles = Article.objects.all()[:8]

    # Get featured articles
    featured_articles = Article.objects.filter(is_featured=True)

    return render(request, 'app/index.html', context = {
        'articles': local_articles,
        'featured': featured_articles,
    })