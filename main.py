import pandas as pd
import time

df = pd.read_csv("database.csv")

respuestas = []

respuestas.append(int(input("Cuantas horas pasas escuchando musica al dia?: ")))
respuestas.append(int(input("Escuchas musica mientras trabajas o estudias? Yes/No: ")))
respuestas.append(int(input("Frecuentemente descubres nueva musica?: ")))
respuestas.append(int(input("Escuchas musica en idiomas no nativos al tuyo?: ")))

print("\nEn las siguientes preguntas podras responder del 1 al 4 siendo 1 'NUNCA' y 4 'Siempre'")

respuestas.append(int(input("Que tan frecuente escuchas musica clasica?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica country?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica EDM?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica folk?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica gospel?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica hip hop?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica jazz?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica K pop?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica latina?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica lofi?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica metal?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica pop?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica R&B?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica rap?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica rock?: ")))
respuestas.append(int(input("Que tan frecuente escuchas musica de videojuegos?: ")))

print("\nDe la siguiente lista, escribe el NUMERO de tu genero favorito:")
print("1. Clasica   2. Country   3. EDM       4. Folk")
print("5. Gospel    6. Hip hop   7. Jazz      8. K pop")
print("9. Latina    10. Lofi     11. Metal    12. Pop")
print("13. R&B      14. Rap      15. Rock     16. Videojuegos")

fav_genre = int(input("\nCual es tu genero favorito? (Ingresa el numero): "))

for i in range(1, 17):
    if i == fav_genre:
        respuestas.append(1)
    else:
        respuestas.append(0)


datocurioso = (respuestas[0]*24)/100
show = f"Pasas {datocurioso}% de tu dia escuchando musica"
for letra in show:
    print(letra, end='')
    #time.sleep(1)

print("\nEspera.")
