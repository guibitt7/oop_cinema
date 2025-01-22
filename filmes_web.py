from playwright.sync_api import Playwright, sync_playwright, Error, Page
import clipboard
from time import sleep

class FilmeWeb:

    def __init__(self):
        self._page = Page
        self._playwright = Playwright
        self.lista_filmes = []

    def _criar_navegador(self):
        navegador = self._playwright.chromium.launch(headless=False)
        return navegador

    def _ir_adoro_cinema(self):
        try:
            navegador = self._criar_navegador()

            self._pagina = navegador.new_page()
            self._pagina.goto('https://www.adorocinema.com/')
            sleep(2)
            return True

        except Error as e:
            print(e)

    def _copiar_conteudo(self, texto_xpath):
        try:
            self._texto = self._pagina.text_content(texto_xpath, timeout=300000)
            if self._texto:
                clipboard.copy(self._texto)
                return self._texto

            self._pagina.close()

            print("Erro ao copiar o conteudo")

        except Error as e:
            print(e)


    def _formatar_filmes_dict(self):
        filme1_nome = self._copiar_conteudo(texto_xpath='//*[@id="roller-3"]/div[1]/div/div[1]/div/div/a').strip()
        filme2_nome = self._copiar_conteudo(texto_xpath='//*[@id="roller-3"]/div[1]/div/div[2]/div/div/a').strip()
        filme3_nome = self._copiar_conteudo(texto_xpath='//*[@id="roller-3"]/div[1]/div/div[3]/div/div/a').strip()
        filme4_nome = self._copiar_conteudo(texto_xpath='//*[@id="roller-3"]/div[1]/div/div[4]/div/div/a').strip()

        filme1_diretor = self._copiar_conteudo(texto_xpath='//*[@id="roller-3"]/div[1]/div/div[1]/div/div/div').strip()
        filme2_diretor = self._copiar_conteudo(texto_xpath='//*[@id="roller-3"]/div[1]/div/div[2]/div/div/div').strip()
        filme3_diretor = self._copiar_conteudo(texto_xpath='//*[@id="roller-3"]/div[1]/div/div[3]/div/div/div').strip()
        filme4_diretor = self._copiar_conteudo(texto_xpath='//*[@id="roller-3"]/div[1]/div/div[4]/div/div/div').strip()

        self.lista_filmes = [
            {'Nome' : filme1_nome, 'Diretor' : filme1_diretor},
            {'Nome' : filme2_nome, 'Diretor' : filme2_diretor},
            {'Nome' : filme3_nome, 'Diretor' : filme3_diretor},
            {'Nome' : filme4_nome, 'Diretor' : filme4_diretor},
        ]

    def executar_web(self):
        with sync_playwright() as self._playwright:
            verificar = self._ir_adoro_cinema()
            if verificar:
                self._formatar_filmes_dict()
            return self.lista_filmes