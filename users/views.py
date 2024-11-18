from bs4.diagnose import profile
from django.shortcuts import render, redirect
from .models import ProfileUser
from .forms import UserForm, ProfileUserForm

# Create your views here.

def user_list(request):
    profile_users = ProfileUser.objects.all()
    return render(request, 'users/user_list.html', {'profile_users': profile_users})

def user_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileUserForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # Asocia el ProfileUser con el User recién creado
            profile.save()
            return redirect('user_list')
    else:
        user_form = UserForm()
        profile_form = ProfileUserForm()

    return render(request, 'users/user_create.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def user_edit(request, pk):
    profile_user = ProfileUser.objects.get(pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=profile_user.user)
        profile_form = ProfileUserForm(request.POST, request.FILES, instance=profile_user)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save()
            return redirect('user_list')
    else:
        user_form = UserForm(instance=profile_user.user)
        profile_form = ProfileUserForm(instance=profile_user)

    return render(request, 'users/user_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def user_details(request, pk):
    profile_user = ProfileUser.objects.get(pk=pk)
    return render(request, 'users/user_details.html', {'profile_user': profile_user})

def user_delete(request, pk):
    profile_user = ProfileUser.objects.get(pk=pk)
    if request.method == 'POST':
        profile_user.user.delete()
        profile_user.delete()
        return redirect('user_list')
    return render(request, 'users/user_delete.html', {'profile_user': profile_user})