"""
Este archivo contiene todas las funciones comunes para todas las ventanas del simulador.
"""

import math
import numpy as np
from scipy import special as sp
from scipy.signal import find_peaks

def qfunc(x):
    """
    Función que calcula el valor de QFunc(x), como en MATLAB.

    :param x: Argumento de la función.
    :return: QFunc(X)
    """
    return 0.5-0.5*sp.erf(x/math.sqrt(2))

def qfuncinv(x):
    """
    Función que calcula el valor de la función inversa de QFunc(x), como en MATLAB.

    :param x: Argumento de la función.
    :return: QFuncInv(X)
    """

    return math.sqrt(2)*sp.erfinv(1-2*x)

def bases(t, nMuestrasSimb, tsimb, tipoOnda, frecuencia, fase, t1, t2, fSample):
    """
    Función que devuelve un arreglo con una base de energía unitaria de la forma que haya ingresado el usuario.

    :param t: Vector tiempo.
    :param nMuestrasSimb: Número de muestras en un símbolo.
    :param tsimb: Tiempo de símbolo en segundos.
    :param tipoOnda: Opción ingresada por el usuario.
    :param frecuencia: Frecuencia de portadora.
    :param fase: Fase de símbolo sinusoide.
    :param t1: Tiempo de inicio en símbolo de duración variable.
    :param t2: Tiempo de finalización en símbolo de duración variable.
    :param fSample: Frecuencia de muestreo.

    :return: Arreglo con la base.
    """
    #0 - Pulso nulo
    #1 - Pulso
    #2 - Medio Pulso'
    #3 - Manchester'
    #4 - Coseno'
    #5 - Pulso de duración variable
    #6 - Coseno de duración variable'

    n = {
        0: 0,
        1: int(0.25 * fSample * tsimb),
        2: int(0.5 * fSample * tsimb),
        3: int(0.75 * fSample * tsimb),
        4: int(fSample * tsimb),
    }

    tipo_signal = {
        0: np.zeros(nMuestrasSimb),
        1: np.ones(nMuestrasSimb),
        2: np.concatenate((np.ones(int(nMuestrasSimb * 0.5)), np.zeros(int(nMuestrasSimb * 0.5)))),
        3: np.concatenate(((np.ones(int(nMuestrasSimb * 0.5))), -np.ones(int(nMuestrasSimb * 0.5)))),
        4: np.cos(2 * np.pi * frecuencia * t + fase),
        5: np.concatenate((np.zeros(n[t1]), np.ones(n[t2] - n[t1]), np.zeros(nMuestrasSimb - n[t2])))
    }

    if tipoOnda==6:
        y=np.multiply(tipo_signal[4],tipo_signal[5])
    else:
        y = tipo_signal[tipoOnda]

    E = (nMuestrasSimb / fSample) * np.mean(np.multiply(y,y))

    if tipoOnda != 0:
        y=y/(math.sqrt(E))

    return y

def simbolos(t, nMuestrasSimb, tsimb, tipoOnda, frecuencia, fase, amplitud, t1, t2, fSample):
    """
    Función que devuelve un arreglo con el símbolo seleccionado por el usuario.

    :param t: Vector tiempo.
    :param nMuestrasSimb: Número de muestras en un símbolo.
    :param tsimb: Tiempo de símbolo en segundos.
    :param tipoOnda: Opción ingresada por el usuario.
    :param frecuencia: Frecuencia de portadora.
    :param fase: Fase de símbolo sinusoide.
    :param amplitud: Amplitud del símbolo.
    :param t1: Tiempo de inicio en símbolo de duración variable.
    :param t2: Tiempo de finalización en símbolo de duración variable.
    :param fSample: Frecuencia de muestreo.
    :return: Arreglo con el símbolo ingresado.
    """

    # t1 y t2:
    # 0: 0%
    # 1: 25%
    # 2: 50%
    # 3: 75%
    # 4: 100%

    n = {
        0: 0,
        1: int(0.25 * fSample * tsimb),
        2: int(0.5 * fSample * tsimb),
        3: int(0.75 * fSample * tsimb),
        4: int(fSample * tsimb),
    }

    #tipoOnda
    # 0 - Pulso nulo
    # 1 - Pulso
    # 2 - Medio Pulso
    # 3 - Manchester
    # 4 - Coseno
    # 5 - Pulso de duración variable
    # 6 - Coseno de duración variable

    tipo_signal = {
        0: np.zeros(nMuestrasSimb),
        1: amplitud * np.ones(nMuestrasSimb),
        2: amplitud * np.concatenate((np.ones(int(nMuestrasSimb * 0.5)), np.zeros(int(nMuestrasSimb * 0.5)))),
        3: amplitud * np.concatenate(((np.ones(int(nMuestrasSimb * 0.5))), -np.ones(int(nMuestrasSimb * 0.5)))),
        4: amplitud * np.cos(2 * np.pi * frecuencia * t + fase),
        5: amplitud * np.concatenate((np.zeros(n[t1]), np.ones(n[t2] - n[t1]), np.zeros(nMuestrasSimb - n[t2])))
    }

    if tipoOnda==6:
        y=(1/amplitud)*np.multiply(tipo_signal[4],tipo_signal[5])
    else:
        y = tipo_signal[tipoOnda]

    return y

def esCoseno(simbolo, fSample):
    """
    Función que detecta sí un símbolo es sinusoide o no.

    :param simbolo: Arreglo con el símbolo.
    :param fSample: Frecuencia de muestreo.
    :return: True si es el símbolo es sinusoide.
    """
    n = simbolo.size
    timestep = 1 / fSample
    fourier = np.fft.fft(simbolo)
    frequencies = np.fft.fftfreq(n, d=timestep)
    magnitudes = abs(fourier[np.where(frequencies >= 0)])

    peak_frequency = np.argmax(magnitudes)

    if peak_frequency>2:
        return True
    else:
        return False

def gramSchmidt(s1, s2, s3, s4, nMuestrasSimb, fSample):
    """
    Función que halla las bases ortogonales para los símbolos ingresado por el usario.

    :param s1: Símbolo 1.
    :param s2: Símbolo 2.
    :param s3: Símbolo 3.
    :param s4: Símbolo 4.
    :param nMuestrasSimb: Número de muestras por símbolo.
    :param fSample: Frecuencia de muestreo.

    :return: Bases ortogonales U1 y U2.
    """
    E1 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s1, s1))

    if E1 == 0 or E1 < math.pow(10, -3):
        U1 = np.zeros(nMuestrasSimb)
    else:
        U1 = s1 / (math.sqrt(E1))

    # Numerador y denominador de la base U2:
    # Pruebo con el simbolo 2
    u2Num = np.subtract(s2, (((nMuestrasSimb / fSample) * np.mean(np.multiply(s2, U1))) * U1))
    u2Denom = math.sqrt((nMuestrasSimb / fSample) * np.mean(np.multiply(u2Num, u2Num)))

    if u2Denom == 0 or u2Denom < math.pow(10, -3):
        # Pruebo con el simbolo 3
        u2Num = np.subtract(s3, (((nMuestrasSimb / fSample) * np.mean(np.multiply(s3, U1))) * U1))
        u2Denom = math.sqrt((nMuestrasSimb / fSample) * np.mean(np.multiply(u2Num, u2Num)))

        if u2Denom == 0 or u2Denom < math.pow(10, -3):
            # Pruebo con el simbolo 4
            u2Num = np.subtract(s4, (((nMuestrasSimb / fSample) * np.mean(np.multiply(s4, U1))) * U1))
            u2Denom = math.sqrt((nMuestrasSimb / fSample) * np.mean(np.multiply(u2Num, u2Num)))

            if u2Denom == 0 or u2Denom < math.pow(10, -3):
                U2 = np.zeros(nMuestrasSimb)
            else:
                U2 = u2Num / u2Denom
        else:
            U2 = u2Num / u2Denom
    else:
        U2 = u2Num / u2Denom

    return (U1,U2)

def senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, nTotalSimb):
    """
    Función que genera la señal aleatoria a partir de los símbolos ingresados.

    :param s1: Símbolo 1.
    :param s2: Símbolo 2.
    :param s3: Símbolo 3.
    :param s4: Símbolo 4.
    :param tSimb: Tiempo de símbolo en segundos.
    :param nMuestrasSimb: Número de muestras por símbolo.
    :param nroSimb: Número de símbolos en que compone la señal (2, 3 o 4).
    :param nTotalSimb: Número de símbolos totales de la señal en tiempo.
    :return: Senal: Arreglo con la señal en tiempo / t2: Vector tiempo de la señal en tiempo. /Bits: Vector con los números aleatorios que generan la señal.

    """

    nMuestrasSenal = nTotalSimb * nMuestrasSimb

    senal = np.empty(nMuestrasSenal)
    t2 = np.linspace(0, tSimb * nTotalSimb, nMuestrasSenal)

    if nroSimb == 2:
        bits = np.random.randint(2, size=nTotalSimb)

        for i in range(nTotalSimb):
            if bits[i] == 1:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            else:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2

    elif nroSimb == 3:
        bits = np.random.randint(3, size=nTotalSimb)

        for i in range(nTotalSimb):
            if bits[i] == 1:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            elif bits[i] == 2:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2
            else:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s3

    elif nroSimb == 4:
        bits = np.random.randint(4, size=nTotalSimb)

        for i in range(nTotalSimb):
            if bits[i] == 1:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            elif bits[i] == 2:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2
            elif bits[i] == 3:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s3
            else:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s4

    return (senal,t2,bits)

def senalAleatoriaMasSimbolos(simbolos, tSimb, nMuestrasSimb, nroSimb, nTotalSimb):
    """
    Función que genera la señal aleatoria para señales de 8 o 16 símbolos (8-PSK y 16QAM).

    :param simbolos: Vector con los símbolos de la señal.
    :param tSimb:
    :param nMuestrasSimb:
    :param nroSimb:
    :param nTotalSimb:
    :return: Senal: Arreglo con la señal en tiempo / t2: Vector tiempo de la señal en tiempo. /Bits: Vector con los números aleatorios que generan la señal.
    """
    nMuestrasSenal = nTotalSimb * nMuestrasSimb

    senal = np.empty(nMuestrasSenal)
    t2 = np.linspace(0, tSimb * nTotalSimb, nMuestrasSenal)

    if nroSimb == 8:
        s1, s2, s3, s4, s5, s6, s7, s8 = simbolos

        bits = np.random.randint(8, size=nTotalSimb)

        for i in range(nTotalSimb):
            if bits[i] == 1:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            elif bits[i] == 2:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2
            elif bits[i] == 3:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s3
            elif bits[i] == 4:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s4
            elif bits[i] == 5:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s5
            elif bits[i] == 6:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s6
            elif bits[i] == 7:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s7
            else:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s8

    if nroSimb == 16:
        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16 = simbolos

        bits = np.random.randint(16, size=nTotalSimb)
        for i in range(nTotalSimb):
            if bits[i] == 1:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            elif bits[i] == 2:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2
            elif bits[i] == 3:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s3
            elif bits[i] == 4:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s4
            elif bits[i] == 5:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s5
            elif bits[i] == 6:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s6
            elif bits[i] == 7:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s7
            elif bits[i] == 8:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s8
            elif bits[i] == 9:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s9
            elif bits[i] == 10:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s10
            elif bits[i] ==11:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s11
            elif bits[i] == 12:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s12
            elif bits[i] == 13:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s13
            elif bits[i] == 14:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s14
            elif bits[i] == 15:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s15
            else:
                senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s16

    return (senal,t2,bits)

def calcularAnchoBanda(tipoOnda, fSimb, nroSimb, freqs = [0,0,0,0], tipoSenalBBPB = 1):
    """
    Esta función calcula el ancho de banda práctico de la señal, a partir de los símbolos que la compone.

    :param tipoOnda: Vector con los tipo de onda de cada símbolo.
    :param fSimb: Frecuencia de símbolo.
    :param nroSimb: Número de símbolos que compone la señal.
    :param freqs: Vector con las frecuencia de portadora de la señal.
    :param tipoSenalBBPB: Flag que indica si la señal es bandabase o pasabanda.
    :return: Ancho de banda práctico de la señal.
    """

    # senalBBPB = 1 Bandabase, senalBBPB = 2 Pasabanda, senalBBPB = 0 ambas.
    tipoOnda1,tipoOnda2,tipoOnda3,tipoOnda4 = tipoOnda

    #Si la señal es Pasabanda (opción 2 o 0) organizo las frecuencias.
    if tipoSenalBBPB != 1:
        frecuencias = [*set(freqs)] #quita los elementos repetidos

        for i in range(len(frecuencias)):
            if frecuencias[i]==0:
                frecuencias.pop(i)
                break

        frecuencias.sort()
        numFreq = len(frecuencias)

    if nroSimb == 2:
        anchoBanda = fSimb
        if tipoOnda1==2 or tipoOnda1==3 or tipoOnda1==6 or tipoOnda2==2 or tipoOnda2==3 or tipoOnda2==6:
            anchoBanda = 2 * fSimb
        if tipoOnda1==5 or tipoOnda1==7 or tipoOnda2==5 or tipoOnda2==7:
            anchoBanda = 4 * fSimb


    elif nroSimb ==3:
        anchoBanda = fSimb
        if tipoOnda1==2 or tipoOnda1==3 or tipoOnda1==6 or tipoOnda2==2 or tipoOnda2==3 or tipoOnda2==6 or tipoOnda3==2 or tipoOnda3==3 or tipoOnda3==6:
            anchoBanda = 2 * fSimb
        if tipoOnda1==5 or tipoOnda1==7 or tipoOnda2==5 or tipoOnda2==7 or tipoOnda3==5 or tipoOnda3==7:
            anchoBanda = 4 * fSimb

    else:
        anchoBanda = fSimb
        if tipoOnda1==2 or tipoOnda1==3 or tipoOnda1==6 or tipoOnda2==2 or tipoOnda2==3 or tipoOnda2==6 or tipoOnda3==2 or tipoOnda3==3 or tipoOnda3==6 or tipoOnda4==2 or tipoOnda4==3 or tipoOnda4==6:
            anchoBanda = 2 * fSimb
        if tipoOnda1==5 or tipoOnda1==7 or tipoOnda2==5 or tipoOnda2==7 or tipoOnda3==5 or tipoOnda3==7 or tipoOnda4==5 or tipoOnda4==7:
            anchoBanda = 4 * fSimb

    if tipoSenalBBPB == 2:
        if numFreq == 1:
            anchoBanda = 2 * anchoBanda
        else:
            anchoBanda = (frecuencias[1]-frecuencias[0]) + (2*anchoBanda)

    if tipoSenalBBPB == 0:
        anchoBanda = frecuencias[0]+anchoBanda

    return anchoBanda

def senalBandabasePasabanda(s1, s2, s3, s4, nroSimb, fSample, nMuestrasSimb):
    """
    Función que devuelve un flag para conocer si la señal es bandabase, pasabanda o ambas.

    :param s1: Símbolo 1
    :param s2: Símbolo 2
    :param s3: Símbolo 3
    :param s4: Símbolo 4
    :param nroSimb: Número de símbolos que componen la señal.
    :param fSample: Frecuencia de muestreo.
    :param nMuestrasSimb: Número de muestras en un símbolo.
    :return: 1 si la señal es bandabase, 2 si es pasabanda o 0 si es bandabase y pasabanda.
    """
    if nroSimb == 2:
        s1V=esCoseno(s1,fSample)

        E = (nMuestrasSimb / fSample) * np.mean(np.multiply(s2, s2))
        if E != 0:
            s2V = esCoseno(s2, fSample)
        else:
            s2V = s1V

        #print('s1V '+str(s1V))
        #print('s2V '+str(s2V))

        if (s1V+s2V) == 2:
            return 2
        elif (s1V+s2V) == 0:
            return 1
        else:
            return 0

    elif nroSimb == 3:
        s1V=esCoseno(s1,fSample)

        E = (nMuestrasSimb / fSample) * np.mean(np.multiply(s2, s2))
        if E != 0:
            s2V = esCoseno(s2, fSample)
        else:
            s2V = s1V

        E = (nMuestrasSimb / fSample) * np.mean(np.multiply(s3, s3))
        if E != 0:
            s3V = esCoseno(s3, fSample)
        else:
            s3V = s2V

        #print('s1V '+str(s1V))
        #print('s2V '+str(s2V))
        #print('s3V '+str(s3V))


        if (s1V+s2V+s3V) == 3:
            return 2
        elif (s1V+s2V+s3V) == 0:
            return 1
        else:
            return 0

    elif nroSimb == 4:
        s1V=esCoseno(s1,fSample)

        E = (nMuestrasSimb / fSample) * np.mean(np.multiply(s2, s2))
        if E != 0:
            s2V = esCoseno(s2, fSample)
        else:
            s2V = s1V

        E = (nMuestrasSimb / fSample) * np.mean(np.multiply(s3, s3))
        if E != 0:
            s3V = esCoseno(s3, fSample)
        else:
            s3V = s2V

        E = (nMuestrasSimb / fSample) * np.mean(np.multiply(s4, s4))
        if E != 0:
            s4V = esCoseno(s4, fSample)
        else:
            s4V = s3V

        #print('s1V '+str(s1V))
        #print('s2V '+str(s2V))
        #print('s3V '+str(s3V))
        #s4V = esCosenoTest(s4, fSample)
        #print('s4V '+str(s4V))


        if (s1V+s2V+s3V+s4V) == 4:
            return 2
        elif (s1V+s2V+s3V+s4V) == 0:
            return 1
        else:
            return 0

    else:
        return 2

def verificarDelta(DEP, senalBBPB, numFreq):
    """
    Función que detecta aproximadamente la presencia de picos en la DEP.

    :param DEP: Arreglo con la DEP de la señal.
    :param senalBBPB: Flag que indica si la señal es pasabanda o bandabase.
    :param numFreq: Número de frecuencias de portadora (0, 1 o 2)
    :return: True si hay deltas, False caso contrario.
    """

    corte = find_peaks(DEP, height=0.99,width=1)
    indexDelta = 0

    if senalBBPB==1:
        if len(corte[0])==1:
            indexDelta = corte[0][0]
            return (True,indexDelta)
        else:
            return (False,indexDelta)

    elif senalBBPB==2:
        if len(corte[0]) == 2 or len(corte[0]) == 4:
            indexDelta = corte[0][0]
            return (True,indexDelta)
        else:
            return (False,indexDelta)

    else:
        if numFreq == 1:
            if len(corte[0]) == 3:
                indexDelta = corte[0][0]
                return (True,indexDelta)
            else:
                return (False,indexDelta)
        else:
            if len(corte[0]) == 5:
                indexDelta = corte[0][0]
                return (True,indexDelta)
            else:
                return (False,indexDelta)

def distancia(xa, ya, xb, yb):
    """
    Función que devuelve la distancia entre dos puntos con coordenadas (xa,ya) y (xb,yb)

    :param xa: Coordenada Xa
    :param ya: Coordenada Ya
    :param xb: Coordenada Xb
    :param yb: Coordenada Yb
    :return: Distancia entre los dos puntos.
    """

    d = math.sqrt(math.pow(xa-xb, 2) + math.pow(ya-yb, 2))
    return d

def expresionEta(dmin, nroSimb, nDmin, nTotalSimb, E, nivelRuido):
    """
    Esta función obtiene los 3 niveles de ruido (eta) para las características dadas de la señal.

    :param dmin: Distancia mínima en el diagrama de constelación.
    :param nroSimb: Número de símbolos que compone la señal.
    :param nDmin: Número de veces que la distancia mínima está presente en la constelación.
    :param nTotalSimb: Número total de símbolos en la señal en tiempo.
    :param E: Energía promedio.
    :param nivelRuido: Nivel de ruido ingresado por el usuario.
    :return: X = nivel de eta ingresado por el usuario, Y = probabilidad de error para el caso simulado. etaGraf y PeGraf ejes para la gráfica de probabilidad de error.
    """

    peMin = 1 / nTotalSimb
    peMax = (0.5 * nDmin / nroSimb) - 0.15

    if (0.5 * nDmin / nroSimb) >= 1:
        peMax = 0.5

    etaMin = 0.5 * math.pow(dmin / (qfuncinv((nroSimb / nDmin) * (peMin))), 2)
    etaMax = 0.5 * math.pow(dmin / (qfuncinv((nroSimb / nDmin) * (peMax))), 2)

    ejeXmax = 10 * math.log10(E / etaMin)
    ejeXmin = 10 * math.log10(E / etaMax)

    ejeXpe3 = (ejeXmin + (1 / 10) * ejeXmax) / (1 + (1 / 10))
    ejeXpe2 = (ejeXmin + (7 / 4) * ejeXmax) / (1 + (7 / 4))
    ejeXpe1 = (ejeXmin + (10) * ejeXmax) / (1 + (10))

    eta = {
        0: 0,
        1: E * math.pow(10, -ejeXpe1 / 10),
        2: E * math.pow(10, -ejeXpe2 / 10),
        3: E * math.pow(10, -ejeXpe3 / 10),
    }

    X = eta[nivelRuido]

    try:
        Y = (nDmin / nroSimb) * qfunc(dmin / math.sqrt(2*X))
    except:
        Y = 0

    etaGraf = np.linspace(etaMin, etaMax, 15000)
    peGraf = (nDmin / nroSimb) * qfunc(dmin / np.sqrt(2*etaGraf))

    return (X, Y, etaGraf, peGraf, dmin, nDmin)

def obtenerEta(coord,nroSimb, E, nTotalSimb,nivelRuido):
    """
    Esta función obtiene la distancia mínima y el número de veces que esa distancia está presente en el diagrama de constelación.

    :param coord: Coordenadas de los símbolos en el diagrama de constelación.
    :param nroSimb: Número de símbolos que compone la señal.
    :param E: Energía promedio.
    :param nTotalSimb: Número total de símbolos de la señal en tiempo.
    :param nivelRuido: Nivel de ruido ingresado por el usuario.

    :return: eta
    """

    if nroSimb == 2:
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]

        d12 = distancia(x1, y1, x2, y2)

        dmin = d12
        nDmin = 2
        eta = expresionEta(dmin, nroSimb, nDmin, nTotalSimb, E, nivelRuido)

    elif nroSimb == 3:
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]
        x3 = coord[4]
        y3 = coord[5]


        d12 = distancia(x1, y1, x2, y2)
        d13 = distancia(x1, y1, x3, y3)
        d23 = distancia(x2, y2, x3, y3)

        """
        print("x1, y1:", x1, y1)
        print("x2, y2:", x2, y2)
        print("x3, y3:", x3, y3)
        print("D12: ", d12)
        print("D13: ", d13)
        print("D23: ", d23)
        """

        cont=0
        dmin = np.amin(np.array([d12,d13,d23]))

        if math.isclose(dmin,d12, rel_tol=1*(10**(-2))) == True:
            cont=cont+1
        if math.isclose(dmin,d13, rel_tol=1*(10**(-2))) == True:
            cont=cont+1
        if math.isclose(dmin,d23, rel_tol=1*(10**(-2))) == True:
            cont=cont+1
        nDmin = cont*2

        eta = expresionEta(dmin, nroSimb, nDmin, nTotalSimb, E, nivelRuido)

    elif nroSimb == 4:
        x1,y1,x2,y2,x3,y3,x4,y4 = coord

        d12 = distancia(x1, y1, x2, y2)
        d13 = distancia(x1, y1, x3, y3)
        d14 = distancia(x1, y1, x4, y4)
        d23 = distancia(x2, y2, x3, y3)
        d24 = distancia(x2, y2, x4, y4)
        d34 = distancia(x3, y3, x4, y4)

        cont = 0
        dmin = np.amin(np.array([d12, d13, d14, d23, d24, d34]))

        if math.isclose(dmin, d12) == True:
            cont = cont + 1
        if math.isclose(dmin, d13) == True:
            cont = cont + 1
        if math.isclose(dmin, d14) == True:
            cont = cont + 1
        if math.isclose(dmin, d23) == True:
            cont = cont + 1
        if math.isclose(dmin, d24) == True:
            cont = cont + 1
        if math.isclose(dmin, d34) == True:
            cont = cont + 1
        nDmin = cont*2
        eta = expresionEta(dmin, nroSimb, nDmin, nTotalSimb, E, nivelRuido)

    elif nroSimb == 8:
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]

        d12 = distancia(x1, y1, x2, y2)

        dmin = d12

        # print('La distancia minima ' + str(dmin))

        nDmin = 16

        eta = expresionEta(dmin, nroSimb, nDmin, nTotalSimb, E, nivelRuido)

    else:
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]

        d12 = distancia(x1, y1, x2, y2)

        dmin = d12

        # print('La distancia minima ' + str(dmin))

        nDmin = 48

        eta = expresionEta(dmin, nroSimb, nDmin, nTotalSimb, E, nivelRuido)

    return eta

def calcularPe(nTotalSimb,rec,bits):
    """
    Esta función calcula el valor de la probabilidad de error como la relación entre el número de símbolos errados y la cantidad total de símbolos transmitidos.

    :param nTotalSimb: Número total de símbolos.
    :param rec: Bits recibidos.
    :param bits: Bits transmitidos.

    :return: pe = probabilidad de error, primerError = ubicación del primer error, cont = número de errores que ocurrieron.
    """

    # Se calcula la Probabilidad de Error como nErrores/NSimbolosTotales
    primerError = 0
    cont = 0
    for i in range(nTotalSimb):
        if rec[i] - bits[i] != 0:
            # Se guarda la posición del primer error que sucede
            if cont == 0:
                primerError = i
            cont = cont + 1

    pe = cont / nTotalSimb

    return (pe,primerError,cont)

def deteccionDistancia(coord, s1, s2, s3, s4, nroSimb, detU1, detU2, nTotalSimb, nMuestrasSimb):
    """
    Esta función devuelve la señal y los bits detectados utilizando las proyecciones de los símbolos sobre las bases y un criterio de distancia

    :param coord: Coordenada de los símbolos originales.
    :param s1: Símbolo 1.
    :param s2: Símbolo 2.
    :param s3: Símbolo 3.
    :param s4: Símbolo 4.
    :param nroSimb: Número de símbolos de la señal.
    :param detU1: Vector con las proyección de los símbolos con la base U1.
    :param detU2: Vector con las proyección de los símbolos con la base U2.
    :param nTotalSimb: Número total de símbolos en la señal en tiempo.
    :param nMuestrasSimb: Número de muestras por símbolo.
    :return: Señal en tiempo detectada y los bits detectados.
    """
    nMuestrasSenal = nTotalSimb * nMuestrasSimb
    rec = np.empty(nTotalSimb)
    senalDet = np.empty(nMuestrasSenal)

    if nroSimb == 2:
        x1,y1,x2,y2 = coord

        for i in range(nTotalSimb):
            d1 = distancia(x1, y1, detU1[i], detU2[i])
            d2 = distancia(x2, y2, detU1[i], detU2[i])
            distancias = [d1,d2]
            distancias = np.array(distancias)
            distanciaminima = np.argmin(distancias)
            if distanciaminima == 0:
                rec[i] = 1
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            else:
                rec[i] = 0
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2

    if nroSimb == 3:
        x1,y1,x2,y2,x3,y3 = coord

        for i in range(nTotalSimb):
            d1 = distancia(x1, y1, detU1[i], detU2[i])
            d2 = distancia(x2, y2, detU1[i], detU2[i])
            d3 = distancia(x3, y3, detU1[i], detU2[i])
            distancias = [d1,d2,d3]
            distancias = np.array(distancias)
            distanciaminima = np.argmin(distancias)
            if distanciaminima == 0:
                rec[i] = 1
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            elif distanciaminima == 1:
                rec[i] = 2
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2
            else:
                rec[i] = 0
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s3

    if nroSimb == 4:
        x1,y1,x2,y2,x3,y3,x4,y4 = coord

        for i in range(nTotalSimb):
            d1 = distancia(x1, y1, detU1[i], detU2[i])
            d2 = distancia(x2, y2, detU1[i], detU2[i])
            d3 = distancia(x3, y3, detU1[i], detU2[i])
            d4 = distancia(x4, y4, detU1[i], detU2[i])
            distancias = [d1,d2,d3,d4]
            distancias = np.array(distancias)
            distanciaminima = np.argmin(distancias)
            if distanciaminima == 0:
                rec[i] = 1
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            elif distanciaminima == 1:
                rec[i] = 2
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2
            elif distanciaminima == 2:
                rec[i] = 3
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s3
            else:
                rec[i] = 0
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s4
    return (senalDet, rec)

def deteccionDistanciaMasSimbolos(coord, simbolos, nroSimb, detU1, detU2, nTotalSimb, nMuestrasSimb):
    """
    Esta función devuelve la señal y los bits detectados utilizando las proyecciones de los símbolos sobre las bases y un criterio de distancia, para señales con 8 y 16 símbolos.


    :param coord: Coordenada de los símbolos originales.
    :param simbolos: Vector con los símbolos de la señal.
    :param nroSimb: Número de símbolos de la señal.
    :param detU1: Vector con las proyección de los símbolos con la base U1.
    :param detU2: Vector con las proyección de los símbolos con la base U2.
    :param nTotalSimb: Número total de símbolos en la señal en tiempo.
    :param nMuestrasSimb: Número de muestras por símbolo.
    :return: Señal en tiempo detectada y los bits detectados.
    """
    nMuestrasSenal = nTotalSimb * nMuestrasSimb
    rec = np.empty(nTotalSimb)
    senalDet = np.empty(nMuestrasSenal)

    s1 = simbolos[0]
    s2 = simbolos[1]
    s3 = simbolos[2]
    s4 = simbolos[3]
    s5 = simbolos[4]
    s6 = simbolos[5]
    s7 = simbolos[6]
    s8 = simbolos[7]

    if nroSimb == 8:
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]
        x3 = coord[4]
        y3 = coord[5]
        x4 = coord[6]
        y4 = coord[7]
        x5 = coord[8]
        y5 = coord[9]
        x6 = coord[10]
        y6 = coord[11]
        x7 = coord[12]
        y7 = coord[13]
        x8 = coord[14]
        y8 = coord[15]

        for i in range(nTotalSimb):
            d1 = distancia(x1, y1, detU1[i], detU2[i])
            d2 = distancia(x2, y2, detU1[i], detU2[i])
            d3 = distancia(x3, y3, detU1[i], detU2[i])
            d4 = distancia(x4, y4, detU1[i], detU2[i])
            d5 = distancia(x5, y5, detU1[i], detU2[i])
            d6 = distancia(x6, y6, detU1[i], detU2[i])
            d7 = distancia(x7, y7, detU1[i], detU2[i])
            d8 = distancia(x8, y8, detU1[i], detU2[i])

            distancias = [d1, d2, d3, d4, d5, d6, d7, d8]
            distancias = np.array(distancias)
            distanciaminima = np.argmin(distancias)
            if distanciaminima == 0:
                rec[i] = 1
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            elif distanciaminima == 1:
                rec[i] = 2
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2
            elif distanciaminima == 2:
                rec[i] = 3
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s3
            elif distanciaminima == 3:
                rec[i] = 4
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s4
            elif distanciaminima == 4:
                rec[i] = 5
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s5
            elif distanciaminima == 5:
                rec[i] = 6
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s6
            elif distanciaminima == 6:
                rec[i] = 7
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s7
            else:
                rec[i] = 0
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s8

    if nroSimb == 16:
        s9 = simbolos[8]
        s10 = simbolos[9]
        s11 = simbolos[10]
        s12 = simbolos[11]
        s13 = simbolos[12]
        s14 = simbolos[13]
        s15 = simbolos[14]
        s16 = simbolos[15]

        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]
        x3 = coord[4]
        y3 = coord[5]
        x4 = coord[6]
        y4 = coord[7]
        x5 = coord[8]
        y5 = coord[9]
        x6 = coord[10]
        y6 = coord[11]
        x7 = coord[12]
        y7 = coord[13]
        x8 = coord[14]
        y8 = coord[15]
        x9 = coord[16]
        y9 = coord[17]
        x10 = coord[18]
        y10 = coord[19]
        x11 = coord[20]
        y11 = coord[21]
        x12 = coord[22]
        y12 = coord[23]
        x13 = coord[24]
        y13 = coord[25]
        x14 = coord[26]
        y14 = coord[27]
        x15 = coord[28]
        y15 = coord[29]
        x16 = coord[30]
        y16 = coord[31]

        for i in range(nTotalSimb):
            d1 = distancia(x1, y1, detU1[i], detU2[i])
            d2 = distancia(x2, y2, detU1[i], detU2[i])
            d3 = distancia(x3, y3, detU1[i], detU2[i])
            d4 = distancia(x4, y4, detU1[i], detU2[i])
            d5 = distancia(x5, y5, detU1[i], detU2[i])
            d6 = distancia(x6, y6, detU1[i], detU2[i])
            d7 = distancia(x7, y7, detU1[i], detU2[i])
            d8 = distancia(x8, y8, detU1[i], detU2[i])
            d9 = distancia(x9, y9, detU1[i], detU2[i])
            d10 = distancia(x10, y10, detU1[i], detU2[i])
            d11 = distancia(x11, y11, detU1[i], detU2[i])
            d12 = distancia(x12, y12, detU1[i], detU2[i])
            d13 = distancia(x13, y13, detU1[i], detU2[i])
            d14 = distancia(x14, y14, detU1[i], detU2[i])
            d15 = distancia(x15, y15, detU1[i], detU2[i])
            d16 = distancia(x16, y16, detU1[i], detU2[i])

            distancias = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16]
            distancias = np.array(distancias)
            distanciaminima = np.argmin(distancias)
            if distanciaminima == 0:
                rec[i] = 1
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s1
            elif distanciaminima == 1:
                rec[i] = 2
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s2
            elif distanciaminima == 2:
                rec[i] = 3
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s3
            elif distanciaminima == 3:
                rec[i] = 4
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s4
            elif distanciaminima == 4:
                rec[i] = 5
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s5
            elif distanciaminima == 5:
                rec[i] = 6
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s6
            elif distanciaminima == 6:
                rec[i] = 7
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s7
            elif distanciaminima == 7:
                rec[i] = 8
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s8
            elif distanciaminima == 8:
                rec[i] = 9
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s9
            elif distanciaminima == 9:
                rec[i] = 10
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s10
            elif distanciaminima == 10:
                rec[i] = 11
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s11
            elif distanciaminima == 11:
                rec[i] = 12
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s12
            elif distanciaminima == 12:
                rec[i] = 13
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s13
            elif distanciaminima == 13:
                rec[i] = 14
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s14
            elif distanciaminima == 14:
                rec[i] = 15
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s15
            else:
                rec[i] = 0
                senalDet[nMuestrasSimb * i:nMuestrasSimb * (i + 1)] = s16

    return (senalDet, rec)

def convertirFase(fase):
    """
    Esta función convierte la fase string en float, principalmente para el manejo de la palabra "pi"

    :param fase: Fase en String.
    :return: Fase en float.
    """

    fase = fase.lower()  #todoen minusculas
    fase = "".join(fase.split())  # quitar cualquier espacio
    division = False

    if "-pi" in fase:
        fase = fase.replace('-pi', '-' + str(math.pi))

    elif "pi" in fase:
        fase = fase.replace('pi', ' ' + str(math.pi))

    if "/" in fase:
        fase = fase.replace('/', ' ')
        division = True

    if "*" in fase:
        fase = fase.replace("*", "")

    if "(" in fase:
        fase = fase.replace("(", "")

    if ")" in fase:
        fase = fase.replace(")", "")

    if "," in fase:
        fase = fase.replace(",", ".")

    fase = fase.strip()

    # Convierto en float
    if " " in fase:
        fase = fase.split(' ')
        if division and len(fase) == 3:
            faseFloat = (float(fase[0]) * float(fase[1])) / float(fase[2])
        elif division and len(fase) == 2:
            faseFloat = float(fase[0]) / float(fase[1])
        elif not (division) and len(fase) == 2:
            faseFloat = float(fase[0]) * float(fase[1])
    else:
        faseFloat = float(fase)

    return faseFloat

def factorCorrelacion(E0, E1, s0, s1, nMuestrasSimb, fSample):
    """
    Esta función devuelve el factor de correlación lambda entre dos símbolos.

    :param E0: Energía del primer símbolo.
    :param E1: Energía del segundo símbolo.
    :param s0: Arreglo con el primer símbolo.
    :param s1: Arreglo con el segundo símbolo.
    :param nMuestrasSimb: Número de muestras por símbolo.
    :param fSample: Frecuencia de muestreo.
    :return: Factor lambda de correlación.
    """

    if E0==0 or E1==0:
        factorLambda = 0
    else:
        factorLambda = (1/(math.sqrt(E0*E1))) * (nMuestrasSimb / fSample) * np.mean(np.multiply(s0, s1))
    return factorLambda

def numeroCiclosEnteros(freqPortadora, freqSimbolo, tipoOnda):
    """
    Esta función calcula si la combinación entre Frecuencia de Portadora y Tiempo de Símbolo resulta en un símbolo con un número entero de ciclos.

    :param freqPortadora: Frecuencia de portadora.
    :param freqSimbolo: Frecuencia de símbolo.
    :param tipoOnda: Tipo de onda del símbolo, para saber si es de duración variable o completa.
    :return: True si tiene un número de ciclos entero, Falso caso contrario.
    """

    #tSimb = 1.3 es diferente
    if math.isclose(0.769230769231, freqSimbolo):
        if tipoOnda == 4:
            resto = math.fmod(freqPortadora, round(freqSimbolo, 10))
        else:
            resto = math.fmod(freqPortadora, round(4 * freqSimbolo, 10))

        if math.isclose(resto, 0, abs_tol=0.001):
            return True
        else:
            return False
    else:
        x = freqPortadora
        if tipoOnda == 4:
            y = round(freqSimbolo, 16)
        else:
            y = round(freqSimbolo * 4, 16)
        div = x / y

        if div.is_integer():
            return True
        else:
            return False

def ortogonalPolarProporcional(x_ortogonal, x_polar, x_proporcional, factorLambda):
    """
    Función que define a partir del factor de correlación lambda si dos símbolos cumplen alguna relación de ortogonalidad, polaridad o proporcionalidad.

    :param x_ortogonal: Boolean de ortogonalidad.
    :param x_polar: Boolean de polaridad.
    :param x_proporcional: Boolean de proporcionalidad.
    :param factorLambda: Factor lambda de correlación.
    :return: Booleans de ortogonalidad, proporcionalidad y polaridad.
    """

    if math.isclose(factorLambda, 0, abs_tol=0.01):
        x_ortogonal = True
    elif math.isclose(factorLambda, -1, abs_tol=0.01):
        x_polar = True
    elif math.isclose(factorLambda, 1, abs_tol=0.01):
        x_proporcional = True

    return (x_ortogonal,x_polar, x_proporcional)

def resultadosNumericos(simbolos_senal, nroSimb, nMuestrasSimb, fSample, fSimb, tipoOndas, frecuencias):
    """
    Esta función calcula los distintos resultados númericos presentes en la simulación.

    :param simbolos_senal: Arreglo con los símbolos de la señal.
    :param nroSimb: Número de símbolos en la señal.
    :param nMuestrasSimb: Número de muestras en un símbolo.
    :param fSample: Frecuencia de muestreo.
    :param fSimb: Frecuencia de símbolo.
    :param tipoOndas: Vector con los tipos de ondas presentes en la señal.
    :param frecuencias: Vector con las frecuencias de portadora presentes en la señal.
    :return: Las relaciones de Polaridad, Proporcionalidad y Ortogonalidad, la energía de los símbolos y si cumplen la relación de ciclos enteros.
    """
    if nroSimb == 2:
        s1,s2,s3,s4 = simbolos_senal
        tipoOndaS1, tipoOndaS2, tipoOndaS3, tipoOndaS4 = tipoOndas
        freqS1, freqS2, freqs3, freqs4 = frecuencias

        s1s2_ortogonal, s1s2_polar, s1s2_proporcional = False, False, False
        numCiclosEnterosS1,numCiclosEnterosS2 = False, False

        #Energia de los simbolos
        E1 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s1, s1))
        E2 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s2, s2))

        factorLambda = factorCorrelacion(E1,E2,s1,s2,nMuestrasSimb,fSample)

        if math.isclose(factorLambda,0,abs_tol=0.01):
            s1s2_ortogonal = True
        elif math.isclose(factorLambda,-1,abs_tol=0.01):
            s1s2_polar = True
        elif math.isclose(factorLambda,1,abs_tol=0.01):
            s1s2_proporcional = True

        if tipoOndaS1 == 4 or tipoOndaS1 ==6:
            numCiclosEnterosS1 = numeroCiclosEnteros(freqS1,fSimb,tipoOndaS1)

        if tipoOndaS2 == 4 or tipoOndaS2 ==6:
            numCiclosEnterosS2 = numeroCiclosEnteros(freqS2,fSimb,tipoOndaS2)

        ortogonalidad = (s1s2_ortogonal)
        polaridad = (s1s2_polar)
        proporcionalidad = (s1s2_proporcional)

        energia = (E1,E2)
        numCiclos = (numCiclosEnterosS1,numCiclosEnterosS2)

        return (ortogonalidad,polaridad,proporcionalidad,energia,numCiclos)

    elif nroSimb == 3:
        s1,s2,s3,s4 = simbolos_senal
        tipoOndaS1, tipoOndaS2, tipoOndaS3, tipoOndaS4 = tipoOndas
        freqS1, freqS2, freqS3, freqS4 = frecuencias
        numCiclosEnterosS1,numCiclosEnterosS2,numCiclosEnterosS3 = False, False, False

        s1s2_ortogonal, s1s2_polar, s1s2_proporcional = False, False, False
        s1s3_ortogonal, s1s3_polar, s1s3_proporcional = False, False, False
        s2s3_ortogonal, s2s3_polar, s2s3_proporcional = False, False, False

        #Energia de los simbolos
        E1 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s1, s1))
        E2 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s2, s2))
        E3 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s3, s3))

        #S1 Y S2
        factorLambda = factorCorrelacion(E1,E2,s1,s2,nMuestrasSimb,fSample)
        if math.isclose(factorLambda,0,abs_tol=0.01):
            s1s2_ortogonal = True
        elif math.isclose(factorLambda,-1,abs_tol=0.01):
            s1s2_polar = True
        elif math.isclose(factorLambda,1,abs_tol=0.01):
            s1s2_proporcional = True

        #S1 Y S3
        factorLambda = factorCorrelacion(E1,E3,s1,s3,nMuestrasSimb,fSample)
        if math.isclose(factorLambda,0,abs_tol=0.01):
            s1s3_ortogonal = True
        elif math.isclose(factorLambda,-1,abs_tol=0.01):
            s1s3_polar = True
        elif math.isclose(factorLambda,1,abs_tol=0.01):
            s1s3_proporcional = True

        #S2 Y S3
        factorLambda = factorCorrelacion(E2,E3,s2,s3,nMuestrasSimb,fSample)
        if math.isclose(factorLambda,0,abs_tol=0.01):
            s2s3_ortogonal = True
        elif math.isclose(factorLambda,-1,abs_tol=0.01):
            s2s3_polar = True
        elif math.isclose(factorLambda,1,abs_tol=0.01):
            s2s3_proporcional = True


        #Verificar si los simbolos tienen ciclos enteros
        if tipoOndaS1 == 4 or tipoOndaS1 ==6:
            numCiclosEnterosS1 = numeroCiclosEnteros(freqS1, fSimb, tipoOndaS1)

        if tipoOndaS2 == 4 or tipoOndaS2 ==6:
            numCiclosEnterosS2 = numeroCiclosEnteros(freqS2, fSimb, tipoOndaS2)

        if tipoOndaS3 == 4 or tipoOndaS3 ==6:
            numCiclosEnterosS3 = numeroCiclosEnteros(freqS3, fSimb, tipoOndaS3)



        ortogonalidad = (s1s2_ortogonal, s1s3_ortogonal, s2s3_ortogonal)
        polaridad = (s1s2_polar,s1s3_polar,s2s3_polar)
        proporcionalidad = (s1s2_proporcional,s1s3_proporcional,s2s3_proporcional)

        energia = (E1,E2,E3)
        numCiclos = (numCiclosEnterosS1,numCiclosEnterosS2,numCiclosEnterosS3)

        return (ortogonalidad,polaridad,proporcionalidad,energia,numCiclos)

    elif nroSimb == 4:
        s1, s2, s3, s4 = simbolos_senal
        tipoOndaS1, tipoOndaS2, tipoOndaS3, tipoOndaS4 = tipoOndas
        freqS1, freqS2, freqS3, freqS4 = frecuencias
        numCiclosEnterosS1,numCiclosEnterosS2,numCiclosEnterosS3, numCiclosEnterosS4 = False, False, False, False


        s1s2_ortogonal, s1s2_polar, s1s2_proporcional = False, False, False
        s1s3_ortogonal, s1s3_polar, s1s3_proporcional = False, False, False
        s1s4_ortogonal, s1s4_polar, s1s4_proporcional = False, False, False
        s2s3_ortogonal, s2s3_polar, s2s3_proporcional = False, False, False
        s2s4_ortogonal, s2s4_polar, s2s4_proporcional = False, False, False
        s3s4_ortogonal, s3s4_polar, s3s4_proporcional = False, False, False

        # Energia de los simbolos
        E1 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s1, s1))
        E2 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s2, s2))
        E3 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s3, s3))
        E4 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s4, s4))


        # S1 Y S2
        factorLambda = factorCorrelacion(E1, E2, s1, s2, nMuestrasSimb, fSample)
        if math.isclose(factorLambda, 0, abs_tol=0.01):
            s1s2_ortogonal = True
        elif math.isclose(factorLambda, -1, abs_tol=0.01):
            s1s2_polar = True
        elif math.isclose(factorLambda, 1, abs_tol=0.01):
            s1s2_proporcional = True

        # S1 Y S3
        factorLambda = factorCorrelacion(E1, E3, s1, s3, nMuestrasSimb, fSample)
        if math.isclose(factorLambda, 0, abs_tol=0.01):
            s1s3_ortogonal = True
        elif math.isclose(factorLambda, -1, abs_tol=0.01):
            s1s3_polar = True
        elif math.isclose(factorLambda, 1, abs_tol=0.01):
            s1s3_proporcional = True

        # S1 Y S4
        factorLambda = factorCorrelacion(E1, E4, s1, s4, nMuestrasSimb, fSample)
        if math.isclose(factorLambda, 0, abs_tol=0.01):
            s1s4_ortogonal = True
        elif math.isclose(factorLambda, -1, abs_tol=0.01):
            s1s4_polar = True
        elif math.isclose(factorLambda, 1, abs_tol=0.01):
            s1s4_proporcional = True

        # S2 Y S3
        factorLambda = factorCorrelacion(E2, E3, s2, s3, nMuestrasSimb, fSample)
        if math.isclose(factorLambda, 0, abs_tol=0.01):
            s2s3_ortogonal = True
        elif math.isclose(factorLambda, -1, abs_tol=0.01):
            s2s3_polar = True
        elif math.isclose(factorLambda, 1, abs_tol=0.01):
            s2s3_proporcional = True

        # S2 Y S4
        factorLambda = factorCorrelacion(E2, E4, s2, s4, nMuestrasSimb, fSample)
        if math.isclose(factorLambda, 0, abs_tol=0.01):
            s2s4_ortogonal = True
        elif math.isclose(factorLambda, -1, abs_tol=0.01):
            s2s4_polar = True
        elif math.isclose(factorLambda, 1, abs_tol=0.01):
            s2s4_proporcional = True


        # S3 Y S4
        factorLambda = factorCorrelacion(E3, E4, s3, s4, nMuestrasSimb, fSample)
        if math.isclose(factorLambda, 0, abs_tol=0.01):
            s3s4_ortogonal = True
        elif math.isclose(factorLambda, -1, abs_tol=0.01):
            s3s4_polar = True
        elif math.isclose(factorLambda, 1, abs_tol=0.01):
            s3s4_proporcional = True


        # Verificar si los simbolos tienen ciclos enteros
        if tipoOndaS1 == 4 or tipoOndaS1 == 6:
            numCiclosEnterosS1 = numeroCiclosEnteros(freqS1, fSimb, tipoOndaS1)

        if tipoOndaS2 == 4 or tipoOndaS2 == 6:
            numCiclosEnterosS2 = numeroCiclosEnteros(freqS2, fSimb, tipoOndaS2)

        if tipoOndaS3 == 4 or tipoOndaS3 == 6:
            numCiclosEnterosS3 = numeroCiclosEnteros(freqS3, fSimb, tipoOndaS3)

        if tipoOndaS4 == 4 or tipoOndaS4 == 6:
            numCiclosEnterosS4 = numeroCiclosEnteros(freqS4, fSimb, tipoOndaS4)

        ortogonalidad = (s1s2_ortogonal, s1s3_ortogonal, s1s4_ortogonal,s2s3_ortogonal,s2s4_ortogonal,s3s4_ortogonal)
        polaridad = (s1s2_polar, s1s3_polar, s1s4_polar,s2s3_polar,s2s4_polar,s3s4_polar)
        proporcionalidad = (s1s2_proporcional, s1s3_proporcional, s1s4_proporcional,s2s3_proporcional,s2s4_proporcional,s3s4_proporcional)

        energia = (E1, E2, E3, E4)
        numCiclos = (numCiclosEnterosS1, numCiclosEnterosS2, numCiclosEnterosS3, numCiclosEnterosS4)

        return (ortogonalidad, polaridad, proporcionalidad, energia, numCiclos)

    elif nroSimb == 8:
        s1, s2, s3, s4, s5, s6, s7, s8  = simbolos_senal
        freqS1, freqS2, freqs3, freqs4 = frecuencias

        E1 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s1, s1))
        E2 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s2, s2))
        E3 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s3, s3))
        E4 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s4, s4))
        E5 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s5, s5))
        E6 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s6, s6))
        E7 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s7, s7))
        E8 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s8, s8))

        numCiclosEnteros = numeroCiclosEnteros(freqS1, fSimb, 4)

        ortogonalidad = 0
        polaridad = 0
        proporcionalidad = 0

        energia = (E1,E2, E3, E4, E5, E6, E7, E8)
        numCiclos = numCiclosEnteros

        return (ortogonalidad,polaridad,proporcionalidad,energia,numCiclos)

    else:
        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16  = simbolos_senal
        freqS1, freqS2, freqs3, freqs4 = frecuencias

        E1 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s1, s1))
        E2 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s2, s2))
        E3 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s3, s3))
        E4 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s4, s4))
        E5 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s5, s5))
        E6 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s6, s6))
        E7 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s7, s7))
        E8 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s8, s8))
        E9 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s9, s9))
        E10 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s10, s10))
        E11 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s11, s11))
        E12 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s12, s12))
        E13 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s13, s13))
        E14 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s14, s14))
        E15 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s15, s15))
        E16 = (nMuestrasSimb / fSample) * np.mean(np.multiply(s16, s16))

        numCiclosEnteros = numeroCiclosEnteros(freqS1, fSimb, 4)

        ortogonalidad = 0
        polaridad = 0
        proporcionalidad = 0

        energia = (E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, E13, E14, E15, E16)
        numCiclos = numCiclosEnteros

        return (ortogonalidad, polaridad, proporcionalidad, energia, numCiclos)

def coordenadas(coord, nroSimb):
    """
    Devuelve las coordenadas de forma separada.

    :param coord: Vector con las coordenadas.
    :param nroSimb: Número de símbolos en la señal.
    :return: Cada una de las coordenadas de la señal en el diagrama de constelación.
    """
    if nroSimb==2:
        s1X, s1Y, s2X, s2Y = coord

        return (s1X,s1Y,s2X,s2Y)

    elif nroSimb==3:
        s1X, s1Y, s2X, s2Y, s3X, s3Y = coord

        return (s1X,s1Y,s2X,s2Y, s3X, s3Y)


    elif nroSimb==4:
        s1X, s1Y, s2X, s2Y, s3X, s3Y, s4X, s4Y = coord

        return (s1X,s1Y,s2X,s2Y, s3X, s3Y, s4X, s4Y)