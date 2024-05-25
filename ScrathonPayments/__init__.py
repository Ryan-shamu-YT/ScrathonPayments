import scratchattach as scratch3
import requests

convert = ["false", "true"]

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
                raise ValueError("User {} did not use Scrathon before!".format(username))
        else:
            raise ValueError("User {} does not exist on scratch!".format(username))

        if self.username != "None":
            print("Started Scrathon as {}! All funds earned will go to mentioned user".format(self.username))

        @client.request
        def purchase(price):
            request = requests.post("http://45.140.188.129:6623/transaction", json={
                "price": price,
                "buyer": client.get_requester(),
                "seller": self.username
            })
            try:
                success = str(request.json().get("success")) == "True"
            except Exception as e:
                print(f"Didn't recognise json: {request.text}")
                raise e from None
            return convert[success]
        @client.request
        def userexist():
            request = requests.post("http://45.140.188.129:6623/userexist/", json={"username": client.get_requester()})
            try:
                success = str(request.json().get("userexist")) == "True"
            except Exception as e:
                print(f"Didn't recognise json: {request.text}")
                raise e from None
            return convert[success]
        @client.request
        def purchasecheck(price):
            request = requests.post("http://45.140.188.129:6623/checkpurchase", json={
                "price": price,
                "buyer": client.get_requester(),
                "seller": self.username
            })
            try:
                success = str(request.json().get("success")) == "True"
            except Exception as e:
                print(f"Didn't recognise json: {request.text}")
                raise e from None
            return convert[success]
