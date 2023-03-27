import json
from flask import Flask, render_template, redirect, request

app = Flask("main")

income = []


@app.route('/')
def home():
    total_sales = 0
    for sale in income:
        total_sales += float(sale['price'])
    return render_template('index.html', name="Sales records", sales=income, total=round(total_sales, 2))

@app.route('/add_sale', methods=['POST'])
def add_income():
    income.append(
        {
            'product': request.form['product'],
            'price': request.form['price']
        }
    )
    return redirect('/')

def save_sales():
    with open('sales.txt','w') as file:
        file.write(json.dumps(income))
        
def load_sales():
    global income
    with open('sales.txt','r') as file:
        income = json.loads("".join(file.readlines()))
    

if __name__=="__main__":
    app.run()
