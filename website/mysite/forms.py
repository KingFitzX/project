from django import forms

class ButtonForm(forms.Form):
    pressed = forms.BooleanField(label="pressed", required=False)
    scid = forms.UUIDField(label="scid")