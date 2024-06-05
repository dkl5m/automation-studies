import openpyxl
#entrar na planilha

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_products = workbook['Produtos']

#copiar info de um campo e colar no seu campo correspondente
#repetir esses passos para outros campos até preencher campos da página
#clicar em próximo
#repetir os mesmos passos e ir para a próxima página (página 2)
#repetir os mesmos passos e finalizar o cadastro do produto e clicar em concluir
#clicar em ok
#clicar em ok (mensagem de salvamento)
#clicar em "adicionar mais um" e repetir processo até finalizar a planilha

