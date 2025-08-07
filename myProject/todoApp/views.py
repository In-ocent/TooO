from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import TodoItem
# Create your views here.


def FirstView(request):
    return render(request, 'todoApp/index.html')


def HomeView(request):
    if request.method == 'POST':
        to_do_list = request.POST.get('to-do-listed')
        new_todo = TodoItem(user=request.user,  description=to_do_list)
        new_todo.save()

    all_todo = TodoItem.objects.filter(user=request.user)
    context = {
        'todos': all_todo
    }
    return render(request, 'todoApp/todo.html', context)


def RegisterView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f'name {username}, emaill {email}, password {password}')

        if len(password) < 5:
            messages.error(
                request, 'your password must be atlist 5 characters')
            return redirect('register')

        get_all_new_user = User.objects.filter(username=username).exists()
        if get_all_new_user:
            messages.error(
                request, ' Username already taken. Please choose another one.')
            return redirect('register')

        else:
            new_user = User.objects.create_user(
                username=username, password=password, email=email)
            new_user.save()
            messages.success(request, 'Acount successfully created')
            return redirect('login')

    return render(request, 'todoApp/register.html', {})


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        validated_user = authenticate(username=username, password=password)
        if validated_user is not None:
            login(request, validated_user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid crendencials')
            return redirect('login')
    return render(request, 'todoApp/login.html', {})


def delete(request, id):
    Todo.objects.filter(id=id).delete()
    return redirect('home')


def update(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = True
    todo.save()
    return redirect('home')
