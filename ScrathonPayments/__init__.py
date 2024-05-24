import scratchattach as scratch3
import requests

class Scrathon:

    def __init__(self, username, client: scratch3.CloudRequests):
        self.client = client
        self.username = "None"
        try:
            scratch3.get_user(username)
            userexists = True
        except scratch3.exceptions.UserNotFound:
            userexists = False
        if userexists:
            if requests.post("http://45.140.188.129:6623/userexist/", json={"username": username}).json() == {"userexist": "True"}:
                self.username = str(username)
            else:
                print("User {} did not use Scrathon before!".format(username))
        else:
            print("User {} does not exist on scratch!".format(username))

        if self.username != "None":
            print("Started Scrathon as {}! All funds earned will go to mentioned user".format(self.username))

        @client.request
        def purchase(price):
            request = requests.post("http://45.140.188.129:6623/transaction", json={
                "price": price,
                "buyer": client.get_requester(),
                "seller": self.username
            })

            return request.json()
        @client.request
        def purchasecheck(price):
            request = requests.post("http://45.140.188.129:6623/checkpurchase", json={
                "price": price,
                "buyer": client.get_requester(),
                "seller": self.username
            })

            return request.json()
