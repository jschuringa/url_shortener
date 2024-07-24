import unittest
import logging
import sys


def test_post_valid(test_client):
    response = test_client.post(
            "/url",
            json={"target": "https://google.com"},
        )
    assert response.status_code == 200
    assert response.json()['short'] != None


def test_post_bad_request(test_client):
    response = test_client.post(
        "/url",
        json={"target": "foobar"},
    )
    assert response.status_code == 400


def test_redirect_exists(test_client):
    # typically we'd insert data into the db instead of hitting the endpoint 
    # but that's a lot of setup for this small project
    response = test_client.post(
        "/url",
        json={"target": "https://google.com"},
    )
    
    assert response.status_code == 200
    short = response.json()['short']

    response = test_client.get(
        f"/{short}"
    )
    logging.getLogger("Tester").debug(response)
    assert response.status_code == 404
    

def test_redirect_not_found(test_client):
    response = test_client.get(
        "/asdf"
    )
    assert response.status_code == 404