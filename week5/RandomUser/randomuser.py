import pip._vendor.requests
requests = pip._vendor.requests

class User():
    def __init__(self,first,last,email,username,password,uuid,phone,cell,picLarge,picThumb):
        self.first = first
        self.last = last
        self.email = email
        self.username = username
        self.password = password
        self.uuid = uuid
        self.phone = phone
        self.cell = cell
        self.picLarge = picLarge
        self.picThumb = picThumb

    def setFirst(self, first):
        self.first = first
    
    def setLast(self, last):
        self.last = last

    def setEmail(self, email):
        self.email = email

    def setPass(self, password):
        self.password = password

    def setUUID(self, uuid):
        self.uuid = uuid

    def setPhone(self, phone):
        self.phone = phone

    def setCell(self, cell):
        self.cell = cell
    
    def setLarge(self, picLarge):
        self.picLarge = picLarge
    
    def setThumb(self, picThumb):
        self.picThumb = picThumb

    def getFirst(self):
        return self.first
    
    def getLast(self):
        return self.last
    
    def getEmail(self):
        return self.email

    def __str__(self):
        retStr = self.first
        retStr += " "
        retStr += self.last
        retStr += "EMAIL: ".join(self.email)
        return retStr

class AuthorizedUsers():
    def __init__(self):
        self.authUsers = []

    def addUser(self, user):
        self.authUsers.append(user)

    def showUsers(self):
        for user in self.authUsers:
            print(user)

def getData():
    URL = "https://randomuser.me/api/?results=10"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

authorizedUsers = AuthorizedUsers()
jsonData = getData()

for currentUser in jsonData['results']:
    userName = currentUser['name']
    users = []

    for user in currentUser['email']:
        users.append(user['first'])

        newUser = User(userName, users)
        authorizedUsers.addUser(newUser)

authorizedUsers.showUsers()