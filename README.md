# Proyecto Urban Grocers 
## QA-project-Urban-Grocers-app
#### _Aldana Guzmán Aylín, grupo QA-16, 7mo sprint._
- Este proyecto consiste en comprobar cómo la aplicación de Urban Grocers crea kits de productos. 


- Mediante una lista de comprobación, para el campo "name" en la solicitud de creación de un kit de productos, se llevan a cabo una serie de pruebas automatizadas,  
donde se evalúa específicamente la entrada de datos del parámetro "name".

- **Documentación** : _ApiDocs_. Ejecutar la función get_docs() del archivo _sender_stand_request.py_.
### **Tecnologías y técnicas utilizadas**: 
El lenguaje utilizado es _Python_ y la estructura del código se basa en el uso de funciones. 

El proyecto consta de 2 archivos que contienen los datos para enviar las solicitudes: _configuration.py_ y _data.py_. 

Otro archivo que controla las solicitudes post para crear un kit y un usuario: _sender_stand_request.py_. 

Y por último el archivo que contiene las funciones para evaluar las solicitudes y respuestas a la aplicación: _create_kit_name_kit_test.py_.

### Pruebas
1. En el archivo _configuration.py_ se encuentran las rutas para enviar las solicitudes. 
Para iniciar, es necesario cambiar la ruta _URL_SERVICE_ con la dirección actualizada del servidor.
2. Ejecutar el archivo _sender_stand_request.py_ para crear un usuario y obtener el token de autenticación (authToken).
3. Ir al archivo _create_kit_name_kit_test.py_ y cambiar la configuración de ejecución a Pytest. Una vez configurado, correr el código y esperar a que las pruebas terminen de ejecutarse. 

