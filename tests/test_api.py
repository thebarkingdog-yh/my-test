import json

import pytest
import requests


def test_ex1():
    assert 1 == 1


def test_ex2():
    assert 1 == 5


def test_ex3():
    assert 1 == 3


@pytest.mark.skip()
def test_ping_api():
    api_url = "http://0.0.0.0:9736/api/ping_api/ping"
    response = requests.get(api_url)
    assert response.status_code == 204


@pytest.mark.skip()
def test_context_chain_api():
    api_url = "http://0.0.0.0:9736/api/v1/single/custom"
    data = {
        "prompt": "你能幫我做什",
        "system_prompt": "",
        "streaming": True,
        "custom_model": {
            "llm_name": "gpt-3.5-turbo-1106-openai",
            "timeout": -1,
            "max_retries": 2,
            "temperature": 0,
        },
    }
    response = requests.post(api_url, data=json.dumps(data))
    assert response.status_code == 200


@pytest.mark.skip()
def test_chain_api():
    api_url = "http://0.0.0.0:9736/api/v1/single/custom"
    data = {
        "prompt": "你能幫我做什",
        "system_prompt": "",
        "streaming": True,
        "custom_model": {
            "llm_name": "gpt-3.5-turbo-1106-openai",
            "timeout": 20,
            "max_retries": 2,
            "temperature": 0,
        },
    }
    response = requests.post(api_url, data=json.dumps(data))
    assert response.status_code == 200
