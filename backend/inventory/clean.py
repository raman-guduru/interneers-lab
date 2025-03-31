from . import models
from . import repository
import mongoengine
mongoengine.connect("mongodb_data")

def clean_product():
    print("cleaning...")
    qs = models.Product.objects.all()
    rep = repository.ProductRepository()
    for doc in qs:
        try:
            repository.ProductRepository.save(rep,doc)
        except Exception as e:
            print(f'{doc.pk} is invalid ,')
            print(e)
            print(' deleting..')
            repository.ProductRepository.delete(rep,doc)
            
clean_product()