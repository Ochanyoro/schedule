from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Schedule(models.Model):
    """スケジュール管理モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    schedule_start = models.DateField(
        verbose_name='予定日[初め]',
        blank=False,
        null=False,
    )
    # サンプル項目2 日付時刻
    schedule_end = models.DateField(
        verbose_name='予定日[終わり]',
        blank=False,
        null=False,
    )
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = "Schedule"

    def __str__(self):
        return self.title
