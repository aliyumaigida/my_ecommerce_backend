from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.db.models import Avg
from . models import ProductRating, Review

@receiver(post_save, sender=Review)
def update_product_rating_on_save(sender, instance, **kwargs):
    product = instance.product
    reviews = product.review.all()
    total_review = reviews.count()

    
    review_average = reviews.aggregate(Avg("rating"))["rating__avg"] or 0.0

    product_rating, create = ProductRating.objects.get_or_create(product=product)
    product_rating.average_rating = review_average
    product_rating.total_review
    product_rating.save()

@receiver(post_delete, sender=Review)
def update_product_rating_on_delete(sender, instance, **kwargs):
    product = instance.product
    reviews = product.review.all()
    total_review = reviews.count()

    review_average = reviews.aggregate(Avg("rating"))["rating__avg"] or 0.0

    product_rating, create = ProductRating.objects.get_or_create(product=product)
    product_rating.average_rating = review_average
    product_rating.total_review
    product_rating.save()    

