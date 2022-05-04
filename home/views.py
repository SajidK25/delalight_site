from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from home.models import (AboutHome, AboutUs, Blog, Expertise, Team, Testimonial)

# Create your views here.

def index(request):
    abouthome = AboutHome.objects.last()
    team = Team.objects.order_by('-create_date')[:3]
    testimonial = Testimonial.objects.order_by('-create_date')[:3]
    expertises = Expertise.objects.all()
    context = {
        'abouthome': abouthome,
        'team': team,
        'testimonial': testimonial,
        'expertises': expertises,
    }
    return render(request, 'home/index.html', context)

def about(request):
    aboutus = AboutUs.objects.last()
    context = {
        'aboutus': aboutus
    }
    return render(request, 'home/about-us.html', context)

def expertise(request):
    expertise = Expertise.objects.all()
    context = {
        'expertise': expertise
    }
    return render(request, 'home/expertise.html', context)


def expertisedetail(request, pk):
    expertise = Expertise.objects.get(id=pk)
    context = {
        'expertise': expertise
    }
    return render(request, 'home/expertise-detail.html', context)


def cases(request):
    return render(request, 'home/cases.html', context=None)

def testimonials(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial
    }
    return render(request, 'home/testimonials.html', context)

def team(request):
    return render(request, 'home/team.html', context=None)

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'home/blog.html', context)

def blogdetail(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {
        'blog': blog
    }
    return render(request, 'home/blog-detail.html', context)

def contactus(request):
    return render(request, 'home/contact-us.html', context=None)

def teamdetail(request, pk):
    team = Team.objects.get(id=pk)
    context = {
        'team': team
    }
    return render(request, 'home/team-detail.html', context)

