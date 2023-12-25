from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Post.Status.PUBLISHED)
class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, #якщо з БД буде видалений автор, то і пости також будуть видалені
                               related_name='blog_posts') #ім'я зворотнього зв'язку

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager() #менеджер, применяемый по умолчанию
    published =PublishedManager() #конкретно-прикладной менеджер

    class Meta: #визначає метадані моделі
        ordering = ['-publish'] #Щоб в блозі нові пости публікувались зверху
        indexes = [
            models.Index(fields=['-publish']) #Визначає індекси в БД
        ]

    def __str__(self):
        return self.title