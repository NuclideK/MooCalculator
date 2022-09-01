from difflib import get_close_matches
from termcolor import colored
from time import sleep

import os
import colorama
colorama.init()
import examplestudent
import FileManager
import LogicHandler
import webHandler
import chartHandler

###################################
currentVersion = "v1.0.0"
###################################
allStudents = {}
def checkUpdates():
    LogicHandler.indicateLoading("Checking for updates")
    try:
        latest = webHandler.getLatestVersion()
        if (latest["name"] != currentVersion):
            print(f"""{colored("Newer version was found!",color="yellow")}
{"-"*len(f'Newest version: {latest["name"]}')}
{colored(f"Your version: {currentVersion}",color="red")}
{colored(f'Newest version: {latest["name"]}',color="green")}
{"-"*len(f'Newest version: {latest["name"]}')}
{colored(f'Update description:',color="blue")}
{colored(latest["body"])}
            """)

            if (input("Would you like to update now? (Y/N): ").lower() == "y"):
                sleep(1)
                LogicHandler.indicateLoading("> Opening web browser <")
                sleep(1)
                webHandler.openWebsite(latest["html_url"])
                sleep(1)
                print()
                LogicHandler.indicateSuccess("> Shutting down <")
                sleep(5)
                os._exit(1)
            else:
                print(colored('You can always update later by running the "update" command',color="blue"))
                print()
        else:
            print(colored("You are using the latest version",color="green"))
    except:
        LogicHandler.indicateFailure(" > Update check failed < ")
    return False

def errPrint(string: str):
    print(colored((string),color="red"))

def inStudents(className: str):
    tiedostot = FileManager.getInFiles(f"Lisää oppilaat luokkaan {className}")
    students = {}
    for tiedosto in tiedostot:
        with open(tiedosto) as f:
            for i in f:
                try:
                    arr = i.replace('"','').split(",")
                    students[arr[0]] = LogicHandler.rowToStudent(arr)
                except:
                    pass
        global allStudents
        allStudents[className] = students.copy()
        
def createClass(className: str,students: dict):
    futureClass = {}    
    for i in students:
        futureClass[i] = students[i]
    allStudents[className] = futureClass

def getClass(className: str):
    return allStudents[className]

def printAllStudents():
    for i in allStudents:
        for j in allStudents[i]:
            print(allStudents[i][j],end="\n\n")

def getBestStudents():
    bestStudents = {}
    for i in allStudents:
        bestStudents[i] = LogicHandler.getBestStudent(allStudents[i])
    return bestStudents

def getGlobalTotalScore():
    total = 0
    for i in allStudents:
        total += LogicHandler.totalScore(allStudents[i])
    return total

def getGlobalAverageScore():
    lenght = 0
    score = 0
    for i in allStudents:
        lenght += len(allStudents[i])
    score = getGlobalTotalScore()
    try:
        return score/lenght
    except ZeroDivisionError:
        return 0

def getStudentByName(name: str):
    for i in allStudents:
        for j in allStudents[i]:
            if name.split(" ") == allStudents[i][j]["name"]: return allStudents[i][j]

def getStudentByEmail(email: str):
    for i in allStudents:
        for j in allStudents[i]:
            if email == allStudents[i][j]["email"]: return allStudents[i][j]

def getStudentById(id: str):
    for i in allStudents:
        for j in allStudents[i]:
            if id == allStudents[i][j]["id"]: return allStudents[i][j]

commands = {
    "help": "Displays all commands",
    "exit": "Closes down the program",
    "addclass": "Adds students to class <arg1> (prompts with file to get students from)",
    "displayclass": "Prints out all students of class <arg1>",
    "displayall": "Prints out all loaded students",
    "visual": "Visualizes the students in a graph",
    "mock": "Testing command, generates random students",
    "outstudents": "outputs students from class <arg1> to a chosen file",
    "globaloutstudents": "outputs every student loaded to a chosen file",
    "gettotalscore": "Adds up all the progress made by a class <arg1>",
    "getaveragescore": "Counts the average student in class <arg1>",
    "getbeststudent": "prints the best student in class <arg1>",
    "getelite": "Creates a class formed from the top student from each existing class",
    "globalaverage": "Calculates and displays the average score across all classes",
    "visualizeclasses": "Makes a graph about each class compared to eachother",
    "update": "Checks for updates",
    "system": "Executes <arg1> as a system command"
}
print()
checkUpdates()
print()
programRunning = True

while programRunning:
    x = input("> ")
    if (x == ""): continue
    command = x.lower().split(" ")[0]
    args = x.lower().split(" ")[1:]
    if (command == "exit"  or command[0] == "&"):
        LogicHandler.indicateSuccess()
        programRunning = False

    elif (command == "help"):
        if (len(args) == 0):
            print(colored("\n-- Commands --","blue"))
            for i in commands:
                print(colored(i + " -> " + commands[i],"green"))
            print()
        else:
            if args[0] in commands:
                print(colored(f'{args[0]} -> {commands[args[0]]}',color="blue"))
            else:
                errPrint(f"{args[0]} isn't a valid command")

    elif (command == "addclass"):
        if (len(args) != 1): errPrint("Usage: addclass <classname>")
        else:
            luokka = args[0]
            inStudents(luokka)
            LogicHandler.indicateSuccess()

    elif (command == "displayclass"):
        if ((len(args) != 1)): errPrint("Usage: displayclass <classname>")
        else:
            sClass = getClass(args[0])
            for i in sClass:
                print(sClass[i],end="\n\n")

    elif (command == "displayall"):
        print()
        printAllStudents()

    elif (command == "visual"):
        if len(args) != 5: errPrint("Usage: visual (<classname:string>/!all) (bar/hbar/pie/bubble)> <wtitle:string> <anonymous:bool> <sort:bool>")
        else:
            if args[0] != "!all":
                chartHandler.visualize(getClass(args[0]),type=args[1],wtitle=args[2],anon=(args[3] == "true"),sort=(args[4] == "true"))
            else:
                chartHandler.visualize(LogicHandler.classify(allStudents),type=args[1],wtitle=args[2],anon=(args[3] == "true"),sort=(args[4] == "true"))
            LogicHandler.indicateSuccess()

    elif (command == "mock"):
        if (len(args) != 1): errPrint("Usage: mock <studentamount:integer>")
        else:
            students = {}
            for i in range(int(args[0])):
                students[i] = examplestudent.mockStudent()
                LogicHandler.progressBar(i+1,int(args[0]))
            allStudents["mock"] = students
            LogicHandler.indicateSuccess()

    elif (command == "outstudents"):
        if (len(args) != 1): errPrint("Usage: outstudents <classname;string> <personal:bool>")
        else: FileManager.outStudents(allStudents[args[0]],)

    elif (command == "globaloutstudents"):
        if len(args) != 1: errPrint("Usage: globaloutstudents <personal:bool>")
        else: FileManager.outGlobalStudents(allStudents,(args[0] == "true"))

    elif (command == "gettotalscore"):
        if (len(args) != 1): errPrint("Usage: getTotalScore <classname:str>")
        else:
            print(LogicHandler.totalScore(allStudents[args[0]]))

    elif (command == "getaveragescore"):
        if (len(args) != 1): errPrint("Usage: getAverage <classname:str>")
        else:
            print(LogicHandler.averageScore(allStudents[args[0]]))

    elif (command == "getbeststudent"):
        if len(args) != 1: errPrint("Usage: getbeststudent <class:string>")
        else:
            print(LogicHandler.getBestStudent(allStudents[args[0]]))

    elif (command == "getelite"):
        createClass("_elite_",getBestStudents())
        print(f'{colored("From each class, the top student has been added to a central class called ",color="green")}{colored("_elite_",color="blue")}')
    
    elif (command == "globalaverage"):
        print(f"The average score across all classes is {getGlobalAverageScore()}")

    elif (command == "visualizeclasses"):
        classes = {}
        for i in allStudents:
            classes[i] = {
                "classname": i,
                "scores": [LogicHandler.getBestStudent(allStudents[i])["total_score"],LogicHandler.averageScore(allStudents[i])]
            }
        chartHandler.visualizeClasses(classes)
    
    elif (command == "update"):
        checkUpdates()
    
    elif (command == "system"):
        arguments = ""
        for i in args:
            arguments += f"{i} "
        arguments = arguments[:-1]
        os.system(arguments)
    
    else:
        close = get_close_matches(command,list(commands.keys()))
        errPrint(f"{command} is not a valid command.")
        if (len(close) > 0):
            out = f'{colored("Did you mean one of theses? ",color="blue")}'
            for i in close:
                out += colored(f" {i}",color="green")
            print(out)
print("\n"*10)