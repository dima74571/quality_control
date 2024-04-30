from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from quality_control.models import FeatureRequest, BugReport


def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = f"<h1>Контроль качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a><br>{bug.status}</li>'
    bugs_html += "</ul>"
    return HttpResponse(bugs_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = f'<h1>Название:{bug.title}</h1><p>Описание:{bug.description}</p><br>Статус:{bug.status}<br>Приоритет:{bug.priority}<br>Проект:{bug.project}<br>Название задачи:{bug.task}'
        return HttpResponse(response_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a><br>{feature.status}</li>'
    features_html += "</ul>"
    return HttpResponse(features_html)


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = f'<h1>Название:{feature.title}</h1><p>Описание:{feature.description}</p><br>Статус:{feature.status}<br>Приоритет:{feature.priority}<br>Проект:{feature.project}<br>Название задачи:{feature.task}'
        return HttpResponse(response_html)
