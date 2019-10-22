def handle_query():
    query = input("Enter Query - ")
    query_vector = embed_text([query])[0]
    
    #Query for Cosin Similarity
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
    
    
    #returning results
    print("{} total hits.".format(response["hits"]["total"]["value"]))
    for hit in response["hits"]["hits"]:
        print("id: {}, score: {}".format(hit["_id"], hit["_score"]))
        print(hit["_source"])
        print()