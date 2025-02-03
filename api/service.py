import requests

class NumberAPISerivice:
    base_url = "http://numbersapi.com/"

    def get_fun_fact(self, number):

        response = requests.get(f"{self.base_url}{number}/math")

        if response.status_code == 200:
            return response.text

        return "An Error Occured"