from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import TravelPlan, Review, ReviewResponse
from apps.accounts.models import CustomUser
from django.contrib import messages
from django.db import IntegrityError
from  django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.urls import reverse_lazy
from rest_framework import viewsets
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TripForm, ReviewForm, ReviewResponseForm



# ==== Home View ==== #

def index(request):
	return render(request, "trip/index.html")


# # =============== Class Based Views =============== #


# # ==== Trip List View ==== #


class DashboardView(LoginRequiredMixin, ListView):

	model = TravelPlan
	template_name = "trip/dashboard_view.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["travelplan_createdby"] = self.travelplan_createdby
		return context


	def get(self, request, *args, **kwargs):
		alltrips = TravelPlan.objects.all().order_by('-startDate')
		reviews = Review.objects.all().order_by('-created_at')
		userstrips = self.request.user.joiners.all()

		data = {
			'userstrips': userstrips,
			'alltrips': alltrips,
			'reviews': reviews,

		}
		return render(request, self.template_name, data)


# # # ==== Trip Detail View ==== #

class TripDetail(LoginRequiredMixin, DetailView):
	model = TravelPlan
	template_name = "trip/trip_detail.html"

# # # ==== Review/Review Comment Detail View ==== #

class ReviewDetail(LoginRequiredMixin, DetailView):
	model = Review
	template_name = "trip/review_detail.html"


class CommentDetail(LoginRequiredMixin, DetailView):
	model = ReviewResponse
	template_name = "trip/review_detail.html"

	def get(self, request, *args, **kwargs):
		response = ReviewResponse.objects.all()
		comments = ReviewResponse.objects.get(id=id)

		data = {
			'response': response,
			'comments': comments,

		}
		return render(request, self.template_name, data)


# # # ==== Trip Create View ==== #

class TripCreate(LoginRequiredMixin, CreateView):
	model = TravelPlan
	form_class = TripForm
	template_name = "trip/trip_create.html"
	success_url = reverse_lazy('dash')


	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

# # # ==== Review/Review Comment Create View ==== #

class ReviewCreate(LoginRequiredMixin, CreateView):
	model = Review 
	form_class = ReviewForm
	template_name = "trip/review_create.html"
	success_url = reverse_lazy('dash')

	def form_valid(self, form):
		form.instance.name = self.request.user
		return super().form_valid(form)

class ReviewComment(LoginRequiredMixin, CreateView):
	model = ReviewResponse
	form_class =  ReviewResponseForm
	template_name = "trip/review_comment.html"
	success_url = reverse_lazy('dash')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


# # # ==== Trip Delete View ==== #

class TripDelete(LoginRequiredMixin, DeleteView):
	model = TravelPlan
	template_name = "trip/trip_delete.html"
	context_object_name = "removetrip"
	success_url = reverse_lazy('dash')



# # # ==== Trip Update View ==== #

class TripUpdate(LoginRequiredMixin, UpdateView):
	model = TravelPlan
	form_class = TripForm
	template_name = "trip/trip_update.html"
	success_url = reverse_lazy('dash')

	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.created_by != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)


# # # ==== Trip Joiners View ==== #

class JoinTrip(LoginRequiredMixin, generic.RedirectView):
	
	def get(self, request, pk, *args, **kwargs):
		print(pk)
		plan = TravelPlan.objects.get(id=pk)
		user = self.request.user
		plan.travelBuddy.add(user)
		return redirect("/dashboard")
