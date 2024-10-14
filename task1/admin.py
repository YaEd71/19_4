from django.contrib import admin
from .models import Buyer, Game
# Register your models here.


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age') # В списке отображаются имя, баланс и возраст
    list_filter = ('age',) #  Фильтр по возрасту
    search_fields = ('name',) # Поиск по имени
# Поля разделены на две секции: "Основная информация" и "Финансы"
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'age')
        }),
        ('Финансы', {
            'fields': ('balance',)
        }),
    )

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
# В списке отображаются название, стоимость, размер и наличие возрастного ограничения
    list_display = ('title', 'cost', 'size', 'age_limited')
    list_filter = ('age_limited', 'cost') # фильтры по наличию возрастного ограничения и стоимости
    search_fields = ('title', 'description') # Поиск  по названию и описанию
# Поля разделены на три секции: "Основная информация", "Технические детали" и "Ограничения"
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description')
        }),
        ('Технические детали', {
            'fields': ('size', 'cost')
        }),
        ('Ограничения', {
            'fields': ('age_limited',)
        }),
    )
# Горизонтальный фильтр для поля buyer (ManyToMany связь), что упрощает выбор покупателей для игры
    filter_horizontal = ('buyer',)