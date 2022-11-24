from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count

from .models import Decrees, DecreesChanged, Type
from .forms import DecreeForm


@login_required()
def decree_list(request):
    """Главная страница"""
    decrees = Decrees.objects.all()
    types = Type.objects.annotate(sum_documents=Count('decree_type'))

    def count_documents():
        sum_count = []

        for type in types:
            if type.sum_documents > 0:
                sum_count.append(type.sum_documents)
        return sum_count

    context = {
        'title': 'Главная страница',
        'decrees': decrees,
        'types': types,
        'types_': count_documents(),
    }
    return render(request, 'decree/index.html', context)


@login_required()
def decree_create(request):
    """Добавить новый документ"""
    form = DecreeForm()
    context = {
        'title': 'Добавить документ',
        'form': form
    }
    return render(request, 'decree/create.html', context)


@login_required()
def decree_changed_create(request, decree_id):
    """Добавить новое внесение изменений"""
    form = DecreeForm()
    context = {
        'title': 'Добавить изменения',
        'form': form
    }
    return render(request, 'decree/create_changed.html', context)


@login_required()
def decree_detail(request, decree_id):
    """Детальный просмотр документа"""
    decree = get_object_or_404(Decrees, pk=decree_id)
    context = {
        'title': decree.title,
        'dec': decree
    }
    return render(request, 'decree/detail.html', context)


@login_required()
def decree_changed_detail(request, decree_id, decree_changed_id):
    """Детальный просмотр прикрепленного документа"""
    decree_changed = get_object_or_404(DecreesChanged, pk=decree_changed_id)
    context = {
        'title': decree_changed.title,
        'decree_changed': decree_changed
    }
    return render(request, 'decree/decree_changed_detail.html', context)