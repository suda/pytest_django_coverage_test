from django.shortcuts import render

def landing(request):
    return render(request, "render_something/index.html", {})