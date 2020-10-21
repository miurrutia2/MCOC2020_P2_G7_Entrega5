from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *

def caso_L():
    
    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 
    
    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N
    kgf = 9.80665*N
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
    
    ret.agregar_nodo(19.0,0,66)         # Nodo 88   (punto 11)
    ret.agregar_nodo(19.0,B,66)         # Nodo 89
    ret.agregar_nodo(22.0,0,67.9)       # Nodo 90
    ret.agregar_nodo(22.0,B,67.9)     # Nodo 91
    ret.agregar_nodo(32.0,0,74.1)       # Nodo 92
    ret.agregar_nodo(32.0,B,74.1)     # Nodo 93
    ret.agregar_nodo(42.0,0,79.6)       # Nodo 94
    ret.agregar_nodo(42.0,B,79.6)     # Nodo 95
    ret.agregar_nodo(52.0,0,84.3)       # Nodo 96
    ret.agregar_nodo(52.0,B,84.3)     # Nodo 97
    ret.agregar_nodo(62.0,0,88.3)       # Nodo 98
    ret.agregar_nodo(62.0,B,88.3)     # Nodo 99
    ret.agregar_nodo(72.0,0,91.7)     # Nodo 100
    ret.agregar_nodo(72.0,B,91.7)   # Nodo 101
    ret.agregar_nodo(82.0,0,94.3)     # Nodo 102
    ret.agregar_nodo(82.0,B,94.3)   # Nodo 103
    ret.agregar_nodo(92.0,0,96.3)    # Nodo 104
    ret.agregar_nodo(92.0,B,96.3)  # Nodo 105
    ret.agregar_nodo(102.0,0,97.5)      # Nodo 106
    ret.agregar_nodo(102.0,B,97.5)    # Nodo 107
    ret.agregar_nodo(112.0,0,98.1)    # Nodo 108
    ret.agregar_nodo(112.0,B,98.1)  # Nodo 109
    ret.agregar_nodo(122.0,0,97.9)    # Nodo 110
    ret.agregar_nodo(122.0,B,97.9)  # Nodo 111
    ret.agregar_nodo(132.0,0,97.1)    # Nodo 112
    ret.agregar_nodo(132.0,B,97.1)  # Nodo 113
    ret.agregar_nodo(142.0,0,95.6)    # Nodo 114
    ret.agregar_nodo(142.0,B,95.6)  # Nodo 115
    ret.agregar_nodo(152.0,0,93.3)    # Nodo 116
    ret.agregar_nodo(152.0,B,93.3)  # Nodo 117
    ret.agregar_nodo(162.0,0,90.4)    # Nodo 118
    ret.agregar_nodo(162.0,B,90.4)  # Nodo 119
    ret.agregar_nodo(174.0,0,86)      # Nodo 120   (punto 25)
    ret.agregar_nodo(174.0,B,86)    # Nodo 121      


    ret.agregar_nodo(4,0,97)        # Nodo 122  (punto 8)
    ret.agregar_nodo(4,B,97)        # Nodo 123

    ret.agregar_nodo(8,0,92)        #Nodo 124   (punto 9)
    ret.agregar_nodo(8,B,92)        # Nodo 125

    ret.agregar_nodo(8,0,97)        #Nodo 126       
    ret.agregar_nodo(8,B,97)        #Nodo 127

    ret.agregar_nodo(12,0,83)       #Nodo 128   (punto 10)
    ret.agregar_nodo(12,B,83)       #Nodo 129

    ret.agregar_nodo(12,0,97)       #Nodo 130
    ret.agregar_nodo(12,B,97)       #Nodo 131

    ret.agregar_nodo(19,0,97)       #Nodo 132
    ret.agregar_nodo(19,B,97)       #Nodo 133

    ret.agregar_nodo(22,0,97)       # Nodo 134
    ret.agregar_nodo(22,B,97)       # Nodo 135

    ret.agregar_nodo(32,0,97)       # Nodo 136
    ret.agregar_nodo(32,B,97)       # Nodo 137

    ret.agregar_nodo(42,0,97)       # Nodo 138
    ret.agregar_nodo(42,B,97)       # Nodo 139          

    ret.agregar_nodo(52,0,97)       # Nodo 140
    ret.agregar_nodo(52,B,97)       # Nodo 141

    ret.agregar_nodo(62,0,97)       # Nodo 142
    ret.agregar_nodo(62,B,97)       # Nodo 143

    ret.agregar_nodo(72,0,97)       # Nodo 144
    ret.agregar_nodo(72,B,97)       # Nodo 145

    ret.agregar_nodo(82,0,97)       # Nodo 146
    ret.agregar_nodo(82,B,97)       # Nodo 147

    ret.agregar_nodo(92,0,97)       # Nodo 148
    ret.agregar_nodo(92,B,97)       # Nodo 149

    ret.agregar_nodo(174,0,97)       # Nodo 150
    ret.agregar_nodo(174,B,97)       # Nodo 151

    ret.agregar_nodo(162,0,97)       # Nodo 152
    ret.agregar_nodo(162,B,97)       # Nodo 153

    ret.agregar_nodo(152,0,97)       # Nodo 154
    ret.agregar_nodo(152,B,97)       # Nodo 155

    ret.agregar_nodo(142,0,97)       # Nodo 156
    ret.agregar_nodo(142,B,97)       # Nodo 157

    ret.agregar_nodo(188,0,93)       # Nodo 158     (punto 26)
    ret.agregar_nodo(188,B,93)       # Nodo 159

    ret.agregar_nodo(188,0,97)       # Nodo 160
    ret.agregar_nodo(188,B,97)       # Nodo 161

    ret.agregar_nodo(205,0,95)       # Nodo 162     (punto 27)
    ret.agregar_nodo(205,B,95)       # Nodo 163

    ret.agregar_nodo(205,0,97)       # Nodo 164
    ret.agregar_nodo(205,B,97)       # Nodo 165




    
#   Barras 

    props = [8*cm, 5*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
 
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

    ret.agregar_barra(Barra(88, 90, *props))
    ret.agregar_barra(Barra(89, 91, *props))
    ret.agregar_barra(Barra(90, 92, *props))
    ret.agregar_barra(Barra(91, 93, *props))
    ret.agregar_barra(Barra(92, 94, *props))
    ret.agregar_barra(Barra(93, 95, *props))
    ret.agregar_barra(Barra(94, 96, *props))
    ret.agregar_barra(Barra(95, 97, *props))
    ret.agregar_barra(Barra(96, 98, *props))
    ret.agregar_barra(Barra(97, 99, *props))
    ret.agregar_barra(Barra(98, 100, *props))
    ret.agregar_barra(Barra(99, 101, *props))
    ret.agregar_barra(Barra(100, 102, *props))
    ret.agregar_barra(Barra(101, 103, *props))
    ret.agregar_barra(Barra(102, 104, *props))
    ret.agregar_barra(Barra(103, 105, *props))
    ret.agregar_barra(Barra(104, 106, *props))
    ret.agregar_barra(Barra(105, 107, *props))
    ret.agregar_barra(Barra(106, 108, *props))
    ret.agregar_barra(Barra(107, 109, *props))
    ret.agregar_barra(Barra(108, 110, *props))
    ret.agregar_barra(Barra(109, 111, *props))
    ret.agregar_barra(Barra(110, 112, *props))
    ret.agregar_barra(Barra(111, 113, *props))
    ret.agregar_barra(Barra(112, 114, *props))
    ret.agregar_barra(Barra(113, 115, *props))
    ret.agregar_barra(Barra(114, 116, *props))
    ret.agregar_barra(Barra(115, 117, *props))
    ret.agregar_barra(Barra(116, 118, *props))
    ret.agregar_barra(Barra(117, 119, *props))
    ret.agregar_barra(Barra(118, 120, *props))
    ret.agregar_barra(Barra(119, 121, *props))


    #barras que conforman la malla sobre el arco

    ret.agregar_barra(Barra(122, 126, *props))
    ret.agregar_barra(Barra(123, 127, *props))

    ret.agregar_barra(Barra(124, 126, *props))
    ret.agregar_barra(Barra(125, 127, *props))

    ret.agregar_barra(Barra(128, 130, *props))
    ret.agregar_barra(Barra(129, 131, *props))

    ret.agregar_barra(Barra(88, 132, *props))
    ret.agregar_barra(Barra(89, 133, *props))    

    ret.agregar_barra(Barra(90, 134, *props))
    ret.agregar_barra(Barra(91, 135, *props))

    ret.agregar_barra(Barra(92, 136, *props))
    ret.agregar_barra(Barra(93, 137, *props))

    ret.agregar_barra(Barra(94, 138, *props))
    ret.agregar_barra(Barra(95, 139, *props))

    ret.agregar_barra(Barra(96, 140, *props))
    ret.agregar_barra(Barra(97, 141, *props))

    ret.agregar_barra(Barra(98, 142, *props))
    ret.agregar_barra(Barra(99, 143, *props))

    ret.agregar_barra(Barra(100, 144, *props))
    ret.agregar_barra(Barra(101, 145, *props))

    ret.agregar_barra(Barra(102, 146, *props))
    ret.agregar_barra(Barra(103, 147, *props))

    ret.agregar_barra(Barra(104, 148, *props))
    ret.agregar_barra(Barra(105, 149, *props))

    ret.agregar_barra(Barra(122, 126, *props))
    ret.agregar_barra(Barra(123, 127, *props))

    ret.agregar_barra(Barra(126, 130, *props))
    ret.agregar_barra(Barra(127, 131, *props))

    ret.agregar_barra(Barra(130, 132, *props))
    ret.agregar_barra(Barra(131, 133, *props))

    ret.agregar_barra(Barra(132, 134, *props))
    ret.agregar_barra(Barra(133, 135, *props))

    ret.agregar_barra(Barra(134, 136, *props))
    ret.agregar_barra(Barra(133, 137, *props))

    ret.agregar_barra(Barra(136, 138, *props))
    ret.agregar_barra(Barra(137, 139, *props))

    ret.agregar_barra(Barra(138, 140, *props))
    ret.agregar_barra(Barra(139, 141, *props))

    ret.agregar_barra(Barra(140, 142, *props))
    ret.agregar_barra(Barra(141, 143, *props))

    ret.agregar_barra(Barra(142, 144, *props))
    ret.agregar_barra(Barra(143, 145, *props))

    ret.agregar_barra(Barra(144, 146, *props))
    ret.agregar_barra(Barra(145, 147, *props))

    ret.agregar_barra(Barra(146, 148, *props))
    ret.agregar_barra(Barra(147, 149, *props))

    ret.agregar_barra(Barra(150, 120, *props))
    ret.agregar_barra(Barra(151, 121, *props))

    ret.agregar_barra(Barra(152, 118, *props))
    ret.agregar_barra(Barra(153, 119, *props))

    ret.agregar_barra(Barra(154, 116, *props))
    ret.agregar_barra(Barra(155, 117, *props))

    ret.agregar_barra(Barra(156, 114, *props))
    ret.agregar_barra(Barra(157, 115, *props))

    ret.agregar_barra(Barra(150, 152, *props))
    ret.agregar_barra(Barra(151, 153, *props))

    ret.agregar_barra(Barra(152, 154, *props))
    ret.agregar_barra(Barra(153, 155, *props))

    ret.agregar_barra(Barra(154, 156, *props))
    ret.agregar_barra(Barra(155, 157, *props))

    ret.agregar_barra(Barra(156, 112, *props))
    ret.agregar_barra(Barra(157, 113, *props))

    ret.agregar_barra(Barra(148, 106, *props))
    ret.agregar_barra(Barra(149, 107, *props))

    ret.agregar_barra(Barra(158, 160, *props))
    ret.agregar_barra(Barra(159, 161, *props))

    ret.agregar_barra(Barra(162, 164, *props))
    ret.agregar_barra(Barra(163, 165, *props))

    ret.agregar_barra(Barra(164, 160, *props))
    ret.agregar_barra(Barra(165, 161, *props))

    ret.agregar_barra(Barra(160, 150, *props))
    ret.agregar_barra(Barra(161, 151, *props))


    #barras que unen ambas caras del arco

    ret.agregar_barra(Barra(90, 91, *props))
    ret.agregar_barra(Barra(92, 93, *props))
    ret.agregar_barra(Barra(94, 95, *props))
    ret.agregar_barra(Barra(96, 97, *props))
    ret.agregar_barra(Barra(98, 99, *props))
    ret.agregar_barra(Barra(100, 101, *props))
    ret.agregar_barra(Barra(102, 103, *props))
    ret.agregar_barra(Barra(104, 105, *props))
    ret.agregar_barra(Barra(106, 107, *props))
    ret.agregar_barra(Barra(108, 109, *props))
    ret.agregar_barra(Barra(110, 111, *props))
    ret.agregar_barra(Barra(112, 113, *props))
    ret.agregar_barra(Barra(114, 115, *props))
    ret.agregar_barra(Barra(116, 117, *props))
    ret.agregar_barra(Barra(118, 119, *props))


    #barras que unen tablero con estructura inferior

    ret.agregar_barra(Barra(2, 126, *props))
    ret.agregar_barra(Barra(3, 127, *props))

    ret.agregar_barra(Barra(4, 126, *props))
    ret.agregar_barra(Barra(5, 127, *props))

    ret.agregar_barra(Barra(4, 130, *props))
    ret.agregar_barra(Barra(5, 131, *props))

    ret.agregar_barra(Barra(6, 130, *props))
    ret.agregar_barra(Barra(7, 131, *props))

    ret.agregar_barra(Barra(8, 134, *props))
    ret.agregar_barra(Barra(9, 135, *props))

    ret.agregar_barra(Barra(10, 134, *props))
    ret.agregar_barra(Barra(11, 135, *props))

    ret.agregar_barra(Barra(12, 136, *props))
    ret.agregar_barra(Barra(13, 137, *props))

    ret.agregar_barra(Barra(14, 136, *props))
    ret.agregar_barra(Barra(15, 137, *props))

    ret.agregar_barra(Barra(16, 138, *props))
    ret.agregar_barra(Barra(17, 139, *props))

    ret.agregar_barra(Barra(18, 138, *props))
    ret.agregar_barra(Barra(19, 139, *props))

    ret.agregar_barra(Barra(20, 140, *props))
    ret.agregar_barra(Barra(21, 141, *props))

    ret.agregar_barra(Barra(22, 140, *props))
    ret.agregar_barra(Barra(23, 141, *props))

    ret.agregar_barra(Barra(24, 142, *props))
    ret.agregar_barra(Barra(25, 143, *props))

    ret.agregar_barra(Barra(26, 142, *props))
    ret.agregar_barra(Barra(27, 143, *props))

    ret.agregar_barra(Barra(28, 144, *props))
    ret.agregar_barra(Barra(29, 145, *props))

    ret.agregar_barra(Barra(30, 144, *props))
    ret.agregar_barra(Barra(31, 145, *props))

    ret.agregar_barra(Barra(32, 146, *props))
    ret.agregar_barra(Barra(33, 147, *props))

    ret.agregar_barra(Barra(34, 146, *props))
    ret.agregar_barra(Barra(35, 147, *props))

    ret.agregar_barra(Barra(36, 148, *props))
    ret.agregar_barra(Barra(37, 149, *props))

    ret.agregar_barra(Barra(38, 148, *props))
    ret.agregar_barra(Barra(37, 149, *props))

    ret.agregar_barra(Barra(40, 106, *props))
    ret.agregar_barra(Barra(41, 107, *props))

    ret.agregar_barra(Barra(42, 106, *props))
    ret.agregar_barra(Barra(43, 107, *props))

    ret.agregar_barra(Barra(44, 108, *props))
    ret.agregar_barra(Barra(45, 109, *props))

    ret.agregar_barra(Barra(46, 108, *props))
    ret.agregar_barra(Barra(47, 109, *props))

    ret.agregar_barra(Barra(48, 110, *props))
    ret.agregar_barra(Barra(49, 111, *props))

    ret.agregar_barra(Barra(50, 110, *props))
    ret.agregar_barra(Barra(51, 111, *props))

    ret.agregar_barra(Barra(52, 112, *props))
    ret.agregar_barra(Barra(53, 113, *props))

    ret.agregar_barra(Barra(54, 112, *props))
    ret.agregar_barra(Barra(55, 113, *props))

    ret.agregar_barra(Barra(56, 156, *props))
    ret.agregar_barra(Barra(57, 157, *props))

    ret.agregar_barra(Barra(58, 156, *props))
    ret.agregar_barra(Barra(59, 157, *props))

    ret.agregar_barra(Barra(60, 154, *props))
    ret.agregar_barra(Barra(61, 155, *props))

    ret.agregar_barra(Barra(62, 154, *props))
    ret.agregar_barra(Barra(63, 155, *props))

    ret.agregar_barra(Barra(64, 152, *props))
    ret.agregar_barra(Barra(65, 153, *props))

    ret.agregar_barra(Barra(66, 152, *props))
    ret.agregar_barra(Barra(67, 153, *props))

    ret.agregar_barra(Barra(68, 150, *props))
    ret.agregar_barra(Barra(69, 151, *props))

    ret.agregar_barra(Barra(70, 150, *props))
    ret.agregar_barra(Barra(71, 151, *props))

    ret.agregar_barra(Barra(72, 150, *props))
    ret.agregar_barra(Barra(73, 151, *props))
 
    ret.agregar_barra(Barra(74, 160, *props))
    ret.agregar_barra(Barra(75, 161, *props))

    ret.agregar_barra(Barra(76, 160, *props))
    ret.agregar_barra(Barra(77, 161, *props))

    ret.agregar_barra(Barra(78, 160, *props))
    ret.agregar_barra(Barra(79, 161, *props))

    ret.agregar_barra(Barra(80, 164, *props))
    ret.agregar_barra(Barra(81, 165, *props))

    ret.agregar_barra(Barra(82, 164, *props))
    ret.agregar_barra(Barra(83, 165, *props))

    ret.agregar_barra(Barra(84, 164, *props))
    ret.agregar_barra(Barra(85, 165, *props))










    # Restricciones


    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)

    ret.agregar_restriccion(1, 0, 0)
    ret.agregar_restriccion(1, 1, 0)
    ret.agregar_restriccion(1, 2, 0)

    ret.agregar_restriccion(86, 0, 0)
    ret.agregar_restriccion(86, 1, 0)
    ret.agregar_restriccion(86, 2, 0)

    ret.agregar_restriccion(87, 0, 0)
    ret.agregar_restriccion(87, 1, 0)
    ret.agregar_restriccion(87, 2, 0)

    ret.agregar_restriccion(88, 0, 0)
    ret.agregar_restriccion(88, 1, 0)
    ret.agregar_restriccion(88, 2, 0)

    ret.agregar_restriccion(89, 0, 0)
    ret.agregar_restriccion(89, 1, 0)
    ret.agregar_restriccion(89, 2, 0)

    ret.agregar_restriccion(120, 0, 0)
    ret.agregar_restriccion(120, 1, 0)
    ret.agregar_restriccion(120, 2, 0)

    ret.agregar_restriccion(121, 0, 0)
    ret.agregar_restriccion(121, 1, 0)
    ret.agregar_restriccion(121, 2, 0)

    ret.agregar_restriccion(122, 0, 0)
    ret.agregar_restriccion(122, 1, 0)
    ret.agregar_restriccion(122, 2, 0)

    ret.agregar_restriccion(123, 0, 0)
    ret.agregar_restriccion(123, 1, 0)
    ret.agregar_restriccion(123, 2, 0)

    ret.agregar_restriccion(124, 0, 0)
    ret.agregar_restriccion(124, 1, 0)
    ret.agregar_restriccion(124, 2, 0)

    ret.agregar_restriccion(125, 0, 0)
    ret.agregar_restriccion(125, 1, 0)
    ret.agregar_restriccion(125, 2, 0)

    ret.agregar_restriccion(128, 0, 0)
    ret.agregar_restriccion(128, 1, 0)
    ret.agregar_restriccion(128, 2, 0) 

    ret.agregar_restriccion(129, 0, 0)
    ret.agregar_restriccion(129, 1, 0)
    ret.agregar_restriccion(129, 2, 0) 

    ret.agregar_restriccion(158, 0, 0)
    ret.agregar_restriccion(158, 1, 0)
    ret.agregar_restriccion(158, 2, 0)

    ret.agregar_restriccion(162, 0, 0)
    ret.agregar_restriccion(162, 1, 0)
    ret.agregar_restriccion(162, 2, 0) 


    for i in range(2,86):
        ret.agregar_fuerza(i,2,-2*F)

    ret.agregar_fuerza(0,2,-F)
    ret.agregar_fuerza(1,2,-F)
    ret.agregar_fuerza(86,2,-F)
    ret.agregar_fuerza(87,2,-F)


    
    return ret