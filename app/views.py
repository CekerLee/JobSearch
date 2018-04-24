from django.shortcuts import render

# Create your views here.
from elasticsearch import Elasticsearch

client = Elasticsearch(hosts=["127.0.0.1"])


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def result(request):
    key = request.GET.get('text')
    response = client.search(
        index="job_finder",
        doc_type="job51",
        body={
            "query": {
                "multi_match": {
                    "query": key,
                    "fields": ["title"]
                }
            },
        }
    )
    context = {"context": response}
    return render(request, 'app/result.html', context)
