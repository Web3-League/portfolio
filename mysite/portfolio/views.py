from django.shortcuts import render, redirect
from django.contrib import messages
from .form import MessageForm


# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès.')
            return redirect('contact')
    else:
        form = MessageForm()

    return render(request, 'portfolio.html', {'form': form})

def blog_index(request):
    return render(request, 'blog.html')

def search(request):
    return render(request, 'search.html')