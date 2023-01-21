from django.shortcuts import render
from django.views import generic


class indexView(generic.TemplateView):
    template_name = "main/index.html"
    extra_context = {"page_title": "Home"}
