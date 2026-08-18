pg = lambda x: x*2

def main():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    lista_pg = list(map(pg, numeros))

    for n in lista_pg:
        print(n)

if __name__ == "__main__":
    main()