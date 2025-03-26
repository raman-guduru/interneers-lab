from mongoengine import *


# Create your model here.
class Product(Document):
    name = StringField(max_length=255)
    description = StringField(null=True, blank=True)
    category = StringField(max_length=255)
    brand = StringField(max_length=255,default="Generic")
    price = DecimalField(min_value=0,max_digits=10, precision=2)
    quantity = IntField(min_value=0)

    def __str__(self):
        return self.name