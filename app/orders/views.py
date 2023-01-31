from django.views.generic.edit import CreateView
from orders.forms import OrderForm
from django.urls import reverse_lazy
from common.views import TitleMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.core.mail import send_mail





class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('index')
    title = 'Wedding Look - Запись на примерку'

    def form_valid(self, form):
        data = form.data
        subject = f'Запись на примерку для {data["first_name"]} {data["last_name"]} Телефон: {data["phoneNumber"]}'
        email(subject, data["phoneNumber"])
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)

def email(subject, content):
    send_mail(
        subject,
        content,
        settings.EMAIL_HOST_USER,
        ['igonin.nikita1326@mail.ru']
    )

def success(request):
    return HttpResponse('Письмо отправлено!')