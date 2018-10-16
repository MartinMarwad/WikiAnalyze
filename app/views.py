# from django.views.generic import TemplateView
from django.shortcuts import render
from core.wikipedia import Wikipedia


def index(request):

    return render(request, "index.html")

def search(request):
    query = request.GET.get('q', '')

    wikipedia = Wikipedia(query)
    results = wikipedia.search(query)

    return render(request, 'search_results.html', context={"search_results": results, 'query': query})

def wikipage(request, query):
    # Replace underscores (used in url) with spaces, and lowercase.
    query.replace('_', ' ').lower()

    # Get Wikipedia structured information
    wikipedia = Wikipedia(query)
    query_infobox = wikipedia.get_infobox()
    query_image = wikipedia.get_image()
    query_logo = wikipedia.get_logo()
    query_summary = wikipedia.get_summary_formated()

    context = {
        "query": query.capitalize(),
        "query_infobox": query_infobox,
        "query_summary": query_summary,
    }

    # Filter bad data
    if query_image:
        context['query_image'] = query_image

    if query_logo:
        context['query_logo'] = query_logo


    return render(request, 'wikipage.html', context=context)

def search_results(request):
    return render(request, "index.html")
