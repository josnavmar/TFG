from django.shortcuts import render


def index(request):
    return render(request, "text_analysis_sentiment/index.html", {})

