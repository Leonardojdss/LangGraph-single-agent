from src.tools.tools import Tools
from langchain_core.tools import tool
import requests

class ToolViaCep(Tools):
    
    @staticmethod
    @tool
    def tool(cep: str) -> dict:
        """
        Search for an address by CEP (Postal Code) using the ViaCEP API.
        """
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        return response.json()
    
# test
# print(ToolViaCep.via_cep_api.invoke(
#     {"cep": "01001-000"}
#     )
# ) 
# Response 
"""
{
    "cep": "01001-000",
    "logradouro": "Praça da Sé",
    "complemento": "lado ímpar",
    "bairro": "Sé",
    "localidade": "São Paulo",
    "uf": "SP",
    "ibge": "3550308",
    "gia": "1004",
    "ddd": "11",
    "siafi": "7087"
}
"""
