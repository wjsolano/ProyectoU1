def agenteAltavoz():
    """
        Se prepara los estados que tendra el agente, se indica 0 si el altavoz
        hace sonido, mientras que, 1 significa que el altavoz esta en silencio
    """ 
    estados_objetivos={'estadoPasillo1':'0','estadoPasillo2':'0','estadoPasillo3':'0',
    'estadoPasillo4':'0','estadoCajas':'0', 'estadoEstacionamiento':'0','estadoAdministracion':'0',
    'estadoBodega':'0',}
    #el costo siempre inicia en cero
    costo=0
#LLAMANDO A LA FUNCION
agenteAltavoz()