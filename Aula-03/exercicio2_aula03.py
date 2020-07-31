"""
Exercicio 02
Crie um programa com selenium que
    º Jogue o jogo
    º Quando você ganhar, o script deve parar de ser executado
link: https://curso-python-selenium.netlify.app/exercicio_02.html
"""


from selenium.webdriver import Firefox
from time import sleep

url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

navegador = Firefox()

navegador.get(url)

sleep(5)

ps = navegador.find_elements_by_tag_name("p")
a = navegador.find_element_by_tag_name("a")

num_esperado = ps[-1].text[-1]

while True:
    a.click()
    ps = navegador.find_elements_by_tag_name("p")
    if ps[-1].text[-1] == num_esperado:
        print(ps[-1].text)
        break

sleep(5)
navegador.quit()





