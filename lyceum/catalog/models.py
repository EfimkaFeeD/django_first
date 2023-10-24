__all__ = ["Tag", "Category", "Item", "Images"]

import os

import django.core.exceptions
import django.core.validators
import django.db.models as models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from catalog.validators import ValidateMustContain
from core.models import AbstractCatalogModel


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
            django.core.validators.RegexValidator("^[-_A-Za-z0-9\\s]+$"),
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
            django.core.validators.RegexValidator("^[-_A-Za-z0-9\\s]+$"),
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
        Category,
        on_delete=models.CASCADE,
        default="",
        verbose_name="категория",
        help_text="Выберите категорию",
        related_name="category",
    )
    tags = models.ManyToManyField(
        Tag,
        default="",
        verbose_name="теги",
        help_text="Добавьте теги. P.S.:",
        related_name="tags",
    )

    main_image = models.ImageField(
        "картинка для товара",
        help_text="Добавьте картинку для товара (она переделается в 300x300)",
        upload_to="catalog/images/main_images/",
        default=None,
        blank=True,
    )

    def main_image_to_300x300(self):
        return get_thumbnail(
            self.main_image,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.main_image:
            return mark_safe(f"<img src='{self.main_image.url}' width='50'")

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True


class Images(models.Model):
    class Meta:
        verbose_name = "картинка"
        verbose_name_plural = "картинки"

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name="товар",
        help_text="Товар к которому добавить картинку",
        related_name="item",
    )

    image = models.ImageField(
        upload_to="catalog/images/item_images/",
        default=None,
        verbose_name="картинка",
        help_text="Картинка для товара (переделается в 300x300)",
    )

    def __str__(self):
        return os.path.split(self.image.name)[1][:250]

    def image_to_300x300(self):
        return get_thumbnail(self.image, "300x300", crop="center", quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(f"<img src='{self.image.url}' width='50'")

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True
