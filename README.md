# estructuras_repetitivas_3147245
Proyecto para trabajar ciclos for y while en python 

## Conceptos clave para trabajar en ciclos:

* **Breakpoint*(Punto de interrupcion)**: Herramienta
    Para ejecutar codigo, una instruccion a la
    vez (depuracion-debugger)
    Permite ver el valor de las variables definidas 
    en un proframa a traves de la ejeucion de 
    codigo, Permitiendo observar que el comportamiento del programa/codigo a traves del tiempo

* **Variable contadora(COntador)**: Variiable
a la cual podemoos aumentar(disminuir) su valor
en una ddeterminada cantidad constante (de 1 en 1, de 2 en 2, etc).

-Una variable contadora se debe iniciallizar 
**antes de la estrutura repetitiva** con un valor inicial (0)
- UNa variable contadora, por lo general se nombra con las letras i,j 
- Una variable contadora **debe participar en la condicional del ciclo**
- Toda variable contadora debe tener **intstruccion de incremento** para aumentar su valor:
- **Instrucciones de incremento
(sintaxis)
-Variable-operador de asignación-variable contadora-signo para incrementar + signo para descrementar- -valor a aumentar-variable constante.**

- En un ciclo de while, la intruccion de incremento se pone
**al final del bloque de codigo del ciclo**

* **Iteraccion** : Un recorrido en la ejecucion de un ciclo.

## Ciclo while 

Estructura que permite ejecutar 
un bloque de codigo un numero determinado
de veces.
El  bloque de codigo dentro del ciclo 
while se ejecutara sucesivamente
**mientras la condicional sea
evalado como VERDAD.** 

### Sintaxis en python:
```
while condicional:
        intruccion1
        intruccion2
        intruccion3
        .....
        intruccion n

```

## Ciclo for

Se utiliza (pythonn) para recorrer 
conjuntos de datos (estructuras de datos - colecciones de datos)

* EL ciclo recorrera cada dato en la estructura desde el priemro hasta el ultimo

* EL elemento recorrido se asgina a una variable en el ciclo 

### Sintaxis for:
```
     for <cariable> in <conexion de datos>:
        intruccion1
        intruccion2
        intruccion3
        .....
        intruccion n
    
```