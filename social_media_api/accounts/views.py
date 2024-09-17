from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def registration(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = User.objects.get(user_id = pk)

        if request.method == 'POST':
            #get current user
            current_user = request.user.profile
            action = request.POST['follow']

            #follow or unfollow
            if action == 'unfollow_user':
                current_user.following.remove(profile)
            else:
                current_user.following.add(profile)
            
            #save the profile
            current_user.save()
        return render(request, 'profile.html', {'profile': profile})
    else:
        messages.success(request, ('You must be logged in'))
        return redirect('login')