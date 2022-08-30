from pydoc import classname
import LogicHandler
LogicHandler.indicateLoading("Loading " + __name__)
import plotly.express as px
import plotly.graph_objects as go

def visualize(dic, wtitle="Score",anon=False,type="bar",sort=False):
    nimet,pisteet = LogicHandler.ListifyStudents(dic,anon,sort)
    r = {
        "name": nimet,
        "score": pisteet
    }
    if type == "bar":
        fig = px.bar(r, x='name', y='score',title=wtitle,color="score")
    elif type == "hbar":
        fig = px.bar(r, x='score', y='name',orientation="h",title=wtitle,color="score")
    elif type == "pie":
        fig = px.pie(r, names='name', values='score',title=wtitle,color="score")
    elif type == "bubble":
        fig = px.scatter(
            r,
            x='name',
            y='score',
            size="score",
            color="score",
            title=wtitle,
        )
    fig.show()

def visualizeClasses(classes: dict):
    ways = ["Top Score", "Average Score"]
    prepareddata = []
    for i in classes:
        prepareddata.append(
            go.Bar(name=classes[i]["classname"], x=ways, y = classes[i]["scores"])
        )
    fig = go.Figure(
        data = prepareddata
    )
    fig.update_layout(barmode='group')
    fig.show()

LogicHandler.indicateSuccess(f"{__name__} loaded [S]")