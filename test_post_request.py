import requests

endpoint = 'https://e0a0x0x8gk.execute-api.us-east-1.amazonaws.com/crm-prod'

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

# Define your payload
params = {
    "invoiceId": "12345",
    "accountId": "user@example.com",
    "amount": "19.99",
    "currency": "USD",
    "paymentAmount": "19.99",
    "paymentCurrency": "USD",
    "status": "succeeded",
}

res = requests.post(endpoint, headers=headers, data=params)
print(res.json())