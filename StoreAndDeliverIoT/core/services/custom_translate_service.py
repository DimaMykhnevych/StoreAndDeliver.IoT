from core.constants.language import Language
from core.enums.temperature_unit import TemperatureUnit
from core.models.user_settings import UserSettings

en = {
    'about': 'About',
    'program': 'Program',
    'developers': 'Developers',
    'current_active_requests': 'Current active cargo requests',
    'store': 'Store',
    'deliver': 'Deliver',
    'loading': 'Loading...',
    'required_settings': 'Required Indicators Settings',
    'start': 'Start',
    'stop': 'Stop',
    'enable_security_mode': 'Enable security mode',
    'disable_security_mode': 'Disable security mode',
    'about_program': 'About program',
    'about_program_description': 'StoreAndDeliver IoT program to track environmental conditions of stored '
                                 'and delivered cargo.\nLink to website: ',
    'about_developers': 'About developers',
    'about_developers_description': 'Program was developed by Dmytro Mykhnevych, '
                                    'student of Kharkiv National University of Radio Electronics.\n'
                                    'Email: dmytro.mykhnevych@nure.ua',
    'temperature': 'Temperature',
    'humidity': 'Humidity',
    'luminosity': 'Luminosity',
    'language': 'Language',
    'english': 'English',
    'ukrainian': 'Ukrainian',
    'russian': 'Russian',
    'celsius': 'Celsius',
    'fahrenheit': 'Fahrenheit',
    'kelvin': 'Kelvin',
    'dashboard': 'Dashboard',
    'login': 'Login',
    'username': 'Username: ',
    'password': 'Password: ',
    'log_in': 'Log In',
    'access_denied': 'Access denied',
    'invalid_credentials': 'Username or password is invalid',
    'email_confirmation_required': 'You need to confirm your email',
    'low_temperature': 'The temperature is below the permissible value. Increasing the temperature.',
    'high_temperature': 'The temperature is higher than the permissible value. Lowering the temperature.',
    'low_humidity': 'The humidity is below the permissible value. Increasing the humidity.',
    'high_humidity': 'The humidity is higher than the permissible value. Lowering the humidity.',
    'low_luminosity': 'The luminosity is below the permissible value. Increasing the luminosity.',
    'high_luminosity': 'The luminosity is higher than the permissible value. Lowering the luminosity.'
}
ua = {
    'about': 'Інформація',
    'program': 'Програма',
    'developers': 'Розробники',
    'current_active_requests': 'Поточні активні заяви',
    'store': 'Зберігання',
    'deliver': 'Перевезення',
    'loading': 'Завантаження...',
    'required_settings': 'Налаштовані показники середовища',
    'start': 'Увімкнути',
    'stop': 'Вимкнути',
    'enable_security_mode': 'Увікмнути режим охорони',
    'disable_security_mode': 'Вимкнути режим охорони',
    'about_program': 'Про програму',
    'about_program_description': 'StoreAndDeliver IoT програма для підтримання необхідного рівня значень показників '
                                 'оточоючого середовища '
                                 'під час перевезення або збереження вантажів.\nПосилання на вебсайт: ',
    'about_developers': 'Про розробників',
    'about_developers_description': 'Програма була розроблена Михневичем Дмитром, '
                                    'студентом Харківського національного університету радіоелектроніки.\n'
                                    'Email: dmytro.mykhnevych@nure.ua',
    'temperature': 'Температура',
    'humidity': 'Вологість',
    'luminosity': 'Освітленність',
    'language': 'Мова',
    'english': 'Англійська',
    'ukrainian': 'Українська',
    'russian': 'Російська',
    'celsius': 'Цельсій',
    'fahrenheit': 'Фаренгейт',
    'kelvin': 'Кельвін',
    'dashboard': 'Панель управління',
    'login': 'Вхід',
    'username': 'Ім\'я користувача: ',
    'password': 'Пароль: ',
    'log_in': 'Увійти',
    'access_denied': 'Доступ заборонено',
    'invalid_credentials': 'Ім\'я або пароль невірні',
    'email_confirmation_required': 'Підтвердіть свою електрону пошту',
    'low_temperature': 'Температура нижче за допустиме значення. Підвищення температури.',
    'high_temperature': 'Температура вижче за допустиме значення. Зниження температури.',
    'low_humidity': 'Вологість нижче за допустиме значення. Підвищення вологості.',
    'high_humidity': 'Вологість вижче за допустиме значення. Зниження вологості.',
    'low_luminosity': 'Освітленність нижче за допустиме значення. Підвищення освітленності.',
    'high_luminosity': 'Освітленність вижче за допустиме значення. Зниження освітленності.'
}
ru = {
    'about': 'Информация',
    'program': 'Программа',
    'developers': 'Разработчики',
    'current_active_requests': 'Текущие активные заявки',
    'store': 'Хранение',
    'deliver': 'Доставка',
    'loading': 'Загрузка...',
    'required_settings': 'Настроенные показатели окрущающей среды',
    'start': 'Включить',
    'stop': 'Выключить',
    'enable_security_mode': 'Включить режим охраны',
    'disable_security_mode': 'Выключить режим охраны',
    'about_program': 'Про программу',
    'about_program_description': 'StoreAndDeliver IoT программа для поддержки необходимого уровня значений '
                                 'показателей окружающей среды '
                                 'во время перевозки или хранения грузов.\nСсылка на вебсайт: ',
    'about_developers': 'Про разработчиков',
    'about_developers_description': 'Программа была разработана Михневичем Дмитрием, '
                                    'студентом Харьковского национального университета радиоэлектроники.\n'
                                    'Email: dmytro.mykhnevych@nure.ua',
    'temperature': 'Температура',
    'humidity': 'Влажность',
    'luminosity': 'Освещенность',
    'language': 'Язык',
    'english': 'Английский',
    'ukrainian': 'Украинский',
    'russian': 'Русский',
    'celsius': 'Цельсий',
    'fahrenheit': 'Фаренгейт',
    'kelvin': 'Кельвин',
    'dashboard': 'Панель управления',
    'login': 'Вход',
    'username': 'Имя пользователя: ',
    'password': 'Пароль: ',
    'log_in': 'Войти',
    'access_denied': 'Доступ запрещен',
    'invalid_credentials': 'Имя или пароль неверны',
    'email_confirmation_required': 'Подтвердите свою электронную почту',
    'low_temperature': 'Температура ниже допустимого значения. Повышение температуры.',
    'high_temperature': 'Температура выше допустимого значения. Понижение температуры.',
    'low_humidity': 'Влажность ниже допустимого значения. Повышение влажности.',
    'high_humidity': 'Влажность выше допустимого значения. Понижение влажности.',
    'low_luminosity': 'Освещенность ниже допустимого значения. Повышение освещенности.',
    'high_luminosity': 'Освещенность выше допустимого значения. Понижение освещенности.'
}


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


def get_temperature_unit_symbol():
    if UserSettings.temperature_unit == TemperatureUnit.CELSIUS:
        return '°C'
    elif UserSettings.temperature_unit == TemperatureUnit.FAHRENHEIT:
        return '°F'
    elif UserSettings.temperature_unit == TemperatureUnit.KELVIN:
        return 'K'
    return '°C'
