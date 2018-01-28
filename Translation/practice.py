import requests
import os


def translation(path_in, path_out, lang_from, lang_to='ru'):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param path_in: <str> path for file for translation.
    :param path_out: <str> path for output file for translation.
    :param lang_from: <str> language of source.
    :param lang_to: <str> language of target.
    :return: <str> translated text.
    """
    lang = lang_from + '-' + lang_to
    with open(path_in) as f:
        data = f.read()
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    params = {
        'key': key,
        'lang': lang,
        'text': data,
    }
    response = requests.get(url, params=params).json()
    with open(path_out, 'w') as f:
        f.write(' '.join(response.get('text', [])))
    return ' '.join(response.get('text', []))


path_de_from = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DE.txt')
path_es_from = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ES.txt')
path_fr_from = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'FR.txt')
path_de_to = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DE_RU.txt')
path_es_to = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ES_RU.txt')
path_fr_to = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'FR_RU.txt')

de_ru = translation(path_de_from, path_de_to, 'de')
es_ru = translation(path_es_from, path_es_to, 'es')
fr_ru = translation(path_fr_from, path_fr_to, 'fr')
