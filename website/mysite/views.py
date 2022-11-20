from django.shortcuts import render
import numpy as np

import scenarios.interface as interface
import neuralnet.neuralnet as nn
import neuralnet.nnutils as nu
from .forms import ButtonForm
from .models import ParamSet, Result

neuralnet = nn.NeuralNet()

def homepage(request):
    return render(request, "mysite/homepage.html", {"title": "Homepage"})

def button(request):
    sc = interface.gen_scenario()

    airesult = nu.numpy_array_to_float(neuralnet.calc_prediction(nu.dicts_to_numpy_array(sc["parameters"])))
    print(airesult)

    paramset = ParamSet()
    paramset.genParamSet(sc["parameters"])
    paramset.ai_result = airesult

    paramset.save()

    return render(request, "mysite/button.html", {"title": "Button", "scenario":sc["scenario"], "scid": paramset.id})

def button_results(request):
    if request.method == "POST":
        form = ButtonForm(request.POST)

        if form.is_valid():
            # print(form.scid)
            # print(form.pressed)

            pressed = form.cleaned_data["pressed"]

            if pressed:
                p = {"pressedtext": "pressed"}
            else:
                p = {"pressedtext": "didn't press"}

            p["pressed"] = pressed

            paramset = ParamSet.objects.get(id=form.cleaned_data["scid"])
            print(paramset)

            result = Result()
            result.params = paramset
            result.pressed = pressed
            result.save()

            p["aiPressed"] = paramset.ai_result >= 0.5

            neuralnet.train(nu.dicts_to_numpy_array(paramset.paramsToDict()), np.array([[float(pressed)]]), 1)

            return render(request, "mysite/buttonresults.html", p)
        else:
            print(form.errors)

def showcase(request):
    return render(request, "mysite/showcase.html", {})

def showcase_results(request):
    return None
