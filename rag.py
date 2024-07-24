from langchain_community.vectorstores.chroma import Chroma
from langchain_community.chat_models.ollama import ChatOllama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.vectorstores.utils import filter_complex_metadata

from langchain.prompts import ChatPromptTemplate

from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import JSONLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.document_loaders import WebBaseLoader

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_openai import ChatOpenAI, OpenAIEmbeddings



from dotenv import load_dotenv
import os

class KeplerChat:
    vector_store = None
    retriever = None
    chain = None 

    def __init__(self):
        load_dotenv(dotenv_path='api_keys.env')  # This loads environment variables from the .env file
        openai_api_key = os.getenv('OPENAI_API_KEY')

        self.model = ChatOpenAI(openai_api_key=openai_api_key)
        self.prompt = PromptTemplate.from_template(
            """
            You are an AI assistant on a homeschooling platform. Answer the question based on the provided context. 
            If no suitable courses are found, inform the user and recommend one similar course, explaining its relevance briefly. 
            {context}

            Question: {question}
            """
        )
    
    def ingest(self):
        load_dotenv(dotenv_path='api_keys.env')  # This loads environment variables from the .env file
        openai_api_key = os.getenv('OPENAI_API_KEY')
        
        embedder = OpenAIEmbeddings(openai_api_key=openai_api_key)

        loader = JSONLoader(file_path="kepler_teacher_course_data.json", jq_schema=".teachers[]", text_content=False)
        documents = loader.load()

        vector_store = Chroma.from_documents(documents, embedding=embedder)
        self.retriever = vector_store.as_retriever(
            search_kwargs={
                'k': 2
            },
        )

        self.chain = ({
            "context" : self.retriever,
            "question" : RunnablePassthrough()
                       }
                        | self.prompt
                        | self.model
                        | StrOutputParser()
                       )
        
    def ask(self, query: str):
        # Debug statement to check if chain is not None
        if self.chain is None:
            print("Chain is not initialized.")
        else:
            print("Chain is initialized and ready to invoke.")
        return self.chain.invoke(query)
    
    def clear(self):
        self.vector_store = None
        self.retriever = None
        self.chain = None