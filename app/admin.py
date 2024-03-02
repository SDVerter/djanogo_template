from django.contrib import admin

# Register your models here.

from django.apps import apps
from .models import Page
from markdownx.admin import MarkdownxModelAdmin

from reversion.admin import VersionAdmin
from import_export.admin import ImportExportModelAdmin

app = apps.get_app_config('app')
class BaseModelAdmin(MarkdownxModelAdmin, VersionAdmin, ImportExportModelAdmin):
    pass

for model_name, model in app.models.items():
    if hasattr(model, 'autoshowadmin'):
        if model.autoshowadmin:
            admin.site.register(model, BaseModelAdmin)