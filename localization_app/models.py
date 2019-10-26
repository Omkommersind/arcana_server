from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=2)

    def __str__(self):
        return '%s' % self.code

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class DataString(models.Model):
    def __str__(self):
        from localization_app.repositories import LocalizedStringRepository
        return 'ID: %d, %s' % (self.id, LocalizedStringRepository.get_default_localization(self))

    class Meta:
        verbose_name = 'Строка данных'
        verbose_name_plural = 'Строки данных'


class LocalizedString(models.Model):
    data = models.TextField(default="")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    destination = models.ForeignKey(DataString, on_delete=models.CASCADE)

    def __str__(self):
        return 'ID: %d' % self.id

    class Meta:
        verbose_name = 'Локализованная строка'
        verbose_name_plural = 'Локализованные строки'

