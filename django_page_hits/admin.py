import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import PageHit


class PageHitAdmin(admin.ModelAdmin):
    list_display = ('url', 'visit_date', 'anonymous_hits', 'registered_hits')
    list_filter = ('url', 'visit_date')
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


admin.site.register(PageHit, PageHitAdmin)
