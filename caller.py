import web_client

url = "https://www.openexchangerates.org"
app_id = "f4ac58b20ec54e19b5ac494b52c7c05c"

WClient = web_client.WebClient(url, app_id)
WClient.write_to_base()