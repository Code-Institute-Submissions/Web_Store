from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


def index(request):
    '''Return the index.html file '''
    return render(request, 'index.html')
    
def logout(request):
    ''' log the user out '''
    auth.logout(request)
    messages.success(request, "You Have Successfully Logged Out!")
    return redirect(reverse('index'))
    
def login(request):
    return render(request, 'login.html')