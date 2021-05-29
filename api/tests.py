from django.test import TestCase
from django.db.models import F

from api.models import Foo
from decimal import Decimal

class TestSimple(TestCase):
    def test_simple(self):
        f = Foo.objects.create(amount=Decimal('0.5'))

        f.amount = F('amount') - Decimal('0.4')

        f.save(update_fields=['amount', ])

        f.refresh_from_db()

        self.assertEqual(
            f.amount,
            Decimal('0.1')
        )
