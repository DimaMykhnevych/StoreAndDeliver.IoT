from dataclasses import dataclass
from core.constants.language import Language


@dataclass
class UserSettings:
    language: Language = Language.ua
