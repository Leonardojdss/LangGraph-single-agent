"""
LangGraph Single Agent - Ponto de Entrada Principal

Este módulo serve como ponto de entrada para a aplicação do agente de IA.
O agente utiliza LangGraph para orquestrar ferramentas de consulta CEP e 
extração de dados web, mantendo memória de conversação.

Autor: Leonardo José da Silva
GitHub: https://github.com/Leonardojdss
"""

from src.utils.chat import chat

if __name__ == "__main__":
    chat()