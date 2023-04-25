# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:01:18 2023

@author: ahmet
"""

"""
P : Nominal yatak basıncı (Pa)
W : Yatak yükü (Newton cinsinden)
r : Mil çapı (mm)
c : Radyal boşluk (mm)
l : Yatak boyu (mm)
N : dönüş hızı (rps)
u : mü (Pa.s)
h0 : minimum film kalınlığı (Şekil 12-16 -h0/c-)
E : Eksantrisite oranı -boyutsuz- (Şekil 12-16)
f : Sürtünme katsayısı (Şekil 12-18)
T : Mil üzerindeki sürtünme kuvveti (N.m)
hp : Sürtünme güç kaybı (W)
Q : Hacimsel debi (mm^3/s)
Qs : Kenar sızıntı debisi (mm^3/s)

fi : Minumum film kalınlığının pozisyonu (derece)
teta_Pmax : Yağ filmindeki maksimum basınç değerinin oluştuğu konumun derecesi (derece)
teta_P0 : Film basıncının bittiği pozisyon (derece)
"""


from math import pi
from sympy import symbols

# çevrimler

def mm2m(mm):
    return mm / 1000

def MPa2Pa(MPa):
    return MPa * 10**6

def Pa2MPa(Pa):
    return Pa / 10**6

def rpm2rps(rpm):
    return rpm / 60

def m2_to_m3(m2):
    return m2 / 10**6

# formüller

def nominal_bearing_pressure(W, r, l):
    P = W / (2 * mm2m(r) * mm2m(l))
    print(f"{P} Pa")
    return P

def Sommerfeld(r, c, u, N, P):
    S = ((r / c) ** 2) * ((u * N) / P)
    print(f"{S} = (({r} mm / {c} mm) ** 2) * (({u} Pa.s * {N} rps) / {P} Pa)")
    return S

def h0_calculate(h0pc, c):
    h0 = h0pc * c
    print(f"h0 = {h0}")
    return h0

def l_per_d(l, r):
    l_per_d = l / (2 * r)
    print(f"l / d = {l_per_d}")
    return l_per_d

def eccentricity(epc, c):
    E = epc * c
    print(f"Eksantrisite oranı : E = {E}")
    return E

def coefficient_of_friction(rcf, r, c):
    f = rcf * (c / r)
    print(f"Sürtünme katsayısı : f = {f}")
    return f

def friction_torque(f, W, r):
    T = f * W * mm2m(r)
    print(f"Mil üzerindeki sürtünme kuvveti : T = {T} N.m")
    return T

def hp_loss(T, N):
    hp = T * N * 2 * pi
    print(f"Güç kaybı : (Hp)loss = {hp} W")
    return hp

def hp_loss2(f, W, r, N):
    hp = f * W * r * N * 2 * pi
    print(f"Güç kaybı : (Hp)loss = {hp} W")
    return hp

def hp_loss_miss(frc, c, W, N):
    hp = frc * c * W * N * 2 * pi
    print(f"Güç kaybı : (Hp)loss = {hp} W")
    return hp

def volumetric_flow(QpValues, r, c, N, l):
    Q = QpValues * r * c * N * l
    print(f"Hacimsel debi : Q = {Q} mm^3/s")
    return Q

def side_flow_rate(QpQs, Q):
    Qs = QpQs * Q
    print(f"Kenar sızıntı debisi : Qs = {Qs} mm^3/s")
    return Qs
    
def maximum_film_pressure(PpPmax, P):
    Pmax = P / PpPmax
    print(f"Maksimum film basıncı : Pmax = {Pmax} Pa")
    return Pmax

def minimum_radial_clearance(db, dm):
    cmin = (db - dm) / 2
    print(f"Minimum radyal boşluk : cmin = {cmin}")
    return cmin
    
def Hloss_calculate(hCR, A, a, Tf, Th):
    Hloss = ((hCR * A) / (a + 1)) * (Tf - Th)
    return Hloss

# ***Sembollerin yanındaki p harfleri per anlamında kullanılmıştır. PpPmax = P/Pmax vb.