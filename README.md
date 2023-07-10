# OpenPayd_API
This repo has all the information of the OpenPayd API. 
### The link used for the API Docs is: https://apidocs.openpayd.com/reference/getting-started-with-your-api
# The task is to obtain the IBAN number and the account number of the user
## The steps are as follows:
1. Get the access token by giving currency and username as the input
2. Obtain the AccountHolderID in the response of the above request
3. Passing AccountHolderID as a parameter to creating a new account in OpenPayd
4. After that an internal Account number is generated as a response to the above request
5. Using this internalAccountNumber to create a new request for IBAN and account number
6. The response of this query will contain IBAN number and account number.
