# Generated by Django 5.1.4 on 2024-12-18 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, null=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(blank=True, null=True, upload_to='books/', verbose_name='Файл книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('fiction', 'Худ. произведение'), ('textbook', 'Учебник')], max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=100, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=100, verbose_name='Издатель'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveIntegerField(verbose_name='Год издания'),
        ),
    ]
