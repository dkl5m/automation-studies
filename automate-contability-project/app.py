import openpyxl
import pyperclip
import pyautogui
from time import sleep

#site usado para cadastro: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazBjS0tXQWVDUVdoRUtYNk1XWmVGZmQyOGtTZ3xBQ3Jtc0ttUkJId01jNVlXOWgycG1pSmN3bjZIV1REdEY4NnQ5SXZjclFMdVg4aGtkenU1WWQzTGVkRUZlR2JSdmtpSDhNXzRDUGdlQXZOMlpwaVlWS015Nzl3aTJmRmVXVmthalNwbW1OSEtQUTlneTBJel9JYw&q=https%3A%2F%2Fcadastro-produtos-devaprender.netlify.app%2F&v=UtkPIpov6h8

#entrar na planilha
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_products = workbook['Produtos']

#copiar info de um campo e colar no seu campo correspondente
for row in sheet_products.iter_rows(min_row=2):
    
        # Page 1
    # Product name
    product_name = row[0].value
    pyperclip.copy(product_name)
    pyautogui.click(1500,305,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product description
    product_description = row[1].value
    pyperclip.copy(product_description)
    pyautogui.click(1500,415,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product category
    product_category = row[2].value
    pyperclip.copy(product_category)
    pyautogui.click(1500,515,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product code
    product_code = row[3].value
    pyperclip.copy(product_code)
    pyautogui.click(1500,615,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product weight
    product_weight = row[4].value
    pyperclip.copy(product_weight)
    pyautogui.click(1500,690,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product dimensions
    product_dimension = row[5].value
    pyperclip.copy(product_dimension)
    pyautogui.click(1500,780,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Click next button
    pyautogui.click(1455,855,duration=1)
    sleep(4)
    
        # Page 2
    # Product price
    product_price = row[6].value
    pyperclip.copy(product_price)
    pyautogui.click(1500,325,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product quantity
    product_quantity = row[7].value
    pyperclip.copy(product_quantity)
    pyautogui.click(1500,415,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product validity_date
    product_validity_date = row[8].value
    pyperclip.copy(product_validity_date)
    pyautogui.click(1500,505,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product color
    product_color = row[9].value
    pyperclip.copy(product_color)
    pyautogui.click(1500,575,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product size
    product_size = row[10].value
    pyperclip.copy(product_size)
    pyautogui.click(1500,690,duration=1)
    if product_size == 'Pequeno':
        pyautogui.click(1500,705,duration=1)
    elif product_size == 'Médio':
        pyautogui.click(1500,730,duration=1)
    else:
        pyautogui.click(1500,750,duration=1)
    
    # Product material
    product_material = row[11].value
    pyperclip.copy(product_material)
    pyautogui.click(1500,655,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Click next button
    pyautogui.click(1500,808,duration=1)
    sleep(4)
    
        # Page 3
    # Product manufacturer
    product_manufacturer = row[12].value
    pyperclip.copy(product_manufacturer)
    pyautogui.click(1470,345,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product country of origin
    product_country_of_origin = row[13].value
    pyperclip.copy(product_country_of_origin)
    pyautogui.click(1470,425,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product observations
    product_observations = row[14].value
    pyperclip.copy(product_observations)
    pyautogui.click(1470,525,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product bars_code
    product_bars_code = row[15].value
    pyperclip.copy(product_bars_code)
    pyautogui.click(1470,655,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Product warehouse_location
    product_warehouse_location = row[16].value
    pyperclip.copy(product_warehouse_location)
    pyautogui.click(1470,735,duration=1)
    pyautogui.hotkey('ctrl v')
    
    # Click finish button ("concluir")
    pyautogui.click(1485,815,duration=1)
    sleep(2)
    # Click confirm inclusion button
    pyautogui.click(1885,195,duration=1)
    sleep(2)
    # Click confirmation 2 button
    pyautogui.click(1885,192,duration=1)
    sleep(2)
    # Click add one more button
    pyautogui.click(1695,580,duration=1)
    sleep(2)
    

#repetir esses passos para outros campos até preencher campos da página
#clicar em próximo
#repetir os mesmos passos e ir para a próxima página (página 2)
#repetir os mesmos passos e finalizar o cadastro do produto e clicar em concluir
#clicar em ok
#clicar em ok (mensagem de salvamento)
#clicar em "adicionar mais um" e repetir processo até finalizar a planilha

