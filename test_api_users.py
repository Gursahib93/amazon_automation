import requests
import pytest
import unittest

url = "https://jsonplaceholder.typicode.com"


def test_api():
    response = requests.get(f"{url}/users")
    assert response.status_code == 200

def test_users_count():
    response = requests.get(f"{url}/users")
    response_json = response.json()
    user_count = len(response_json)
    assert user_count >= 10
