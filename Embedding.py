
#getting vector representation of our document
def embed_text(text):
    vectors = bc.encode(text)
    return [vector.tolist() for vector in vectors]       