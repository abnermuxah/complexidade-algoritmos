f = open('knapPI_3_10000_1000_1','r')
f = (str.split(f.read(), "\n"))
tam , cap_max = f[0].split(" ")
tam = int(tam)
cap_max = int(cap_max)
custo_kg = []

for i in range(1,tam+1):
    valor , peso = f[i].split(" ")
    peso = int(peso)
    valor = int(valor)
    custo_kg.append((peso/valor,valor,peso,i))
custo_kg = sorted(custo_kg) # <- O(N * Log N)
vlr = 0
cap = 0
i = 0
for i in custo_kg:
   if (cap + i[2]) <= cap_max :
       vlr = vlr + i[1]
       cap = cap + i[2]


print("R$ : ",vlr)
print("Kg Armazenado: ", cap)
print("Capacidade Total:", cap_max)



