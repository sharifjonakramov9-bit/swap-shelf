from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book, BookCondition, BookStatus, BookType, Genre


class BookAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            telegram_id=123456789,
            password="testpass123",
            name="Ali",
            phone="+998901234567",
        )
        self.other_user = get_user_model().objects.create_user(
            telegram_id=987654321,
            password="testpass123",
            name="Vali",
            phone="+998901234568",
        )
        self.genre = Genre.objects.create(name="Fantasy")
        self.book = Book.objects.create(
            owner=self.user,
            title="Sariq devni minib",
            author="Xudoyberdi To'xtaboyev",
            genre=self.genre,
            condition=BookCondition.GOOD,
            type=BookType.BORROW,
            description="Bolalar uchun qiziqarli asar",
            image="https://example.com/book.jpg",
            status=BookStatus.AVAILABLE,
            share=True,
        )

    def test_anyone_can_list_books(self):
        response = self.client.get(reverse("book-list-create"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], self.book.title)

    def test_authenticated_user_can_create_book(self):
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse("book-list-create"),
            {
                "title": "Ikki eshik orasi",
                "author": "O'tkir Hoshimov",
                "genre": self.genre.id,
                "condition": BookCondition.NEW,
                "type": BookType.BOTH,
                "description": "Mashhur roman",
                "image": "https://example.com/other-book.jpg",
                "status": BookStatus.AVAILABLE,
                "share": False,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest("id").owner, self.user)

    def test_non_owner_cannot_update_book(self):
        self.client.force_authenticate(self.other_user)

        response = self.client.patch(
            reverse("book-detail", kwargs={"pk": self.book.pk}),
            {"title": "Yangi nom"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Sariq devni minib")
