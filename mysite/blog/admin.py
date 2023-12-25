from django.contrib import admin
from .models import Post

@admin.register(Post) #Реєстрація моделі в адмін панелі. З'явилася панелька з постами на головній сторінці.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author'] #бічний фільтр
    search_fields = ['title', 'body'] #рядок пошуку
    prepopulated_fields = {'slug': ('title',)} #Автоматичне заповнення при створенні нового посту рядка slug рядком title
    raw_id_fields = ['author'] #при натисканні на лупу з'являється віджет де можна обрати автора серед тисячі авторів замість випадаючого списку
    date_hierarchy = 'publish' #навігація по місяцях і датах
    ordering = ['status', 'publish'] #задані критерії сортування