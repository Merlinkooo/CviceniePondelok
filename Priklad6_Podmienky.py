body = int(input('Zadaj získaný počet bodov: '))
if body >= 90:
    print('za', body, "bodov získavaš známku A")
elif body >= 80:
    print("za", body, "bodov získavaš známku B")
elif body >= 70:
    print("za", body, "bodov získavaš známku C")
elif body >= 60:
    print("za", body, "bodov získavaš známku D")
elif body >= 50:
    print("za", body, "bodov získavaš známku E")
else:
    print("za", body, "bodov získavaš známku FX")

print("")

cislo = int(input("Zadaj cislo delitelne 2 a 5 bez zvyšku"))

if cislo % 2 == 0 and cislo % 5 ==0:
    print("cislo", cislo, "je delitelne 2 a 5 bez zvyšku")
else:
    print("cislo", cislo, "nie je delitelne 2 a 5 bez zvyšku!!!")
