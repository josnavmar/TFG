from django.conf.urls import url
from apps.text_analysis_sentiment.views import index

urlpatterns = [
    url(r'^$', index),
 
]