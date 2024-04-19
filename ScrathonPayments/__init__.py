import scratchattach as scratch3
import requests

class Scrathon():

    def __init__(self, username):
        self.username = "None"
        try:
            scratch3.get_user(username)
            userexists = True
        except scratch3.exceptions.UserNotFound:
            userexists = False
        if userexists:
            if requests.post("http://196.27.127.58:12211/userexist/", json={"username": username}).json == {"userexist": "True"}:
                self.username = str(username)
            else:
                print("User {} did not use Scrathon before!".format(username))
        else:
            print("User {} does not exist on scratch!".format(username))

        if self.username != "None":
            print("Started Scrathon as {}! All funds earned will go to mentioned user".format(self.username))

    def purchase(self, price, user):
        request = requests.post("http://196.27.127.58:12211/transaction", json={
            "price": price,
            "buyer": user,
            "seller": self.username
        })

        return request.json()
    
    def purchasecheck(self, price, user):
        request = requests.post("http://196.27.127.58:12211/checkpurchase", json={
            "price": price,
            "buyer": user,
            "seller": self.username
        })

        return request.json()
