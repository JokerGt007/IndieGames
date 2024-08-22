from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField(default=2000)  # Campo para armazenar apenas o ano
    website = models.URLField()
    
    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    platforms = models.ManyToManyField(Platform)
    genre = models.ManyToManyField(Genre)
    image = models.CharField(max_length=200, default='https://i.ytimg.com/vi/Cr5rQ1NZ0Tw/maxresdefault.jpg')
    link = models.CharField(max_length=100, default='https://store.steampowered.com/')

    def __str__(self):
        return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()
    review_date = models.DateField()
    reviewer_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.game.title} - {self.rating}'

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_joined = models.DateField()

    def __str__(self):
        return self.username

class Screenshot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.TextField()
    linkimage = models.CharField(max_length=100, default='https://store.steampowered.com/')

    def __str__(self):
        return self.description[:50]

class Achievement(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Discount(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    discount_percentage = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.discount_percentage}% off on {self.game.title}'
