from django.db import models


class HeaderNavigation(models.Model):
    title = models.CharField("Название", max_length=32)
    link = models.URLField("Ссылка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Навигационный элемент"
        verbose_name_plural = "Навигационные элементы"


class Adventage(models.Model):
    adventage_row_1 = models.CharField("Строка 1", max_length=32)
    adventage_row_2 = models.CharField("Строка 2", max_length=32, help_text="ТЕКСТ &lt;span&gt;текст&lt;/span&gt;")
    adventage_row_3 = models.CharField("Строка 3", max_length=32)

    def __str__(self):
        return f"{self.adventage_row_1} {self.adventage_row_2} {self.adventage_row_3}"

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
