#pip install luigi
#para acessar a tela digite no terminal luigid, em segida va em uma nova aba do navegador e escreva Localhost:8082

import luigi
import json
import requests

class StockTwitScrape(luigi.Task):
    
    def output(self):
        return luigi.LocalTarget("raw_data.json")
    
    def run(self):
        return super().run()


