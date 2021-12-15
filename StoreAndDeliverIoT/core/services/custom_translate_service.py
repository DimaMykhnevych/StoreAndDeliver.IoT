from core.constants.language import Language
from core.models.user_settings import UserSettings


en = {'about': 'About'}
ua = {'about': 'Інформація'}
ru = {'about': 'Информация'}


def _(key):
    if UserSettings.language is None:
        return
    if UserSettings.language == Language.en:
        return en[key]
    elif UserSettings.language == Language.ua:
        return ua[key]
    elif UserSettings.language == Language.ru:
        return ru[key]
    else:
        return en[key]
