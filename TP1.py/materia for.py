#promdioPm es promedio primera materia
#primeraM es primera materia
a=3
for a in range (1):                                                                         
    materia1=[input("\n Cargue la primera materia: \n")]
    materia2=[input("\nCargue la segunda materia: \n")]
    materia3=[input("\nCargue la tercera materia: \n")]
    materia4=[input("\nCargue la cuarta materia: \n")]
nota1=[0]
print()
for b in range (3):
    materia1.append(float(input("\n Agrege la nota de "+str(materia1[0])+": \n")))
    materia2.append(float(input("\nAgrege la nota de "+str(materia2[0])+": \n")))
    materia3.append(float(input("\nAgrege la nota de "+str(materia3[0])+": \n")))
    materia4.append(float(input("\nAgrege la nota de "+str(materia4[0])+": \n")))

primeraM=float(materia1[1]+materia1[2]+materia1[3])
promedioPm=float(primeraM/3)
print ('tu promedio de '+str(materia1[0])+' es de '+str(promedioPm))

segundaM=float(materia2[1]+materia2[2]+materia2[3])
promedioSm=float(segundaM/3)
print ('tu promedio de '+str(materia2[0])+' es de '+str(promedioSm))

terceraM=float(materia3[1]+materia3[2]+materia3[3])
promedioTm=float(terceraM/3)
print ('tu promedio de '+str(materia3[0])+' es de '+str(promedioTm))

cuartaM=float(materia4[1]+materia4[2]+materia4[3])
promedioCm=float(cuartaM/3)
print ('tu promedio de '+str(materia4[0])+' es de '+str(promedioCm))

if promedioPm>=8:
    print (str(materia1[0])+" esta promocionada")
if promedioSm>=8:
    print (str(materia2[0])+" esta promocionada")
if promedioTm>=8:
    print (str(materia3[0])+" esta promocionada")
if promedioCm>=8:
    print (str(materia4[0])+" esta promocionada")

if promedioCm<8:
    print (str(materia1[0])+" esta aprobada")
if promedioSm<8:
    print (str(materia2[0])+" esta aprobada")
if promedioTm<8:
    print (str(materia3[0])+" esta aprobada")
if promedioCm<8:
    print (str(materia4[0])+" esta aprobada")

if promedioPm<6:
    print (str(materia1[0])+" esta desaprobada")
if promedioSm<6:
    print (str(materia2[0])+" esta desaprobada")
if promedioTm<6:
    print (str(materia3[0])+" esta desaprobada")
if promedioCm<6:
    print (str(materia4[0])+" esta desaprobada")