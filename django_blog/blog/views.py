from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/login/')
    else:
        form = SignUpForm()

    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST['email']
        user.save()
    return render(request, 'blog/profile.html')