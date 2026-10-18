# 🎵 Music Habits Age Predictor

Un sistema de Machine Learning en Python diseñado para predecir la edad de un usuario basándose en sus hábitos de consumo musical y preferencias de género. 

Este proyecto implementa un modelo de **Regresión Lineal Simple** alimentado por una base de datos de comportamiento musical (`database.csv`), recolectando datos en tiempo real mediante una interfaz interactiva por consola.

## Características Principales

- **Recolección Dinámica de Datos:** Interfaz de línea de comandos (CLI) interactiva que recopila hábitos de escucha (horas por día, descubrimiento de música, idiomas).
- **Procesamiento de Géneros Musicales:** Evaluación de 16 géneros distintos y aplicación de codificación para el género favorito del usuario.
- **Predicción con Machine Learning:** Utiliza regresión lineal para correlacionar los patrones de escucha con la edad cronológica.
- **Analíticas en Tiempo Real:** Cálculo de métricas personalizadas (ej. porcentaje del día dedicado a escuchar música).
- **Sistema de Recomendación Comunitario:** Base de conocimientos de retroalimentación donde los usuarios pueden recibir y aportar nuevas recomendaciones musicales según su género favorito.

## Tecnologías Utilizadas

- **Python 3.x** - Lenguaje principal.
- **Pandas** - Manipulación y análisis de datos de la base original (`database.csv`).
- **Scikit-learn** *(En desarrollo)* - Entrenamiento y ejecución del modelo de Regresión Lineal.
- **Time** - Gestión de pausas e interfaces de carga en consola.

## Instalación y Ejecución

1. Clona este repositorio:
   git clone [https://github.com/tu-usuario/music-age-predictor.git](https://github.com/tu-usuario/music-age-predictor.git)
2. Instala las dependencias necesarias:
   pip install pandas scikit-learn
3. Asegúrate de que el archivo database.csv se encuentre en la misma ruta que el script principal.
4. Ejecuta el programa:
   python main.py
   
## Estructura del Proyecto
├── main.py              # Script principal y lógica de interacción
├── database.csv         # Dataset de entrenamiento (hábitos vs. edad)
├── README.md            # Documentación del proyecto
└── requirements.txt     # Dependencias del entorno

### Pseudocódigo
INICIO DEL PROGRAMA

  // Fase 1: Inicialización y Modelado
  Importar librerías (pandas, time, sklearn)
  Cargar "database.csv" en DataFrame
  Entrenar Modelo_Regresion_Lineal usando DataFrame (X = hábitos, y = edad)

  // Fase 2: Definición de Funciones
  FUNCION respuestas_user():
      Crear lista vacía 'respuestas'
      
      Agregar a 'respuestas': input_entero("Horas al día")
      Agregar a 'respuestas': input("Escucha trabajando?")
      Agregar a 'respuestas': input("Descubre nueva música?")
      Agregar a 'respuestas': input("Escucha otros idiomas?")
      
      Lista generos_musicales = [clasica, country, EDM, folk, ...]
      PARA CADA genero EN generos_musicales:
          frecuencia = input_entero("Frecuencia de escucha de " + genero + " (1-4)")
          Agregar frecuencia a 'respuestas'
      
      Imprimir opciones de género favorito (1 a 16)
      fav_genre = input_entero("Número de género favorito")
      
      PARA i DESDE 1 HASTA 16:
          SI i == fav_genre:
              Agregar 1 a 'respuestas'
          SINO:
              Agregar 0 a 'respuestas'
              
      RETORNAR 'respuestas' y 'fav_genre'
  FIN FUNCION

  FUNCION analiticas(ans, fav_genre, modelo):
      Calcular porcentaje_dia = (ans[0] * 24) / 100
      Imprimir "Pasas " + porcentaje_dia + "% del día escuchando música"
      
      SI fav_genre está entre 1 y 16:
          Obtener nombre_genero basado en fav_genre
          Mostrar recomendación predeterminada del género
          Pedir al usuario nueva_recomendacion
          Guardar nueva_recomendacion en el diccionario de recomendaciones
      SINO:
          Imprimir "Género no soportado"

      // Integración de predicción
      edad_predicha = modelo.predecir(ans)
      Imprimir "El modelo predice que tu edad es: " + edad_predicha
  FIN FUNCION

  // Fase 3: Bucle Principal de Ejecución
  acabar = Falso
  MIENTRAS acabar == Falso HACER:
      lista_respuestas, genero_favorito = llamar respuestas_user()
      
      Imprimir "Procesando..."
      PARA i DESDE 3 HASTA 1 PASO -1:
          Imprimir "Cargando analíticas en " + i
          Esperar 1 segundo
          
      llamar analiticas(lista_respuestas, genero_favorito, Modelo_Regresion_Lineal)
      
      continuar = input("¿Desea continuar? y/n")
      SI continuar == "n" ENTONCES:
          acabar = Verdadero
          
FIN DEL PROGRAMA

## Autor
Jesús Juan De Jesús Juárez
Ingeniería en Inteligencia Artificial y Ciencia de Datos
Tecnológico de Monterrey, Campus Querétaro
Proyecto final de programación.

