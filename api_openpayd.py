
import time
# Get_access_token
import requests
currency = 'INR'
username = 'Shrey'
url = "https://sandbox.openpayd.com/api/oauth/token?grant_type=client_credentials"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
    "authorization": "Basic c2hyZXk6WlYrUDgjZXBtNw=="
}

response = requests.post(url, headers=headers)

a = response.text
a = a[1:len(a)-1]
a= a.split(":")
access_token = a[1][1:]
access_token = access_token[:-14]
accountHolderId = a[5][1:]
accountHolderId = accountHolderId[:-14]
# print(accountHolderId)

# *******************************************************
# Create Account

import requests

url = "https://sandbox.openpayd.com/api/accounts"

payload = {
    "currency": f"{currency}",
    "friendlyName": f"{username}"
}
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "x-account-holder-id": f"{accountHolderId}",
    "Authorization": f"Bearer {access_token}"
}
 
response = requests.post(url, json=payload, headers=headers)

b = response.text
b = b.split(':')
status = b[5]
status = status.split(',')
status = status[0]
status = status.replace("\"", '')
status = status.replace(' ', '')
internalAccountId = b[-1]
internalAccountId = internalAccountId.split('\n')
internalAccountId = internalAccountId[0].replace('"','').replace(' ','')
# print(internalAccountId)
# print(status)

# *****************************************************
# list bank accounts
import requests

url = f"https://sandbox.openpayd.com/api/bank-accounts?internalAccountId={internalAccountId}&currency={currency}&status=ACTIVE"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "x-account-holder-id": f"{accountHolderId}",
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)

c = response.text
c = c.split(":")
print(c)
IBAN = c[6].split(",")
IBAN = IBAN[0].replace('\"','')
print("IBAN: " +IBAN)
acc_num = c[8].split(',')
acc_num = acc_num[0].replace('\"','')
print("Account number: "+acc_num)
