
# MCOC2020_P2_G7_Entrega5

El primer diseño es un puente con arco bajo el tablero. Este tablero que tiene un largo total de 215 metros, se dividió en tramos de 5 metros, obteniendo un total de 43 tramos.

![](Imagenes/Puente_arco.png)

Este diseño no se pudo comprobar, por lo que fue cambiado.

En segundo lugar, se realizo el siguiente diseño:

![](Imagenes/Diseño2.png)

El cual es un puente con perfil cajon. Inicialmente, el diseño se realizó con un radio igual a 8 cm y un espesor de 5 mm, cumpliendo con ambos casos. Las propiedades de cada barra fueron props = [8 cm, 5 mm, 200 GPa, 7600 kg/m^3, 420 MPa]. A lo que nos dimos cuenta que el diseño estaba sobredimensionado por lo que para reducir el peso se cambiaron las propiedades.

![](Imagenes/Diseño_R8.png)

Para optimizar el peso, se disminuyó el radio a 4 cm y el espesor a 1 mm, volviendo a cumplir con los 2 casos. Nuevamente se considero que el diseño estaba sobrediseñado pero a menor medida que el diseño anterior.

![](Imagenes/Diseño_R4.png)

Luego, se volvió a disminuir el radio, esta vez dejandolo en 1 cm, y este no cumplió con el caso 2. En esta caso como el diseño no cumplió, se consideró como subestimado, por lo que se requieren barras de mayor área. 

![](Imagenes/Diseño_R1.png)

Finalmente, llegamos a que al aumentar el radio a 2 cm, el diseño si cumplia con ambos casos. por lo que este es el diseño definitivo con props = [2 cm, 1 mm, 200 GPa, 7600 kg/m^3, 420 MPa].


![](Imagenes/Diseño_R2.png)


