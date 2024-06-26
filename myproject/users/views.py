from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form  = UserCreationForm()
    context = {'form': form} 
    return render(request, 'users/register.html',context)


def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        form =  AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user )
            return redirect('posts:list')
    
    else :
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/login.html',context)
