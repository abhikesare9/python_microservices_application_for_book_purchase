from urllib import response
import requests
from . import BOOK_API_URL

class BookClient:
    @staticmethod
    def get_books():
        response = requests.get(BOOK_API_URL + '/api/book/all')
        return response.json()

    @staticmethod
    def get_book(slug):
        requests.get(BOOK_API_URL + '/api/book/'+slug)
        return response.json()

    