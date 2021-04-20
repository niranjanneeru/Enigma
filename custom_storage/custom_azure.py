from storages.backends.azure_storage import AzureStorage

class PublicAzureStorage(AzureStorage):
    account_name = 'csilocalhost'
    account_key = 'R2/0J5+J9/40XuGa7Zmq9C+//dE/DBWXw0tBsdEm5yv4RTxjBmSSz8bdjjVmCmQ8LrIPfAK2UnJn9Q6MF0bW1w=='
    azure_container = 'media'
    expiration_secs = None
