# deret aritmatika
start = int(input("Start :"))
end = int(input("End :"))
step = int(input("Beda :"))
hasil = []
hasil.append(start)
while start != end:
    start = start + step
    hasil.append(start)
print(hasil)