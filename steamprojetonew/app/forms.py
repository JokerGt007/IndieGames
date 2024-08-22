from django import forms
from .models import Game, Developer, Platform, Genre, Review, User, Screenshot, Achievement, Event, Discount

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'release_date', 'description', 'price', 'developer', 'platforms', 'genre', 'image', 'link']

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['name', 'country', 'founded_year', 'website']

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name', 'release_date', 'manufacturer']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'rating', 'review_text', 'review_date', 'reviewer_name']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'date_joined']

class ScreenshotForm(forms.ModelForm):
    class Meta:
        model = Screenshot
        fields = ['game', 'description', 'linkimage']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['game', 'title', 'description', 'points']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'description']

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['game', 'discount_percentage', 'start_date', 'end_date']