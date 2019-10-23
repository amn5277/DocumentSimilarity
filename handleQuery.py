from elasticsearch import Elasticsearch
from Embedding import embed_text

def handle_query(query):
    
    query_vector = embed_text([query])[0]
  
    script_query = {
        "script_score":{
            "query":{"match_all":{}},
            "script": {
                "source":"cosineSimilarity(params.query_vector, doc['title_vector']) + 1.0",
                "params": {"query_vector": query_vector}
            }
        }
    }
    
    
    response = client.search(index=INDEX_NAME,body={
            "size": SEARCH_SIZE,
            "query": script_query,
            "_source": {"includes": ["title", "body"]}
        }
    )
    

    for hit in response["hits"]["hits"]:
        hits = hit["_id"], hit["_score"],hit["_source"]
    
    return hits



