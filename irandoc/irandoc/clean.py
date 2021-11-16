import re
valid_character = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9",
                        u"۰", u"۱", u"۲", u"۳", u"۴", u"۵", u"۶", u"۷", u"۸", u"۹",
                        u"آ", u"ئ", u"ا", u"ب", u"ت", u"ث", u"ج", u"ح", u"خ", u"د",
                        u"ذ", u"ر", u"ز", u"س", u"ش", u"ص", u"ض", u"ط", u"ظ", u"ع",
                        u"غ", u"ف", u"ق", u"ل", u"م", u"ن", u"ه", u"چ", u"ژ", u"ک",
                        u"گ", u"ی", u"ی", u" ", u"و", u"پ", u"\u200c"]

dic_incorrect_to_correct = {u"ٱ": u"آ", u"ﺁ": u"آ",
                                 u"ﺌ": u"ئ", u"ﺋ": u"ئ",
                                 u"ﺍ": u"ا", u"ﺎ": u"ا",
                                 u"ﺏ": u"ب", u"ﺒ": u"ب", u"ﺐ": u"ب", u"ﺑ": u"ب",
                                 u"ﺕ": u"ت", u"ﺗ": u"ت", u"ﺖ": u"ت", u"ﺘ": u"ت",
                                 u"ﺚ": u"ث", u"ﺛ": u"ث", u"ﺜ": u"ث",
                                 u"ﺞ": u"ج", u"ﺠ": u"ج", u"ﺟ": u"ج", u"ﺝ": u"ج",
                                 u"ﺤ": u"ح", u"ﺣ": u"ح", u"ﺢ": u"ح",
                                 u"ﺨ": u"خ", u"ﺧ": u"خ", u"ﺦ": u"خ",
                                 u"ﺩ": u"د", u"ﺪ": u"د",
                                 u"ﺬ": u"ذ", u"ﺫ": u"ذ",
                                 u"ﺭ": u"ر", u"ﺮ": u"ر",
                                 u"ﺰ": u"ز", u"ﺯ": u"ز",
                                 u"ﺲ": u"س", u"ﺱ": u"س", u"ﺴ": u"س", u"ﺳ": u"س",
                                 u"ﺵ": u"ش", u"ﺶ": u"ش", u"ﺸ": u"ش", u"ﺷ": u"ش",
                                 u"ﺺ": u"ص", u"ﺼ": u"ص", u"ﺻ": u"ص",
                                 u"ﺿ": u"ض", u"ﻀ": u"ض", u"ﺽ": u"ض",
                                 u"ﻂ": u"ط", u"ﻄ": u"ط", u"ﻃ": u"ط",
                                 u"ﻈ": u"ظ", u"ﻇ": u"ظ",
                                 u"ﻊ": u"ع", u"ﻌ": u"ع", u"ﻋ": u"ع", u"ﻉ": u"ع",
                                 u"ﻎ": u"غ", u"ﻐ": u"غ", u"ﻏ": u"غ", u"ﻍ": u"غ",
                                 u"ﻑ": u"ف", u"ﻒ": u"ف", u"ﻔ": u"ف", u"ﻓ": u"ف",
                                 u"ﻕ": u"ق", u"ﻖ": u"ق", u"ﻘ": u"ق", u"ﻗ": u"ق",
                                 u"ﻝ": u"ل", u"ﻞ": u"ل", u"ﻠ": u"ل", u"ﻟ": u"ل",
                                 u"ﻡ": u"م", u"ﻢ": u"م", u"ﻤ": u"م", u"ﻣ": u"م",
                                 u"ﻦ": u"ن", u"ﻥ": u"ن", u"ﻨ": u"ن", u"ﻧ": u"ن",
                                 u"ە": u"ه", u"ھ": u"ه", u"ﻬ": u"ه", u"ﻩ": u"ه", u"ﻫ": u"ه",
                                 u"ﻪ": u"ه",
                                 u"ﮤ": u"ه",
                                 u"ۀ": u"ه", u"ة": u"ه", u"ہ": u"ه",
                                 u"ۆ": u"و", u"ﻭ": u"و", u"ﻮ": u"و", u"ۊ": u"و", u"ؤ": u"و",
                                 u"ﭙ": u"پ", u"ﭘ": u"پ", u"ﭗ": u"پ",
                                 u"ﭻ": u"چ", u"ﭽ": u"چ", u"ﭼ": u"چ",
                                 u"ﮊ": u"ژ",
                                 u"ﻛ": u"ک", u"ﻛ": u"ک", u"ﮏ": u"ک", u"ﮑ": u"ک", u"ﮐ": u"ک",
                                 u"ك": u"ک",
                                 u"ڪ": u"ک",
                                 u"ﻚ": u"ک", u"ګ": u"ک", u"ﻜ": u"ک",
                                 u"ﮓ": u"گ", u"ﮒ": u"گ", u"ﮕ": u"گ", u"ﮔ": u"گ",
                                 u"ﻱ": u"ی", u"ﻲ": u"ی", u"ﯾ": u"ی", u"ﻰ": u"ی", u"ﻴ": u"ی",
                                 u"ﻯ": u"ی",
                                 u"ﻳ": u"ی",
                                 u"ﯼ": u"ی", u"ﯽ": u"ی", u"ﯿ": u"ی", u"ي": u"ی", u"ى": u"ی",
                                 u"ے": u"ی",
                                 u"ێ": u"ی",
                                 u"ې": u"ی",
                                 u"ّ": u"",  # تشدید
                                 u"\u2009": u" ", u"\u200a": u" ", u"\u00a0": u" ",  # space \u00a0
                                 u"\u200e": u"\u200c", u"\u2029": u"\u200c"  ,# halfspace
                                u"\u200c":' '
                                 }
def clean_character( text):
    """
    متن را تبدیل به لیستی از کاراکتر می‌کند و تک تک آنها را اصلاح می‌کند در آخر کاراکترها را بهم چسبنده تا متن تمیز شده و کامل بدست آید
    :param text: متن ورودی
    :return: متن تمیز شده و تعداد کاراکترهایی که تمیز شده
    """
    if isinstance(text, bytes):
        text = text
    number_of_edits = 0
    text = re.sub("\s\s+", " ", text).strip()
    list_char = list(text)

    for index, val in enumerate(list_char):
        if val in dic_incorrect_to_correct:
            list_char[index] = dic_incorrect_to_correct[val]
            number_of_edits += 1
    return ('').join(list_char), number_of_edits

def clean_pattern_for_regex( text_or_list):
    """
    در این تابع علاوه بر اصلاح کاراکترها به فرم استاندارد، تمامی کاراکترهای غیر الفبای فارسی و اعداد و همچنین نقطه و نیمفاصله حذف می‌شوند
    :param text_or_list: ورودی یک متن یا لیستی از متن هست
    :return: خروجی متن تمیزشده است
    """
    if not type(text_or_list) == list:
        if isinstance(text_or_list, str):
            text_or_list = text_or_list
        regex = u"[^" + ('').join(valid_character) + u"]"
        clean_text, _ = clean_character(text_or_list)
        clean_text = re.sub(regex, " ", clean_text)
        clean_text = re.sub("\s\s+", " ", clean_text).strip()

        return clean_text
    if type(text_or_list) == list:
        clean_list_names = []
        regex = u"[^" + ("").join(valid_character) + u"]"
        for name in text_or_list:

            name_unicode = name
            if isinstance(name, str):
                name_unicode = name

            clean_name, _ = clean_character(name_unicode)
            clean_name = re.sub(regex, " ", clean_name)
            clean_name = re.sub("\s+", " ", clean_name).strip()
            if clean_name.strip() != "":
                clean_list_names.append(clean_name.strip())

        update_clean_list_names = [x for x in clean_list_names if x]
        return update_clean_list_names