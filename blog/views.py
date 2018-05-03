from django.shortcuts import render
from django.core.paginator import Paginator
from .models import BlogPost


# Create your views here.
def index(request):
    context_list = BlogPost.objects.all()
    # 将blog对象的tag属性遍历出来，并放入一个空列表tags_list里
    tags_list = [blog_obj.tag for blog_obj in context_list]
    # 统计每个tag出现的次数,用一个空列表来接收字典，如果字典不在列表里，就把它放进去，完成去重
    tag_count = []
    for tag in tags_list:
        tag_times = tags_list.count(tag)
        tag_dirt = {'tag': tag, 'tag_times': tag_times}
        if tag_dirt not in tag_count:
            tag_count.append(tag_dirt)
    # tag_list用set()去重
    tags = set(tags_list)
    paginator = Paginator(context_list, 3)
    page = request.GET.get('page')
    context = paginator.get_page(page)
    return render(request, 'blog/index.html', {'context': context, 'tags': tags, 'tags_list': tags_list, 'tag_count': tag_count})


def article(request, blog_id):
    context = BlogPost.objects.all().filter(id=blog_id)
    return render(request, 'blog/article.html', {'context': context})


def about(request):
    return render(request, 'blog/about.html')


def top_search(request):
    return render(request, 'search/search.html')
