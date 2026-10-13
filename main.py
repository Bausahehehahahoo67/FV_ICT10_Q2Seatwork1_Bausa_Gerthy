from pyscript import document, display

membersFirst = ["Gerthy", "Jericho", "Joaquin", "Eran", "Louie", "Carlos", "Philip", "Jarvis"]
membersLast = ["Bausa", "Magsalin", "Castor", "Diaz", "Lee", "Borromeo", "Ponce", "Joven"]

def checkers_membershippers (e):
    document.getElementById("result").innerHTML = ""
    document.getElementById("first").value
    document.getElementById("last").value
    
    membersF = document.getElementById("first").value
    membersL = document.getElementById("last").value

    full_name = membersF + " " + membersL

    result = document.getElementById("result")

    result.innerText = "Sorry " + full_name + ", your name is not on the list."

    
