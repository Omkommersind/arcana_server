from .models import DataString, LocalizedString
from arcana_server.settings import DEFAULT_LANGUAGE_CODE


class LanguageRepository:
    @classmethod
    def try_get_language_by_code(cls, language_code):
        from localization_app.models import Language

        query = Language.objects.filter(code=language_code)
        if query.exists():
            return query.first()
        return None

    @classmethod
    def get_default_language(cls):
        return LanguageRepository.try_get_language_by_code(DEFAULT_LANGUAGE_CODE)


class LocalizedStringRepository:

    @classmethod
    def try_get_localized_string(cls, data_string: DataString, language_code: str):
        language = LanguageRepository.try_get_language_by_code(language_code)
        if language is not None:
            query = LocalizedString.objects.filter(destination=data_string, language=language)
            if query.exists():
                return query.first().data

        query = LocalizedString.objects.filter(destination=data_string, language=LanguageRepository.get_default_language())
        if query.exists():
            return query.first().data

        return ''

    @classmethod
    def get_default_localization(cls, data_string: DataString):
        return cls.try_get_localized_string(data_string, DEFAULT_LANGUAGE_CODE)
