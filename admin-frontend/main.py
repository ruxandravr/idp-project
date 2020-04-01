from flask import Flask, render_template, request, redirect, url_for
import requests
import csv
import sys

app = Flask(__name__)

signed_in = False

def verify_user(user, pwd):
    url = sys.argv[1] + "verify_user/" + user + "/" + pwd
    resp = requests.get(url)
    resp = resp.text
    print("resp verify user is: ", resp, file=sys.stderr)
    if resp == "yes":
        return True
    return False

def get_tranzactions():
    url = sys.argv[1] + "get_tranzactions"
    resp = requests.get(url)
    resp = resp.json()
    print("resp get_tranzactions: ", resp, file=sys.stderr)
    return resp

def get_drinks():
    url = sys.argv[1] + "get_items/drink"
    resp = requests.get(url)
    resp = resp.json()
    print("resp get_drinks: ", resp, file=sys.stderr)
    return resp

def get_food():
    url = sys.argv[1] + "get_items/food"
    resp = requests.get(url)
    resp = resp.json()
    print("resp get_food: ", resp, file=sys.stderr)
    return resp

def get_inventory():
    url = sys.argv[1] + "get_inventory"
    resp = requests.get(url)
    resp = resp.json()
    print("resp get_inventory: ", resp, file=sys.stderr)
    return resp

def get_cards():
    url = sys.argv[1] + "get_cards"
    resp = requests.get(url)
    resp = resp.json()
    print("resp get_cards: ", resp, file=sys.stderr)
    return resp

def modify_drink_table(id, name, price):
    url = sys.argv[1] + "modify_drink/" + id + "/" + name + "/" + price
    resp = requests.get(url)
    resp = resp.text
    print("resp modify_drink: ", resp, file=sys.stderr)

def modify_food_table(id, name, price):
    url = sys.argv[1] + "modify_food/" + id + "/" + name + "/" + price
    resp = requests.get(url)
    resp = resp.text
    print("resp modify_food: ", resp, file=sys.stderr)

def modify_inventory_table(id, name, dealer, quant):
    url = sys.argv[1] + "modify_inventory/" + id + "/" + name + "/" + dealer + "/" + quant
    resp = requests.get(url)
    resp = resp.text
    print("resp modify_inventory: ", resp, file=sys.stderr)

def add_card_table(name, number, month, year, cvv, sold):
    url = sys.argv[1] + "add_card/" + number + "/" + name + "/" + month + "/" + year + "/" + cvv + "/" + sold
    resp = requests.get(url)
    resp = resp.text
    print("resp modify_inventory: ", resp, file=sys.stderr)

# admin app's main page displays all the options
@app.route('/', methods=['GET', 'POST'])
def login() -> str:
    return render_template("login.html")

@app.route('/validate_login', methods=['GET', 'POST'])
def validate_login() -> str:
    global signed_in
    if request.method == 'POST':
        formDetails = request.form
        user = formDetails['user']
        pwd = formDetails['pwd']
        print("username and password", user, pwd, file=sys.stderr)
        if verify_user(user, pwd):
            signed_in = True
            return render_template("main.html")
    return render_template("login.html")

# admin app's main page displays all the options
@app.route('/main', methods=['GET', 'POST'])
def main() -> str:
    return render_template("main.html")

@app.route('/visualize_tranzactions', methods=['GET', 'POST'])
def visualize_tranzactions() -> str:
    return render_template("visualize_tranzactions.html", row=get_tranzactions())

@app.route('/visualize_drinks', methods=['GET', 'POST'])
def visualize_drinks() -> str:
    return render_template("visualize_drinks.html", row=get_drinks())

@app.route('/visualize_food', methods=['GET', 'POST'])
def visualize_food() -> str:
    return render_template("visualize_food.html", row=get_food())

@app.route('/visualize_inventory', methods=['GET', 'POST'])
def visualize_inventory() -> str:
    return render_template("visualize_inventory.html", row=get_inventory())

@app.route('/visualize_cards', methods=['GET', 'POST'])
def visualize_cards() -> str:
    return render_template("visualize_cards.html", row=get_cards())

@app.route('/modify_drink', methods=['GET', 'POST'])
def modify_drink() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        name = formDetails['name']
        price = formDetails['price']
        print("modify drink", id, name, price, file=sys.stderr)
        modify_drink_table(id, name, price)
        return render_template("main.html")
    return render_template("modify_drink.html")

@app.route('/modify_food', methods=['GET', 'POST'])
def modify_food() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        name = formDetails['name']
        price = formDetails['price']
        print("modify food", id, name, price, file=sys.stderr)
        modify_food_table(id, name, price)
        return render_template("main.html")
    return render_template("modify_food.html")

@app.route('/modify_inventory', methods=['GET', 'POST'])
def modify_inventory() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        name = formDetails['name']
        dealer = formDetails['dealer']
        quant = formDetails['quant']
        print("modify inventory", id, name, dealer, quant, file=sys.stderr)
        modify_inventory_table(id, name, dealer, quant)
        return render_template("main.html")
    return render_template("modify_inventory.html")


@app.route('/add_card', methods=['GET', 'POST'])
def add_card() -> str:
    if request.method == 'POST':
        formDetails = request.form
        name = formDetails['name']
        number = formDetails['number']
        month = formDetails['month']
        year = formDetails['year']
        cvv = formDetails['cvv']
        sold = formDetails['sold']
        print("add card", number, name, month, year, cvv, sold, file=sys.stderr)
        add_card_table(name, number, month, year, cvv, sold)
        return render_template("main.html")
    return render_template("add_card.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5003)
