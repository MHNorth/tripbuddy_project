from django.contrib import admin

# Register your models here.
from .models import TravelPlan, Review, ReviewResponse


admin.site.register(TravelPlan)
admin.site.register(Review)
admin.site.register(ReviewResponse)
