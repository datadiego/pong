# bz11-pong

Clon del clásico juego PONG de Atari.

## Como colaborar en este proyecto

Primero debes clonar este repositorio en tu PC.

Es recomendable usar un entorno virtual antes de instalar las dependencias.

```
python -m venv env

# En MacOS o Linux
source ./env/bin/activate

# En Windows (con cmd/símbolo del sistema)
.\env\Scripts\activate
```

Una vez creado y activado el entorno virtual, ya puedes instalar las dependencias

```
pip install -r requirements.txt
```

Para arrancar el juego basta con ejecutar desde la línea de comandos:

```
python pong.py
```
##Controles
Jugador 1:
Arriba: W
Abajo: S

Jugador 2:
Arriba: Flecha de dirección arriba
Abajo: Flecha de dirección abajo

Podemos activar y desactivar el efecto de filtro CRT con la variable _CRT en la linea 79 del archivo pong.py

##Fallos conocidos:
- En ciertas posiciones, la bola puede quedarse atravesada en la pala
