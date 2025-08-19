import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

class ConnectionAzureOpenai():
    
    @staticmethod
    def llm_azure_openai():
        llm = init_chat_model(
            "azure_openai:gpt-4.1",
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        )
        return llm