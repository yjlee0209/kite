from django.db import models
from django.urls import reverse
import uuid
from datetime import date
from django.contrib.auth.models import User


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Language(models.Model):
    """Model representing a language."""
    name = models.CharField(max_length=200, help_text="Enter rhe book's natural language.")

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=12, help_text='13 Character <a href"https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language',on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def __str__(self):
        """String fot respresenting the Model object."""
        return self.title

    def get_absolute_url(self):
        """Return the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
    
class BookInstance(models.Model):
    """Model representing a specific copy of book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particulat book across whole library.')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability',
    )

    class Meta:
        ordering = ['due_back']
        permission = (("can_mark_returned", "Set bood as returned"))

    def __str__(self):
        """String for repersenting the Model object."""
        return '{0} ({1})'.format(self.id, self.book.title)

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    data_of_birth = models.DateField(null=True, blank=True)
    data_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Return the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'