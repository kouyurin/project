from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Nvmc


# Create your views here.
class NvmcList(ListView):
    model = Nvmc
    context_object_name = "tasks"

class NvmcDetail(DetailView):
    model = Nvmc
    context_object_name = "task"