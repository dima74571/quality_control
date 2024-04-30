from django.contrib import admin
from .models import BugReport, FeatureRequest


def set_status_completed(modeladmin, request, queryset):
    queryset.update(status='completed')


set_status_completed.short_description = 'Установить статус "Завершена"'


class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Общая информация', {
            'fields': ('title', 'description')
        }),
        ('Проект и Задача', {
            'fields': ('project', 'task')
        }),
        ('Статус и Приоритет', {
            'fields': ('status', 'priority')
        }),
        ('Временные метки', {
            'fields': (('created_at', 'updated_at'),),
            'classes': ('collapse',)  # Эта группа будет сжата по умолчанию
        }),
    )
    actions = [set_status_completed]



admin.site.register(BugReport, BugReportAdmin)

class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description')
        }),
        ('Проект и Задача', {
            'fields': ('project', 'task')
        }),
        ('Статус и Приоритет', {
            'fields': ('status', 'priority')
        }),
        ('Даты', {
            'fields': (('created_at', 'updated_at'),),
            'classes': ('collapse',)
        }),
    )

admin.site.register(FeatureRequest, FeatureRequestAdmin)
