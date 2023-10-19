from django.db import models


class AbstractCatalogModel(models.Model):
    name = models.CharField(
        "Название", help_text="Дайте товару имя", max_length=150
    )
    is_published = models.BooleanField(
        "Опубликовано", help_text="Статус публикации", default=True
    )

    class Meta:
        abstract = True
