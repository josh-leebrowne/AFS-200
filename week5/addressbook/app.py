from flask import Flask
import requests
from addressbook import Contact, AddressBook

app = Flask(__name__)
response = requests.get('https://randomuser.me/api/?results=25&nat=us')
data = response.json()

my_book = AddressBook()

for user in data['results']:
    firstName = user['name']['first']
    lastName = user['name']['last']
    email = user['email']
    phone = user['phone']
    photo = user['picture']['thumbnail']

    my_contacts = Contact(firstName, lastName, email, phone, photo)
    my_book.addAddress(my_contacts)

print(my_book.addresses)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()