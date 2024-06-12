# passo-a-passo
# -passar info da planilha para .word
# -salvar .word em uma pasta especifica (contratos)
# -repetir para o resto da planilha

from openpyxl import load_workbook
from docx import Document
from datetime import datetime

#entrar na planilha
workbook = load_workbook('fornecedores.xlsx')
sheet_products = workbook['Produtos']

