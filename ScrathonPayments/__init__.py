import json
import re
import requests


class Scrathon():

    def __init__(self, username):
        self.username = str(username)

        print("Started Scrathon as {}! All funds earned will go to mentioned user".format(username))

    def purchase(self, price, user):
        request = requests.post("https://scrathon.justablock.online/transaction", json={
            "price": price,
            "buyer": user,
            "seller": self.username
        })

        return request.content
    
    def purchasecheck(self, price, user):
        request = requests.post("https://scrathon.justablock.online/checkpurchase", json={
            "price": price,
            "buyer": user,
            "seller": self.username
        })

        return request.content

