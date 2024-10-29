from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            url_instance = URL(original_url=original_url)
            url_instance.save()
            return render(request, 'shortener/home.html', {'short_url': url_instance.short_url})
    else:
        form = URLForm()
        return render(request, 'shortener/home.html', {'form': form})

def redirect_to_url(request, short_url):
    url_instance = get_object_or_404(URL, short_url = short_url)
    return redirect(url_instance.original_url) 
        