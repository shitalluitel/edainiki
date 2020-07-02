from django.template import engines

from apps.common.utils.template_util import generate_letter, generate_form
from apps.setting.constants import NIBEDAN
from apps.setting.models import LetterTemplate


class GenerateDetailPageFromTemplate:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object
        if obj:
            temp_obj = LetterTemplate.objects.get(
                model=obj.__class__.__name__,
                type=NIBEDAN
            )
            if temp_obj:
                template = generate_letter(
                    instance=obj,
                    letter_template=temp_obj.template
                )
            else:
                template = '<h3> Doesn\'t have any template. </h3>'
            context['template'] = template
        return context


class DynamicFormsetMixin:
    def get_formset(self):
        formset_class = hasattr(self, 'formset_class')
        assert formset_class, 'Must specify formset class.'
        return getattr(self, 'formset_class')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formset = getattr(self, 'get_formset')()
        if self.request.method == 'POST':
            formset = formset(self.request.POST)
        else:
            formset = formset
        context['formset'] = formset
        template = generate_form(
            form=context.get('form'),
            formset=context.get('formset')
        )
        form = None
        if template:
            template = engines['django'].from_string(template)
            form = template.render(context, self.request)

        context['form'] = form
        return context


class DynamicFormMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        template = engines['django'].from_string(
            generate_form(
                form=context.get('form'),
            )
        )
        context['form'] = template.render(context, self.request)
        return context
