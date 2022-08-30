import LogicHandler
LogicHandler.indicateLoading("Loading " + __name__)
from tkinter import filedialog

def getInFile(titteli="Valitse input tiedosto"):
    filetypes = (
        ('CSV tiedostot', '*.csv'),
        ('Kaikki tiedostot', '*.*')
    )
    return filedialog.askopenfile(title=titteli)

def getInFiles(titteli="Valitse input-tiedosto(t)"):
    filetypes = (
        ('CSV tiedostot', '*.csv'),
        ('Kaikki tiedostot', '*.*')
    )
    return filedialog.askopenfilenames(title=titteli)
    
def getOutFile(titteli="Valitse/Nimeä output-tiedosto"):
    return filedialog.asksaveasfilename(title=titteli)

def outStudents(students: dict,personal=True,file="!ask"):
    if file=="!ask": file = getOutFile()
    with open(file,"w") as wipe: pass
    with open(file,"a") as f:
        for i in students:
            student = students[i]
            rivi = ""
            if personal:
                rivi += f'"{student["id"]}",'
                rivi += f'"{student["name"][0]}",'
                rivi += f'"{student["name"][1]}",'
                rivi += f'"{student["organization"]}",'
                rivi += f'"{student["email"]}",'
            for i in student["courses"]:
                rivi += f'"{i}",'
            rivi += f'"{student["total_score"]}"'
            f.write(rivi + "\n")

def outGlobalStudents(globalStudents: dict,personal=True,file="!ask"):
    if file=="!ask": file = getOutFile()
    with open(file,"w") as wipe: pass
    with open(file,"a") as f:
        for j in globalStudents:
            students = globalStudents[j]
            for i in students:
                student = students[i]
                rivi = ""
                if personal:
                    rivi += f'"{student["id"]}",'
                    rivi += f'"{student["name"][0]}",'
                    rivi += f'"{student["name"][1]}",'
                    rivi += f'"{student["organization"]}",'
                    rivi += f'"{student["email"]}",'
                for i in student["courses"]:
                    rivi += f'"{i}",'
                rivi += f'"{student["total_score"]}"'
                f.write(rivi + "\n")

LogicHandler.indicateSuccess(f"{__name__} loaded [S]")