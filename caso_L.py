from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *
import numpy as np
def caso_L():
    
    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 
    
    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    kgf = 9.80665*N
    KN = 1000*N
    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa


    
    #Parametros
    L = 5.0 * m
    B = 2.0 * m
    H = 3.5 * m
    q  = 400*kgf/m**2
    F = q*L*B
    F  = F/4

    #Inicializar modelo
    ret = Reticulado()
    
    #Nodos tablero



    ret.agregar_nodo(0.0,0,100)         # Nodo 0  (punto 7)
    ret.agregar_nodo(0.0,B,100)       # Nodo 1
    ret.agregar_nodo(5.0,0,100)         # Nodo 2   
    ret.agregar_nodo(5.0,B,100)       # Nodo 3
    ret.agregar_nodo(10.0,0,100)        # Nodo 4
    ret.agregar_nodo(10.0,B,100)      # Nodo 5
    ret.agregar_nodo(15.0,0,100)        # Nodo 6
    ret.agregar_nodo(15.0,B,100)      # Nodo 7
    ret.agregar_nodo(20.0,0,100)        # Nodo 8
    ret.agregar_nodo(20.0,B,100)      # Nodo 9
    ret.agregar_nodo(25.0,0,100)        # Nodo 10
    ret.agregar_nodo(25.0,B,100)      # Nodo 11
    ret.agregar_nodo(30.0,0,100)        # Nodo 12
    ret.agregar_nodo(30.0,B,100)      # Nodo 13
    ret.agregar_nodo(35.0,0,100)        # Nodo 14
    ret.agregar_nodo(35.0,B,100)      # Nodo 15
    ret.agregar_nodo(40.0,0,100)        # Nodo 16
    ret.agregar_nodo(40.0,B,100)      # Nodo 17
    ret.agregar_nodo(45.0,0,100)        # Nodo 18
    ret.agregar_nodo(45.0,B,100)      # Nodo 19
    ret.agregar_nodo(50.0,0,100)        # Nodo 20
    ret.agregar_nodo(50.0,B,100)      # Nodo 21
    ret.agregar_nodo(55.0,0,100)        # Nodo 22
    ret.agregar_nodo(55.0,B,100)      # Nodo 23
    ret.agregar_nodo(60.0,0,100)        # Nodo 24
    ret.agregar_nodo(60.0,B,100)      # Nodo 25
    ret.agregar_nodo(65.0,0,100)        # Nodo 26
    ret.agregar_nodo(65.0,B,100)      # Nodo 27
    ret.agregar_nodo(70.0,0,100)        # Nodo 28
    ret.agregar_nodo(70.0,B,100)      # Nodo 29
    ret.agregar_nodo(75.0,0,100)        # Nodo 30
    ret.agregar_nodo(75.0,B,100)      # Nodo 31
    ret.agregar_nodo(80.0,0,100)        # Nodo 32
    ret.agregar_nodo(80.0,B,100)      # Nodo 33
    ret.agregar_nodo(85.0,0,100)        # Nodo 34
    ret.agregar_nodo(85.0,B,100)      # Nodo 35
    ret.agregar_nodo(90.0,0,100)        # Nodo 36
    ret.agregar_nodo(90.0,B,100)      # Nodo 37
    ret.agregar_nodo(95.0,0,100)        # Nodo 38
    ret.agregar_nodo(95.0,B,100)      # Nodo 39
    ret.agregar_nodo(100.0,0,100)       # Nodo 40
    ret.agregar_nodo(100.0,B,100)     # Nodo 41
    ret.agregar_nodo(105.0,0,100)       # Nodo 42
    ret.agregar_nodo(105.0,B,100)     # Nodo 43
    ret.agregar_nodo(110.0,0,100)       # Nodo 44
    ret.agregar_nodo(110.0,B,100)     # Nodo 45
    ret.agregar_nodo(115.0,0,100)       # Nodo 46
    ret.agregar_nodo(115.0,B,100)     # Nodo 47
    ret.agregar_nodo(120.0,0,100)       # Nodo 48
    ret.agregar_nodo(120.0,B,100)     # Nodo 49
    ret.agregar_nodo(125.0,0,100)       # Nodo 50
    ret.agregar_nodo(125.0,B,100)     # Nodo 51
    ret.agregar_nodo(130.0,0,100)       # Nodo 52
    ret.agregar_nodo(130.0,B,100)     # Nodo 53
    ret.agregar_nodo(135.0,0,100)       # Nodo 54
    ret.agregar_nodo(135.0,B,100)     # Nodo 55
    ret.agregar_nodo(140.0,0,100)       # Nodo 56
    ret.agregar_nodo(140.0,B,100)     # Nodo 57
    ret.agregar_nodo(145.0,0,100)       # Nodo 58
    ret.agregar_nodo(145.0,B,100)     # Nodo 59
    ret.agregar_nodo(150.0,0,100)       # Nodo 60
    ret.agregar_nodo(150.0,B,100)     # Nodo 61
    ret.agregar_nodo(155.0,0,100)       # Nodo 62
    ret.agregar_nodo(155.0,B,100)     # Nodo 63
    ret.agregar_nodo(160.0,0,100)       # Nodo 64
    ret.agregar_nodo(160.0,B,100)     # Nodo 65
    ret.agregar_nodo(165.0,0,100)       # Nodo 66
    ret.agregar_nodo(165.0,B,100)     # Nodo 67
    ret.agregar_nodo(170.0,0,100)       # Nodo 68
    ret.agregar_nodo(170.0,B,100)     # Nodo 69
    ret.agregar_nodo(175.0,0,100)       # Nodo 70
    ret.agregar_nodo(175.0,B,100)     # Nodo 71
    ret.agregar_nodo(180.0,0,100)       # Nodo 72
    ret.agregar_nodo(180.0,B,100)     # Nodo 73
    ret.agregar_nodo(185.0,0,100)       # Nodo 74
    ret.agregar_nodo(185.0,B,100)     # Nodo 75
    ret.agregar_nodo(190.0,0,100)       # Nodo 76
    ret.agregar_nodo(190.0,B,100)     # Nodo 77
    ret.agregar_nodo(195.0,0,100)       # Nodo 78
    ret.agregar_nodo(195.0,B,100)     # Nodo 79
    ret.agregar_nodo(200.0,0,100)       # Nodo 80
    ret.agregar_nodo(200.0,B,100)     # Nodo 81
    ret.agregar_nodo(205.0,0,100)       # Nodo 82
    ret.agregar_nodo(205.0,B,100)     # Nodo 83
    ret.agregar_nodo(210.0,0,100)       # Nodo 84   
    ret.agregar_nodo(210.0,B,100)     # Nodo 85 
    ret.agregar_nodo(215.0,0,100)       # Nodo 86
    ret.agregar_nodo(215.0,B,100)     # Nodo 87     (punto 28) 


#   Nodos Estructura
    j = np.arange(5.0,215,5)
    for i in j:
        ret.agregar_nodo(i, 0, 105)
        ret.agregar_nodo(i, B,105)

    ret.agregar_nodo(105, 1, 105)#172

    ret.agregar_nodo(110, 1, 105)#173




    
#   Barras 

    props = [2*cm, 1*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
 
#    Barras Tablero

    ret.agregar_barra(Barra(0, 2, *props))
    ret.agregar_barra(Barra(1, 3, *props))
    ret.agregar_barra(Barra(2, 4, *props))
    ret.agregar_barra(Barra(3, 5, *props))
    ret.agregar_barra(Barra(4, 6, *props))
    ret.agregar_barra(Barra(5, 7, *props))
    ret.agregar_barra(Barra(6, 8, *props))
    ret.agregar_barra(Barra(7, 9, *props))
    ret.agregar_barra(Barra(8, 10, *props))
    ret.agregar_barra(Barra(9, 11, *props))
    ret.agregar_barra(Barra(10, 12, *props))
    ret.agregar_barra(Barra(11, 13, *props))
    ret.agregar_barra(Barra(12, 14, *props))
    ret.agregar_barra(Barra(13, 15, *props))
    ret.agregar_barra(Barra(14, 16, *props))
    ret.agregar_barra(Barra(15, 17, *props))
    ret.agregar_barra(Barra(16, 18, *props))
    ret.agregar_barra(Barra(17, 19, *props))
    ret.agregar_barra(Barra(18, 20, *props))
    ret.agregar_barra(Barra(19, 21, *props))
    ret.agregar_barra(Barra(20, 22, *props))
    ret.agregar_barra(Barra(21, 23, *props))
    ret.agregar_barra(Barra(22, 24, *props))
    ret.agregar_barra(Barra(23, 25, *props))
    ret.agregar_barra(Barra(24, 26, *props))
    ret.agregar_barra(Barra(25, 27, *props))
    ret.agregar_barra(Barra(26, 28, *props))
    ret.agregar_barra(Barra(27, 29, *props))
    ret.agregar_barra(Barra(28, 30, *props))
    ret.agregar_barra(Barra(29, 31, *props))
    ret.agregar_barra(Barra(30, 32, *props))
    ret.agregar_barra(Barra(31, 33, *props))
    ret.agregar_barra(Barra(32, 34, *props))
    ret.agregar_barra(Barra(33, 35, *props))
    ret.agregar_barra(Barra(34, 36, *props))
    ret.agregar_barra(Barra(35, 37, *props))
    ret.agregar_barra(Barra(36, 38, *props))
    ret.agregar_barra(Barra(37, 39, *props))
    ret.agregar_barra(Barra(38, 40, *props))
    ret.agregar_barra(Barra(39, 41, *props))
    ret.agregar_barra(Barra(40, 42, *props))
    ret.agregar_barra(Barra(41, 43, *props))
    ret.agregar_barra(Barra(42, 44, *props))
    ret.agregar_barra(Barra(43, 45, *props))
    ret.agregar_barra(Barra(44, 46, *props))
    ret.agregar_barra(Barra(45, 47, *props))
    ret.agregar_barra(Barra(46, 48, *props))
    ret.agregar_barra(Barra(47, 49, *props))
    ret.agregar_barra(Barra(48, 50, *props))
    ret.agregar_barra(Barra(49, 51, *props))
    ret.agregar_barra(Barra(50, 52, *props))
    ret.agregar_barra(Barra(51, 53, *props))
    ret.agregar_barra(Barra(52, 54, *props))
    ret.agregar_barra(Barra(53, 55, *props))
    ret.agregar_barra(Barra(54, 56, *props))
    ret.agregar_barra(Barra(55, 57, *props))
    ret.agregar_barra(Barra(56, 58, *props))
    ret.agregar_barra(Barra(57, 59, *props))
    ret.agregar_barra(Barra(58, 60, *props))
    ret.agregar_barra(Barra(59, 61, *props))
    ret.agregar_barra(Barra(60, 62, *props))
    ret.agregar_barra(Barra(61, 63, *props))
    ret.agregar_barra(Barra(62, 64, *props))
    ret.agregar_barra(Barra(63, 65, *props))
    ret.agregar_barra(Barra(64, 66, *props))
    ret.agregar_barra(Barra(65, 67, *props))
    ret.agregar_barra(Barra(66, 68, *props))
    ret.agregar_barra(Barra(67, 69, *props))
    ret.agregar_barra(Barra(68, 70, *props))
    ret.agregar_barra(Barra(69, 71, *props))
    ret.agregar_barra(Barra(70, 72, *props))
    ret.agregar_barra(Barra(71, 73, *props))
    ret.agregar_barra(Barra(72, 74, *props))
    ret.agregar_barra(Barra(73, 75, *props))
    ret.agregar_barra(Barra(74, 76, *props))
    ret.agregar_barra(Barra(75, 77, *props))
    ret.agregar_barra(Barra(76, 78, *props))
    ret.agregar_barra(Barra(77, 79, *props))
    ret.agregar_barra(Barra(78, 80, *props))
    ret.agregar_barra(Barra(79, 81, *props))
    ret.agregar_barra(Barra(80, 82, *props))
    ret.agregar_barra(Barra(81, 83, *props))
    ret.agregar_barra(Barra(82, 84, *props))
    ret.agregar_barra(Barra(83, 85, *props))
    ret.agregar_barra(Barra(84, 86, *props))
    ret.agregar_barra(Barra(85, 87, *props))

    ret.agregar_barra(Barra(0, 1, *props))
    ret.agregar_barra(Barra(2, 3, *props))
    ret.agregar_barra(Barra(4, 5, *props))
    ret.agregar_barra(Barra(6, 7, *props))
    ret.agregar_barra(Barra(8, 9, *props))
    ret.agregar_barra(Barra(10, 11, *props))
    ret.agregar_barra(Barra(12, 13, *props))
    ret.agregar_barra(Barra(14, 15, *props))
    ret.agregar_barra(Barra(16, 17, *props))
    ret.agregar_barra(Barra(18, 19, *props))
    ret.agregar_barra(Barra(20, 21, *props))
    ret.agregar_barra(Barra(22, 23, *props))
    ret.agregar_barra(Barra(24, 25, *props))
    ret.agregar_barra(Barra(26, 27, *props))
    ret.agregar_barra(Barra(28, 29, *props))
    ret.agregar_barra(Barra(30, 31, *props))
    ret.agregar_barra(Barra(32, 33, *props))
    ret.agregar_barra(Barra(34, 35, *props))
    ret.agregar_barra(Barra(36, 37, *props))
    ret.agregar_barra(Barra(38, 39, *props))
    ret.agregar_barra(Barra(40, 41, *props))
    ret.agregar_barra(Barra(42, 43, *props))
    ret.agregar_barra(Barra(44, 45, *props))
    ret.agregar_barra(Barra(46, 47, *props))
    ret.agregar_barra(Barra(48, 49, *props))
    ret.agregar_barra(Barra(50, 51, *props))
    ret.agregar_barra(Barra(52, 53, *props))
    ret.agregar_barra(Barra(54, 55, *props))
    ret.agregar_barra(Barra(56, 57, *props))
    ret.agregar_barra(Barra(58, 59, *props))
    ret.agregar_barra(Barra(60, 61, *props))
    ret.agregar_barra(Barra(62, 63, *props))
    ret.agregar_barra(Barra(64, 65, *props))
    ret.agregar_barra(Barra(66, 67, *props))
    ret.agregar_barra(Barra(68, 69, *props))
    ret.agregar_barra(Barra(70, 71, *props))
    ret.agregar_barra(Barra(72, 73, *props))
    ret.agregar_barra(Barra(74, 75, *props))
    ret.agregar_barra(Barra(76, 77, *props))
    ret.agregar_barra(Barra(78, 79, *props))
    ret.agregar_barra(Barra(80, 81, *props))
    ret.agregar_barra(Barra(82, 83, *props))
    ret.agregar_barra(Barra(84, 85, *props))
    ret.agregar_barra(Barra(86, 87, *props))
 

    ret.agregar_barra(Barra(0, 3, *props))
    ret.agregar_barra(Barra(1, 2, *props))
    ret.agregar_barra(Barra(2, 5, *props))
    ret.agregar_barra(Barra(3, 4, *props))
    ret.agregar_barra(Barra(4, 7, *props))
    ret.agregar_barra(Barra(5, 6, *props))
    ret.agregar_barra(Barra(6, 9, *props))
    ret.agregar_barra(Barra(7, 8, *props))
    ret.agregar_barra(Barra(8, 11, *props))
    ret.agregar_barra(Barra(9, 10, *props))
    ret.agregar_barra(Barra(10, 13, *props))
    ret.agregar_barra(Barra(11, 12, *props))
    ret.agregar_barra(Barra(12, 15, *props))
    ret.agregar_barra(Barra(13, 14, *props))
    ret.agregar_barra(Barra(14, 17, *props))
    ret.agregar_barra(Barra(15, 16, *props))
    ret.agregar_barra(Barra(16, 19, *props))
    ret.agregar_barra(Barra(17, 18, *props))
    ret.agregar_barra(Barra(18, 21, *props))
    ret.agregar_barra(Barra(19, 20, *props))
    ret.agregar_barra(Barra(20, 23, *props))
    ret.agregar_barra(Barra(21, 22, *props))
    ret.agregar_barra(Barra(22, 25, *props))
    ret.agregar_barra(Barra(23, 24, *props))
    ret.agregar_barra(Barra(24, 27, *props))
    ret.agregar_barra(Barra(25, 26, *props))
    ret.agregar_barra(Barra(26, 29, *props))
    ret.agregar_barra(Barra(27, 28, *props))
    ret.agregar_barra(Barra(28, 31, *props))
    ret.agregar_barra(Barra(29, 30, *props))
    ret.agregar_barra(Barra(30, 33, *props))
    ret.agregar_barra(Barra(31, 32, *props))
    ret.agregar_barra(Barra(32, 35, *props))
    ret.agregar_barra(Barra(33, 34, *props))
    ret.agregar_barra(Barra(34, 37, *props))
    ret.agregar_barra(Barra(35, 36, *props))
    ret.agregar_barra(Barra(36, 39, *props))
    ret.agregar_barra(Barra(37, 38, *props))
    ret.agregar_barra(Barra(38, 41, *props))
    ret.agregar_barra(Barra(39, 40, *props))
    ret.agregar_barra(Barra(40, 43, *props))
    ret.agregar_barra(Barra(41, 42, *props))
    ret.agregar_barra(Barra(42, 45, *props))
    ret.agregar_barra(Barra(43, 44, *props))
    ret.agregar_barra(Barra(44, 47, *props))
    ret.agregar_barra(Barra(45, 46, *props))
    ret.agregar_barra(Barra(46, 49, *props))
    ret.agregar_barra(Barra(47, 48, *props))
    ret.agregar_barra(Barra(48, 51, *props))
    ret.agregar_barra(Barra(49, 50, *props))
    ret.agregar_barra(Barra(50, 53, *props))
    ret.agregar_barra(Barra(51, 52, *props))
    ret.agregar_barra(Barra(52, 55, *props))
    ret.agregar_barra(Barra(53, 54, *props))
    ret.agregar_barra(Barra(54, 57, *props))
    ret.agregar_barra(Barra(55, 56, *props))
    ret.agregar_barra(Barra(56, 59, *props))
    ret.agregar_barra(Barra(57, 58, *props))
    ret.agregar_barra(Barra(58, 61, *props))
    ret.agregar_barra(Barra(59, 60, *props))
    ret.agregar_barra(Barra(60, 63, *props))
    ret.agregar_barra(Barra(61, 62, *props))
    ret.agregar_barra(Barra(62, 65, *props))
    ret.agregar_barra(Barra(63, 64, *props))
    ret.agregar_barra(Barra(64, 67, *props))
    ret.agregar_barra(Barra(65, 66, *props))
    ret.agregar_barra(Barra(66, 69, *props))
    ret.agregar_barra(Barra(67, 68, *props))
    ret.agregar_barra(Barra(68, 71, *props))
    ret.agregar_barra(Barra(69, 70, *props))
    ret.agregar_barra(Barra(70, 73, *props))
    ret.agregar_barra(Barra(71, 72, *props))
    ret.agregar_barra(Barra(72, 75, *props))
    ret.agregar_barra(Barra(73, 74, *props))
    ret.agregar_barra(Barra(74, 77, *props))
    ret.agregar_barra(Barra(75, 76, *props))
    ret.agregar_barra(Barra(76, 79, *props))
    ret.agregar_barra(Barra(77, 78, *props))
    ret.agregar_barra(Barra(78, 81, *props))
    ret.agregar_barra(Barra(79, 80, *props))
    ret.agregar_barra(Barra(80, 83, *props))
    ret.agregar_barra(Barra(81, 82, *props))
    ret.agregar_barra(Barra(82, 85, *props))
    ret.agregar_barra(Barra(83, 84, *props))
    ret.agregar_barra(Barra(84, 87, *props))
    ret.agregar_barra(Barra(85, 86, *props))



#   Barras Estructura general

    #barras longitudinales estructura arco
    for i in range(88,170):

        ret.agregar_barra(Barra(i, i+2, *props))

    for i in range(0,84):
        ret.agregar_barra(Barra(i, i+88, *props))

    j = np.arange(88, 130, 2)
    for i in j:
        ret.agregar_barra(Barra(i, i+1, *props))
    for i in np.arange(134,171,2):
        ret.agregar_barra(Barra(i, i+1, *props))

    ret.agregar_barra(Barra(86,170,*props))
    ret.agregar_barra(Barra(87,171,*props))
    ret.agregar_barra(Barra(130, 172, *props))
    ret.agregar_barra(Barra(131, 172, *props))
    ret.agregar_barra(Barra(132, 173, *props))
    ret.agregar_barra(Barra(133, 173, *props))
    for i in range(4,42):
        ret.agregar_barra(Barra(i,i+84, *props))
    for i in range(43,85):
        ret.agregar_barra(Barra(i, i+82, *props))


    ret.agregar_restriccion(0, 0 ,0)
    ret.agregar_restriccion(0, 1 ,0)
    ret.agregar_restriccion(0, 2 ,0)
    ret.agregar_restriccion(1, 0 ,0)
    ret.agregar_restriccion(1, 1 ,0)
    ret.agregar_restriccion(1, 2 ,0)
    ret.agregar_restriccion(86, 0 ,0)
    ret.agregar_restriccion(86, 1 ,0)
    ret.agregar_restriccion(86, 2 ,0)
    ret.agregar_restriccion(87, 0 ,0)
    ret.agregar_restriccion(87, 1 ,0)
    ret.agregar_restriccion(87, 2 ,0)
    ret.agregar_restriccion(84, 0 ,0)
    ret.agregar_restriccion(84, 1 ,0)
    ret.agregar_restriccion(84, 2 ,0)
    ret.agregar_restriccion(85, 0 ,0)
    ret.agregar_restriccion(85, 1 ,0)
    ret.agregar_restriccion(85, 2 ,0)
    ret.agregar_restriccion(2, 0 ,0)
    ret.agregar_restriccion(2, 1 ,0)
    ret.agregar_restriccion(2, 2 ,0)
    ret.agregar_restriccion(3, 0 ,0)
    ret.agregar_restriccion(3, 1 ,0)
    ret.agregar_restriccion(3, 2 ,0)

    for i in range(88,174):
        ret.agregar_restriccion(i, 0 ,0)
        ret.agregar_restriccion(i, 1 ,0)
        ret.agregar_restriccion(i, 2 ,0)

    


    for i in range(2,86):
        ret.agregar_fuerza(i,2,-2*F)

    ret.agregar_fuerza(0,2,-F)
    ret.agregar_fuerza(1,2,-F)
    ret.agregar_fuerza(86,2,-F)
    ret.agregar_fuerza(87,2,-F)


    
    return ret