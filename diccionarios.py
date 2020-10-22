def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    print(mi_diccionario) # {'llave1': 1, 'llave2': 2, 'llave3': 3}
    print(mi_diccionario['llave2']) # 2

##############
    poblacion_paises = {
        "Colombia": 50,
        "Argentina": 44,
        "Brasil": 210,
    }

    print(poblacion_paises['Colombia']) # 50
    
    ## Bucles:
    for pais in poblacion_paises.keys():
        print(pais) ## Colombia - Argentina - Brasil

    for pais in poblacion_paises.values():
        print(pais) ## 50 - 44 - 210

    for pais in poblacion_paises.items():
        print(pais) ## ('Colombia', 50) - ('Argentina', 44) - ('Brasil', 210)

    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " millones de habitantes")
            # Colombia tiene 50 millones de habitantes
            # Argentina tiene 44 millones de habitantes
            # Brasil tiene 210 millones de habitantes

if __name__ == "__main__":
    run()