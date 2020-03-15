from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from apps.setting.models import Setting
from apps.setting.controller.forms import (SettingCreateForm, SettingUpdateForm)


class SettingCreateView(CreateView):
    queryset = Setting.objects.all()
    form_class = SettingCreateForm
    template_name = 'setting/create.html'
    success_url = reverse_lazy('setting:list')


class SettingListView(ListView):
    queryset = Setting.objects.all()
    template_name = 'setting/list.html'


class SettingEditView(UpdateView):
    queryset = Setting.objects.all()
    form_class = SettingUpdateForm
    template_name = 'setting/create.html'
    success_url = reverse_lazy('setting:list')


class SettingDetailView(DetailView):
    queryset = Setting.objects.all()
    template_name = 'setting/list.html'


class SettingDeleteView(DeleteView):
    queryset = Setting.objects.all()
    template_name = 'setting/create.html'
    success_url = reverse_lazy('setting:list')

