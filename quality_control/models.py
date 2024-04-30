from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    title = models.CharField(max_length=255, verbose_name="Краткое описание бага")
    description = models.TextField(verbose_name="Полное описание бага")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект")
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, verbose_name="Задача")
    status = models.CharField(max_length=50, verbose_name="Статус бага", choices=[
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена')
    ])
    priority = models.IntegerField(verbose_name="Приоритет", choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего обновления")

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название запроса на функцию")
    description = models.TextField(verbose_name="Описание запроса")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект")
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, verbose_name="Задача")
    status = models.CharField(max_length=50, verbose_name="Статус запроса", choices=[
        ('under_review', 'Рассмотрение'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено')
    ])
    priority = models.IntegerField(verbose_name="Приоритет", choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего обновления")

    def __str__(self):
        return self.title
