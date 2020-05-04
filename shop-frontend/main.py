from flask import Flask, render_template, request, redirect, url_for
import requests
import csv
import sys

app = Flask(__name__)

products = []
products_ids = []

drinks = []
food = []

def get_drinks():
    global drinks
    url = sys.argv[1] + "drinks"
    resp = requests.get(url)
    resp = resp.json()
    drinks = resp
    print("resp drinks is: ", resp, file=sys.stderr)


def get_food():
    global food
    url = sys.argv[1] + "food"
    resp = requests.get(url)
    resp = resp.json()
    food = resp
    print("resp food is: ", resp, file=sys.stderr)

def get_drink_price(id):
    get_drinks()
    for _id, name, price in drinks:
        if id == _id:
            print("Found price", file=sys.stderr)
            return price
    return 0

def get_drink_name(id):
    get_drinks()
    for _id, name, price in drinks:
        if id == _id:
            print("Found name", file=sys.stderr)
            return name
    return ""

def get_food_price(id):
    get_food()
    for _id, name, price in food:
        if id == _id:
            print("Found price", file=sys.stderr)
            return price
    return 0

def get_food_name(id):
    get_food()
    for _id, name, price in food:
        if id == _id:
            print("Found name", file=sys.stderr)
            return name
    return ""

def verify_card(number, name, month, year, cvv):
    url = sys.argv[1] + "verify_card/" + number + "/" + name + "/" + month + "/" + year + "/" + cvv
    resp = requests.get(url)
    resp = resp.text
    print("resp card is: ", resp, file=sys.stderr)
    if resp == "yes":
        return True
    return False

def complete_tranzaction(arg):
    url = sys.argv[1] + "complete_tranzaction/" + arg
    resp = requests.get(url)
    resp = resp.text
    print("resp tranzaction is: ", resp, file=sys.stderr)
    if resp == "yes":
        return True
    return False

# admin app's main page displays all the options
@app.route('/', methods=['GET', 'POST'])
def main() -> str:
    get_drinks()
    get_food()
    return render_template("main.html")

# meniu page displays all products
@app.route('/meniu', methods=['GET', 'POST'])
def meniu() -> str:
    get_drinks()
    drinks_dict = {}
    for id, name, price in drinks:
        drinks_dict[id] = (name, price)
    return render_template("meniu.html", drinks=drinks_dict)

# food meniu page displays all products
@app.route('/meniu-food', methods=['GET', 'POST'])
def meniu_food() -> str:
    get_food()
    food_dict = {}
    for id, name, price in food:
        food_dict[id] = (name, price)
    return render_template("meniu-food.html", food=food_dict)

# displays checkout form
@app.route('/checkout', methods=['GET', 'POST'])
def checkout() -> str:
    if request.method == 'POST':
        formDetails = request.form
        print(formDetails['cardname'], file=sys.stderr)
    global products
    total = 0
    for _, v in products:
        total += v
    return render_template("checkout.html", num=len(products), products=products, total=total)

# displays contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact() -> str:
    return render_template("contact.html")

@app.route('/btn1')
def btn1():
    id = "b1"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn1', file=sys.stderr)
    return ""

@app.route('/btn2')
def btn2():
    id = "b2"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn2', file=sys.stderr)
    return ""

@app.route('/btn3')
def btn3():
    id = "b3"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn3', file=sys.stderr)
    return ""

@app.route('/btn4')
def btn4():
    id = "b4"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn4', file=sys.stderr)
    return ""

@app.route('/btn5')
def btn5():
    id = "b5"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn5', file=sys.stderr)
    return ""

@app.route('/btn6')
def btn6():
    id = "b6"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn6', file=sys.stderr)
    return ""

@app.route('/btn7')
def btn7():
    id = "b7"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn7', file=sys.stderr)
    return ""

@app.route('/btn8')
def btn8():
    id = "b8"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn8', file=sys.stderr)
    return ""

@app.route('/btn9')
def btn9():
    id = "b9"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn9', file=sys.stderr)
    return ""

@app.route('/btn10')
def btn10():
    id = "b10"
    price = get_drink_price(id)
    name = get_drink_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btn10', file=sys.stderr)
    return ""

@app.route('/btnf1')
def btnf1():
    id = "m1"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf1', file=sys.stderr)
    return ""

@app.route('/btnf2')
def btnf2():
    id = "m2"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf2', file=sys.stderr)
    return ""

@app.route('/btnf3')
def btnf3():
    id = "m3"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf3', file=sys.stderr)
    return ""

@app.route('/btnf4')
def btnf4():
    id = "m4"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf4', file=sys.stderr)
    return ""

@app.route('/btnf5')
def btnf5():
    id = "m5"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf5', file=sys.stderr)
    return ""

@app.route('/btnf6')
def btnf6():
    id = "m6"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf6', file=sys.stderr)
    return ""

@app.route('/btnf7')
def btnf7():
    id = "m7"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf7', file=sys.stderr)
    return ""

@app.route('/btnf8')
def btnf8():
    id = "m8"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf8', file=sys.stderr)
    return ""

@app.route('/btnf9')
def btnf9():
    id = "m9"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf9', file=sys.stderr)
    return ""

@app.route('/btnf10')
def btnf10():
    id = "m10"
    price = get_food_price(id)
    name = get_food_name(id)
    global products
    global products_ids
    products_ids.append(id)
    products.append((name, price))
    print('Btnf10', file=sys.stderr)
    return ""

@app.route('/deleteCart')
def deleteCart():
    global products
    global products_ids
    products = []
    products_ids = []
    print('delete cart', file=sys.stderr)
    return render_template("checkout.html", num=0, products=products, total=0)

@app.route('/buy',  methods=['GET', 'POST'])
def buy():
    global products
    global products_ids
    # [TODO] send products to backend to complete tranzaction
    if request.method == 'POST':
        formDetails = request.form
        name = formDetails['cardname']
        number = formDetails['cardnumber']
        month = formDetails['expmonth']
        year = formDetails['expyear']
        cvv = formDetails['cvv']
        if not verify_card(number, name, month, year, cvv):
            # [TODO] mesaj eroare ca nu-i bun cardul
            print("Error in card ", file=sys.stderr)
            products = []
            products_ids = []
            return render_template("error_message.html", msg="Card incorect/Fonduri insuficiente.")
        else:
            products_ids.insert(0, number)
            if not complete_tranzaction(str(products_ids)):
                products = []
                products_ids = []
                return render_template("error_message.html", msg="Produs indisponibil.")
        products = []
        products_ids = []
        return render_template("success_message.html")
    products = []
    products_ids = []
    print('buy cart', file=sys.stderr)
    return render_template("checkout.html", num=0, products=products, total=0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
