from django.contrib import admin
from .models import BugReport, FeatureRequest

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    # какие поля отображаются на странице списка объектов в административном интерфейсе
    list_display = ('title', 'project', 'task', 'status', 'priority',  'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')  # список фильтров для поиска
    # создает поисковую строку, чтобы отбирать объекты
    search_fields = ('title', 'project', 'status', 'priority')

    # поля, которые показываются при создании новог ообъекта класса
    fieldsets = [
        (None, {
            "fields":
                    ["title",
                     "description",
                     "project",
                     "task"
                     ],
                },
        ),
        ('Advanced', {
            'fields': ["status", "priority"]
            }
        )
    ]

    def edit_status_to_new(self, request, queryset):
        queryset.update(status='New')
    def edit_status_to_progress(self, request, queryset):
        queryset.update(status='In_progress')

    def edit_status_to_completed(self, request, queryset):
        queryset.update(status='Completed')

    actions = ['edit_status_to_new', 'edit_status_to_progress', 'edit_status_to_completed']


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    # какие поля отображаются на странице списка объектов в административном интерфейсе
    list_display = ('title', 'project', 'task', 'status', 'priority',  'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')  # список фильтров для поиска
    # создает поисковую строку, чтобы отбирать объекты
    search_fields = ('title', 'project', 'status', 'priority')

    # поля, которые показываются при создании новог ообъекта класса
    fieldsets = [
        (None, {
            "fields":
                    ["title",
                     "description",
                     "project",
                     "task"
                     ],
                },
        ),
        ('Advanced', {
            'fields': ["status", "priority"]
            }
        )
    ]