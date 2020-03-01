from django.shortcuts import render, redirect, reverse

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from apps.settings.models import Settings
from apps.settings.controller.forms import (SettingsCreateForm, SettingsUpdateForm)


class SettingsCreateView(CreateView):
    queryset = Settings.objects.all()
    form_class = SettingsCreateForm
    template_name = 'settings/create.html'
    success_url = 'settings:list'


class SettingsListView(ListView):
    queryset = Settings.objects.all()
    template_name = 'settings/list.html'


class SettingsEditView(UpdateView):
    queryset = Settings.objects.all()
    form_class = SettingsUpdateForm
    template_name = 'settings/create.html'
    success_url = 'settings:list'


class SettingsDetailView(DetailView):
    queryset = Settings.objects.all()
    template_name = 'settings/list.html'


class SettingsDeleteView(DeleteView):
    queryset = Settings.objects.all()
    template_name = 'settings/create.html'
    success_url = 'settings:list'

