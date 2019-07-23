##source ~/tensorflow/bin/activate


from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import numpy
import pandas as pd


###############################################################################
#
# SUJETO 1 Relajado
#
###############################################################################


RAF3_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/AF3.csv", delimiter=",")
RAF3_1 = RAF3_1.astype(np.float64)

RAF4_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/AF4.csv", delimiter=",")
RAF4_1 = RAF4_1.astype(np.float64)


RF3_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/F3.csv", delimiter=",")
RF3_1 = RF3_1.astype(np.float64)


RF8_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/F8.csv", delimiter=",")
RF8_1 = RF8_1.astype(np.float64)

RFC5_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/FC5.csv", delimiter=",")
RFC5_1 = RFC5_1.astype(np.float64)

RO2_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/O2.csv", delimiter=",")
RO2_1 = RO2_1.astype(np.float64)

RP8_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/P8.csv", delimiter=",")
RP8_1 = RP8_1.astype(np.float64)


RT8_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/T8.csv", delimiter=",")
RT8_1 = RT8_1.astype(np.float64)

RP7_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/P7.csv", delimiter=",")
RP7_1 = RP7_1.astype(np.float64)


RT7_1 = genfromtxt("Extraccion/Sujeto_1/Relajado/T7.csv", delimiter=",")
RT7_1 = RT7_1.astype(np.float64)
###############################################################################
#
# SUJETO 1 Estres
#
###############################################################################


EAF3_1 = genfromtxt("Extraccion/Sujeto_1/Estres/AF3.csv", delimiter=",")
EAF3_1 = EAF3_1.astype(np.float64)

EAF4_1 = genfromtxt("Extraccion/Sujeto_1/Estres/AF4.csv", delimiter=",")
EAF4_1 = EAF4_1.astype(np.float64)


EF3_1 = genfromtxt("Extraccion/Sujeto_1/Estres/F3.csv", delimiter=",")
EF3_1 = EF3_1.astype(np.float64)


EF8_1 = genfromtxt("Extraccion/Sujeto_1/Estres/F8.csv", delimiter=",")
EF8_1 = EF8_1.astype(np.float64)

EFC5_1 = genfromtxt("Extraccion/Sujeto_1/Estres/FC5.csv", delimiter=",")
EFC5_1 = EFC5_1.astype(np.float64)

EO2_1 = genfromtxt("Extraccion/Sujeto_1/Estres/O2.csv", delimiter=",")
EO2_1 = EO2_1.astype(np.float64)

EP8_1 = genfromtxt("Extraccion/Sujeto_1/Estres/P8.csv", delimiter=",")
EP8_1 = EP8_1.astype(np.float64)


ET8_1 = genfromtxt("Extraccion/Sujeto_1/Estres/T8.csv", delimiter=",")
ET8_1 = ET8_1.astype(np.float64)

#EP7_1 = genfromtxt("Extraccion/Sujeto_1/Estres/P7.csv", delimiter=",")
#EP7_1 = EP7_1.astype(np.float64)


ET7_1 = genfromtxt("Extraccion/Sujeto_1/Estres/T7.csv", delimiter=",")
ET7_1 = ET7_1.astype(np.float64)



###############################################################################
#
# SUJETO 2 Relajado
#
###############################################################################


RAF3_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/AF3.csv", delimiter=",")
RAF3_2 = RAF3_2.astype(np.float64)

RAF4_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/AF4.csv", delimiter=",")
RAF4_2 = RAF4_2.astype(np.float64)


RF3_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/F3.csv", delimiter=",")
RF3_2 = RF3_2.astype(np.float64)


RF8_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/F8.csv", delimiter=",")
RF8_2 = RF8_2.astype(np.float64)

RFC5_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/FC5.csv", delimiter=",")
RFC5_2 = RFC5_2.astype(np.float64)

RO2_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/O2.csv", delimiter=",")
RO2_2 = RO2_2.astype(np.float64)

RP8_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/P8.csv", delimiter=",")
RP8_2 = RP8_2.astype(np.float64)


RT8_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/T8.csv", delimiter=",")
RT8_2 = RT8_2.astype(np.float64)

RF7_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/F7.csv", delimiter=",")
RF7_2 = RF7_2.astype(np.float64)


RT7_2 = genfromtxt("Extraccion/Sujeto_2/Relajado/T7.csv", delimiter=",")
RT7_2 = RT7_2.astype(np.float64)




###############################################################################
#
# SUJETO 2 Estres
#
###############################################################################


EAF3_2 = genfromtxt("Extraccion/Sujeto_2/Estres/AF3.csv", delimiter=",")
EAF3_2 = EAF3_2.astype(np.float64)

EAF4_2 = genfromtxt("Extraccion/Sujeto_2/Estres/AF4.csv", delimiter=",")
EAF4_2 = EAF4_2.astype(np.float64)


EF3_2 = genfromtxt("Extraccion/Sujeto_2/Estres/F3.csv", delimiter=",")
EF3_2 = EF3_2.astype(np.float64)


EF8_2 = genfromtxt("Extraccion/Sujeto_2/Estres/F8.csv", delimiter=",")
EF8_2 = EF8_2.astype(np.float64)

EFC5_2 = genfromtxt("Extraccion/Sujeto_2/Estres/FC5.csv", delimiter=",")
EFC5_2 = EFC5_2.astype(np.float64)

EO2_2 = genfromtxt("Extraccion/Sujeto_2/Estres/O2.csv", delimiter=",")
EO2_2 = EO2_2.astype(np.float64)

EP8_2 = genfromtxt("Extraccion/Sujeto_2/Estres/P8.csv", delimiter=",")
EP8_2 = EP8_2.astype(np.float64)


ET8_2 = genfromtxt("Extraccion/Sujeto_2/Estres/T8.csv", delimiter=",")
ET8_2 = ET8_2.astype(np.float64)

EF7_2 = genfromtxt("Extraccion/Sujeto_2/Estres/F7.csv", delimiter=",")
EF7_2 = EF7_2.astype(np.float64)


ET7_2 = genfromtxt("Extraccion/Sujeto_2/Estres/T7.csv", delimiter=",")
ET7_2 = ET7_2.astype(np.float64)



###############################################################################
#
# SUJETO 3 Relajado
#
###############################################################################

RAF3_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/AF3.csv", delimiter=",")
RAF3_3 = RAF3_3.astype(np.float64)

RAF4_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/AF4.csv", delimiter=",")
RAF4_3 = RAF4_3.astype(np.float64)


RF3_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/F3.csv", delimiter=",")
RF3_3 = RF3_3.astype(np.float64)


RF8_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/F8.csv", delimiter=",")
RF8_ = RF8_3.astype(np.float64)

RFC5_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/FC5.csv", delimiter=",")
RFC5_3 = RFC5_3.astype(np.float64)

RO2_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/O2.csv", delimiter=",")
RO2_3 = RO2_3.astype(np.float64)

RP8_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/P8.csv", delimiter=",")
RP8_3 = RP8_3.astype(np.float64)


RT8_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/T8.csv", delimiter=",")
RT8_3 = RT8_3.astype(np.float64)

RF7_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/F7.csv", delimiter=",")
RF7_3 = RF7_3.astype(np.float64)


#RT7_3 = genfromtxt("Extraccion/Sujeto_3/Relajado/T7.csv", delimiter=",")
#RT7_3 = RT7_3.astype(np.float64)
###############################################################################
#
# SUJETO 3 Estres
#
###############################################################################

EAF3_3 = genfromtxt("Extraccion/Sujeto_3/Estres/AF3.csv", delimiter=",")
EAF3_3 = EAF3_3.astype(np.float64)

EAF4_3 = genfromtxt("Extraccion/Sujeto_3/Estres/AF4.csv", delimiter=",")
EAF4_3 = EAF4_3.astype(np.float64)


EF3_3 = genfromtxt("Extraccion/Sujeto_3/Estres/F3.csv", delimiter=",")
EF3_3 = EF3_3.astype(np.float64)


EF8_3 = genfromtxt("Extraccion/Sujeto_3/Estres/F8.csv", delimiter=",")
EF8_3 = EF8_3.astype(np.float64)

EFC5_3 = genfromtxt("Extraccion/Sujeto_3/Estres/FC5.csv", delimiter=",")
EFC5_3 = EFC5_3.astype(np.float64)

EO2_3 = genfromtxt("Extraccion/Sujeto_3/Estres/O2.csv", delimiter=",")
EO2_3 = EO2_3.astype(np.float64)

EP8_3 = genfromtxt("Extraccion/Sujeto_3/Estres/P8.csv", delimiter=",")
EP8_3 = EP8_3.astype(np.float64)


ET8_3 = genfromtxt("Extraccion/Sujeto_3/Estres/T8.csv", delimiter=",")
ET8_3 = ET8_3.astype(np.float64)

EF7_3 = genfromtxt("Extraccion/Sujeto_3/Estres/F7.csv", delimiter=",")
EF7_3 = EF7_3.astype(np.float64)


ET7_3 = genfromtxt("Extraccion/Sujeto_3/Estres/T7.csv", delimiter=",")
ET7_3 = ET7_3.astype(np.float64)

###############################################################################
#
# SUJETO 4 Relajado
#
###############################################################################

RAF3_4 = genfromtxt("Extraccion/Sujeto_4/Relajado/AF3.csv", delimiter=",")
RAF3_4 = RAF3_4.astype(np.float64)

RAF4_4 = genfromtxt("Extraccion/Sujeto_4/Relajado/AF4.csv", delimiter=",")
RAF4_4 = RAF4_4.astype(np.float64)


RF3_4 = genfromtxt("Extraccion/Sujeto_4/Relajado/F3.csv", delimiter=",")
RF3_4 = RF3_4.astype(np.float64)


RF8_4 = genfromtxt("Extraccion/Sujeto_4/Relajado/F8.csv", delimiter=",")
RF8_4 = RF8_4.astype(np.float64)

RFC5_4 = genfromtxt("Extraccion/Sujeto_4/Relajado/FC5.csv", delimiter=",")
RFC5_4 = RFC5_4.astype(np.float64)

RO2_4 = genfromtxt("Extraccion/Sujeto_4/Relajado/O2.csv", delimiter=",")
RO2_4 = RO2_4.astype(np.float64)

RP8_4 = genfromtxt("Extraccion/Sujeto_4/Relajado/P8.csv", delimiter=",")
RP8_4 = RP8_4.astype(np.float64)


RT8_4 = genfromtxt("Extraccion/Sujeto_4/Relajado/T8.csv", delimiter=",")
RT8_4 = RT8_4.astype(np.float64)

RF7_4 = genfromtxt("Extraccion/Sujeto_4/Relajado/F7.csv", delimiter=",")
RF7_4 = RF7_4.astype(np.float64)


###############################################################################
#
# SUJETO 4 Estres
#
###############################################################################

EAF3_4 = genfromtxt("Extraccion/Sujeto_4/Estres/AF3.csv", delimiter=",")
EAF3_4 = EAF3_4.astype(np.float64)

EAF4_4 = genfromtxt("Extraccion/Sujeto_4/Estres/AF4.csv", delimiter=",")
EAF4_4 = EAF4_4.astype(np.float64)


EF3_4 = genfromtxt("Extraccion/Sujeto_4/Estres/F3.csv", delimiter=",")
EF3_4 = EF3_4.astype(np.float64)


EF8_4 = genfromtxt("Extraccion/Sujeto_4/Estres/F8.csv", delimiter=",")
EF8_4 = EF8_4.astype(np.float64)

EFC5_4 = genfromtxt("Extraccion/Sujeto_4/Estres/FC5.csv", delimiter=",")
EFC5_4 = EFC5_4.astype(np.float64)

EO2_4 = genfromtxt("Extraccion/Sujeto_4/Estres/O2.csv", delimiter=",")
EO2_4 = EO2_4.astype(np.float64)

EP8_4 = genfromtxt("Extraccion/Sujeto_4/Estres/P8.csv", delimiter=",")
EP8_4 = EP8_4.astype(np.float64)

ET8_4 = genfromtxt("Extraccion/Sujeto_4/Estres/T8.csv", delimiter=",")
ET8_4 = ET8_4.astype(np.float64)

EF7_4 = genfromtxt("Extraccion/Sujeto_4/Estres/F7.csv", delimiter=",")
EF7_4 = EF7_4.astype(np.float64)

###############################################################################
#
# SUJETO 5 Relajado
#
###############################################################################



RAF3_5 = genfromtxt("Extraccion/Sujeto_5/Relajado/AF3.csv", delimiter=",")
RAF3_5 = RAF3_5.astype(np.float64)

RAF4_5 = genfromtxt("Extraccion/Sujeto_5/Relajado/AF4.csv", delimiter=",")
RAF4_5 = RAF4_5.astype(np.float64)


RF3_5 = genfromtxt("Extraccion/Sujeto_5/Relajado/F3.csv", delimiter=",")
RF3_5 = RF3_5.astype(np.float64)


RF8_5 = genfromtxt("Extraccion/Sujeto_5/Relajado/F8.csv", delimiter=",")
RF8_5 = RF8_5.astype(np.float64)

RFC_5 = genfromtxt("Extraccion/Sujeto_5/Relajado/FC5.csv", delimiter=",")
RFC_5 = RFC_5.astype(np.float64)

RO2_5 = genfromtxt("Extraccion/Sujeto_5/Relajado/O2.csv", delimiter=",")
RO2_5 = RO2_5.astype(np.float64)

RP8_5 = genfromtxt("Extraccion/Sujeto_5/Relajado/P8.csv", delimiter=",")
RP8_5 = RP8_5.astype(np.float64)


RT8_5 = genfromtxt("Extraccion/Sujeto_5/Relajado/T8.csv", delimiter=",")
RT8_5 = RT8_5.astype(np.float64)


RF7_5 = genfromtxt("Extraccion/Sujeto_5/Relajado/F7.csv", delimiter=",")
RF7_5 = RF7_5.astype(np.float64)
###############################################################################
#
# SUJETO 5 Estres
#
###############################################################################



EAF3_5 = genfromtxt("Extraccion/Sujeto_5/Estres/AF3.csv", delimiter=",")
EAF3_5 = EAF3_5.astype(np.float64)

EAF4_5 = genfromtxt("Extraccion/Sujeto_5/Estres/AF4.csv", delimiter=",")
EAF4_5 = EAF4_5.astype(np.float64)


EF3_5 = genfromtxt("Extraccion/Sujeto_5/Estres/F3.csv", delimiter=",")
EF3_5 = EF3_5.astype(np.float64)


EF8_5 = genfromtxt("Extraccion/Sujeto_5/Estres/F8.csv", delimiter=",")
EF8_5 = EF8_5.astype(np.float64)

EFC_5 = genfromtxt("Extraccion/Sujeto_5/Estres/FC5.csv", delimiter=",")
EFC_5 = EFC_5.astype(np.float64)

EO2_5 = genfromtxt("Extraccion/Sujeto_5/Estres/O2.csv", delimiter=",")
EO2_5 = EO2_5.astype(np.float64)

EP8_5 = genfromtxt("Extraccion/Sujeto_5/Estres/P8.csv", delimiter=",")
EP8_5 = EP8_5.astype(np.float64)


ET8_5 = genfromtxt("Extraccion/Sujeto_5/Estres/T8.csv", delimiter=",")
ET8_5 = ET8_5.astype(np.float64)


EF7_5 = genfromtxt("Extraccion/Sujeto_5/Estres/F7.csv", delimiter=",")
EF7_5 = EF7_5.astype(np.float64)
###############################################################################
#
# SUJETO 6 Relajado
#
###############################################################################



RAF3_6 = genfromtxt("Extraccion/Sujeto_5/Relajado/AF3.csv", delimiter=",")
RAF3_6 = RAF3_6.astype(np.float64)

RAF4_6 = genfromtxt("Extraccion/Sujeto_5/Relajado/AF4.csv", delimiter=",")
RAF4_6 = RAF4_6.astype(np.float64)


RF3_6 = genfromtxt("Extraccion/Sujeto_5/Relajado/F3.csv", delimiter=",")
RF3_6 = RF3_6.astype(np.float64)


RF8_6 = genfromtxt("Extraccion/Sujeto_5/Relajado/F8.csv", delimiter=",")
RF8_6 = RF8_6.astype(np.float64)

RFC_6 = genfromtxt("Extraccion/Sujeto_5/Relajado/FC5.csv", delimiter=",")
RFC_6 = RFC_6.astype(np.float64)

RO2_6 = genfromtxt("Extraccion/Sujeto_5/Relajado/O2.csv", delimiter=",")
RO2_6 = RO2_6.astype(np.float64)

RP8_6 = genfromtxt("Extraccion/Sujeto_5/Relajado/P8.csv", delimiter=",")
RP8_6 = RP8_6.astype(np.float64)


RT8_6 = genfromtxt("Extraccion/Sujeto_5/Relajado/T8.csv", delimiter=",")
RT8_6 = RT8_6.astype(np.float64)


RF7_6 = genfromtxt("Extraccion/Sujeto_5/Relajado/F7.csv", delimiter=",")
RF7_6 = RF7_6.astype(np.float64)
###############################################################################
#
# SUJETO 6 Estres
#
###############################################################################

EAF3_6 = genfromtxt("Extraccion/Sujeto_5/Estres/AF3.csv", delimiter=",")
EAF3_6 = EAF3_6.astype(np.float64)

EAF4_6 = genfromtxt("Extraccion/Sujeto_5/Estres/AF4.csv", delimiter=",")
EAF4_6 = EAF4_6.astype(np.float64)


EF3_6 = genfromtxt("Extraccion/Sujeto_5/Estres/F3.csv", delimiter=",")
EF3_6 = EF3_6.astype(np.float64)


EF8_6 = genfromtxt("Extraccion/Sujeto_5/Estres/F8.csv", delimiter=",")
EF8_6 = EF8_6.astype(np.float64)

EFC_6 = genfromtxt("Extraccion/Sujeto_5/Estres/FC5.csv", delimiter=",")
EFC_6 = EFC_6.astype(np.float64)

EO2_6 = genfromtxt("Extraccion/Sujeto_5/Estres/O2.csv", delimiter=",")
EO2_6 = EO2_6.astype(np.float64)

EP8_6 = genfromtxt("Extraccion/Sujeto_5/Estres/P8.csv", delimiter=",")
EP8_6 = EP8_6.astype(np.float64)


ET8_6 = genfromtxt("Extraccion/Sujeto_5/Estres/T8.csv", delimiter=",")
ET8_6 = ET8_6.astype(np.float64)


EF7_6 = genfromtxt("Extraccion/Sujeto_5/Estres/F7.csv", delimiter=",")
EF7_6 = EF7_6.astype(np.float64)


##############################################################################
#
# SUJETO 7 Relajado
#
###############################################################################



RAF3_7 = genfromtxt("Extraccion/Sujeto_5/Relajado/AF3.csv", delimiter=",")
RAF3_7 = RAF3_7.astype(np.float64)

RAF4_7 = genfromtxt("Extraccion/Sujeto_5/Relajado/AF4.csv", delimiter=",")
RAF4_7 = RAF4_7.astype(np.float64)


RF3_7 = genfromtxt("Extraccion/Sujeto_5/Relajado/F3.csv", delimiter=",")
RF3_7 = RF3_7.astype(np.float64)


RF8_7 = genfromtxt("Extraccion/Sujeto_5/Relajado/F8.csv", delimiter=",")
RF8_7 = RF8_7.astype(np.float64)

RFC_7 = genfromtxt("Extraccion/Sujeto_5/Relajado/FC5.csv", delimiter=",")
RFC_7 = RFC_7.astype(np.float64)

RO2_7 = genfromtxt("Extraccion/Sujeto_5/Relajado/O2.csv", delimiter=",")
RO2_7 = RO2_7.astype(np.float64)

RP8_7 = genfromtxt("Extraccion/Sujeto_5/Relajado/P8.csv", delimiter=",")
RP8_7 = RP8_7.astype(np.float64)


RT8_7 = genfromtxt("Extraccion/Sujeto_5/Relajado/T8.csv", delimiter=",")
RT8_7 = RT8_7.astype(np.float64)


RF7_7 = genfromtxt("Extraccion/Sujeto_5/Relajado/F7.csv", delimiter=",")
RF7_7 = RF7_7.astype(np.float64)
###############################################################################
#
# SUJETO 7 Estres
#
###############################################################################



EAF3_7 = genfromtxt("Extraccion/Sujeto_5/Estres/AF3.csv", delimiter=",")
EAF3_7 = EAF3_7.astype(np.float64)

EAF4_7 = genfromtxt("Extraccion/Sujeto_5/Estres/AF4.csv", delimiter=",")
EAF4_7 = EAF4_7.astype(np.float64)


EF3_7 = genfromtxt("Extraccion/Sujeto_5/Estres/F3.csv", delimiter=",")
EF3_7 = EF3_7.astype(np.float64)


EF8_7 = genfromtxt("Extraccion/Sujeto_5/Estres/F8.csv", delimiter=",")
EF8_7 = EF8_7.astype(np.float64)

EFC_7 = genfromtxt("Extraccion/Sujeto_5/Estres/FC5.csv", delimiter=",")
EFC_7 = EFC_7.astype(np.float64)

EO2_7 = genfromtxt("Extraccion/Sujeto_5/Estres/O2.csv", delimiter=",")
EO2_7 = EO2_7.astype(np.float64)

EP8_7 = genfromtxt("Extraccion/Sujeto_5/Estres/P8.csv", delimiter=",")
EP8_7 = EP8_7.astype(np.float64)


ET8_7 = genfromtxt("Extraccion/Sujeto_5/Estres/T8.csv", delimiter=",")
ET8_7 = ET8_7.astype(np.float64)


EF7_7 = genfromtxt("Extraccion/Sujeto_5/Estres/F7.csv", delimiter=",")
EF7_7 = EF7_7.astype(np.float64)


##############################################################################
#
# SUJETO 8 Relajado
#
###############################################################################



RAF3_8 = genfromtxt("Extraccion/Sujeto_5/Relajado/AF3.csv", delimiter=",")
RAF3_8 = RAF3_8.astype(np.float64)

RAF4_8 = genfromtxt("Extraccion/Sujeto_5/Relajado/AF4.csv", delimiter=",")
RAF4_8 = RAF4_8.astype(np.float64)


RF3_8 = genfromtxt("Extraccion/Sujeto_5/Relajado/F3.csv", delimiter=",")
RF3_8 = RF3_8.astype(np.float64)


RF8_8 = genfromtxt("Extraccion/Sujeto_5/Relajado/F8.csv", delimiter=",")
RF8_8 = RF8_8.astype(np.float64)

RFC_8 = genfromtxt("Extraccion/Sujeto_5/Relajado/FC5.csv", delimiter=",")
RFC_8 = RFC_8.astype(np.float64)

RO2_8 = genfromtxt("Extraccion/Sujeto_5/Relajado/O2.csv", delimiter=",")
RO2_8 = RO2_8.astype(np.float64)

RP8_8 = genfromtxt("Extraccion/Sujeto_5/Relajado/P8.csv", delimiter=",")
RP8_8 = RP8_8.astype(np.float64)


RT8_8 = genfromtxt("Extraccion/Sujeto_5/Relajado/T8.csv", delimiter=",")
RT8_8 = RT8_8.astype(np.float64)


RF7_8 = genfromtxt("Extraccion/Sujeto_5/Relajado/F7.csv", delimiter=",")
RF7_8 = RF7_8.astype(np.float64)
###############################################################################
#
# SUJETO 8 Estres
#
###############################################################################



EAF3_8 = genfromtxt("Extraccion/Sujeto_5/Estres/AF3.csv", delimiter=",")
EAF3_8 = EAF3_8.astype(np.float64)

EAF4_8 = genfromtxt("Extraccion/Sujeto_5/Estres/AF4.csv", delimiter=",")
EAF4_8 = EAF4_8.astype(np.float64)


EF3_8 = genfromtxt("Extraccion/Sujeto_5/Estres/F3.csv", delimiter=",")
EF3_8 = EF3_8.astype(np.float64)


EF8_8 = genfromtxt("Extraccion/Sujeto_5/Estres/F8.csv", delimiter=",")
EF8_8 = EF8_8.astype(np.float64)

EFC_8 = genfromtxt("Extraccion/Sujeto_5/Estres/FC5.csv", delimiter=",")
EFC_8 = EFC_8.astype(np.float64)

EO2_8 = genfromtxt("Extraccion/Sujeto_5/Estres/O2.csv", delimiter=",")
EO2_8 = EO2_8.astype(np.float64)

EP8_8 = genfromtxt("Extraccion/Sujeto_5/Estres/P8.csv", delimiter=",")
EP8_8 = EP8_8.astype(np.float64)


ET8_8 = genfromtxt("Extraccion/Sujeto_5/Estres/T8.csv", delimiter=",")
ET8_8 = ET8_8.astype(np.float64)


EF7_8 = genfromtxt("Extraccion/Sujeto_5/Estres/F7.csv", delimiter=",")
EF7_8 = EF7_8.astype(np.float64)

###############################################################################
#
# PLOT RELAJADO ESCENARIO 1 ALPHA
#
###############################################################################

fig = plt.figure()
x_1 = fig.add_subplot(111)




R_AF3_1 = RAF3_1[0:1000:, 0]
R_AF4_1 = RAF4_1[0:1000:, 0 ]
R_F3_1  = RF3_1[0:1000,  0 ]
R_F8_1 = RF8_1[0:1000:, 0 ]
R_FC5_1  = RFC5_1[0:1000:, 0  ]
R_O2_1  = RO2_1[0:1000:, 0  ]
R_P8_1  = RP8_1[0:1000:,0 ]
R_T8_1  = RT8_1[0:1000:,0 ]
R_P7_1  = RP7_1[0:1000:,0 ]
R_T7_1  = RT7_1[0:1000:,0 ]


###############################################################################
E_AF3_1 = EAF3_1[0:1000:, 0 ]
E_AF4_1 = EAF4_1[0:1000:, 0 ]
E_F3_1  = EF3_1[0:1000:,  0 ]
E_F8_1 = EF8_1[0:1000:, 0 ]
E_FC5_1  = EFC5_1[0:1000:, 0  ]
E_O2_1  = EO2_1[0:1000:, 0  ]
E_P8_1  = EP8_1[0:1000:,0 ]
E_T8_1  = ET8_1[0:1000:,0 ]
#E_P7_1  = EP7_1[500:1500:,2 ]
E_T7_1  = ET7_1[0:1000:,0 ]
###############################################################################
R_AF3_2 = RAF3_2[0:1000:, 0 ]
R_AF4_2 = RAF4_2[0:1000:, 0 ]
R_F3_2  = RF3_2[0:1000:,  0 ]
R_F8_2 = RF8_2[0:1000:, 0 ]
R_FC5_2  = RFC5_2[0:1000:, 0  ]
R_O2_2  = RO2_2[0:1000:, 0  ]
R_P8_2  = RP8_2[0:1000:,0 ]
R_T8_2  = RT8_2[0:1000:,0 ]
#R_P7_2  = RP7_2[500:1500:,2 ]
R_T7_2  = RT7_2[0:1000:,0 ]

###############################################################################
E_AF3_2 = EAF3_2[0:1000:,0 ]
E_AF4_2 = EAF4_2[0:1000:, 0 ]
E_F3_2  = EF3_2[0:1000:,  0 ]
E_F8_2 = EF8_2[0:1000:, 0 ]
E_FC5_2  = EFC5_2[0:1000:, 0  ]
E_O2_2  = EO2_2[0:1000:, 0  ]
E_P8_2  = EP8_2[0:1000:,0 ]
E_T8_2  = ET8_2[0:1000:,0 ]

E_T7_2  = ET7_2[0:1000:,0 ]

###############################################################################
R_AF3_3 = RAF3_3[0:1000:, 0 ]
R_AF4_3 = RAF4_3[0:1000:, 0 ]
R_F3_3  = RF3_3[0:1000:,  0 ]
R_F8_3 = RF8_3[0:1000:, 0 ]
R_FC5_3  = RFC5_3[0:1000:, 0  ]
R_O2_3  = RO2_3[0:1000:, 0  ]
R_P8_3  = RP8_3[0:1000:,0 ]
R_T8_3  = RT8_3[0:1000:,0 ]
#R_P7_3  = RP7_3[500:1500:,2 ]
#R_T7_3  = RT7_3[500:1500:,2 ]

###############################################################################
E_AF3_3 = EAF3_3[0:1000:, 0 ]
E_AF4_3 = EAF4_3[0:1000:, 0 ]
E_F3_3  = EF3_3[0:1000:,  0 ]
E_F8_3 = EF8_3[0:1000:, 0 ]
E_FC5_3  = EFC5_3[0:1000:, 0  ]
E_O2_3  = EO2_3[0:1000:, 0  ]
E_P8_3  = EP8_3[0:1000:,0 ]
E_T8_3  = ET8_3[0:1000:,0 ]
#E_P7_3  = EP7_3[500:1500:,2 ]
E_T7_3  = ET7_3[0:1000:,0 ]

###############################################################################

R_AF3_4 = RAF3_4[0:1000:, 0 ]
R_AF4_4 = RAF4_4[0:1000:, 0 ]
R_F3_4  = RF3_4[0:1000:,  0 ]
R_F8_4 = RF8_4[0:1000:, 0 ]
R_FC5_4  = RFC5_4[0:1000:, 0  ]
R_O2_4  = RO2_4[0:1000:, 0  ]
R_P8_4  = RP8_4[0:1000:,0 ]
R_T8_4  = RT8_4[0:1000:,0 ]
#R_P7_4  = RP7_4[500:1500:,2 ]
#R_T7_4  = RT7_4[500:1500:,2 ]

###############################################################################
E_AF3_4 = EAF3_4[0:1000:, 0 ]
E_AF4_4 = EAF4_4[0:1000:, 0 ]
E_F3_4  = EF3_4[0:1000:,  0 ]
E_F8_4 = EF8_4[0:1000:, 0 ]
E_FC5_4  = EFC5_4[0:1000:, 0  ]
E_O2_4  = EO2_4[0:1000:, 0  ]
E_P8_4  = EP8_4[0:1000:,0 ]
E_T8_4  = ET8_4[0:1000:,0 ]
#E_P7_4 = EP7_4[500:1500:,2 ]
#E_T7_4  = ET7_4[500:1500:,2 ]
###############################################################################
R_AF3_5 = RAF3_5[0:1000:, 0 ]
R_AF4_5 = RAF4_5[0:1000:, 0 ]
R_F3_5  = RF3_5[0:1000:,  0 ]
R_F8_5 = RF8_5[0:1000:, 0 ]
R_FC5_5  = RFC_5 [0:1000:, 0  ]
R_O2_5  = RO2_5[0:1000:, 0  ]
R_P8_5  = RP8_5[0:1000:,0 ]
R_T8_5  = RT8_5[0:1000:,0 ]
#R_P7_5  = RP7_5[500:1500:,2 ]
#R_T7_5  = RT7_5[500:1500:,2 ]

###############################################################################
E_AF3_5 = EAF3_5[0:1000:, 0 ]
E_AF4_5 = EAF4_5[0:1000:, 0 ]
E_F3_5  = EF3_5[0:1000:,  0 ]
E_F8_5 = EF8_5[0:1000:, 0 ]
E_FC5_5  = EFC_5[0:1000:, 0  ]
E_O2_5  = EO2_5[0:1000:, 0  ]
E_P8_5  = EP8_5[0:1000:,0 ]
E_T8_5  = ET8_5[0:1000:,0 ]
#E_P7_5 = EP7_5[500:1500:,2 ]
#E_T7_5  = ET7_5[500:1500:,2 ]


###############################################################################
R_AF3_6 = RAF3_6[0:1000:, 0]
R_AF4_6 = RAF4_6[0:1000:, 0 ]
R_F3_6  = RF3_6[0:1000,  0 ]
R_F8_6 = RF8_6[0:1000:, 0 ]
R_FC5_6  = RFC5_6[0:1000:, 0  ]
R_O2_6  = RO2_6[0:1000:, 0  ]
R_P8_6  = RP8_6[0:1000:,0 ]
R_T8_6  = RT8_6[0:1000:,0 ]
R_P7_6  = RP7_6[0:1000:,0 ]
R_T7_6  = RT7_6[0:1000:,0 ]


###############################################################################
E_AF3_6 = EAF3_6[0:1000:, 0 ]
E_AF4_6 = EAF4_6[0:1000:, 0 ]
E_F3_6  = EF3_6[0:1000:,  0 ]
E_F8_6 = EF8_6[0:1000:, 0 ]
E_FC5_6  = EFC5_6[0:1000:, 0  ]
E_O2_6  = EO2_6[0:1000:, 0  ]
E_P8_6  = EP8_6[0:1000:,0 ]
E_T8_6  = ET8_6[0:1000:,0 ]
#E_P7_6  = EP7_6[500:1500:,2 ]
E_T7_6  = ET7_6[0:1000:,0 ]
###############################################################################
R_AF3_7 = RAF3_7[0:1000:, 0 ]
R_AF4_7 = RAF4_7[0:1000:, 0 ]
R_F3_7  = RF3_7[0:1000:,  0 ]
R_F8_7 = RF8_7[0:1000:, 0 ]
R_FC5_7  = RFC5_7[0:1000:, 0  ]
R_O2_7  = RO2_7[0:1000:, 0  ]
R_P8_7  = RP8_7[0:1000:,0 ]
R_T8_7  = RT8_7[0:1000:,0 ]
#R_P7_7  = RP7_7[500:1500:,2 ]
R_T7_7  = RT7_7[0:1000:,0 ]

###############################################################################
E_AF3_7 = EAF3_7[0:1000:, 0 ]
E_AF4_7 = EAF4_7[0:1000:, 0 ]
E_F3_7  = EF3_7[0:1000:,  0 ]
E_F8_7 = EF8_7[0:1000:, 0 ]
E_FC5_7  = EFC5_7[0:1000:, 0  ]
E_O2_7  = EO2_7[0:1000:, 0  ]
E_P8_7  = EP8_7[0:1000:,0 ]
E_T8_7  = ET8_7[0:1000:,0 ]
#E_P7_7  = EP7_7[500:1500:,2 ]
E_T7_7  = ET7_7[0:1000:,0 ]

###############################################################################
E_AF3_8 = EAF3_8[0:1000:,0 ]
E_AF4_8 = EAF4_8[0:1000:, 0 ]
E_F3_8  = EF3_8[0:1000:,  0 ]
E_F8_8 = EF8_8[0:1000:, 0 ]
E_FC5_8  = EFC5_8[0:1000:, 0  ]
E_O2_8  = EO2_8[0:1000:, 0  ]
E_P8_8  = EP8_8[0:1000:,0 ]
E_T8_8  = ET8_8[0:1000:,0 ]
E_T7_8  = ET7_8[0:1000:,0 ]

###############################################################################
R_AF3_8 = RAF3_8[0:1000:, 0 ]
R_AF4_8 = RAF4_8[0:1000:, 0 ]
R_F3_8  = RF3_8[0:1000:,  0 ]
R_F8_8 = RF8_8[0:1000:, 0 ]
R_FC5_8  = RFC5_8[0:1000:, 0  ]
R_O2_8  = RO2_8[0:1000:, 0  ]
R_P8_8  = RP8_8[0:1000:,0 ]
R_T8_8  = RT8_8[0:1000:,0 ]
#R_P7_8  = RP7_8[500:1500:,2 ]
#R_T7_8  = RT7_8[500:1500:,2 ]

###############################################################################


SujE_1=numpy.array([E_AF3_1,E_AF4_1,E_F3_1,E_F8_1,E_FC5_1,E_O2_1,E_P8_1,E_T8_1])
SujE_2=numpy.array([E_AF3_2,E_AF4_2,E_F3_2,E_F8_2,E_FC5_2,E_O2_2,E_P8_2,E_T8_2])
SujE_3=numpy.array([E_AF3_3,E_AF4_3,E_F3_3,E_F8_3,E_FC5_3,E_O2_3,E_P8_3,E_T8_3])
SujE_4=numpy.array([E_AF3_4,E_AF4_4,E_F3_4,E_F8_4,E_FC5_4,E_O2_4,E_P8_4,E_T8_4])
SujE_5=numpy.array([E_AF3_5,E_AF4_5,E_F3_5,E_F8_5,E_FC5_5,E_O2_5,E_P8_5,E_T8_5])
SujE_6=numpy.array([E_AF3_6,E_AF4_6,E_F3_6,E_F8_6,E_FC5_6,E_O2_6,E_P8_6,E_T8_6])
SujE_7=numpy.array([E_AF3_7,E_AF4_7,E_F3_7,E_F8_7,E_FC5_7,E_O2_7,E_P8_7,E_T8_7])
SujE_8=numpy.array([E_AF3_8,E_AF4_8,E_F3_8,E_F8_8,E_FC5_8,E_O2_8,E_P8_8,E_T8_8])

SujR_1=numpy.array([R_AF3_1,R_AF4_1,R_F3_1,R_F8_1,R_FC5_1,R_O2_1,R_P8_1,R_T8_1])
SujR_2=numpy.array([R_AF3_2,R_AF4_2,R_F3_2,R_F8_2,R_FC5_2,R_O2_2,R_P8_2,R_T8_2])
SujR_3=numpy.array([R_AF3_3,R_AF4_3,R_F3_3,R_F8_3,R_FC5_3,R_O2_3,R_P8_3,R_T8_3])
SujR_4=numpy.array([R_AF3_4,R_AF4_4,R_F3_4,R_F8_4,R_FC5_4,R_O2_4,R_P8_4,R_T8_4])
SujR_5=numpy.array([R_AF3_5,R_AF4_5,R_F3_5,R_F8_5,R_FC5_5,R_O2_5,R_P8_5,R_T8_5])
SujR_6=numpy.array([R_AF3_6,R_AF4_6,R_F3_6,R_F8_6,R_FC5_6,R_O2_6,R_P8_6,R_T8_6])
SujR_7=numpy.array([R_AF3_7,R_AF4_7,R_F3_7,R_F8_7,R_FC5_7,R_O2_7,R_P8_7,R_T8_7])
SujR_8=numpy.array([R_AF3_8,R_AF4_8,R_F3_8,R_F8_8,R_FC5_8,R_O2_8,R_P8_8,R_T8_8])
###############################################################################


def normaliza(array):
    return (array - array.mean()) / array.std()

normalized_r1 = normaliza(SujE_1)
normalized_r2 = normaliza(SujE_2)
normalized_r3 = normaliza(SujE_3)
normalized_r4 = normaliza(SujE_4)
normalized_r5 = normaliza(SujE_5)
normalized_r6 = normaliza(SujE_6)
normalized_r7 = normaliza(SujE_7)
normalized_r8 = normaliza(SujE_8)

normalized_E1 = normaliza(SujR_1)
normalized_E2 = normaliza(SujR_2)
normalized_E3 = normaliza(SujR_3)
normalized_E4 = normaliza(SujR_4)
normalized_E5 = normaliza(SujR_5)
normalized_E6 = normaliza(SujR_6)
normalized_E7 = normaliza(SujR_7)
normalized_E8 = normaliza(SujR_8)



np.savetxt("febrero/DELTA/Relajado.csv",
           np.c_[SujR_1,SujR_2,SujR_3,SujR_4,SujR_5,SujR_6,SujR_7,SujR_8],header="SUJETO_1,SUJETO_2,SUJETO_3,SUJETO_4,SUJETO_5,SUJETO_6,SUJETO_7,SUJETO_8",delimiter=",")

np.savetxt("febrero/DELTA/Estresado.csv",np.c_[SujE_1,SujE_2,SujE_3,SujE_4,SujE_5,SujE_6,SujE_7,SujE_8],header="SUJETO_1,SUJETO_2,SUJETO_3,SUJETO_4,SUJETO_5,SUJETO_6,SUJETO_7,SUJETO_8",delimiter=",")



