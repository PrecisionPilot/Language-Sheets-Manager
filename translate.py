import requests, uuid, json, api_key

def translate(input_text: str) -> str:
    # Add your key and endpoint
    key = api_key.api_key
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "eastus"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'yue',
        'to': ['en', 'zh-Hans']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': input_text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return [trns["text"] for trns in response[0]["translations"]]

if __name__ == "__main__":
    print(translate("漢堡包"))