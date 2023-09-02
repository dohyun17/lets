from django.shortcuts import render, get_object_or_404
from django.views.generic import View
# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)