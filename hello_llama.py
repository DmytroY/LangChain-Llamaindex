from llama_index.core import Document,  VectorStoreIndex

documents = [
    Document(text="Abraham Linkoln was the 16th president of USA."),
    Document(text="Abraham Shakespeare was a Florida lottery winner in 1899."),
    Document(text="William Shakespeare married Anna Hathaway.")
]

index = VectorStoreIndex(documents)
query_engine = index.as_query_engine()
responce1 = query_engine.query("Who was Sharespeare's wife?")
print(responce1)