from google.cloud import translate_v2 as translate

translate_client = translate.Client()


def list_languages():
    """Lists all available languages."""

    results = translate_client.get_languages()

    for language in results:
        print(u"{name} ({language})".format(**language))


def list_languages_with_target(target):
    """Lists all available languages and localizes them to the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    results = translate_client.get_languages(target_language=target)

    for language in results:
        print(u"{name} ({language})".format(**language))


list_languages()
# Sample output for supported languages
# Afrikaans (af)
# Albanian (sq)
# Amharic (am)
# Arabic (ar)
# Armenian (hy)
# Azerbaijani (az)
# Basque (eu)
# Belarusian (be)
# Bengali (bn)
# Bosnian (bs)
# Bulgarian (bg)
# Catalan (ca)
# Cebuano (ceb)
# Chichewa (ny)
# Chinese (Simplified) (zh-CN)
# Chinese (Traditional) (zh-TW)
# Corsican (co)
# Croatian (hr)
# Czech (cs)
# Danish (da)
# Dutch (nl)
# English (en)
# Esperanto (eo)
# Estonian (et)
# Filipino (tl)
# Finnish (fi)
# French (fr)
# Frisian (fy)
# Galician (gl)
# Georgian (ka)
# German (de)
# Greek (el)
# Gujarati (gu)
# Haitian Creole (ht)
# Hausa (ha)
# Hawaiian (haw)
# Hebrew (iw)
# Hindi (hi)
# Hmong (hmn)
# Hungarian (hu)
# Icelandic (is)
# Igbo (ig)
# Indonesian (id)
# Irish (ga)
# Italian (it)
# Japanese (ja)
# Javanese (jw)
# Kannada (kn)
# Kazakh (kk)
# Khmer (km)
# Kinyarwanda (rw)
# Korean (ko)
# Kurdish (Kurmanji) (ku)
# Kyrgyz (ky)
# Lao (lo)
# Latin (la)
# Latvian (lv)
# Lithuanian (lt)
# Luxembourgish (lb)
# Macedonian (mk)
# Malagasy (mg)
# Malay (ms)
# Malayalam (ml)
# Maltese (mt)
# Maori (mi)
# Marathi (mr)
# Mongolian (mn)
# Myanmar (Burmese) (my)
# Nepali (ne)
# Norwegian (no)
# Odia (Oriya) (or)
# Pashto (ps)
# Persian (fa)
# Polish (pl)
# Portuguese (pt)
# Punjabi (pa)
# Romanian (ro)
# Russian (ru)
# Samoan (sm)
# Scots Gaelic (gd)
# Serbian (sr)
# Sesotho (st)
# Shona (sn)
# Sindhi (sd)
# Sinhala (si)
# Slovak (sk)
# Slovenian (sl)
# Somali (so)
# Spanish (es)
# Sundanese (su)
# Swahili (sw)
# Swedish (sv)
# Tajik (tg)
# Tamil (ta)
# Tatar (tt)
# Telugu (te)
# Thai (th)
# Turkish (tr)
# Turkmen (tk)
# Ukrainian (uk)
# Urdu (ur)
# Uyghur (ug)
# Uzbek (uz)
# Vietnamese (vi)
# Welsh (cy)
# Xhosa (xh)
# Yiddish (yi)
# Yoruba (yo)
# Zulu (zu)
# Hebrew (he)
# Chinese (Simplified) (zh)
