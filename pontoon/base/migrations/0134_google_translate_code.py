# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-17 18:44
from __future__ import unicode_literals

from bulk_update.helper import bulk_update
from django.db import migrations, models


"""
The map below was generated using the code below, where:
- `pontoon` is a list of pontoon.mozilla.org locale codes
- `google` is a list of Google Translate locales codes
- `map` is PONTOON_TO_GOOGLE_TRANSLATE_MAP
at the time of writing the script.

for p in pontoon:
  if p == 'zh-TW':
    map.append((p, 'zh-TW'))
  elif p == 'he':
    map.append((p, 'iw'))
  elif p == 'jv':
    map.append((p, 'jw'))
  elif p == 'nb-NO':
    map.append((p, 'no'))
  else:
    short = p.split("-")[0]
    if short in google:
      map.append((p, short))
"""
PONTOON_TO_GOOGLE_TRANSLATE_MAP = [
    ("af", "af"),
    ("am", "am"),
    ("ar", "ar"),
    ("az", "az"),
    ("be", "be"),
    ("bg", "bg"),
    ("bn", "bn"),
    ("bn-BD", "bn"),
    ("bn-IN", "bn"),
    ("bs", "bs"),
    ("ca", "ca"),
    ("cs", "cs"),
    ("cy", "cy"),
    ("da", "da"),
    ("de", "de"),
    ("el", "el"),
    ("en", "en"),
    ("en-CA", "en"),
    ("en-GB", "en"),
    ("en-US", "en"),
    ("en-ZA", "en"),
    ("eo", "eo"),
    ("es", "es"),
    ("es-AR", "es"),
    ("es-CL", "es"),
    ("es-ES", "es"),
    ("es-MX", "es"),
    ("et", "et"),
    ("eu", "eu"),
    ("fa", "fa"),
    ("fi", "fi"),
    ("fr", "fr"),
    ("fy-NL", "fy"),
    ("ga-IE", "ga"),
    ("gd", "gd"),
    ("gl", "gl"),
    ("gu-IN", "gu"),
    ("ha", "ha"),
    ("he", "iw"),
    ("hi-IN", "hi"),
    ("hr", "hr"),
    ("ht", "ht"),
    ("hu", "hu"),
    ("hy-AM", "hy"),
    ("id", "id"),
    ("ig", "ig"),
    ("is", "is"),
    ("it", "it"),
    ("ja", "ja"),
    ("jv", "jw"),
    ("ka", "ka"),
    ("kk", "kk"),
    ("km", "km"),
    ("kn", "kn"),
    ("ko", "ko"),
    ("ku", "ku"),
    ("ky", "ky"),
    ("lb", "lb"),
    ("lo", "lo"),
    ("lt", "lt"),
    ("lv", "lv"),
    ("mg", "mg"),
    ("mk", "mk"),
    ("ml", "ml"),
    ("mn", "mn"),
    ("mr", "mr"),
    ("ms", "ms"),
    ("my", "my"),
    ("nb-NO", "no"),
    ("ne-NP", "ne"),
    ("nl", "nl"),
    ("ny", "ny"),
    ("pa-IN", "pa"),
    ("pl", "pl"),
    ("pt-BR", "pt"),
    ("pt-PT", "pt"),
    ("ro", "ro"),
    ("ru", "ru"),
    ("si", "si"),
    ("sk", "sk"),
    ("sl", "sl"),
    ("sn", "sn"),
    ("sq", "sq"),
    ("sr", "sr"),
    ("su", "su"),
    ("sv-SE", "sv"),
    ("sw", "sw"),
    ("ta", "ta"),
    ("te", "te"),
    ("tg", "tg"),
    ("th", "th"),
    ("tl", "tl"),
    ("tr", "tr"),
    ("uk", "uk"),
    ("ur", "ur"),
    ("uz", "uz"),
    ("vi", "vi"),
    ("xh", "xh"),
    ("yo", "yo"),
    ("zh-CN", "zh"),
    ("zh-HK", "zh"),
    ("zh-TW", "zh-TW"),
    ("zu", "zu"),
]


def populate_google_translate_code(apps, schema_editor):
    """
    Add alternative locale codes for our integration with Google Cloud Translation API.
    """
    Locale = apps.get_model("base", "Locale")
    locale_map = {l.code: l for l in Locale.objects.all()}

    for pontoon_code, google_translate_code in PONTOON_TO_GOOGLE_TRANSLATE_MAP:
        if pontoon_code in locale_map:
            locale_map[pontoon_code].google_translate_code = google_translate_code

    bulk_update(list(locale_map.values()), update_fields=["google_translate_code"])


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0133_calculate_strings_with_errors_warnings"),
    ]

    operations = [
        migrations.AddField(
            model_name="locale",
            name="google_translate_code",
            field=models.CharField(
                blank=True,
                help_text='\n        Google Translate maintains its own list of\n        <a href="https://translate.google.com/intl/en/about/languages/">\n        supported locales</a>. Choose a matching locale from the list or leave blank to disable\n        support for Google Cloud Translation machine translation service.\n        ',
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="locale",
            name="ms_terminology_code",
            field=models.CharField(
                blank=True,
                help_text="\n        Microsoft Terminology uses language codes that include both the language and\n        the country/region. Choose a matching locale from the list or leave blank to disable support\n        for Microsoft terminology:\n\n        af-za, am-et, ar-dz, ar-eg, ar-sa, as-in, az-latn-az, be-by, bg-bg, bn-bd, bn-in,\n        bs-cyrl-ba, bs-latn-ba, ca-es, ca-es-valencia, chr-cher-us, cs-cz, cy-gb, da-dk, de-at,\n        de-ch, de-de, el-gr, en-au, en-ca, en-gb, en-hk, en-ie, en-in, en-my, en-ng, en-nz, en-ph,\n        en-pk, en-sg, en-tt, en-us, en-za, es-ar, es-bo, es-cl, es-co, es-cr, es-do, es-ec, es-es,\n        es-gt, es-hn, es-mx, es-ni, es-pa, es-pe, es-pr, es-py, es-sv, es-us, es-uy, es-ve, et-ee,\n        eu-es, fa-ir, fi-fi, fil-ph, fo-fo, fr-be, fr-ca, fr-ch, fr-dz, fr-fr, fr-ma, fr-tn,\n        fuc-latn-sn, ga-ie, gd-gb, gl-es, gu-in, guc-ve, ha-latn-ng, he-il, hi-in, hr-hr, hu-hu,\n        hy-am, id-id, ig-ng, is-is, it-ch, it-it, iu-latn-ca, ja-jp, ka-ge, kk-kz, km-kh, kn-in,\n        ko-kr, kok-in, ku-arab-iq, ky-kg, lb-lu, lo-la, lt-lt, lv-lv, mi-nz, mk-mk, ml-in, mn-mn,\n        mr-in, ms-bn, ms-my, mt-mt, my-mm, nb-no, ne-np, nl-be, nl-nl, nn-no, nso-za, or-in,\n        pa-arab-pk, pa-in, pl-pl, prs-af, ps-af, pt-br, pt-pt, quc-latn-gt, quz-pe, ro-md, ro-ro,\n        ru-kz, ru-ru, rw-rw, sd-arab-pk, si-lk, sk-sk, sl-si, sp-xl, sq-al, sr-cyrl-ba, sr-cyrl-rs,\n        sr-latn-me, sr-latn-rs, sv-se, sw-ke, ta-in, te-in, tg-cyrl-tj, th-th, ti-et, tk-tm, tl-ph,\n        tn-za, tr-tr, tt-ru, ug-cn, uk-ua, ur-pk, uz-cyrl-uz, uz-latn-uz, vi-vn, wo-sn, xh-za,\n        yo-ng, zh-cn, zh-hk, zh-sg, zh-tw, zu-za\n        ",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="locale",
            name="ms_translator_code",
            field=models.CharField(
                blank=True,
                help_text='\n        Microsoft Translator maintains its own list of\n        <a href="https://docs.microsoft.com/en-us/azure/cognitive-services/translator/languages">\n        supported locales</a>. Choose a matching locale from the list or leave blank to disable\n        support for Microsoft Translator machine translation service.\n        ',
                max_length=20,
            ),
        ),
        migrations.RunPython(
            populate_google_translate_code, migrations.RunPython.noop,
        ),
    ]
