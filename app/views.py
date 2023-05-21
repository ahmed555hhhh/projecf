from django.shortcuts import render
from .models import *
# Create your views here.
def p(request):
    if request.method == "POST":
        if "post" in request.POST:
            post = request.POST.get("input")
            Posts(
                post=post
            ).save()
            print(0)
    context = {
        "posts": Posts.objects.all()
    }
    return render(request,"p.html",context)