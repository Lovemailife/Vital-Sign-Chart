print('攝氏華氏溫度換算器')

c = input('攝氏溫度:')
c = float(c)
f = c * 9/5 + 32
print('華氏溫度:', f,'°F')

f = input ('華氏溫度:')
f = float(f)
c = (f-32) * 5/9
print('攝氏溫度:', c,'°C')