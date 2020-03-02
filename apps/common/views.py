from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'main_pages/_home.html'