import random

# Definir listas de alimentos por categoría
pescados_mariscos = ['salmón', 'atún', 'caballa', 'sardinas', 'arenque', 'trucha', 'camarones', 'langostinos', 'calamares']
proteinas = ['pollo', 'pavo', 'huevo', 'tofu']
verduras_bajas_en_carbohidratos = ['espinacas', 'brócoli', 'coliflor', 'espárragos', 'lechuga', 'pepinillos', 'calabacín', 'alcachofa', 'apio', 'berenjena', 'cebolla', 'puerro', 'champiñones']
grasas_saludables = ['aguacate', 'nueces', 'almendras', 'aceite de oliva', 'semillas de chía', 'palta']
frutas_bajas_en_azucar = ['fresas', 'frambuesas', 'moras', 'arándanos', 'kiwi', 'manzana verde', 'pera', 'ciruela', 'cerezas', 'melón']

# Función para generar una comida baja en carbohidratos
def generar_comida_baja_en_carbohidratos():
    comida = []
    comida.append(random.choice(pescados_mariscos))
    comida.append(random.choice(proteinas))
    comida.append(random.choice(verduras_bajas_en_carbohidratos))
    comida.append(random.choice(grasas_saludables))
    comida.append(random.choice(frutas_bajas_en_azucar))
    return comida

# Función para generar una dieta baja en carbohidratos y perder peso
def generar_dieta_baja_en_carbohidratos():
    dieta = {
        'Desayuno': generar_comida_baja_en_carbohidratos(),
        'Almuerzo': generar_comida_baja_en_carbohidratos(),
        'Cena': generar_comida_baja_en_carbohidratos()
    }
    return dieta

# Función para imprimir la dieta
def imprimir_dieta(dieta):
    for comida, alimentos in dieta.items():
        print(comida + ':')
        for alimento in alimentos:
            print('- ' + alimento)
        print()

# Generar y mostrar la dieta baja en carbohidratos y diseñada para perder peso
print("¡Dieta Baja en Carbohidratos para Perder Peso!")
print("================================================")
dieta_baja_en_carbohidratos = generar_dieta_baja_en_carbohidratos()
imprimir_dieta(dieta_baja_en_carbohidratos)

