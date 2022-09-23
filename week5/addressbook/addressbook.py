import requests

class Contact():
    def __init__(self, firstName, lastName, email, phone, photo):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.photo = photo

    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getEmail(self):
        return self.email
    
    def getPhone(self):
        return self.phone
    
    def getPhoto(self):
        return self.photo
    
    def __str__(self):
        return f"Name: {self.firstName} {self.lastName} Email: {self.email}"
    
    def __repr__(self):
        return f"Name: {self.firstName} {self.lastName} Email: {self.email}"

class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results
    
