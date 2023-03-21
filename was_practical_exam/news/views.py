from django.http import HttpResponse
from django.shortcuts import render
from news.models import Article



def index(request):
# Query the database for a list of ALL categories currently stored.
# Order the categories by the number of likes in descending order.
# Retrieve the top 5 only -- or all if less than 5.
# Place the list in our context_dict dictionary (with our boldmessage!)
# that will be passed to the template engine.
    article_list = Article.objects.all()
    context_dict = {}
    context_dict['articles'] = article_list
    # Render the response and send it back!
    return render(request, 'news/index.html', context=context_dict)
