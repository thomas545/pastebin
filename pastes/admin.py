from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

class PasteAdmin(ImportExportModelAdmin):
    pass

class SyntaxHighLightAdmin(ImportExportModelAdmin):
    pass

admin.site.register(SyntaxHighLight, SyntaxHighLightAdmin)
admin.site.register(Paste, PasteAdmin)