import os
import sys
import shutil
import requests
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook

sys.path.append(r"C:\rpa\Python")

from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


class GeraPrecoNestle:
    def __init__(self):
        pass # Logica de negocio removida por seguranca corporativa



    def movimenta_arquivo(self, caminho_arquivo_origem, caminho_arquivo_destino):
        pass # Logica de negocio removida por seguranca corporativa


    
    def obtem_tabela_clientes(self):
        pass # Logica de negocio removida por seguranca corporativa

    

    def gera_preco_tabela_pg(self, codigo_cliente, ean_produto):
        pass # Logica de negocio removida por seguranca corporativa

    

    def ler_guia_eans(self, caminho_arquivo):
        pass # Logica de negocio removida por seguranca corporativa

        

    def carregar_estoque_por_uf(self):
        pass # Logica de negocio removida por seguranca corporativa

        
    
    def obter_estoque(self, ean, uf, estoque_por_uf):
        pass # Logica de negocio removida por seguranca corporativa



    def preencher_precos_final_distri(self, caminho_arquivo, dados_para_preencher):
        pass # Logica de negocio removida por seguranca corporativa

        

    def envia_email(self, destinatarios, assunto, mensagem, anexo):
        pass # Logica de negocio removida por seguranca corporativa
