# ANSI escape codes for colors
RED = "\033[31m"
WHITE = "\033[37m"
YELLOW = "\033[33m"
RESET = "\033[0m"  # Reset to default color

# Variabila de mentinere in bucla alegerii task-ului
valid=True

# Incepe bucla (pentru ca valid are valoarea implicita True)
while valid:
    # Se iese din bucla daca utilizatorul alege 0
    task=int(input("Choose a task(1/2/3/4/5 or 0 for exit):"))  
    if task==1 or task==2 or task==3 or task==4 or task==5 or task==0:
        valid=True
    else:
        print("Alegere invalida")
    if task==1:
        print("Task1 = Suma a trei numere:")
        a=int(input("Primul numar:"))
        b=int(input("Cel de-al doilea numar:"))
        c=int(input("Cel de-al treilea numar:"))
        print(f"{a}+{b}+{c}={a+b+c}")  
        task=0      
    elif task==2:
        print("Task2 - Aistent financiar personal:")
        a=int(input("Salariul lunar:"))
        b=int(input("Rata lunara:"))
        c=int(input("Facturi utilitati:"))
        print(f"Dupa deducerea cheltuielilor, iti raman {a-b-c} lei.")
    elif task==3:
        print("Task3 - Calcul suprafata romb")
        a=int(input("Diagonala 1:"))
        b=int(input("Diagonala 2:"))
        print(f"Suprafata rombului este {(a*b)/2}.")
    elif task==4:
        print(f"{WHITE}To be{RESET}")
        print(f"{RED}or not{RESET}")
        print(f"{WHITE}to be.{RESET}")
    elif task==5:
        print(f"{YELLOW}\"Life is what happens{RESET}")
        print(f"{YELLOW}    when{RESET}")
        print(f"{YELLOW}        you're busy making other plans\"{RESET}")
        print("                                    John Lennon")
    elif task==0:
        # S-a ales alegerea din bucla
        valid=False
else:
    # Se afiseaza in cazul in care s-a ales iesirea din bucla.
    print("O zi placuta, in continuare.")
    valid=False
 