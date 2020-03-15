from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from apps.charkilla.controller.forms import (
    CharkillaCreateForm, CharkillaUpdateForm, CharkillaDetailFormSet)
from apps.charkilla.models import Charkilla
from apps.common.utils.template_util import generate_letter
from apps.setting.models import LetterTemplate


class CharkillaCreateView(CreateView):
    queryset = Charkilla.objects.all()
    form_class = CharkillaCreateForm
    template_name = 'charkilla/create.html'
    success_url = reverse_lazy('charkilla:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = CharkillaDetailFormSet(self.request.POST)
        else:
            context['formset'] = CharkillaDetailFormSet()
        return context

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
            # error_fields = set(
            #     chain.from_iterable(
            #         map(
            #             lambda x: list(x.keys()),
            #             formset.errors
            #         )
            #     )
            # )
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


class CharkillaTemplateView(DetailView):
    template_name = 'common/template.html'
    queryset = Charkilla.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.object
        if object:
            temp_obj = LetterTemplate.objects.filter(
                model=object.__class__.__name__
            ).first()
            if temp_obj:
                template = generate_letter(
                    instance=object,
                    letter_template=temp_obj.template
                )
            else:
                template = '<h3> Doesn\'t have any template. </h3>'
            context['template'] = template
        return context
