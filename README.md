# Scrathon

Scrathon is a Python package designed to interact with the Scrathon platform to allow for purchases in your projects.

## Installation

You can install Scrathon via pip: ```pip install scrathon-payments```

## Usage with [Scratchattach](https://github.com/TimMcCool/scratchattach)

To use Scrathon, you need to instantiate the `Scrathon` class with a valid username. This username will be used to authenticate and perform transactions on the Scrathon platform.


```python
import scratchattach as scratch3
from ScrathonPayments import Scrathon #pip install scrathon-payments

session = scratch3.login("USERNAME_OF_ANY_ACCOUNT_(ACCOUNT_CAN_BE_NEW_SCRATCHER)", "PASSWORD")

conn = session.connect_cloud("YOUR_PROJECT_ID")

ScrathonPayments = Scrathon("USERNAME_OF_ACCOUNT_TO_RECEIVE_FUNDS")

client = scratch3.CloudRequests(conn)

@client.request
def purchase(username, Price):
    Purchase = ScrathonPayments.purchase(Price, username)
    result = "None"
    if Purchase == "You have been banned from selling items in your projects!":
        result = "Fail!"
        
        #In scratch, tell the user the transaction failed
        
    elif Purchase == "User does not have enough money to buy the item!":
        result = "Not enough coins!"
        #In scratch, tell the user they do not have enough coins to make the purchase
    elif Purchase == "Transaction has been added to pending transactions, transaction will go through once the user has confirmed!":
        #In scratch, tell your users to look at the comments of the Scrathon project and find their verification comment in the project's comments, reply to it with 'yes' and the transaction will go through!
        result = "Success!"
    
    return result

@client.request
def purchasecheck(username, Price): #Check if the player bought the item so you can give them the promised item (If you don't give the item to the player you will get banned from selling items)
    PurchaseCheck = ScrathonPayments.purchasecheck(Price, username)

    return PurchaseCheck

client.run()
```


## Methods
```purchase() ```   *Initiates a purchase transaction.*

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Price` | `int` | **Required**. Price the buyer is paying |
| `User` | `str` | **Required**. User paying for your item |

Returns:
```
Status of the transaction, e.g: 
"Transaction has been added to pending transactions, transaction will go through once the user has confirmed!"

"User does not have enough money to buy the item!""

and "You have been banned from selling items in your projects!"
```

```purchasecheck()```  *Checks the status of a purchase transaction.*

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Price` | `int` | **Required**. Price the buyer had paid |
| `User` | `str` | **Required**. User who paid for your item |

Returns:
```
True: The transaction went through (give their item)

False: The transaction did not go through!
```
