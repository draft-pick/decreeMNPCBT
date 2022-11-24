from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Type(models.Model):
    """Тип документа"""
    title = models.CharField("Тип документа", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Тип документа'


class Decrees(models.Model):
    """Приказы"""
    type = models.ForeignKey(
        Type,
        verbose_name="Тип документа",
        null=True,
        on_delete=models.SET_NULL,
        related_name="decree_type"
    )
    title = models.CharField("Название", max_length=200)
    number = models.IntegerField("Номер")
    date_create = models.DateField()
    pub_date = models.DateField(auto_now_add=True)
    file = models.FileField(
        "Файл",
        upload_to="decree/%Y/%m/%d/"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_decree'
    )
    decree = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='main_decree',
                               null=True,
                               blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Приказ'
        verbose_name_plural = 'Приказы'


class DecreesChanged(models.Model):
    """Изменения в приказах"""
    type = models.ForeignKey(
        Type,
        verbose_name="Тип документа",
        null=True,
        on_delete=models.SET_NULL,
        related_name="decree_changed_type"
    )
    decree = models.ForeignKey(
        Decrees,
        verbose_name="Приказ",
        null=True,
        on_delete=models.SET_NULL,
        related_name="decree_changed_decree"
    )
    title = models.CharField("Название", max_length=200)
    number = models.IntegerField("Номер")
    date_create = models.DateField()
    pub_date = models.DateField(auto_now_add=True)
    file = models.FileField(
        "Файл",
        upload_to="decree/%Y/%m/%d/"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_decree_changed'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Изменения'
        verbose_name_plural = 'Изменения'
