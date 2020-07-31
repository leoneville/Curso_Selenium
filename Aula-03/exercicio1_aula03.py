"""
Exercicio 01
Crie um programa com selenium que
° Gere um dicionario, onde a chave é a tag h1
    ° O valor deve ser um novo Dicionario
    ° Cada chave do valor deverá ser o valor de "Atributo"
    ° Cada valor deve ser o texto contido no elemento
Link = https://curso-python-selenium.netlify.app/exercicio_01.html
"""
from selenium.webdriver import Firefox
from time import sleep

url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

navegador = Firefox()
navegador.get(url)

sleep(5)

h1 = navegador.find_element_by_tag_name("h1")

dicio = {h1.text:""}
dicio2 = {}

for i in range(3):
    ps = navegador.find_elements_by_tag_name("p")
    dicio2.update({f"texto{i+1}":ps[i].text})

dicio[h1.text] = dicio2

print(dicio)

navegador.quit()




