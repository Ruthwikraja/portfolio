from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio, Interests, Education, Experience, Summary, ImageFile, Contact

# Create your views here.

def index(request):
     # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    profile = Profile.objects.all()

    # Skills
    categories = Category.objects.all()
    skills = Skills.objects.all()
    s1 = skills[:len(skills)//2]
    s2 = skills[len(skills)//2:]

    # Portfolio
    portfolios = Portfolio.objects.all()
    pc = Portfolio.objects.count()
    image = ImageFile.objects.all() # Access related ImageFile objects
    img = ImageFile.objects.get(is_primary=True)


    #Interests
    technical_interests = Interests.objects.filter(category='technical')
    general_interests = Interests.objects.filter(category='general')
    
    # Resume
    summaries = Summary.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    
    #Contact
    contact = Contact.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'pc':pc,
        'skills': skills,
        's1':s1,
        's2':s2,
        'technical_interests': technical_interests,
        'general_interests': general_interests,
        'education': education,
        'experience': experience,
        'summaries': summaries,
        'image': image,
        'img':img,
        'contact':contact,
        'profile': profile
    }
    return render(request, 'index.html', context)