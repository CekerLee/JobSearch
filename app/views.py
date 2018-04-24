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
    hit_list=[]
    for hit in response["hits"]['hits']:
        hit_dict={}
        hit_dict['title'] = hit["_source"]['title']
        hit_dict['job_url'] = hit["_source"]['job_url']
        hit_dict['job_desc'] = hit["_source"]['job_desc'][:200]
        hit_list.append(hit_dict)
    context = {"context": hit_list}
    return render(request, 'app/result.html', context)
