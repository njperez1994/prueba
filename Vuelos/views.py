from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from Vuelos.models import viaje

# Create your views here.
def main(request):
    return render(request, 'index.html')

def searchbd(searchdata):
    #contador de vuelos validos
    cont = 0
    print("esta es la fecha de salida " + searchdata[6])
    print(searchdata[0]+" "+searchdata[1]+" "+searchdata[2]+" "+searchdata[3]+" "+searchdata[4])
    if viaje.objects.filter(tipo=searchdata[0]).filter(cantidad=searchdata[1]).filter(clase=searchdata[2]).filter(desde=searchdata[3]).filter(hasta=searchdata[4]):
       compf_fecha = viaje.objects.filter(tipo=searchdata[0]).filter(cantidad=searchdata[1]).filter(clase=searchdata[2]).filter(desde=searchdata[3]).filter(hasta=searchdata[4])

       if(searchdata[6]):
           return con_fecha_regreso(compf_fecha, searchdata)
       else:
           return sin_fecha_regreso(compf_fecha, searchdata)


#funciones para cada caso de fechas de regreso
def sin_fecha_regreso(dta,searchdata):
    cont = 0
    for i in dta:
        if (searchdata[5] == str(i.fechasalida)):
            cont = cont + 1
    return cont

def con_fecha_regreso(dta,searchdata):
    cont = 0
    for i in dta:
        if (searchdata[5] == str(i.fechasalida) and searchdata[6] == str(i.fecharegreso)):
            cont = cont + 1
    return cont

def setdata(request):
    if request.method =='POST':
        tipo = request.POST['tipo_viaje']
        cantidad = request.POST['cantidad_viajeros']
        clase = request.POST['clase']
        desde = request.POST['origen']
        hasta = request.POST['destino']
        salida = request.POST['fecha_salida']
        regreso = request.POST['fecha_regreso']

        #Lista de elementos Proporcionados por el cliente
        lista_datos = [tipo,cantidad,clase,desde,hasta,salida,regreso]

       #comprobando datos introducidos por el usuario
        for iter in range(0,(len(lista_datos)-1)):
            if(lista_datos[iter]):
                msaje ="ok"
            else:
                #si encuentra algun campo vacio que no sea la fecha de regreso entonces lanza un mensaje de error
                return render(request, 'index.html',{'merr':'Error al introducir datos. Compruebe espacios en blanco'})
        # llamando a funcion search para encontrar la entrada en la DB
        data = searchbd(lista_datos)

        if(data):
            if(data == 0):
                #si dta no eta vacio pero es 0 entonces lanzo mms de no encontrado
                dat_to_template = {'listadato':data,'mpos':'no encontrado'}
            else:
                # si dta no eta vacio entonces lanzo mms de Ok
                dat_to_template = {'listadato': data, 'mpos': 'encontrado'}
        else:
            # si dta no esta vacio entonces lanzo mss negativo
            dat_to_template = {'listadato':data,'mnega':'no encontrado'}

        """""
        if data:
            print(data.fecharegreso)
            #print(data.tipo +" "+data.cantidad+" "+data.desde+" "+data.hasta+" "+data.fechasalida +" "+data.fecharegreso)
        else:
            print("No se encontraron Resultados")
        """""
    else:
        return redirect('index.html')
    return render(request, 'index.html',dat_to_template)

"""""
def getdata(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = formvuelos(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = formvuelos()
    return render(request, 'index_form_djago.html', {'form': form})
"""""
