from django.contrib import admin
from django import forms

from pontoon.terminology.models import Term, TermTranslation
from pontoon.base.models import Locale


class TermAdmin(admin.ModelAdmin):
    search_fields = [
        "text",
        "part_of_speech",
        "definition",
        "usage",
        "notes",
    ]
    list_display = (
        "text",
        "status",
        "part_of_speech",
        "definition",
        "usage",
        "notes",
        "case_sensitive",
        "exact_match",
        "do_not_translate",
        "forbidden",
    )
    list_editable = (
        "part_of_speech",
        "status",
        "case_sensitive",
        "exact_match",
        "do_not_translate",
        "forbidden",
    )


class LocaleChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{} ({})".format(obj.name, obj.code)


class TermTranslationAdmin(admin.ModelAdmin):
    search_fields = [
        "text",
    ]
    list_display = ("text", "term", "locale", "locale_code")

    def locale_code(self, term_translation):
        return term_translation.locale.code

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "locale":
            return LocaleChoiceField(queryset=Locale.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Term, TermAdmin)
admin.site.register(TermTranslation, TermTranslationAdmin)
