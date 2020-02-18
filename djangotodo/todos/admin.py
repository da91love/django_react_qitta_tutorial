# todos/admin.py
"""
adminを設定して、管理画面からTodoテーブルの操作を行えるようにします。
"""
from django.contrib import admin

from .models import Todo

admin.site.register(Todo)