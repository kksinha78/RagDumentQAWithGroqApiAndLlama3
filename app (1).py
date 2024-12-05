import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchan.text_splitter import RescursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain  # used for RAG Q&A application
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain # used for RAG Q&A application
from langchain_community.vectorstores import FAISS
from langchain_community.documents_loaders import PyPDFDirectoryLoader

#lets load all environment variables
from dotenv import load_dotenv
load_dotenv()

#Load the GROQ api key
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')


