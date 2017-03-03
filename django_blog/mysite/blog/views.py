from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .models import Post

# Create your views here.

def post_list(request):
	objects_list = Post.published.all()
	paginator = Paginator(objects_list, 3) # 2 = number of posts in each page
	page = request.GET.get('page')
	try:
		blog_pages =paginator.page(page)
	except PageNotAnInteger:
		blog_pages = paginator.page(1)
	except EmptyPage:
		blog_pages = paginator.page(paginator.num_pages)

	posts = Post.objects.all()
	return render(request, 'blog/post/list.html', { 'blog_pages':blog_pages ,'posts': posts})

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post,
								   status='published',
								   publish__year=year,
								   publish__month=month,
								   publish__day=day)
	return render(request, 'blog/post/detail.html', {'post': post})