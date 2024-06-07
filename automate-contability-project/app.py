import openpyxl
import pyperclip
#entrar na planilha

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_products = workbook['Produtos']

#copiar info de um campo e colar no seu campo correspondente
for row in sheet_products.iter_rows(min_row=2):
    # Product name
    product_name = row[0].value
    pyperclip.copy(product_name)
    
    # Product description
    product_description = row[1].value
    pyperclip.copy(product_description)
    
    # Product category
    product_category = row[2].value
    pyperclip.copy(product_category)
    
    # Product code
    product_code = row[3].value
    pyperclip.copy(product_code)
    
    # Product weight
    product_weight = row[4].value
    pyperclip.copy(product_weight)
    
    # Product dimensions
    product_dimension = row[5].value
    pyperclip.copy(product_dimension)
    

#repetir esses passos para outros campos até preencher campos da página
#clicar em próximo
#repetir os mesmos passos e ir para a próxima página (página 2)
#repetir os mesmos passos e finalizar o cadastro do produto e clicar em concluir
#clicar em ok
#clicar em ok (mensagem de salvamento)
#clicar em "adicionar mais um" e repetir processo até finalizar a planilha

