# Write code below 💖
CO = int(input('What do you have left in pesos?'))
PE = int(input('What do you have left in soles?'))
BR = int(input('What do you have left in reais?'))
print(CO)
print(PE)
print(BR)
usd = CO*0.00024 + PE*0.28 + BR*0.18
print('USD', round(usd,1))