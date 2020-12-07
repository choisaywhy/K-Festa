import operator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'festival/index.html')

def category(request):
    categories = FestivalCategory.objects.all()
    return render(request, 'festival/category.html', {'categories':categories})

def category_list(request, category_key):
    category = get_object_or_404(FestivalCategory, category_key=category_key)
    festival_all = Festival.objects.filter(category_key=category_key).all()
    page_numbers_range = 9
    # 한 페이지에 나올 게시글 수
    paginator = Paginator(festival_all,page_numbers_range)
    page = request.GET.get('page')
    festivals = paginator.get_page(page)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'festival/category_list.html',{'festival_all':festival_all, 'category':category, 'festivals':festivals, 'page_range':page_range, 'paginator':paginator })