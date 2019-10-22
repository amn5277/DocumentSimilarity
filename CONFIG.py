INDEX_NAME = 'posts'
INDEX_FILE = os.path.join(os.getcwd(), "data\index.json")
DATA_FILE = os.path.join(os.getcwd(), "data\posts.json")
BATCH_SIZE = 1000
SEARCH_SIZE = 5
IP = '137.117.84.80'

#Client Object for Elastic Search
client = Elasticsearch(timeout=100)
bc = BertClient(ip=IP)