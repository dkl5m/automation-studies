"""
I want to see the possibility of creating a program using Python to automate sending the spreadsheet data to fill in the changeable fields in the standard certificate.

Type course name, participant name, type of participation, start date, end date, workload, certificate issuance date.

# get data from spreadsheet
# transfer data from spreadsheet to certificate image

"""

import openpyxl
from PIL import Image, ImageDraw, ImageFont

# Abrir planilha
workbook_students = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_students = workbook_students['Sheet1']

for indexi,row in enumerate(sheet_students.iter_rows(min_row=2,max_row=2)):
    # each cell that contains information
    course_name = row[0].value
    student_name = row[1].value
    participant_type = row[2].value
    start_date = row[3].value
    end_date = row[4].value
    workloads = row[5].value
    certificate_date = row[6].value
    
    # transfer data from spreadsheet to certificate image
    # define font to be used
    name_font = ImageFont.truetype('./tahomabd.ttf',90)
    general_font = ImageFont.truetype('./tahoma.ttf',80)
    date_font = ImageFont.truetype('./tahoma.ttf',55)
    
    image = Image.open('./certificado_padrao.jpg')
    draw = ImageDraw.Draw(image)
    
    # draw data into certificate
    draw.text((1060,955), course_name,fill='black',font=general_font)
    draw.text((1010,825), student_name,fill='black',font=name_font)
    draw.text((1435,1070), participant_type,fill='black',font=general_font)
    draw.text((745,1770), start_date,fill='black',font=date_font)
    draw.text((745,1925), end_date,fill='black',font=date_font)
    draw.text((1490,1188), str(workloads),fill='black',font=general_font)
    draw.text((2220,1920), certificate_date,fill='black',font=date_font)
    
    image.save(f'./{indexi} {student_name} certificate.png')
    