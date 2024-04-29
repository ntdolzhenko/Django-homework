from django.contrib import admin
from .models import Project, Task

#inline class for Task model
class TaskInline(admin.TabularInline):
    model = Task
    extra = 0 # не будут отображаться пустые формы по умолчанию
    # поля, которые можно редактировать
    fields = ('name', 'description', 'assignee', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at') # поля, которые можно только читать
    can_delete = True # поля, которые можно удалить прямо из интерфейса проекта
    show_change_link = True # добавляет ссылку для перехода к форме редактирования задач



# класс админимтратора для модели Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at') # какие поля отображаются на странице списка объектов в административном интерфейсе
    search_fields = ('name', 'description') # создает поисковую строку, чтобы отбирать объекты
    ordering = ('created_at',) # определить порядок сортировки по умолчанию
    date_hierarchy = 'created_at' # навигация по датам

    # подключение inline для Task
    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # какие поля отображаются на странице списка объектов в административном интерфейсе
    list_display = ('name', 'project', 'assignee', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'assignee', 'project') # список фильтров для поиска
    search_fields = ('name', 'description') # создает поисковую строку, чтобы отбирать объекты
    list_editable = ('status', 'assignee') # поля, которые можно редактировать без перехода в режим редактирования
    readonly_fields = ('created_at', 'updated_at') # поля только для чтения в форме редактирования

