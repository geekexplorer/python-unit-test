import requests

class Person():

    def __init__(self, first_name:str, last_name:str, url:str):
        self.first_name:str = first_name
        self.last_name:str = last_name
        self.url:str = url

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def get_web_page(self) -> str:
        try:
            response = requests.get(self.url)
        except requests.RequestException:
            print("Oh noes!")