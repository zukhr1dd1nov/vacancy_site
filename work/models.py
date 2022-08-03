from django.db import models
from common.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class TagModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT, related_name='tags', related_query_name='tags')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

class VacancyModel(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags', related_query_name='tags')
    salary = models.CharField(max_length=255)
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT)
    tags = models.ManyToManyField(TagModel, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

class ComplaintModel(models.Model):
    vacancy = models.ForeignKey(VacancyModel, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'жалоба'
        verbose_name_plural = 'жалобы'