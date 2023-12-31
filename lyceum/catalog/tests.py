__all__ = [
    "CatalogTests",
    "ItemModelsTests",
    "CategoryModelTests",
    "TagModelTests",
]

import django.core.exceptions as exceptions
from django.test import TestCase
from django.urls import reverse
import django.urls.exceptions as url_exceptions

from catalog.models import Category, Item, Tag


class CatalogTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = Category.objects.create(
            is_published=True,
            name="Категория для тестиков",
            slug="category-for-tests",
            weight=999,
        )

        cls.tag = Tag.objects.create(
            is_published=True,
            name="Тег для тестиков",
            slug="tag-for-tests",
        )

        cls.tag_repeat = Tag.objects.create(
            is_published=True,
            name="Тег для тестиков репит",
            slug="tag-for-tests-repeat",
        )

        cls.item = Item.objects.create(
            is_published=True,
            name="Товар для тестиков",
            category=cls.category,
            text="Превосодно тестируемый товар",
        )

    def test_catalog_page(self):
        response = self.client.get(reverse("catalog:item_list"))
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_page(self):
        response = self.client.get(reverse("catalog:item_detail", args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_page_wrong_data(self):
        with self.assertRaises(url_exceptions.NoReverseMatch):
            response = self.client.get(
                reverse("catalog:item_detail", args=["test"]),
            )
            self.assertEqual(response.status_code, 404)

    def test_catalog_re_item_page(self):
        response = self.client.get(reverse("catalog:re_item_detail", args=[2]))
        self.assertContains(response, status_code=200, text=2)

    def test_catalog_re_item_page_wrong_data(self):
        with self.assertRaises(url_exceptions.NoReverseMatch):
            response = self.client.get(
                reverse("catalog:re_item_detail", args=["test2"]),
            )
            self.assertEqual(response.status_code, 404)

    def test_catalog_conv_item_page(self):
        response = self.client.get(reverse("catalog:item_converter", args=[3]))
        self.assertContains(response, status_code=200, text=3)

    def test_catalog_conv_item_page_wrong_data(self):
        with self.assertRaises(url_exceptions.NoReverseMatch):
            response = self.client.get(
                reverse("catalog:item_converter", args=["test3"]),
            )
            self.assertEqual(response.status_code, 404)


class ItemModelsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = Category.objects.create(
            is_published=True,
            name="Категория для тестиков",
            slug="category-for-tests",
            weight=999,
        )

        cls.tag = Tag.objects.create(
            is_published=True,
            name="Тег для тестиков",
            slug="tag-for-tests",
        )

        cls.tag_repeat = Tag.objects.create(
            is_published=True,
            name="Тег для тестиков репит",
            slug="tag-for-tests-repeat",
        )

    def test_correct_item_creation(self):
        items_in_db = Item.objects.count()
        self.item = Item(
            name="Правильный тестовый товар",
            category=self.category,
            text="Превосходно тестируемый товар",
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag, self.tag_repeat)

        self.assertEqual(Item.objects.count(), items_in_db + 1)

    def test_unable_create_no_data(self):
        items_in_db = Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = Item()
            self.item.full_clean()
            self.item.save()

        self.assertEqual(Item.objects.count(), items_in_db)

    def test_unable_create_no_words_in_text(self):
        items_in_db = Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = Item(
                name="Кажется, где-то подвох",
                category=self.category,
                text="Слов не завезли, но вы держитесь",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), items_in_db)

    def test_unable_create_no_category(self):
        items_in_db = Item.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.item = Item(
                name="Категория это вроде нужно, (не уверен точно)",
                text="Превосходно проваливаю тесты с 2023 года :sunglasses:",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag_repeat)

        self.assertEqual(Item.objects.count(), items_in_db)

    def test_correct_creation_no_tags(self):
        items_in_db = Item.objects.count()
        self.item = Item(
            name="UPD: Категория нужна, не ведитесь на скам",
            category=self.category,
            text="Надо сюда ченить написать роскошно, я пока подумаю над этим",
        )
        self.item.full_clean()
        self.item.save()

        self.assertEqual(Item.objects.count(), items_in_db + 1)


class CategoryModelTests(TestCase):
    def test_correct_category_creation(self):
        categories_in_db = Category.objects.count()
        self.category = Category(
            name="Правильная тестовая категория",
            slug="correct-test-category",
            weight=300,
        )
        self.category.full_clean()
        self.category.save()

        self.assertEqual(Category.objects.count(), categories_in_db + 1)

    def test_unable_create_no_data(self):
        categories_in_db = Category.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.category = Category()
            self.category.full_clean()
            self.category.save()

            self.assertEqual(Category.objects.count(), categories_in_db)

    def test_unable_create_bad_slug(self):
        categories_in_db = Category.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.category = Category(
                name="Будем сейчас издеваться над слагом hehe",
                slug="Заходит, значится, в бар программист и фронтендер",
                weight=1500,
            )
            self.category.full_clean()
            self.category.save()

            self.assertEqual(Category.objects.count(), categories_in_db)

    def test_unable_create_bad_weight(self):
        categories_in_db = Category.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.category = Category(
                name="Будем взвешивать импакт жабаскрипта в программировании",
                slug="js-is-bad",
                weight=-1,
            )
            self.category.full_clean()
            self.category.save()

            self.assertEqual(Category.objects.count(), categories_in_db)


class TagModelTests(TestCase):
    def test_correct_tag_creation(self):
        tags_in_db = Tag.objects.count()
        self.tag = Tag(name="Правильный тестовый тег", slug="correct-test-tag")
        self.tag.full_clean()
        self.tag.save()

        self.assertEqual(Tag.objects.count(), tags_in_db + 1)

    def test_unable_create_no_data(self):
        tags_in_db = Tag.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.tag = Tag()
            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(Tag.objects.count(), tags_in_db)

    def test_unable_create_too_long_name(self):
        tags_in_db = Tag.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.tag = Tag(
                name="""Тест слишком длинного имени, заодно поможет проверить и
                     в других моделях, ибо валидатор один и тот же. Надо бы тут
                     что-нибудь написать чтобы получилось 150 символов
                     превысить. Чтобы такого можно было бы понаписать, чтобы
                     превысить ограничение в 150 символов на имя? Нужно
                     серьезно над этим порассуждать.""",
                slug="long-name-tag-like-really-long-name",
            )
            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(Tag.objects.count(), tags_in_db)

    def test_unable_create_is_published_not_boolean(self):
        tags_in_db = Tag.objects.count()
        with self.assertRaises(exceptions.ValidationError):
            self.tag = Tag(
                name="Переписывать всю 'Войну и мир' в имя было плохой идеей",
                slug="we-do-a-little-trolling-here",
                is_published=float("inf"),
            )
            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(Tag.objects.count(), tags_in_db)


class ContextTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category_published = Category.objects.create(
            is_published=True,
            name="Категория для тестиков рабочая",
            slug="category-for-tests-working",
            weight=999,
        )

        cls.category_unpublished = Category.objects.create(
            is_published=False,
            name="Категория для тестиков нерабочая",
            slug="category-for-tests-not-working",
            weight=999,
        )

        cls.tag_published = Tag.objects.create(
            is_published=True,
            name="Тег для тестиков рабочий",
            slug="tag-for-tests-working",
        )

        cls.tag_repeat_published = Tag.objects.create(
            is_published=True,
            name="Тег для тестиков репит рабочий",
            slug="tag-for-tests-repeat-working",
        )

        cls.tag_unpublished = Tag.objects.create(
            is_published=False,
            name="Тег для тестиков нерабочий",
            slug="tag-for-tests-not-working",
        )

        cls.tag_repeat_unpublished = Tag.objects.create(
            is_published=False,
            name="Тег для тестиков репит нерабочий",
            slug="tag-for-tests-repeat-not-working",
        )

        cls.item_published = Item.objects.create(
            is_published=True,
            is_on_main=True,
            name="Товар для тестиков рабочий",
            text="Превосходно рабочий товар",
            category=cls.category_published,
        )

        cls.item_unpublished = Item.objects.create(
            is_published=False,
            is_on_main=False,
            name="Товар для тестиков нерабочий",
            text="Превосходно нерабочий товар",
            category=cls.category_published,
        )

        cls.category_published.full_clean()
        cls.category_unpublished.full_clean()
        cls.category_published.save()
        cls.category_unpublished.save()

        cls.tag_published.full_clean()
        cls.tag_repeat_published.full_clean()
        cls.tag_unpublished.full_clean()
        cls.tag_repeat_unpublished.full_clean()
        cls.tag_published.save()
        cls.tag_repeat_published.save()
        cls.tag_unpublished.save()
        cls.tag_repeat_unpublished.save()

        cls.item_published.full_clean()
        cls.item_unpublished.full_clean()
        cls.item_published.save()
        cls.item_unpublished.save()

        cls.item_published.tags.add(
            cls.tag_published,
            cls.tag_repeat_unpublished,
        )
        cls.item_unpublished.tags.add(
            cls.tag_unpublished,
            cls.tag_repeat_published,
        )

    def test_homepage_correct_context(self):
        response = self.client.get(reverse("homepage:home"))
        self.assertIn("items", response.context)

    def test_homepage_context_item_count(self):
        response = self.client.get(reverse("homepage:home"))
        items = response.context["items"]
        self.assertEqual(len(items), 1)

    def test_homepage_context_item_name(self):
        response = self.client.get(reverse("homepage:home"))
        items = response.context["items"]
        self.assertEqual(items[0].name, "Товар для тестиков рабочий")

    def test_homepage_context_item_category_name(self):
        response = self.client.get(reverse("homepage:home"))
        items = response.context["items"]
        self.assertEqual(
            items[0].category.name,
            "Категория для тестиков рабочая",
        )

    def test_homepage_context_item_tags_name(self):
        response = self.client.get(reverse("homepage:home"))
        items = response.context["items"]
        self.assertEqual(
            items[0].tags.all()[0].name,
            "Тег для тестиков рабочий",
        )

    def test_homepage_context_item_type(self):
        response = self.client.get(reverse("homepage:home"))
        items = response.context["items"]
        self.assertIsInstance(items[0], Item)

    def test_catalog_context_item_type(self):
        response = self.client.get(reverse("catalog:item_list"))
        items = response.context["items"]
        self.assertIsInstance(items[0], Item)
