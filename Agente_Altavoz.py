"""
Creando la clase ExcepcionPersonalizada para como dice el nombre, crear una expcepción
que nosotros mismos vamos a personalizar, se le acrega como parámetro un valor tipo
excepción.
"""
class ExcepcionPersonalizada(Exception):
    #constructor que recibe el mensae cuando se haga la excepcion
    def __init__(self, mensaje):
        super().__init__(mensaje)
mensaje = "¡Excepción activada! Algo salió mal."

"""
Se crea la clase generar Excepción que recibe como parámtro un número entero,
el cual se aplica las condicionales para que solo se pueda recibir 1 y 0.
"""
def generarExcepcion(num):
    #valor incertado no valido
    if (num >1):
        raise ExcepcionPersonalizada(mensaje)
    else:
        #valor incertado no valido
        if(num<0):
            raise ExcepcionPersonalizada(mensaje)
        else:
            #EL VALOR SI ES 1 O 0
            print("Registro exitoso")

"""
La siguiente función averigua el método de mensaje que el usaurio desea usar
Puede ser por medio de voz que es el Audio o por Teclado que es escrito, recibe
como parámetro el tipo de mensaje que escribe el usuario
"""
def generarExcepcionMetodoMensaje(metodoMensaje):
    if (metodoMensaje=="Audio"):
        #En el caso de escocger audio simula que el usuario habla por el microfono
        print("***DICIENDO MENSAJE***")
    elif(metodoMensaje=="Teclado"):
        #En el caso de escocger teclado simula que el usuario escribe por teclado
        print("***ESCRIBIENDO MENSAJE***")
    else:
        #EN EL CASO DE NO HABER INSERTADO EL método CORRECTAMENTE DAR ERROR
        raise ExcepcionPersonalizada(mensaje)

"""
Función para preguntar al usuario cual de las dos opciones desea usar para
enviar le mensaje, no recibirá ningun parámetros
"""     
def preguntarEnvioMensaje():
    try:
        #preguntando al usuario que tipo de mensaje desea usar
        metodoMensaje=input("Desea enviar el mensaje por Audio o por Teclado: ")
        #Enviando el tipo de mensaje a la classe excepcion mensaje
        generarExcepcionMetodoMensaje(metodoMensaje) 
    except ExcepcionPersonalizada:
        print("Error: Ingrese la palabra Audio o Teclado ")
        quit()                              #Cerrando el programa       


"""
Se crea una función que sera para el agente de altavoz, el cual recibe los parámetros de los estados
de cada localización con la que se esta trabajando
"""
def agenteAltavoz(estadoSonidoPasillo1,estadoSonidoPasillo2,estadoSonidoPasillo3,estadoSonidoPasillo4,estadoSonidoCajas,estadoSonidoEstacionamiento,estadoSonidoAdministracion,estadoSonidoBodega):
    """
        Se prepara los estados que tendra el agente, se indica 0 si el altavoz
        hace sonido, mientras que, 1 significa que el altavoz esta en silencio
    """ 
    estados_objetivos={'estadoPasillo1':0,'estadoPasillo2':0,'estadoPasillo3':0,
    'estadoPasillo4':0,'estadoCajas':0, 'estadoEstacionamiento':0,'estadoAdministracion':0,
    'estadoBodega':0,}
    #SE INICIALIZA EL COSTO EN CERO 
    costo=0
    """
        Se pregunta al usuario por cada localización, si desea enviar un mensaje por medio del 
        altavoz. En el caso de introducir 1 se dirige a la siguiente localización. Adi hasta la 
        ultima localización que es la bodega.
    """
        

        
    """
    Una vez se tiene el estado de todas las localizaciones, se envian hacia el arreglo que se llama
    estados_objetivos
    """
    estados_objetivos['estadoPasillo1'] = estadoSonidoPasillo1
    estados_objetivos['estadoPasillo2'] = estadoSonidoPasillo2
    estados_objetivos['estadoPasillo3'] = estadoSonidoPasillo3
    estados_objetivos['estadoPasillo4'] = estadoSonidoPasillo4
    estados_objetivos['estadoCajas'] = estadoSonidoCajas
    estados_objetivos['estadoEstacionamiento'] = estadoSonidoEstacionamiento
    estados_objetivos['estadoAdministracion'] = estadoSonidoAdministracion
    estados_objetivos['estadoBodega'] = estadoSonidoBodega

    #mostrar el array del estado inicial de cada una de las zonas
    print("El estado inicial de cada localización es:" + str(estados_objetivos))

    """
    Para cada localización se realiza una accion si el usuario desea enviar un mensaje o no. Para
    ello se hace un recorrido for una sola vez, en la que se pondra condicionales.
    """
    for localizacion1 in range(1):
        if estadoSonidoPasillo1 == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 1 ---")
            preguntarEnvioMensaje() #Llamando al función para preguntar como enviar mensaje
            print("Enviando mensaje a pasillo 1 por medio de Altavoz")
            estados_objetivos['estadoPasillo1'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con éxito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoPasillo1 == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 1 ---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoPasillo1'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO 

    """Ciclo for para saber si se desea enviar un mensaje a Pasillo2"""
    for localizacion2 in range(1):
        if estadoSonidoPasillo2 == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 2 ---")
            preguntarEnvioMensaje()  #Llamando al función para preguntar como enviar mensaje
            print("Enviando mensaje a pasillo 2 por medio de Altavoz")
            estados_objetivos['estadoPasillo2'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con éxito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoPasillo2 == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 2---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoPasillo2'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO 

    """Ciclo for para saber si se desea enviar un mensaje a Pasillo23"""
    for localizacion3 in range(1):
        if estadoSonidoPasillo3 == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 3 ---")
            preguntarEnvioMensaje()  #Llamando al función para preguntar como enviar mensaje
            print("Enviando mensaje a pasillo 3 por medio de Altavoz")
            estados_objetivos['estadoPasillo3'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con éxito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoPasillo3 == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 3 ---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoPasillo3'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO 

    """Ciclo for para saber si se desea enviar un mensaje a Pasillo4"""
    for localizacion4 in range(1):
        if estadoSonidoPasillo4 == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 4 ---")
            preguntarEnvioMensaje()  #Llamando al función para preguntar como enviar mensaje
            print("Enviando mensaje a pasillo 4 por medio de Altavoz")
            estados_objetivos['estadoPasillo4'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con éxito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoPasillo4 == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 4 ---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoPasillo4'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO 

    """Ciclo for para saber si se desea enviar un mensaje a Cajas"""
    for localizacion5 in range(1):
        if estadoSonidoCajas == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Cajas ---")
            preguntarEnvioMensaje()  #Llamando al función para preguntar como enviar mensaje
            print("Enviando mensaje a las cajas por medio de Altavoz")
            estados_objetivos['estadoCajas'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con éxito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoCajas == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Cajas ---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoCajas'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO 

    """Ciclo for para saber si se desea enviar un mensaje a Estacionamiento"""
    for localizacion6 in range(1):
        if estadoSonidoEstacionamiento == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Estacionamiento ---")
            preguntarEnvioMensaje()   #Llamando al función para preguntar como enviar mensaje
            print("Enviando mensaje al estacionamiento por medio de Altavoz")
            estados_objetivos['estadoEstacionamiento'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con éxito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoEstacionamiento == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Estacionamiento ---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoEstacionamiento'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO

    """Ciclo for para saber si se desea enviar un mensaje a Administracion"""
    for localizacion7 in range(1):
        if estadoSonidoAdministracion == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Administracion ---")
            preguntarEnvioMensaje()   #Llamando al función para preguntar como enviar mensaje
            print("Enviando mensaje a administracion por medio de Altavoz")
            estados_objetivos['estadoAdministracion'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con éxito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoAdministracion == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Administracion ---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoAdministracion'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO

    """Ciclo for para saber si se desea enviar un mensaje a Bodega"""
    for localizacion8 in range(1):
        if estadoSonidoBodega == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Bodega ---")
            preguntarEnvioMensaje()  #Llamando al función para preguntar como enviar mensaje
            print("Enviando mensaje a bodega por medio de Altavoz")
            estados_objetivos['estadoBodega'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con éxito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoBodega == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Bodega ---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoBodega'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO


    #estado y costo final
    print("El estado final de cada localización es el siguiente: ")
    print(estados_objetivos)
    print("Costo Final: " + str(costo))


  
if __name__ == "__main__":

    #Solicitando los valores dentro de un try por si existe un error
    try:
        """"
        Solicitando al usuario si quiere o no enviar un mensaje a cada una de las zonas
        """
        estadoSonidoPasillo1=int(input("Ingrese 0 si desea enviar un mensaje al Pasillo1, 1 para pasar a la siguente localización: ")) 
        generarExcepcion(estadoSonidoPasillo1) #ENVIANDO DATO A LA EXCEPCIÓN
        estadoSonidoPasillo2=int(input("Ingrese 0 si desea enviar un mensaje al Pasillo2, 1 para pasar a la siguente localización: ") )
        generarExcepcion(estadoSonidoPasillo2) #ENVIANDO DATO A LA EXCEPCIÓN
        estadoSonidoPasillo3=int(input("Ingrese 0 si desea enviar un mensaje al Pasillo3, 1 para pasar a la siguente localización: ") )
        generarExcepcion(estadoSonidoPasillo3)  #ENVIANDO DATO A LA EXCEPCIÓN
        estadoSonidoPasillo4=int(input("Ingrese 0 si desea enviar un mensaje al Pasillo4, 1 para pasar a la siguente localización: ") )
        generarExcepcion(estadoSonidoPasillo4)  #ENVIANDO DATO A LA EXCEPCIÓN
        estadoSonidoCajas=int(input("Ingrese 0 si desea enviar un mensaje a las cajas, 1 para pasar a la siguente localización: ") )
        generarExcepcion(estadoSonidoCajas) #ENVIANDO DATO A LA EXCEPCIÓN
        estadoSonidoEstacionamiento=int(input("Ingrese 0 si desea enviar un mensaje al estacionamiento, 1 para pasar a la siguente localización: ")) 
        generarExcepcion(estadoSonidoEstacionamiento)  #ENVIANDO DATO A LA EXCEPCIÓN
        estadoSonidoAdministracion=int(input("Ingrese 0 si desea enviar un mensaje a la administracion, 1 para pasar a la siguente localización: ") )
        generarExcepcion(estadoSonidoAdministracion)  #ENVIANDO DATO A LA EXCEPCIÓN
        estadoSonidoBodega=int(input("Ingrese 0 si desea enviar un mensaje a la Bodega, 1 para terminar con las localizaciones: ") )
        generarExcepcion(estadoSonidoBodega)  #ENVIANDO DATO A LA EXCEPCIÓN
    #Excepcion activada en el caso de que el usuario ingrese una letra
    except(ValueError):
        print("Error: Asegurese de insertar números")
        quit() #terminando ejecución

    #Excepcion activada en el caso de que el usuario ingrese un numero difereten que 1 o 0
    except ExcepcionPersonalizada:
        print("Error: Inserte 1 o 0 según lo solicitado ")
        quit() #terminando ejecución
    #LLAMANDO A LA función E INSERTANDO LOS PARÁMETROS
    agenteAltavoz(estadoSonidoPasillo1,estadoSonidoPasillo2,estadoSonidoPasillo3,estadoSonidoPasillo4,estadoSonidoCajas,estadoSonidoEstacionamiento,estadoSonidoAdministracion,estadoSonidoBodega)