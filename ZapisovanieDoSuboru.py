import os.path

subor = open("subor.txt", "w")
subor.write("Prvy riadok textu ")
subor.write("Stale prvy riadok textu\n")
subor.write("Druhy riadok textu")
subor.close()

# if os.path.exists("subor.txt"):
#   os.remove("subor.txt")
# else:
#   print("Subor neexistuje")