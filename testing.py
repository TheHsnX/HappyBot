#####################load a web page##################################

# from langchain_community.document_loaders import WebBaseLoader

# loader = WebBaseLoader("https://techcrunch.com/")

# docs=loader.load()
# print(len(docs))
# print(docs[0].page_content)



#####################load a pdf##################################

# from langchain_community.document_loaders.parsers import RapidOCRBlobParser
# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader(
#     r"C:\Users\hassan\Desktop\langchain\report (1).pdf",
#     mode="page",
#     images_inner_format="markdown-img",
#     images_parser=RapidOCRBlobParser(),
# )
# docs = loader.load()

# print(docs[1])



#####################EMBEDDINGS##################################

# from langchain_ollama import OllamaEmbeddings

# embeddings = OllamaEmbeddings(
#     model="deepseek-r1:1.5b",
# )


# print(len(embeddings.embed_query("Hello, world!")))


#####################TEXT SPLIT##################################

# document='Life is a journey filled with ups and downs, challenges and victories. Every day presents a new opportunity to learn, grow, and become a better version of ourselves. No matter how difficult things may seem, there is always a way forward. With patience, perseverance, and a positive mindset, we can overcome obstacles and achieve our dreams. Keep pushing forward, and success will follow.'

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=10)
# texts = text_splitter.split_text(document)
# print(texts)

#####################vector store##################################

from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="deepseek-r1:1.5b",
)

import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS


vector_store = FAISS(
    embedding_function=embeddings,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)




