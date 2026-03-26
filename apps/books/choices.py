from django.db import models

class BookCondition(models.TextChoices):
    NEW = "new", "New"
    GOOD = "good", "Good"
    FAIR = "fair", "Fair"
    WORN = "worn", "Worn"

class BookType(models.TextChoices):
    BORROW = "borrow", "Borrow"
    PERMANENT = "permanent", "Permanent"
    BOTH = "both", "Both"

class BookStatus(models.TextChoices):
    AVAILABLE = "available", "Available"
    UNAVAILABLE = "unavailable", "Unavailable"