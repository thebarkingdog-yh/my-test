import time

import langid

L = ["Geeksforgeeks is a computer science portal for geeks",
     "Geeksforgeeks - это компьютерный портал для гиков",
     "Geeksforgeeks es un portal informático para geeks",
     "Geeksforgeeks是面向极客的计算机科学门户",
     "Geeksforgeeks geeks के लिए एक कंप्यूटर विज्ञान पोर्टल है",
     "Geeksforgeeksは、ギーク向けのコンピューターサイエンスポータルです。",
     ]

for i in L:
    print(langid.classify(i))

# %%
from lingua import Language, LanguageDetectorBuilder

# detector = LanguageDetectorBuilder.from_all_languages().build()
languages = [Language.CHINESE, Language.ENGLISH, Language.JAPANESE, Language.KOREAN,
             Language.FRENCH, Language.SPANISH, Language.ARABIC, Language.CATALAN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()
output = detector.detect_language_of("today 去 where")
outputs = detector.detect_languages_in_parallel_of(["today 去 where", ""])
print(output.iso_code_639_1.name.lower())
print(outputs)
# %%
from pprint import pprint

languages = detector.compute_language_confidence_values("languages are awesome")
lang = [(lang.language.iso_code_639_1.name.lower(), f"{lang.value:.4f}") for lang in
        languages if lang.value > 0.01]
pprint(lang)


# %%
from pyfranc import franc

franc.lang_detect('Alle menslike wesens word vry')[0][0]  # 'afr'
franc.lang_detect('এটি একটি ভাষা একক IBM স্ক্রিপ্ট')[0][0]  # 'ben'
franc.lang_detect('Alle menneske er fødde til fridom')[0][0]  # 'nno'
franc.lang_detect('')[0][0]  # 'und'

franc.lang_detect('哈囉你好', minlength=3)[0][0]  # 'sco'

# %%
from enum import Enum


class Xyz(str, Enum):
    x = "a"
    y = "b"
    z = ""


Xyz.z.value
