from unittest import TestCase
from question2.storage import JsonData, LocalStorage, Type, Product


class ValidateJonStorage(TestCase):

    def test_insert_operation_json_format(self):
        storage = LocalStorage(Type.Text, "products.json")
        json_data = JsonData(storage)
        product = Product(title='laptop', category='electronics', price=5000,
                          description=" hp ZBOOK series is my favourite series")
        self.assertTrue(json_data.insert(product))

    def test_insert_batch_operation_json_format(self):
        storage = LocalStorage(Type.Text, "products_1.json")
        json_data = JsonData(storage)
        product = Product(title='laptop', category='electronics', price=5000,
                          description=" hp ZBOOK series is my favourite series")
        product1 = Product(title='mobile', category='electronics', price=5600,
                          description=" hp ZBOOK series is my favourite series")
        self.assertTrue(json_data.batch_insert([product, product1]))

    def test_filter_operations_json_format(self):
        storage = LocalStorage(Type.Text, "products_2.json")
        json_data = JsonData(storage)
        product = Product(title='laptop', category='electronics', price=5000,
                          description=" hp ZBOOK series is my favourite series")
        product1 = Product(title='mobile', category='electronics', price=5600,
                           description=" hp ZBOOK series is my favourite series")
        self.assertTrue(json_data.batch_insert([product, product1]))
        self.assertListEqual(json_data.filter(id=product.id), [product.to_dict()])

    def test_update_record_json_format(self):
        storage = LocalStorage(Type.Text, "products_3.json")
        json_data = JsonData(storage)
        product = Product(title='laptop', category='electronics', price=5000,
                          description=" hp ZBOOK series is my favourite series")
        product1 = Product(title='mobile', category='electronics', price=5600,
                           description=" hp ZBOOK series is my favourite series")
        self.assertTrue(json_data.batch_insert([product, product1]))
        product.title = "apple"
        json_data.update(product.id, product)
        self.assertListEqual(json_data.filter(id=product.id), [product.to_dict()])

    def test_delete_operation_json_format(self):
        storage = LocalStorage(Type.Text, "products_4.json")
        json_data = JsonData(storage)
        product = Product(title='laptop', category='electronics', price=5000,
                          description=" hp ZBOOK series is my favourite series")
        product1 = Product(title='mobile', category='electronics', price=5600,
                           description=" hp ZBOOK series is my favourite series")
        self.assertTrue(json_data.batch_insert([product, product1]))
        json_data.delete(product.id)
        self.assertListEqual(json_data.filter(id=product.id), [])


