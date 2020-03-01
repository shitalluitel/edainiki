import os
import shutil

from django.conf import settings
from django.core.management.templates import TemplateCommand

APPS_DIR = settings.APPS_DIR

TEMPLATE_BASE_DIR = 'scratch/app_template'


class Command(TemplateCommand):
    help = (
        f"Creates new controller on the location {APPS_DIR}."
    )
    missing_args_message = "You must provide an App name."

    def handle(self, *args, **options):
        app_name = options.pop('name')
        _ = options.pop('directory')

        print('\n**Initiating startapp command **\n')
        target = os.path.join(APPS_DIR, app_name.lower())
        if not os.path.exists(target):
            os.mkdir(target)
        print(f"Creating controller with name {app_name} ...")
        options.update({
            'template': TEMPLATE_BASE_DIR
        })

        super(Command, self).handle('controller', app_name, target, **options)
        print("Successfully crated controller.")
        print(f"Target for new controller in 'apps.{app_name}'")

        print("** Copying html template files **")

        html_templates_dir = os.path.join(target, 'templates')
        if not os.path.exists(os.path.join(html_templates_dir, f'{ app_name }')):
            os.mkdir(os.path.join(html_templates_dir, f'{ app_name }'))

        html_files = os.listdir(html_templates_dir)

        for file in html_files:
            file_path = os.path.join(html_templates_dir, file)
            if os.path.isfile(file_path):
                shutil.copy(file_path, os.path.join(html_templates_dir, f'{app_name}'))
                if os.path.exists(file_path):
                    os.remove(file_path)

        print("** Copying html template files completed successfully **")
