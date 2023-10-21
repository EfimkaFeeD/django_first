import re

import django.core.exceptions
import django.core.validators
import django.db.models as models
from django.utils.deconstruct import deconstructible

from core.models import AbstractCatalogModel


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
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name

    slug = models.CharField(
        "слаг",
        help_text="Укажите слаг товара",
        unique=True,
        max_length=200,
        validators=[
            django.core.validators.RegexValidator("^[-_A-Za-z0-9\\s]+$")
        ],
    )


class Category(AbstractCatalogModel):
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name

    slug = models.CharField(
        "слаг",
        help_text="Укажите слаг товара",
        unique=True,
        max_length=200,
        validators=[
            django.core.validators.RegexValidator("^[-_A-Za-z0-9\\s]+$")
        ],
    )
    weight = models.IntegerField(
        "вес",
        help_text="Укажите вес товара",
        default=100,
        validators=[
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(32767),
        ],
    )


class Item(AbstractCatalogModel):
    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name

    text = models.TextField(
        "текст",
        help_text="Опишите товар",
        default="",
        validators=[ValidateMustContain("превосходно", "роскошно")],
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=""
    )
    tags = models.ManyToManyField(Tag, default="")
