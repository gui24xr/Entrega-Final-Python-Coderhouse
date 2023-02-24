from django.template import Template

lista_especialidades = [("Otorrinolaringologia", "Otorrinolaringologia"), # Lista de tuplas.
                        ("Nutricion", "Nutricion"),
                        ("Psicologia", "Psicologia"),
                        ("Fonoaudiologia", "Fonoaudiologia"),
                        ("Odontologia", "Odontologia"),
                        ("Clinica", "Clinica"),
                         ("Ginecologia", "Ginecologia"),
                        ("Pediatria", "Pediatria"),] 


lista_obras_sociales = [("OSDE", "OSDE"), # Lista de tuplas.
                        ("GALENO", "GALENO"),
                        ("IOMA", "IOMA"),
                        ("CEDIMEC", "CEDIMEC"),
                        ("OSFE", "OSFE"),
                        ("OSECACO", "OSECACO"),
                        ("MEDIFES", "MEDIFES"),
                        ("Otra", "Otra"),
                        ("S/N","S/N")] 

lista_provincias = [("Buenos Aires", "Buenos Aires"), # Lista de tuplas.
                        ("CABA", "CABA"),
                        ("Catamarca", "Catamarca"),
                        ("Chaco","Chaco"),
                        ("Chubut", "Chubut"),
                        ("Cordoba", "Cordoba"),
                        ("Corrientes", "Corrientes"),
                        ("Entre Rios", "Entre Rios"),
                        ("Formosa", "Formosa"),
                        ("Jujuy", "Jujuy"),
                        ("La Pampa", "La Pampa"),
                        ("La Rioja", "La Rioja"),
                        ("Mendoza", "Mendoza"),
                        ("Misiones", "Misiones"),
                        ("Neuquen", "Neuquen"),
                        ("Rio Negro", "Rio Negro"),
                        ("Salta", "Salta"),
                        ("San Juan", "San Juan"),
                        ("San Luis","San Luis"),
                        ("Santa Cruz", "Santa Cruz"),
                        ("Santa Fe", "Santa Fe"),
                        ("Santiago del Estero", "Santiago del Estero"),
                        ("Tierra del Fuego", "Tierra del Fuego"),
                        ("Tucuman", "Tucuman")]
 
                        


def modelo_to_pandas(lista_de_campos,lista_de_datos):

    tabla = pd.DataFrame(lista_de_datos)
    print("DATA FRAME")
    html_tabla = pd.DataFrame.to_html(tabla)
    #print(html_tabla)
    return html_tabla

   

def generar_tabla(lista_de_campos, lista_de_datos):

    #La cuestion es ir concatenando cadenas para formar mi texto html que voy a convertir en template para incluir en un form de la plantilla.
    print("LEN: DATOS: ", len(lista_de_datos))
    
    if len(lista_de_datos)>=1:
        tabla_html ='<table border="1" class="dataframe"><thead><tr style="text-align: left;">'

        
        for campo in lista_de_campos:             #Sumo los encabezados con los nombres de campos.

            cadena_a_sumar = '<th>'+ campo + '</th>'
            tabla_html = tabla_html+cadena_a_sumar

        #Encabezado de verificar
        cadena_a_sumar = '<th>VERIFICAR </th>'
        tabla_html = tabla_html + cadena_a_sumar  #Sumo el primer encabezado.

        # Sumo otro fragmento.
        tabla_html = tabla_html + '</tr></thead><tbody>'    # Preparo para sumar datos.
        
        i=0
        while i<=len(lista_de_datos)-1:                     # Siempre sumo un check a cada fila
        
        
            for campo in lista_de_campos:
            
                if campo in ['APELLIDO','NOMBRE']:
                    cadena_a_sumar = '<td><b><FONT COLOR="blue">'+ (str(lista_de_datos[i].get(str(campo)))).upper() + '</FONT></b></td>'
                    tabla_html = tabla_html + cadena_a_sumar
                else:
                    cadena_a_sumar = '<td>'+ str(lista_de_datos[i].get(str(campo))) + '</td>'
                    tabla_html = tabla_html + cadena_a_sumar

            #checkbox_name = str(lista_de_datos[i].get(str('DNI')))
            #checkbox = '<input type="checkbox" name="' + checkbox_name + '">'
            #tabla_html = tabla_html + '<td>'+ checkbox + '</td>'
        
            tabla_html = tabla_html + '<td><a href="login.html">Ver/Editar</a></td>' 
            tabla_html = tabla_html + '</tr>'
        
            i+=1

        tabla_html = tabla_html + '</tbody></table>'
    
        return Template(tabla_html)
    
    else:
        return Template("NO EXISTEN DATOS PARA SU CONSULTA")


#Agarra el diccionario que devolvio el sevidor y lo procesa para obtener y limpiar las claves que envio
def procesar_lista_verificados(diccionario):

    lista_verificados = list(diccionario.keys()) # Ya tengo las claves que envio el servidor de las que estaban marcadas.
    

    if len(lista_verificados)>1:
        lista_verificados.remove(lista_verificados[0])
        return lista_verificados
    else:
        return [] #Devuelvo una lista vacia si no hay verificados.
    

    
