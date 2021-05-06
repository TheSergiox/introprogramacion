import matplotlib.pyplot as plt

#Grafico de Barras
ingresos = [834,100,740,726,525,627,637,858,792,822,910,919]
meses = ['Enero','Febrero','Marzo','Abril','Mayor','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
plt.bar(meses, ingresos, width=0.7, color='b')
#-----------------------
plt.title('Dienero que ingresa por mes de un empleado durante el 2020')
plt.xlabel('Meses del año')
plt.ylabel('Ingresos en miles de Pesos')
plt.savefig('graficoBIngresos.png')
#-----------------------
plt.show()


#Grafico Torta
pieLabels =['Bogota','Medellin','Barranquilla','Cali','Bucaramanga']
sizes =[63.72,72.863,83.93,42.28,32.72]
explode = [0.1,0,0,0,0]
def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento

    for i in range (len(labels)):
        pieLabels[i] += indicador+str(round(sizes[i]/acumulador*100,2)) +'%'

etiquetarElementosPorcentuales(sizes, pieLabels , '-')
plt.pie(sizes,labels=pieLabels,explode=explode, shadow = 0.5, counterclock = 1)
#----------------------------
plt.title('Ciudades principales de Colombia')
plt.savefig('GraficoTCiudades.png')
#----------------------------
plt.show()