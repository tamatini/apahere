from django.shortcuts import render

# Create your views here.
def blog_page(request):
    return render(request, 'blog.html')


def new_post_page(request):
    return render(request, 'new_post.html')