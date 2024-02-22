# importing required modules
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# ----------- Library Management System Models ------------

# Book model to store book details
class Book(models.Model):
    # Fields for Book model
    book_name = models.CharField(max_length=150)
    author_name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=30, unique=True, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=2000)
    book_add_time = models.TimeField(default=timezone.now())
    book_add_date = models.DateField(default=date.today())

    # Meta class to define unique constraints
    class Meta:
        unique_together = ('book_name', 'author_name')

    # String representation of Book instance
    def __str__(self):
        return self.book_name

# IssuedItem model to store issued book details
class IssuedItem(models.Model):
    # Foreign keys to Book and User models
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today(), blank=False)
    return_date = models.DateField(blank=True, null=True)

    # Property to get book name
    @property
    def book_name(self):
        return self.book_id.book_name

    # Property to get username
    @property
    def username(self):
        return self.user_id.username

    # Property to get ISBN
    @property
    def isbn(self):
        return self.book_id.isbn

    # String representation of IssuedItem instance
    def __str__(self):
        return (
            self.book_id.book_name
            + ' issued by '
            + self.user_id.first_name
            + ' on '
            + str(self.issue_date)
        )

    # Property to get status (In-stock or Out-of-stock)
    @property
    def status(self):
        if self.quantity > 0:
            return 'In-stock'
        else:
            return 'Out-of-stock'
