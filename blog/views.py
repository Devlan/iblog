from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
from .models import BlogPost


# Create your views here.
def index(request):
    context_list = BlogPost.objects.all()
    paginator = Paginator(context_list, 3)
    page = request.GET.get('page')
    context = paginator.get_page(page)
    return render(request, 'blog/index.html', {'context': context})


def about(request):
    return render(request, 'blog/about.html')


def top_search(request):
    return render(request, 'search/search.html')
