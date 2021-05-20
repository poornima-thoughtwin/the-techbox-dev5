from django.shortcuts import render
from django.views.generic.base import TemplateView


def index(request):
	return render(request,'payment/index.html')


class SuccessView(TemplateView):
    template_name = 'payment/success.html'