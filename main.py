from pyscript import document, display

membersFirst = ["Gerthy", "Jericho", "Joaquin", "Eran", "Louie", "Carlos", "Philip", "Jarvis"]
membersLast = ["Bausa", "Magsalin", "Castor", "Diaz", "Lee", "Borromeo", "Ponce", "Joven"]

def checkers_membershippers (e):
    document.getElementById("output").innerHTML = ""
    document.getElementById("first").value
    document.getElementById("last").value
    
    membersF = document.getElementById("first").value
    membersL = document.getElementById("last").value
    check_membership1 = membersFirst in membersF
    check_membership2 = membersLast in membersL

    display(True, "You are a member of Sir Aljo!")
    display(False, "You are NOT a member of Sir Aljo")