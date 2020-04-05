from django.template import engines

from apps.common.utils.template_util import generate_letter, generate_form
from apps.setting.models import LetterTemplate


class GenerateDetailPageFromTemplate:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object
        if obj:
            temp_obj = LetterTemplate.objects.filter(
                model=obj.__class__.__name__
            ).first()
            if temp_obj:
                template = generate_letter(
                    instance=obj,
                    letter_template=temp_obj.template
                )
            else:
                template = '<h3> Doesn\'t have any template. </h3>'
            context['template'] = template
        return context


class CreateFormsetMixin:
    def get_formset(self):
        formset_class = hasattr(self, 'formset_class')
        if formset_class:
            return formset_class
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = getattr(self, 'get_formset')(self.request.POST)
        else:
            context['formset'] = getattr(self, 'get_formset')

        template = engines['django'].from_string(
            generate_form(
                form=context.get('form'),
                formset=context.get('formset')
            )
        )
        context['form'] = template.render(context, self.request)
        return context

