import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InquiryForm,ScheduleCreateForm
from .models import Schedule

logger = logging.getLogger(__name__)
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('manage_schedule:inquiry')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class ScheduleListView(LoginRequiredMixin, generic.ListView):
    model = Schedule
    template_name = 'schedule_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Schedule.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

class ScheduleCreateView(LoginRequiredMixin,generic.CreateView):
    model = Schedule
    template_name = 'schedule_create.html'
    form_class = ScheduleCreateForm
    success_url = reverse_lazy('manage_schedule:schedult_list.html')

    def form_valid(self,form):
        schedule = form.save(commit=False)
        schedule.user = self.request.user
        schedule.save()
        messages.success(self.request,'作成')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.success(self.request,'失敗')
        return super().form_valid(form)
