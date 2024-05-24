# Scrathon

Scrathon is a Python package designed to interact with the Scrathon platform to allow for purchases in your projects.

## Installation

You can install Scrathon via pip: ```pip install scrathon-payments```

## Usage with [Scratchattach](https://github.com/TimMcCool/scratchattach)

To use Scrathon, you need to instantiate the `Scrathon` class with a valid username and scratchattach cloud requests client. These will be used to authenticate and perform transactions on the Scrathon platform.


```python
from os import system
system("pip install scratchattach --upgrade")
system("pip install scrathon-payments --upgrade")
import scratchattach as scratch3
from ScrathonPayments import Scrathon

session = scratch3.login("username of any account (can be an alt with new scratcher)", "password of the account")

conn = session.connect_cloud("YOUR PROJECT ID")

client = scratch3.CloudRequests(conn)

ScrathonPayments = Scrathon("username of account to receive coins", client)

client.run()

#Guess what? That's it!
```
Check out the example project here: https://scratch.mit.edu/projects/996449477/

## Methods
```Scrathon() ```   *Initiates a project connection to Scrathon services.*

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `User` | `str` | **Required**. User to receive funds from purchases |
| `Client` | `scratchattach.CloudRequests` | **Required**. Scratchattach Client |


```
