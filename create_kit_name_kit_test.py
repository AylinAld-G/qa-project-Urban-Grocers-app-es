import sender_stand_request
import data

# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # Se obtiene el token de autenticación de la respuesta en post_new_client_kit
    authToken = sender_stand_request.get_new_user_token()
    # El resultado de la solicitud relevante se guarda en la variable "kit_response"
    kit_response = sender_stand_request.post_new_client_kit(kit_body, authToken)

    #Comprobar si el código de estado es 201
    assert kit_response.status_code==201
    # Comprobar que el campo 'name' de la respuesta sea el mismo valor utilizado en la prueba.
    assert kit_response.json()["name"] == name

## Función de prueba negativa para los casos en los que la solicitud devuelve un error con código 400
def negative_assert_code_400(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    authToken = sender_stand_request.get_new_user_token()
    # El resultado de la solicitud relevante se guarda en la variable "kit_response"
    kit_response = sender_stand_request.post_new_client_kit(kit_body, authToken)

    #Comprobar si el código de respuesta es 400
    assert kit_response.status_code == 400

#Prueba 1: El número permitido de caracteres (1)
# Parámetro "name" contiene 1 letra
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Prueba 2: Parámetro "name" contiene 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc \
                    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd \
                    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda \
                    bcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab \
                    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc \
                    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


#Prueba 3: El número de caracteres es menor que la cantidad permitida (0)
# Parámetro "name" contiene 0 caracteres
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")


#Prueba 4: Parámetro "name" contiene más caracteres que la cantidad permitida (512)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd \
                             abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd \
                             abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd \
                             abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd \
                             abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd \
                             abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd \
                             abcdabcdabcdabcdabcdabcdabcdabcD")


#Prueba 5: Se permiten caracteres especiales
# Parámetro "name" contiene caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("№%@")

# Prueba 6: Se permiten espacios
# Parámetro "name" contiene espacios
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" A Aaa ")

#Prueba 7: Se permiten números
# Parámetro "name" contiene string de números
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

#Prueba 8: El parámetro no se pasa en la solicitud
# El parámetro "name" no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    # El parámetro firstName se elimina de la solicitud
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

#Prueba 9: Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_number_type_get_error_response():
    negative_assert_code_400(123)



