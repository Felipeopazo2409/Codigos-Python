

tabla=[
    {
        "categoria": "acción",
        "juegos": ["GTA","Call of duty","PUBG"]
    },
    {
        "categoria": "aventura",
        "juegos": ["ASSINS","CRASH","Prince of persia"]
    },
    {
        "categoria":"deportes",
        "juegos":["Fifa 21","Pro 21","Moto Gp"]
    }

]

for categoria in tabla:
    print(f"-------Categoria: {categoria['categoria']}")
    for juego in categoria['juegos']:
        print(f"------Juego: {juego}")
