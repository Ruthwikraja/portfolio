from django.contrib import admin
from django.forms import ImageField

# Register your models here.
from .models import Contact, Education, Experience, Home, About, ImageFile, Profile, Category, Skills, Portfolio, Interests, Summary


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(ImageFile)

class ImageFileInline(admin.TabularInline):  # or admin.StackedInline
    model = ImageFile

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [ImageFileInline]

#Interests
admin.site.register(Interests)

#Resume
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Summary)

#Contact
admin.site.register(Contact)