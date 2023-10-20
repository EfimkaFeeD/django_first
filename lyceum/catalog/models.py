import re

from core.models import AbstractCatalogModel

import django.core.exceptions
import django.core.validators
import django.db.models as models
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateMustContain:
    def __init__(self, *args):
        self.args = args

    def __call__(self, value):
        regex = re.findall(r"\w+[А-я]+\w+", value.lower())
        for i in self.args:
            if i in regex:
                return
        words = "или".join([f"`{i}`" for i in self.args])
        raise (
            django.core.exceptions.ValidationError(
                f"В тексте должны быть слова {words}"
            )
        )


class Tag(AbstractCatalogModel):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

    slug = models.CharField(
        "Слаг",
        help_text="Укажите слаг товара",
        unique=True,
        max_length=200,
        validators=[
            django.core.validators.RegexValidator("^[-_A-Za-z0-9\\s]+$")
        ],
    )


class Category(AbstractCatalogModel):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    slug = models.CharField(
        "Слаг",
        help_text="Укажите слаг товара",
        unique=True,
        max_length=200,
        validators=[
            django.core.validators.RegexValidator("^[-_A-Za-z0-9\\s]+$")
        ],
    )
    weight = models.IntegerField(
        "Вес",
        help_text="Укажите вес товара",
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(32767),
        ],
    )


class Item(AbstractCatalogModel):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    text = models.TextField(
        "Текст",
        help_text="Опишите товар",
        default="",
        validators=[ValidateMustContain("превосходно", "роскошно")],
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=""
    )
    tags = models.ManyToManyField(Tag, default="")
