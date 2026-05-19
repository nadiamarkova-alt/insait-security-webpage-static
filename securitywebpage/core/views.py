from django.shortcuts import render
from django.core.paginator import Paginator
from .models import ResearchTopic, Member, Publication


def home(request):
    topics = ResearchTopic.objects.all()[:3]
    members_count = Member.objects.count()
    publications_count = Publication.objects.count()
    return render(request, 'core/home.html', {
        'topics': topics,
        'members_count': members_count,
        'publications_count': publications_count,
    })


def research(request):
    topics = ResearchTopic.objects.all()
    return render(request, 'core/research.html', {'topics': topics})


def members(request):
    faculty = Member.objects.filter(category=Member.Category.FACULTY)
    phd = Member.objects.filter(category=Member.Category.PHD)
    visitors = Member.objects.filter(category=Member.Category.VISITORS)
    return render(request, 'core/members.html', {
        'faculty': faculty,
        'phd': phd,
        'visitors': visitors,
    })


def publications(request):
    year_filter = request.GET.get('year')
    queryset = Publication.objects.all().order_by('-year')
    if year_filter:
        queryset = queryset.filter(year=year_filter)
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    available_years = Publication.objects.values_list('year', flat=True).distinct().order_by('-year')
    return render(request, 'core/publications.html', {
        'page_obj': page_obj,
        'publications': page_obj,
        'available_years': available_years,
        'selected_year': year_filter,
    })


def contact(request):
    return render(request, 'core/contact.html')
