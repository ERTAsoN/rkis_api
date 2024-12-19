from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    biography = models.TextField(blank=True, null=True, verbose_name='Биография')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    def __str__(self):
        return self.name

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', 'Худ. произведение'),
        ('textbook', 'Учебник'),
    ]

    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name='Автор')
    year = models.PositiveIntegerField(verbose_name='Год издания')
    genre = models.CharField(max_length=100, verbose_name='Жанр')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name='Категория')
    publisher = models.CharField(max_length=100, verbose_name='Издатель')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name='Обложка')
    book_file = models.FileField(upload_to='books/', blank=True, null=True, verbose_name='Файл книги')

    class Meta:
        unique_together = ('title', 'author', 'year', 'publisher')

    def __str__(self):
        return self.title
