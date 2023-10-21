from django.db import models


class AbstractCatalogModel(models.Model):
    name = models.CharField(
        "название", help_text="Дайте товару имя", max_length=150, unique=True
    )
    is_published = models.BooleanField(
        "опубликовано", help_text="Статус публикации", default=True
    )

    class Meta:
        abstract = True
