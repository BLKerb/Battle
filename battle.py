teks=input("Antre yon teks svp: ")
vale=0
for k in teks:
  if (k=='a' or k=='e' or k=='i' or k=='o' or k=='u' or k=='y'):
    vale=vale+1
    tape=vale
print("Vale vwayel ki nan ",teks, "se: ",tape)
