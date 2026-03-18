from django.db import models

class Property(models.Model):
    PROPERTY_TYPE = [
        ('Office', 'Office'),
        ('Shop', 'Shop'),
        ('Warehouse', 'Warehouse'),
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE)
    area_sqft = models.PositiveIntegerField()

    furnishing = models.CharField(max_length=50, blank=True)
    parking = models.CharField(max_length=50, blank=True)
    washrooms = models.PositiveIntegerField(default=1)
    floor = models.CharField(max_length=20, blank=True)
    total_floors = models.CharField(max_length=20, blank=True)

    suitable_for = models.CharField(max_length=200, blank=True)
    maintenance = models.CharField(max_length=100, blank=True)
    possession = models.CharField(max_length=100, blank=True)
    property_age = models.CharField(max_length=50, blank=True)

    image = models.ImageField(upload_to='properties/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Enquiry(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('closed', 'Closed'),
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    requirement = models.TextField()
    property = models.ForeignKey(
        Property,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
