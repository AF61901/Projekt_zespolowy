from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormRejestruj, UserUpdateForm, ProfilUpdateForm


def rejestruj(request):
    if request.method == 'POST':
        form = FormRejestruj(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało utworzone!')
            return redirect('loguj')
    else:
        form = FormRejestruj()
    return render(request, 'users/rejestruj.html', {'form': form})

@login_required
def profil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfilUpdateForm(request.POST, request.FILES, instance = request.user.profil)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Konto zostało zaktualizowane!')
            return redirect('profil')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfilUpdateForm(instance = request.user.profil)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profil.html', context)
