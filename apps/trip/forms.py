from django import forms
from django.contrib import admin
from .models import TravelPlan, Review, ReviewResponse


class DateInput(forms.DateInput):
    input_type = 'date'


class TripForm(forms.ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['destination', 'description', 'startDate', 'endDate',]
        exclude = ['created_by']
        widgets = {
            'startDate': DateInput(),
            'endDate': DateInput(),
            }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['trip', 'ratings', 'title', 'comment',]
        exclude = ['name',]


class ReviewResponseForm(forms.ModelForm):
    class Meta:
        model = ReviewResponse
        fields = ['review','response',]
        exclude = ['user',]



