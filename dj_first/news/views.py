from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import News
# from .forms import NewsForm
from .forms import NewsModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    obj = News.objects.all() 
    return render(request, "news/index.html", {"name": obj})




def detail_view(request, pk):
    obj = News.objects.get(id=pk)
    print(request.POST)
    print(request.GET)
    return render(request, "news/detail.html", {'new': obj})

@login_required
def create_views(request):
    form = NewsModelForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
    return render(request, "news/forms.html", {'form': form})

@login_required
def edit_view(request, pk):
    try:
        obj = News.objects.get(id=pk)
    except News.DoesNotExist:
        raise Http404
    if request.method =="POST":
        form = NewsModelForm(request.POST, instance=obj)
        if form.is_valid():
            edited_obj = form.save(commit=False)
            edited_obj.save()
    else:
        form = NewsModelForm(instance=obj)
    return render(request, "news/edit_news_form.html", {"single_object": obj, 'form': form})

@login_required
def delete_view(request, pk):
    try:
        obj = News.objects.get(id=pk)
    except News.DoesNotExist:
        raise Http404

    odj.delete()
    return HttpResponseRedirect(reverse('index'))




