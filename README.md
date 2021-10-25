# python-games-api

Este repositorio incluye una API Rest desarrollada con las siguientes tecnologías:

- PostgreSQL (psycopg2 2.9.1)
- Python 3.6
- Django 3.2.8
- Django Rest Framework 3.12.4

Esta API se ha creado para poder gestionar una red social donde l@s usuari@s registrad@s pueden comunicarse entre sí en unas salas creadas relacionadas con un videojuego.


## Rutas

Este es el listado de rutas a las que se puede acceder desde esta API:

`/admin` Dentro de esta ruta está accesible el dashboard que viene por defecto con Django donde se puede gestionar toda la información disponible en la plataforma.

`/api` Esta es la ruta principal de mi API, separada por cada modelo generado en PostgreSQL.

    - `/games` : GET, POST, PATCH, DELETE
    - `/parties` : GET, POST, PATCH, DELETE
    - `/messages` : GET, POST, PATCH, DELETE
    - `/users` : GET, POST, PATCH, DELETE 

`/rest-auth` Bajo esta ruta están todas aquellas relacionadas con la sesión del usuario:

    - `/login` : Para iniciar una sesión
    - `/logout` : Para cerrar una sesión activa
    - `/user` : Para recibir la información del usuario activo 
    - `/registration` : Para registrar un usuario nuevo en la plataforma
    - `/password/reset/` : Para resetear la contraseña
    - `/password/reset/confirm/` : Para confirmar el reseteo de la contraseña
    - `/password/change/` : Para modificar la contraseña


## Modelos / Models

Como se puede observar en el fichero `gameapi/models.py` he creado los siguientes modelos:

- Game
- Party
- Message
- CustomUser

### Game

Este modelo incluye los siguientes atributos:

- name: Nombre del videojuego.
- added_by: Se relaciona con el usuario que lo crea para posteriormente poder mostrar su creador.
- created_date: Se agrega la fecha de creación.

### Party

Este modelo incluye los siguientes atributos:

- name: Nombre de la sala o party.
- added_by: Se relaciona con el usuario que la crea para posteriormente poder mostrar su creador.
- created_date: Se agrega la fecha de creación.
- game_id: Se relaciona con el juego al que pertenece a través del ID de dicho videojuego.

### Message

Este modelo incluye los siguientes atributos:

- content: Contenido del mensaje.
- added_by: Se relaciona con el usuario que lo crea para posteriormente poder mostrar a quién pertenece.
- created_date: Se agrega la fecha de creación.
- party_id: Se relaciona con la sala a la que pertenece a través del ID de dicha sala.

### CustomUser

Este modelo incluye la siguiente information:

- Hereda todos los atributos y métodos definidos en AbstractUser, por defecto, en Django.
- email: He modificado este campo para que sea único.
- steam_user: He agregado este campo para que el usuario pueda agregar su usuario de Steam.
- discord_user: He agregado este campo para que el usuario pueda agregar su usuario de Discord.

## Serializadores / Serializers

Como se puede observar en el fichero `gameapi/serializers.py` he creado los siguientes serializadores:

- GameSerializer
- PartySerializer
- MessageSerializer
- UserSerializer

Para poder serializar la información que resulta relevante en la aplicación para cada uno de los modelos.


## Vistas / Views

Como se puede observar en el fichero `gameapi/views.py` he creado las siguientes vistas:

- GameViewSet: Donde he ordenado los resultados por nombre y permito el filtrado por este mismo campo.

- PartyViewSet: Donde he ordenado los resultados por nombre y permito el filtrado por el campo: `game_id`.

- MessageViewSet: Donde he ordenado los resultados por su fecha de creación y permito el filtrado por el campo: `party_id`.

- UserViewSet: Donde retorno los usuarios pasados por el UserSerializer con atención en el campo `username`.


## Requisitos funcionales

Siguiendo el enunciado de este proyecto, estas son las funcionalidades que he llevado a cabo:

- RF.1 Los usuarios se tienen que poder registrar a la aplicación, estableciendo un usuario/contraseña.

    - Para ello el cliente puede utilizar el endpoint `/rest-auth/registration` con una petición de tipo POST que incluya en el body la siguiente información:

        {
            "username": "",
            "password1": "",
            "password2": ""
        }

- RF.2 Los usuarios tienen que autenticarse a la aplicación haciendo login.

    - Para ello el cliente puede utilizar el endpoint `/rest-auth/login` con una petición de tipo POST que incluya en el body la siguiente información:

        {
            "username": "",
            "password": ""
        }

- RF.3 Los usuarios tienen que poder crear Parties (grupos) por un determinado videojuego.

    1. Para que el cliente pueda crear una sala o party, antes necesita haber creado un videojuego que pueda asociarle a una sala.
    
    2. Para ello necesitará hacer una petición de tipo POST a este endpoint `/api/games/` con el token en la cabecera de Authorization que la petición login devuelve y con la información que el videojuego precisa para ser creado.

    3. Una vez hecho esto, podrá crear una nueva party, haciendo una petición de tipo POST a este endpoint `/api/parties/` con el token en la cabecera de Authorization que la petición login devuelve y con la información que la sala precisa para ser creada.

- RF.4 Los usuarios tienen que poder buscar Parties seleccionando un videojuego.

    Para poder ofrecer a los clientes una forma de filtrar los resultados he utilizado la dependencia `django-filter` que tras configurarlo permite el filtrado de la siguiente forma:

        - /api/games/?name=Valheim Los juegos pueden ser filtrados por el nombre del videojuego

        - /api/messages/?party_id=1 Los mensajes se pueden filtrar por la party o sala a la que están asociados.

        - /api/parties/?game_id=1 Las salas se pueden filtrar por el juego al que están asociadas.

- RF.5 Los usuarios pueden entrar y salir de una Party.

    Cualquier usuario logeado pueden entrar y salir de una party sin ningún problema.

- RF.6 Los usuarios tienen que poder enviar mensajes a la Party. Estos mensajes tienen que poder ser editados y borrados por su usuario creador.

    Se puede editar y eliminar un mensaje creado previamente, utilizando los métodos PUT o PATCH para editar y DELETE para eliminar haciendo uso de este endpoit: `/api/messages/`

- RF.7 Los mensajes que existan a una Party se tienen que visualizar como un chat común.

    Se pueden visualizar los mensajes asociados a una sala haciendo uso del filtro que he creado para dicho fin. Por ejemplo: `/api/messages/?party_id=1`

- RF.8 Los usuarios pueden introducir y modificar sus datos de perfil, por ejemplo, su usuario de Steam.

    Los usuarios que hay en mi aplicación son una extensión de los que vienen por defecto en Django y como les he agregado los campos: `steam_user` y `discord_user`. Ahora el usuario puede editarlos cada vez que se utilice el endpoint: `/rest-auth/user/` con un verbo de tipo PUT o PATCH.

- RF.9 Los usuarios tienen que poder hacer logout de la aplicación web.

    Los usuarios pueden hacer logout de la applicación haciendo uso del endpoint `/rest-auth/logout`

