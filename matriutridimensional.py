QALU = 3
QASS = 4
QAVA = 2

notes = [None]*QALU

for alu in range(QALU):
    notes[alu] = [None]*QASS
    for ass in range(QASS):
        notes[alu][ass] = [None]*QAVA




# Omplint la matriu amb notes

for alu in range(len(notes)):
    print("NOTES DE L'ALUMNE", alu)
    for ass in range(len(notes[alu])): 
        print("    ASSIG", ass)
        for ava in range(QAVA):
            notes[alu][ass][ava] = int(input(f"       Dis-me la nota de l'ava {ava}:"))


print("-------------------------------------------------------------------------------------------------------------")


# Mostrem la matriu amb este format:
'''
NOTES DE L'ALUMNE 0
    ASSIG 0
       Dis-me la nota de l'ava 0:3
       Dis-me la nota de l'ava 1:4
    ASSIG 1
       Dis-me la nota de l'ava 0:5
       Dis-me la nota de l'ava 1:5
'''
totalNotes = QALU * QASS * QAVA
totalSuma = 0
for alu in range(len(notes)):
    print(f"NOTES DEL L'ALUMNE {alu}")
    for ass in range( len(notes[alu])  ): 
        print(f"ASSIG {ass}")
        for ava in range (len(notes[alu][ass])):
            print(f"La nota de la ava {ava} : {notes[alu][ass][ava]}")
            totalSuma += notes[alu][ass][ava]
            
        print()
# Mostra la nota mitja de totes les notes
mitjatotal = totalSuma/totalNotes
print(f"La mitja de les notes total es {mitjatotal}")

print("-------------------------------------------------------------------------------------------------------------")
# Mostra la nota mitja de cada alumne (mostra número alumne i la seua mitja)
for alu in range(len(notes)):
    print(f"MITJES DE L'ALUMNE {alu}")
    sumaAlumne = 0
    mitjaAlumne = 0
    for ass in range( len(notes[alu])  ): 
        pass
        for ava in range (len(notes[alu][ass])):
            sumaAlumne += notes[alu][ass][ava]

    mitjaAlumne = sumaAlumne / (totalNotes/QALU)
    print(f"La nota mitja es : {mitjaAlumne}")

print("-------------------------------------------------------------------------------------------------------------")

# 4. Mostra la nota mitja de cada avaluació (mostra número avaluació i la seua mitja)

for alu in range(len(notes)):
    totalSumaAva1 = 0
    totalSumaAva2 = 0
    print(f"MITJES DE L'ALUMNE {alu}")
    for ass in range( len(notes[alu])  ): 

        for ava in range (len(notes[alu][ass])):
            if ava == 0:
                    totalSumaAva1 += notes[alu][ass][ava]
            elif ava ==1:
                totalSumaAva2 += notes[alu][ass][ava]
    print(totalSumaAva1,totalSumaAva2, QASS)
    mitjaPrimeraAva = totalSumaAva1 / QASS
    mitjaSegonaAVA = totalSumaAva2 / QASS
    print(f"La mitja del la primera es : {mitjaPrimeraAva}")
    print(f"La mitja del la segona es : {mitjaSegonaAVA}")

print("-------------------------------------------------------------------------------------------------------------")
                               
# 5. Mostra la nota mitja de cada assignatura (mostra número d'assignatura i la seua mitja)

for ass in range(QASS):
    notesAss = 0 
    print(f"ASSIG {ass}")
    for alu in range(QALU):
        for ava in range (QAVA):
            notesAss += notes[alu][ass][ava]

    
    mitjaAss = notesAss / (QAVA * QALU)
    print(f"La mitja de la ass {ass} es {mitjaAss}")