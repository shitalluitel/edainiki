from itertools import chain

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView, FormView

from apps.common.constants import template_map
from apps.setting.controller.forms import LetterTemplateForm, TemplateRedirectForm
from apps.setting.models import LetterTemplate
# from apps.student.utils import generate_letter


class LetterTemplateUpdateView(UpdateView):
    success_url = reverse_lazy('setting:template-create')
    form_class = LetterTemplateForm
    template_name = 'setting/letter_template/letter.html'
    queryset = LetterTemplate.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        non_related_fields, related_fields = self.extract_placeholder()
        context['non_related_fields'] = non_related_fields
        context['related_fields'] = related_fields
        return context

    def extract_placeholder(self):
        instance = self.get_object()
        place_holder = getattr(template_map, instance.model.upper())
        non_related_fields = self.convert_to_dict(
            place_holder.get('non_related_fields')
        )
        related_fields = self.convert_to_dict(
            chain.from_iterable(
                place_holder.get('related_fields').values()
            )
        )
        return non_related_fields, related_fields

    @staticmethod
    def convert_to_dict(data):
        return map(lambda x: '{{ _ }}'.replace('_', x), data)


class TemplateRedirectView(FormView):
    template_name = 'common/create.html'
    form_class = TemplateRedirectForm
    success_url = None

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            model = form.data.get('model')
            type = form.data.get('type')
            obj, created = LetterTemplate.objects.get_or_create(
                model=model,
                type=type
            )
            return redirect('setting:template-update', pk=obj.id)
        else:
            return self.form_invalid(form)

