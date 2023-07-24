from django import forms


# create models for forms
class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    rating = forms.IntegerField(min_value=1, max_value=5)
    feedback = forms.CharField(label="Your feedback.", widget=forms.Textarea(attrs={
        "rows":5,
    }))