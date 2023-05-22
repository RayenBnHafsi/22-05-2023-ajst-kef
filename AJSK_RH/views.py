from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(
        request, "index.html"
    )

def active(request):
    return render(
        request, "activities.html"
    )

def psot(request):
    post= Post.objects.all()

    return render(
        request, "post.html",{
        'posts': post
        }
    )
