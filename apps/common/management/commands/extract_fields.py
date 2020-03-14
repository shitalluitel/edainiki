import json
import pickle

from django.apps import apps
from django.core.management import BaseCommand

from apps.common.utils.commons import extract_related_model_fields, extract_fields


class Command(BaseCommand):
    help = 'Extracts fields from model'

    def add_arguments(self, parser):
        parser.add_argument(
            'model',
            type=str,
            default='all',
            nargs='?',
            help='Name of model whose fields need to be extracted'
        )

    def handle(self, *args, **options):
        model = options.get('model')
        extracted_fields = {}
        if model.lower() == 'all':
            models = list(
                filter(
                    lambda x: 'django.contrib' not in x.__module__,
                    apps.get_models()
                )
            )
            for model in models:
                related_fields = extract_related_model_fields(model)
                non_related_fields = extract_fields(model)[0]
                extracted_fields.update(
                    {
                        model._meta.verbose_name: {
                            'non_related_fields': non_related_fields,
                            'related_fields': related_fields
                        }
                    }
                )
            print(json.dumps(extracted_fields, indent=4, default=str))
            f = open("file.py", "w")
            for key, value in extracted_fields.items():
                f.writelines(f'{key.upper().replace(" ", "_")}={value}')
            f.close()
            return
        print(model)
