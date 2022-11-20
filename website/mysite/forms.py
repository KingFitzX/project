from django import forms
from scenarios.interface import attr_descriptions

class ButtonForm(forms.Form):
    pressed = forms.BooleanField(label="pressed", required=False)
    scid = forms.UUIDField(label="scid")

paramdescs = attr_descriptions()
paramnames = ["cares_about", "no_nukes", "aggression", "international_rep", "population", "provocation"]
formoptions = [[((desc["max"] + desc["min"]) / 2, desc["description"]) for desc in paramdescs[name]] for name in paramnames]

class ShowcaseForm(forms.Form):
    a_ca = forms.CharField(label="Country A: Cares About", widget=forms.Select(choices=formoptions[0]))
    a_nn = forms.CharField(label="Country A: Number of Nukes", widget=forms.Select(choices=formoptions[1]))
    a_a  = forms.CharField(label="Country A: Agression", widget=forms.Select(choices=formoptions[2]))
    a_ir = forms.CharField(label="Country A: International Reputation", widget=forms.Select(choices=formoptions[3]))
    a_p  = forms.CharField(label="Country A: Population", widget=forms.Select(choices=formoptions[4]))
    a_pr = forms.CharField(label="Provocation", widget=forms.Select(choices=formoptions[5]))

    b_ca = forms.CharField(label="Country B: Cares About", widget=forms.Select(choices=formoptions[0]))
    b_nn = forms.CharField(label="Country B: Number of Nukes", widget=forms.Select(choices=formoptions[1]))
    b_a  = forms.CharField(label="Country B: Agression", widget=forms.Select(choices=formoptions[2]))
    b_ir = forms.CharField(label="Country B: International Reputation", widget=forms.Select(choices=formoptions[3]))
    b_p  = forms.CharField(label="Country B: Population", widget=forms.Select(choices=formoptions[4]))
