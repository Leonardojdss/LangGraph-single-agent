from src.tools.tools import Tools
from langchain_agentql.tools import ExtractWebDataTool
from dotenv import load_dotenv

load_dotenv()

class ToolsAgentQL(Tools):

    @staticmethod
    def tool():
        extract_web_data_tool = ExtractWebDataTool()
        return extract_web_data_tool
    
# test
# print(ToolsAgentQL.tools().invoke(
#         {
#             "url": "https://www.agentql.com/blog",
#             "query": "{ posts[] { title url date author } }",
#         },
#     )
# )
# Response
"""
{'data': {'posts': [{'title': 'AgentQL Integrations: The Agentic Web begins now that every page is an enpoint', 'url': 'https://www.agentql.com/blog/2025-recap-integrations', 'date': 'Mar 17, 2025', 'author': 'Rachel-Lee Nabors'}, {'title': 'Hacking with AgentQL at Multimodal AI Agents Hackathon in San Francisco', 'url': 'https://www.agentql.com/blog/2025-multimodal-agents-hackathon', 'date': 'Apr 3, 2025', 'author': 'Rachel-Lee Nabors'}, {'title': "Scrape raw HTML with AgentQL's REST API", 'url': 'https://www.agentql.com/blog/2025-scrape-html-api', 'date': 'Mar 29, 2025', 'author': 'Rachel-Lee Nabors'}, {'title': 'Langflow + AgentQL: drag, drop, and automate Web data in AI pipelines', 'url': 'https://www.agentql.com/blog/2025-langflow-integration', 'date': 'Mar 19, 2025', 'author': 'Rachel-Lee Nabors'}, {'title': 'AgentQL Enters the Agentic World with Langchain and LlamaIndex', 'url': 'https://www.agentql.com/blog/2025-llamaindex-langchain-integration', 'date': 'Mar 14, 2025', 'author': 'Rachel-Lee Nabors'}]}, 'metadata': {'request_id': '6ac24f4f-aceb-4feb-b654-43c100a0f0de', 'generated_query': None, 'screenshot': None}}
"""