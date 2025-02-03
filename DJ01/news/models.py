from django.db import models

class News_post(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    disription = models.CharField('Описание', max_length=150)
    content = models.TextField('Новость')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'