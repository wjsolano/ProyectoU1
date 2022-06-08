def agenteAltavoz():
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
        Se pregunta al usuario por cada localizacion, si desea enviar un mensaje por medio del 
        altavoz. En el caso de introducir 1 se dirige a la siguiente localizacion. Adi hasta la 
        ultima localizacion que es la bodega.
    """
    estadoSonidoPasillo1=int(input("Ingrese 0 si desea enviar un mensaje al Pasillo1, 1 para pasar a la siguente localizacion: ")) 
    estadoSonidoPasillo2=int(input("Ingrese 0 si desea enviar un mensaje al Pasillo2, 1 para pasar a la siguente localizacion: ") )
    estadoSonidoPasillo3=int(input("Ingrese 0 si desea enviar un mensaje al Pasillo3, 1 para pasar a la siguente localizacion: ") )
    estadoSonidoPasillo4=int(input("Ingrese 0 si desea enviar un mensaje al Pasillo4, 1 para pasar a la siguente localizacion: ") )
    estadoSonidoCajas=int(input("Ingrese 0 si desea enviar un mensaje a las cajas, 1 para pasar a la siguente localizacion: ") )
    estadoSonidoEstacionamiento=int(input("Ingrese 0 si desea enviar un mensaje al estacionamiento, 1 para pasar a la siguente localizacion: ")) 
    estadoSonidoAdministracion=int(input("Ingrese 0 si desea enviar un mensaje a la administracion, 1 para pasar a la siguente localizacion: ") )
    estadoSonidoBodega=int(input("Ingrese 0 si desea enviar un mensaje a la Bodega, 1 para terminar con las localizaciones: ") )
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
    print("El estado inicial de cada localizacion es:" + str(estados_objetivos))

    """
    Para cada localizacion se realiza una accion si el usuario desea enviar un mensaje o no. Para
    ello se hace un recorrido for una sola vez, en la que se pondra condicionales.
    """
    for localizacion1 in range(1):
        if estadoSonidoPasillo1 == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 1 ---")
            print("Enviando mensaje a pasillo 1 por medio de Altavoz")
            estados_objetivos['estadoPasillo1'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con exito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoPasillo1 == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 1 ---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoPasillo1'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO 


    #estado y costo final
    print("El estado final de cada localizacion es el siguiente: ")
    print(estados_objetivos)
    print("Costo Final: " + str(costo))
  


#LLAMANDO A LA FUNCION
agenteAltavoz()