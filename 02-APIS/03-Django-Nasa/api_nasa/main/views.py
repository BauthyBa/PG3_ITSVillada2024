from django.shortcuts import render, reverse, redirect
from .form import (Combertir_a_URL,APIMixin)


def index(request):
    if request.method == "POST":
        cat = request.POST.get("cat")
        date = request.POST.get("date")
        if cat:
            if cat == 'apod' and date:
                return Combertir_a_URL(url='main:results', params={"cat": cat, "date": date})
            else:
                return Combertir_a_URL(url='main:results', params={"cat": cat})
    return render(request, 'main/index.html', {})



def results(request):
    cat = request.GET.get("cat")
    date = request.GET.get("date")
    if cat:
        if cat == 'apod' and date:
            results = APIMixin(cat=cat, date=date).get_data()
        else:
            results = APIMixin(cat=cat).get_data()

        if results:
            context = {
                "results": results,
                "cat": cat,
            }
            return render(request, 'main/results.html', context)
    
    return redirect(reverse('main:home'))

