from django.forms import DateInput
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from traitlets import Instance
from pyexpat.errors import messages
from django.contrib import messages
from .models import Zamow, samochody
from .forms import ZamowForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def delete(request, id):
    obj = get_object_or_404(Zamow, id = id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, f'Zamówienie zostało usunięte')
        return redirect('/moje')
    context = {
        "object":obj
    }
    return render(request, 'wynajem/delet.html', context)

def detail(request, id=None):
    detail = get_object_or_404(Zamow,id=id)
    context = {
        "detail": detail,
        "title" : "Szczegóły zamówienia"
    }
    return render(request, 'wynajem/detail.html', context)



def home(request):
    context ={
        'samochody': samochody.objects.all()[:3]
    }
    return render(request, 'wynajem/stronaglowna.html', context)

def onas(request):
    return render(request, 'wynajem/onas.html', {'title': 'O nas'})

def kontakt(request):
    return render(request, 'wynajem/kontakt.html', {'title': 'Kontakt'})

def auta(request):
    context ={
        'samochody': samochody.objects.all(),
        "title" : "Oferta"
    }
    return render(request, 'wynajem/samochody.html', context)

def szczeg(request, id=None):
    detail = get_object_or_404(samochody,id=id)
    context = {
        "detail": detail,
        "title" : "Szczegóły"
    }
    return render(request, 'wynajem/szczeg.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = Zamow
    template_name = 'wynajem/moje.html'
    context_object_name = 'Zamow'

    def get_queryset(self):
        return Zamow.objects.filter(
            user=self.request.user
        )

@login_required
def zam(request, id=None):
    form = ZamowForm(request.POST)
    desc = samochody.objects.get(id=id)
    if not request.user.is_authenticated:
        return redirect('/loguj')

    if form.is_valid():
        data1 = form.cleaned_data['data_odbioru']
        data2 = form.cleaned_data['data_oddania']
        odb1 = form.cleaned_data['miejsce_odbioru']
        odb2 = form.cleaned_data['miejsce_oddania']
        zamowienie = Zamow(user=request.user, samochod=desc,
            data_odbioru=data1, data_oddania=data2, miejsce_odbioru=odb1, miejsce_oddania=odb2)
        is_available = zamowienie.check_dates()

        if data1 > data2:
            messages.warning(request, f'Data się nie zgadza')
            return render(request, 'wynajem/zamow_form.html', {'desc': desc, 'form': form})

        if is_available:
            zamowienie.save()
            return redirect('/moje')
        else:
            messages.warning(request, f'Samochód jest niedostępny w tym terminie!')
            return render(request, 'wynajem/zamow_form.html', {'desc': desc, 'form': form,})


    else:
        return render(request, 'wynajem/zamow_form.html', {'desc': desc, 'form': form})


