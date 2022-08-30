from time import sleep
from termcolor import colored
def indicateLoading(string:str="Loading",animated=True,delay=0.01):
    for i in range(len(string)):
        sleep(delay)
        print(colored(f"\r{string[:i+1]}",on_color="on_yellow"),end="\r")
indicateLoading("Loading " + __name__)

def indicateFailure(string:str="ERROR",animated=True):
    for i in range(len(string)):
        sleep(0.03)
        print(colored(f"\r{string[:i+1]}",color="white",on_color="on_red"),end="\r")
    print()

def indicateSuccess(string:str="Success [S]",animated=True,spaceAtEnd=True):
    if animated:
            for i in string:
                sleep(0.01)
                print(colored(i,on_color="on_green"),end="")
            if spaceAtEnd:
                print()
    else:
        if spaceAtEnd:
            print(colored(string,on_color="on_green"))
        else:
            print(colored(string,on_color="on_green"),end="")

def progressBar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "█" *  int(percent) + "░" * (100 - int(percent))
    if not progress == total:
        print(colored(f"\r{bar} - {percent:.2f}%","yellow"),end="\r")
    else:
        print(colored(f"\r{bar} - {percent:.1f}%","green"),end="\r")

def strArrayToIntArray(strArray: list):
    intArray = []
    for i in strArray:
        intArray.append(int(i))
    return intArray

def rowToStudent(row: list):
    student = {
        "id": row[0],
        "name": ([row[1],row[2]]),
        "organization": row[3],
        "email": row[4],
        "courses": strArrayToIntArray(row[5:19]),
        "total_score": int(row[19])
    }
    return student

def anonymize(oppilaat: dict):
    for i in oppilaat:
        oppilaat[i]["name"] = "[null]"
        oppilaat[i]["email"] = "[null]"
    return True

def removePersonal(oppilas: dict):
    return {"courses": oppilas["courses"], "total_score": oppilas["total_score"]}

def totalScore(oppilaat: dict):
    score = 0
    for i in oppilaat:
        score += oppilaat[i]["total_score"]
    return score

def averageScore(oppilaat: dict):
    return totalScore(oppilaat)/len(oppilaat)

def getBestStudent(oppilaat: dict):
    best = 0
    bestStudent = {}
    for x,i in enumerate(oppilaat):
        if oppilaat[i]["total_score"] > best:
            bestStudent = oppilaat[i]
            best  = bestStudent["total_score"]
    return bestStudent

def ListifyStudents(oppilaat: dict,anon=False,sort=False):
    lista = [[],[]]
    for x,i in enumerate(oppilaat):
        if anon:
            lista[0].append(chr(x))
        else:
            lista[0].append(oppilaat[i]["name"][1])
        lista[1].append(oppilaat[i]["total_score"])
    if sort:
        b,a = list(zip(*sorted(zip(lista[1], lista[0]))))
        return [a,b]
    return lista

def classify(oppilaat: dict):
    f = {}
    a = oppilaat.copy()
    for i in a:
        for j in a[i]:
            f[j] = a[i][j]
    return f
