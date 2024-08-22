from django.contrib import admin
from app.models import *
from .forms import *


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'price', 'developer', 'image', 'link')
    search_fields = ('title',)

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year')
    search_fields = ('name',)

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date')
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'rating', 'review_date', 'reviewer_name')
    search_fields = ('reviewer_name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    search_fields = ('username',)

@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('game', 'description', 'linkimage')
    search_fields = ('game__title',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('game', 'title', 'points')
    search_fields = ('game__title', 'title')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location')
    search_fields = ('name',)

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('game', 'discount_percentage', 'start_date', 'end_date')
    search_fields = ('game__title',)
