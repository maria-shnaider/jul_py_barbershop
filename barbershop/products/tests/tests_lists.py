from datetime import datetime
import json
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.test import APIClient
from apps_generic.whodidit.models import WhoDidIt
from products.models import Catalog, Product
from uuid import uuid4



def _dict_key_quotes(text):
    """ Replaces first two occurrences of double quotes " to single quotes ' in every line
        Is used to print dictionaries formatted according to the project guidelines
        (dict key are in single quotes, texts are in double quotes)
    """
    return '\n'.join([l.replace('"', "'", 2) for l in text.split('\n')])


def dump(response):
    """ Print DRF response data
        Useful for debugging tests. Prints response code and indented JSON data
    :param response: server response provided by DRF testing client (APIClient)
    """

    print("\nURL:", response.request['PATH_INFO'])
    print("Method:", response.request['REQUEST_METHOD'])
    if response.request['QUERY_STRING']:
        print("Query:", response.request['QUERY_STRING'])
    print("\n")
    print("Status code:\n{}\n\nData:\n{}\n".format(
        response.status_code,
        _dict_key_quotes(json.dumps(response.data, indent=4, ensure_ascii=False))
        if hasattr(response, 'data') else None
    ))


class ProductsListTest(TestCase):

    def setUp(self):
        self.c = APIClient()

        user_kw = dict(
            username='tt',
            password='111',
            email='tt' + '.com'
        )

        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.catalog = Catalog.objects.create(slug=str(uuid4()))
        self.product = Product.objects.create(price=20.00, stock=10, catalog_id=self.catalog.id)

        # self.created_on = \
        #     WhoDidIt.updated_on(datetime.datetime.utcnow().
        #                         replace(tzinfo=datetime.timezone(datetime.timedelta(seconds=10800))).isoformat())
        # self.updated_on = \
        #     datetime.datetime.utcnow().replace(tzinfo=datetime.timezone(datetime.timedelta(seconds=10800))).isoformat()

    def test_products_list(self):

        self.c.login(username='tt', password='111')
        response = self.c.get(
            '/products/catalog/products/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)
        print(dir(status))

        self.assertEqual(response.data, {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.product.id,
                        "type": "product",
                        "catalog": self.catalog.id,
                        "name": '',
                        "slug": '',
                        "price": '20.00',
                        "stock": self.product.stock,
                        "available": True,
                        # "created_on": self.product.created,
                        # "updated_on": self.product.updated,
                        "created_by": None,
                        "updated_by": None
                    }
                ]
            }
        )
        print(response.data)

    def test_products_create(self):
        self.assertEqual(True, True)

