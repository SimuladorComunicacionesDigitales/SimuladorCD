# SimCD: Simulador de Comunicaciones Digitales
Simulador para el estudio de señales digitales programado en Python. 

Esta aplicación de escritorio permite el estudio de señales no convencionales, cuyos símbolos pueden ser ingresados por el usuario, con la finalidad de verificar cuáles son los cambios que ocurren en los distintos indicadores clave de una señal digital, como la ocupación espectral y la fortaleza frente al ruido. 

Además tambien permite simular los resultados de señales clásicas como códigos de línea RZ, NRZ, Manchester y modulaciones BPSK, OOK, FSK, QPSK, 8-PSK y 16QAM.

## Funcionamiento del programa
Este simulador funciona a partir del siguiente diagrama de bloque simplificado:
![DiagramaBloque](https://user-images.githubusercontent.com/126732560/222809981-06a2a575-9fad-45e0-8c1c-dd051f7783cc.png)

Los bloques representan:

- **Codificador de Línea // Modulador:** Se genera la señal digital. El simulador posee dos opciones:
  - **Señales clásicas:** señales estandarizadas con características conocidas y aplicaciones prácticas
  - **Señales no convencionales:** señales cuyos símbolos que la conforman son definidas por el usuario. Las señales no convencionales pueden ser ingresadas de dos formas: 
    - **Símbolos:** especificando directamente la forma de sus símbolos. 
    - **Bases:** especificando las bases de la señal para luego ingresar las coordenadas de cada símbolo en el diagrama de constelación.
- **Canal AWGN:** La señal generada es transmitida por un canal con ruido aditivo blanco gaussiano.

- **Receptor Óptimo Gram-Schmidt:** se utiliza un receptor basado en el proceso de ortogonalización Gram-Schmidt para recuperar la señal transmitida con la menor cantidad de errores posibles.

## Archivos .py
- __main.py__ es el archivo ejecutable del programa.
- __Funciones_GUI.py__ es un archivo con todas las funciones comunes que utilizan las ventanas del simulador.

Los demás archivos son las distintas ventanas que componen el simulador:
  - __MainWindow.py__ es el menú inicial del simulador, y __SenalesNoConvencionales.py__ es el menú del módulo de señales no convencionales.
  - __numCiclos.py__ es la ventana de la verificación de Número de Ciclos en Sinusoides y __documentacion.py__ es la ventana de documentación.
  - __SenalesClasicas.py__, __ScreenSimbolos2.py__, __ScreenSimbolos3.py__, __ScreenSimbolos4.py__, __ScreenBases2.py__, __ScreenBases3.py__, y __ScreenBases4.py__ son las ventanas principales que contiene los resultados de los distintos módulos del simulador.
  
  ## Otros archivos:
- __Documentación_Simulador.pdf__ es el documento en PDF con la documentación completa del simulador.
- En la carpeta __/UIs/__ se encuentran los archivos .ui utilizados por las ventanas del simulador, y los archivos .png que se utilizan en el programa.

## Canal de Youtube e Instaladores del simulador

[En este canal de Youtube](https://www.youtube.com/channel/UCgust5DnYAvu9sV0m10zzSA) podrás encontrar el funcionamiento del programa e instrucciones para su instalación.


[En esta carpeta de Drive](https://drive.google.com/drive/folders/1mSQzdSBZGbjdYQhhjNOy4qL1Pa-t2rus?usp=sharing) podrás encontrar los instaladores del simulador tanto para Windows como MacOS.


