from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    true_name = models.CharField(max_length=30)
    birth_year = models.CharField(max_length=20)

    class Meta:
        db_table = 'tb_authors'

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=30, null=False, unique=True)
    publish_day = models.DateField()
    publisher = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_books'

    def __str__(self):
        return self.title
