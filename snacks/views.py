from os import name
from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    fields = ['title','purchaser', 'description']
    model = Snack
class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["title", "description"]

class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    fields = reverse_lazy("snack_list")
