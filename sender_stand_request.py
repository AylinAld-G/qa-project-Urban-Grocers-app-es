import configuration
import requests
import data

#GET
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)


#POST
#Función para crear usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

#Función para crear un kit para el usuario autenticado
def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                          json=kit_body, headers=headers)

response = post_new_client_kit(data.kit_body, data.headers)
print(response.status_code)
print(response.json())

#Función para obtener el token de autenticación (authToken) de la respuesta
def get_new_user_token():
    user_response = post_new_user(data.user_body)
    auth_token = user_response.json().get("authToken")
    return auth_token