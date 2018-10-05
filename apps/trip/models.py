from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.urls import reverse




# ==== Trip Model ==== #

class TravelPlan(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    startDate = models.DateField(null=False, blank=False)
    endDate = models.DateField(null=False, blank=False)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name="creator")
    travelBuddy = models.ManyToManyField(get_user_model(), related_name = "joiners", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return " %s | %s..." % (self.destination, self.description[0:40])



# ==== Original Review Model ==== #


RATING_CHOICES = (
(1, '1'),
(2, '2'),
(3, '3'),
(4, '4'),
(5, '5'),
)

BOOL = (
    (True, 'Yes'),
    (False, 'No'),
)
class Review(models.Model):

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'


    title = models.CharField(max_length=55, default='')
    ratings = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(max_length=500, blank=False)
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name="trip")
    trip = models.ForeignKey(TravelPlan, on_delete=models.CASCADE, null=True, related_name="trip")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class ReviewResponse(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name="commenter")
    review = models.ManyToManyField(Review, blank=True)
    response = models.TextField(max_length=200, blank=False)


    def __str__(self):
        return "Reviewer: %s | Comment: %s" % (self.user, self.response[:25],)




