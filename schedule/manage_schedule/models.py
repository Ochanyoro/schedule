import datetime
from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
# Create your models here.

class Schedule(models.Model):
    """スケジュール管理モデル"""

    user = models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)
    summary = models.CharField('概要', max_length=50)
    description = models.TextField('詳細な説明', blank=True)
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    private_number = models.CharField('他の人に公開用のnumber',max_length=20)
    group_number = models.CharField('グループ用のnumber',max_length=20)

    class Meta:
        verbose_name_plural = "Schedule"

    def __str__(self):
        return self.summary
