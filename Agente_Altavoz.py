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

    """Ciclo for para saber si se desea enviar un mensaje a Pasillo2"""
    for localizacion2 in range(1):
        if estadoSonidoPasillo2 == 0: #SE DESEA ENVIAR UN MENSAJE
            print("--- Pasillo 2 ---")
            print("Enviando mensaje a pasillo 2 por medio de Altavoz")
            estados_objetivos['estadoPasillo2'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con exito")
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
            print("Enviando mensaje a pasillo 3 por medio de Altavoz")
            estados_objetivos['estadoPasillo3'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con exito")
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
            print("Enviando mensaje a pasillo 4 por medio de Altavoz")
            estados_objetivos['estadoPasillo4'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con exito")
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
            print("Enviando mensaje a las cajas por medio de Altavoz")
            estados_objetivos['estadoCajas'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con exito")
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
            print("Enviando mensaje al estacionamiento por medio de Altavoz")
            estados_objetivos['estadoEstacionamiento'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con exito")
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
            print("Enviando mensaje a administracion por medio de Altavoz")
            estados_objetivos['estadoAdministracion'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con exito")
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
            print("Enviando mensaje a bodega por medio de Altavoz")
            estados_objetivos['estadoBodega'] = 0 #ASIGNANDO ESTADO DE SONIDO
            costo+=1                              #AUMENTANDO COSTO
            print("Mensaje enviado por altavoz con exito")
            print("Costo actual: "+str(costo))    #MOSTRANDO EL COSTO  
        elif estadoSonidoBodega == 1:          #SI NO SE DESEA ENVIAR UN MENSAJE
            print("--- Bodega ---")
            print("No se desea enviar mensaje")
            estados_objetivos['estadoBodega'] = 1 #ASIGNANDO ESTADO DE SILENCIO 
            print("Costo actual: "+str(costo))      #MOSTRANDO EL COSTO


    #estado y costo final
    print("El estado final de cada localizacion es el siguiente: ")
    print(estados_objetivos)
    print("Costo Final: " + str(costo))
  


#LLAMANDO A LA FUNCION
agenteAltavoz()