from django import forms
import bootstrap_datepicker_plus as datetimepicker
from django.core.mail import EmailMessage

from .models import Schedule
from password import *

class ManagementForm(forms.Form):
    management_p = forms.CharField(label = 'パスワード',max_length=50)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['management_p'].widget.attrs['placeholder'] = '管理のためのパスワードを入力してください'
        self.fields['management_p'].widget.attrs['class'] = 'form-control col-9'

    def clean_management_p(self):
        management_p =self.cleaned_data['management_p']
        if management_p != edit_password:
            raise forms.ValidationError(
                'パスワードが正しくありません'
            )
        return management_p

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['name'].widget.attrs['class'] = 'form-control col-9'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
        from_email = 'w@gmail.com'
        to_list = [
            'wadaoo0223@icloud.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()


class BS4ScheduleForm(forms.ModelForm):
    """Bootstrapに対応するためのModelForm"""

    class Meta:
        model = Schedule
        fields = ('summary', 'description', 'start_time', 'end_time')
        widgets = {
            'summary': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'start_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'end_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'private_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'group_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),

        }

    def clean_end_time(self):
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        if end_time <= start_time:
            raise forms.ValidationError(
                '終了時間は、開始時間よりも後にしてください'
            )
        return end_time
