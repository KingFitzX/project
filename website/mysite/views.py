from django.shortcuts import render

import scenarios.interface as interface
from .forms import ButtonForm
from .models import ParamSet, Result

def homepage(request):
    return render(request, "mysite/homepage.html", {"title": "Homepage"})

def button(request):
    sc = interface.gen_scenario()

    paramset = ParamSet()
    paramset.genParamSet(sc["parameters"])

    return render(request, "mysite/button.html", {"title": "Button", "scenario":sc["scenario"], "scid": paramset.id})

def button_results(request):
    if request.method == "POST":
        form = ButtonForm(request.POST)

        if form.is_valid():
            # print(form.scid)
            # print(form.pressed)

            if form.cleaned_data["pressed"]:
                p = {"pressedtext": "pressed"}
            else:
                p = {"pressedtext": "didn't press"}

            return render(request, "mysite/buttonresults.html", p)
        else:
            print(form.errors)

def showcase(request):
    return render(request, "mysite/showcase.html", {})

def showcase_results(request):
    return None
