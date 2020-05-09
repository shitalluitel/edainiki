from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from apps.charkilla.controller.forms import (
    CharkillaCreateForm, CharkillaUpdateForm, CharkillaDetailFormSet)
from apps.charkilla.models import Charkilla
from apps.common.mixins import GenerateDetailPageFromTemplate, DynamicFormsetMixin


class CharkillaCreateView(DynamicFormsetMixin, CreateView):
    queryset = Charkilla.objects.all()
    form_class = CharkillaCreateForm
    template_name = 'charkilla/create.html'
    success_url = reverse_lazy('charkilla:list')
    formset_class = CharkillaDetailFormSet

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context.get('formset')

        if formset.is_valid() and form.is_valid():
            charkilla = form.save()
            for _formset in formset.forms:
                charkilla_detail = _formset.save(commit=False)
                charkilla_detail.charkilla = charkilla
                charkilla_detail.save()

            return redirect('student:list')
        else:
            messages.error(
                self.request,
                f'रेकर्ड सम्पादन गर्न सकिएन।'
            )
            return self.render_to_response(self.get_context_data(formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        return self.form_valid(form=self.get_form())


class CharkillaListView(ListView):
    queryset = Charkilla.objects.all()
    template_name = 'charkilla/list.html'


class CharkillaEditView(UpdateView):
    queryset = Charkilla.objects.all()
    form_class = CharkillaUpdateForm
    template_name = 'charkilla/create.html'
    success_url = reverse_lazy('charkilla:list')


class CharkillaDetailView(DetailView):
    queryset = Charkilla.objects.all()
    template_name = 'charkilla/detail.html'


class CharkillaDeleteView(DeleteView):
    queryset = Charkilla.objects.all()
    template_name = 'charkilla/create.html'
    success_url = reverse_lazy('charkilla:list')


class CharkillaTemplateView(DetailView, GenerateDetailPageFromTemplate):
    template_name = 'common/template.html'
    queryset = Charkilla.objects.all()

    # from django.template import engines
    #
    # django_engine = engines['django']
    # template = django_engine.from_string("Hello {{ name }}!")
