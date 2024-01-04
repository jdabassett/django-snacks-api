from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime, timezone, timedelta

from .models import Snack


class SnacksTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="username", email="email", password="password")
        self.snack = Snack.objects.create(owner=self.user, name="name", description="description")

    def test_snack_record(self):
        curr_time = datetime.now(timezone.utc)
        delta = timedelta(minutes=1)
        self.assertEqual(len(Snack.objects.all()),1)
        self.assertIsNotNone(self.snack.created_at)
        self.assertIsNotNone(self.snack.updated_at)
        self.assertEqual(self.snack.owner, self.user)
        self.assertEqual(self.snack.name, "name")
        self.assertEqual(self.snack.description, "description")
        self.assertGreaterEqual(self.snack.created_at, curr_time - delta)
        self.assertLessEqual(self.snack.created_at, curr_time)

    def test_user_record(self):
        self.assertEqual(self.user.username, "username")
        self.assertEqual(self.user.email, "email")

