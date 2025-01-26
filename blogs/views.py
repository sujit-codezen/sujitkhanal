from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from category.models import Category
from .models import Tag
from django.core.paginator import Paginator

# Create your views here.
def blog_list(request):
    post_list = Post.objects.filter(status='published').order_by('-published_at')
    
    category = request.GET.get('category')
    tags = request.GET.get('tags')
    q = request.GET.get('q')
    
    if q:
        post_list = post_list.filter(title__icontains=q)
    
    if category:
        post_list = post_list.filter(category__name=category)
        
    if tags:
        post_list = post_list.filter(tags__name=tags)
    
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    all_tags = Tag.objects.all()

    return render(request, 'blogs/blog_list.html', {
        'posts': page_obj,
        'categories': categories,
        'tags': all_tags,
        'category': category,
        'tags_filter': tags,
        'q': q,
    })
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        category = self.object.category.all()
        context['related_posts'] = Post.objects.filter(category__in=category).exclude(id=self.object.id).order_by('-published_at')[:4]
        return context
    
    