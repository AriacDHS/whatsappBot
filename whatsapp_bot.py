#imports necessários
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#vai até o site
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

#define contatos e grupos para enviar a mensagem
#IMPORTANTE: o contato deve ser inserido na lista considerando letras maiúsculas, minúsculas e caracteres especiais.
contatos = ["Contato 1"]
mensagem = "mensagem teste"

#campo responsável pela pesquisa de contatos "copyable-text selectable-text"
#função de procurar os contatos
def busca_contato(contato):
    #encontra a div responsável pela pesquisa de contatos
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    #digita o nome do contato na div e pressiona Enter para redirecionar para o chat do contato
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#campo responsável pela mensagem "copyable-text selectable-text"
#função de enviar a mensagem
def envia_mensagem(mensagem):
    #encontra a div responsável pelo chat
    #tanto a caixa de pesquisa quanto o chat possuem o mesmo xpath, logo se torna necessário o uso do index[1]
    #para especificar o elemento desejado, o comando .find também deve buscar multiplos elementos ao invés de um único
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click
    time.sleep(3)
    #digita a mensagem no chat e pressiona Enter para enviar
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

#processo de execução de funções
for contato in contatos:
    busca_contato(contato)
    envia_mensagem(mensagem)


