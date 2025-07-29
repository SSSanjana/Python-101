pesos = float(input("What do you have left in pesos?"))
soles = float(input("What do you have left in soles?"))
reais = float(input("What do you have left in reais?"))

p_usd = float((0.054)*pesos)
s_usd = float((0.28)*soles)
r_usd = float((0.18)*reais)

usd = float(p_usd + s_usd + r_usd)
print(usd)
