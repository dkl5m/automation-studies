"""
Quero ver a possibilidade de criar um programa usando Python para automatizar enviando os dados da planilha para preencher os campos mutaveis no certificado padrao.

Tipo nome do curso, nome participante, tipo de participacao, data do inicio, data do final, carga horaria, data de emissao do certificado.

# pegar dados da planilha
# transferir dados da planilha para a imagem do certificado

"""

import openpyxl
from PIL import Image, ImageDraw, ImageFont

# Abrir planilha
workbook_students = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_students = workbook_students['Sheet1']

for indexi,row in enumerate(sheet_students.iter_rows(min_row=2,max_row=2)):
    # cada celula que contem info
    course_name = row[0].value
    student_name = row[1].value
    participant_type = row[2].value
    start_date = row[3].value
    end_date = row[4].value
    workloads = row[5].value
    certificate_date = row[6].value
    
