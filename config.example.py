from metadata.cuckoo_analysis import CuckooAnalysisMetadata

BACKEND = 'tcp://127.0.0.1:9281'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
SECRET_KEY = 'secret-key'
INDEXABLE_PATHS = ['/mnt/samples']
INDEX_TYPE = ['gram3', 'hash4', 'text4', 'wide8']
METADATA_EXTRACTORS = [
    CuckooAnalysisMetadata("/opt/mw/samples/analyses/")
]
