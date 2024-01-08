<<<<<<< HEAD
from haystack.document_stores import InMemoryDocumentStore
#new_branch
document_store = InMemoryDocumentStore(use_bm25=True) #to fill this in with documents

from haystack.utils import fetch_archive_from_http

doc_dir = "data/build_your_first_question_answering_system"

fetch_archive_from_http(
    url="https://s3.eu-central-1.amazonaws.com/deepset.ai-farm-qa/datasets/documents/wiki_gameofthrones_txt1.zip",
    output_dir=doc_dir,
)

import os
from haystack.pipelines.standard_pipelines import TextIndexingPipeline

files_to_index = [doc_dir + "/" + f for f in os.listdir(doc_dir)] 
indexing_pipeline = TextIndexingPipeline(document_store)  #converting downloaded articles into document objects and storing in pipeline
indexing_pipeline.run_batch(file_paths=files_to_index)

from haystack.nodes import BM25Retriever

retriever = BM25Retriever(document_store=document_store) #best match 25

from haystack.nodes import FARMReader

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)
#readers based on DL models, slower than retriever. They figure out best reply amongst all replies given by retriever

from haystack.pipelines import ExtractiveQAPipeline

pipe = ExtractiveQAPipeline(reader, retriever) #this pipeline connects the reader to the retriever

prediction = pipe.run(
    query="what is Jon Snow's real identity", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
)

from haystack.utils import print_answers

print_answers(prediction, details="minimum")  ## Choose from `minimum`, `medium`, and `all`

#edited in new_branch



=======
#post first commit
from haystack.document_stores import InMemoryDocumentStore

document_store = InMemoryDocumentStore(use_bm25=True) #to fill this in with documents

from haystack.utils import fetch_archive_from_http

doc_dir = "data/build_your_first_question_answering_system"

fetch_archive_from_http(
    url="https://s3.eu-central-1.amazonaws.com/deepset.ai-farm-qa/datasets/documents/wiki_gameofthrones_txt1.zip",
    output_dir=doc_dir,
)

import os
from haystack.pipelines.standard_pipelines import TextIndexingPipeline

files_to_index = [doc_dir + "/" + f for f in os.listdir(doc_dir)] 
indexing_pipeline = TextIndexingPipeline(document_store)  #converting downloaded articles into document objects and storing in pipeline
indexing_pipeline.run_batch(file_paths=files_to_index)

from haystack.nodes import BM25Retriever

retriever = BM25Retriever(document_store=document_store) #best match 25

from haystack.nodes import FARMReader

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)
#readers based on DL models, slower than retriever. They figure out best reply amongst all replies given by retriever

from haystack.pipelines import ExtractiveQAPipeline

pipe = ExtractiveQAPipeline(reader, retriever) #this pipeline connects the reader to the retriever

prediction = pipe.run(
    query="what is Jon Snow's real identity", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
)

from haystack.utils import print_answers

print_answers(prediction, details="minimum")  ## Choose from `minimum`, `medium`, and `all`

#now this us in the first branch, pre commit yet



>>>>>>> first_branch_ever
