from ast import Str
from flask import Flask,request,jsonify

import math
from decimal import Decimal, getcontext
from pymongo_test_insert import get_database
from bson.decimal128 import Decimal128, create_decimal128_context
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

dbname = get_database()

getcontext().prec = 8

#numOfTokens = Amount/ Price 
#Amount = numOfTokens * Price 

presentSupply = 0
currentlocalprice = 0
lastTokenPrice =0
app = Flask(__name__)

@app.route('/compute/',methods=['POST', 'GET'])
@cross_origin()
def compute():
    amount = int(request.args.get('tokens'))
    tokensForPrice = PriceToTokens(amount)
    return {"TokensForPrice":Decimal(tokensForPrice)}


@app.route('/currentpriceoftoken/', methods=['GET', 'POST'])
def currentPriceoftoken():
    return {"currentpriceoftoken": Decimal(currentPrice)}

def PriceToTokens(amount):
    getDataBaseValues()
    
    print(presentSupply)
    print(Decimal(currentlocalprice))
    nextTokenPrice = calculatePrice(1)
    print("before looping")
    print(nextTokenPrice)
    count=0    
    while (amount > nextTokenPrice):        
        nextTokenPrice = calculatePrice(1)              
        count = count + 1
    
    print(count)
    updateDataBase()
    return count


def calculatePrice(z):
    global presentSupply
    global currentlocalprice
    global lastTokenPrice

    x= presentSupply + z
    a = Decimal(x/10**11)
    sqrA = Decimal(a**Decimal(0.5))    
    constantmul = Decimal(1000 * sqrA)
    
    
    factorFormula = Decimal(a + Decimal(0.2))
    
    numerator = Decimal(factorFormula**5)
    
    denfact = Decimal(a**10)
    denominatorPrior = Decimal(Decimal(1)+denfact)
    denominator = Decimal(denominatorPrior**Decimal(0.5))
    
    pricePrior = Decimal((numerator/denominator))
    Price = Decimal(pricePrior * constantmul)
    lastTokenPrice = Price
    #print("the price of next token")
    print(Price)
    #finalPrice = Decimal(currentlocalprice-Price)
    print("final")
    #print(finalPrice)
    currentlocalprice = currentlocalprice + Price
    presentSupply = presentSupply + 1    
    return currentlocalprice


@app.route('/getCurrentTokenPrice/', methods=['GET', 'POST'])
def getCurrentTokenPrice():
    # Create a new collection
    collection_name = dbname["YelowCurrentTokenPrice"]
    item_details = collection_name.find()
    print("worldddddddddddd")
    price = (list(item_details)[-1]['price'])   
    #for record in item_details:
    #    price =  record['price']        
    # iterate the MongoDB result dict in Python 3      
    #price_details = [doc for doc in collection_name.find({'price':1})] 
    return Decimal(str(price))


def getBaseTokensupply():
    # Create a new collection
    collection_name = dbname["YellowCurrentTokenSupply"]
    item_details = collection_name.find()
    supply = (list(item_details)[-1]['CurrentTokenSupply'])
    #for record in item_details:
    #    supply =  record['CurrentTokenSupply']
    #    print(record['CurrentTokenSupply'])
    # iterate the MongoDB result dict in Python 3        
    #price_details = [doc for doc in collection_name.find({'price':1})] 
    return Decimal(str(supply))

def updateDataBase():
    collection_name_price = dbname["YelowCurrentTokenPrice"]
    collection_name_token = dbname["YellowCurrentTokenSupply"]
    
    currentTokenSupplyforDB = {
        "CurrentTokenSupply": Decimal128(presentSupply-1)
    }

    currentTokenPriceforDB = {        
        "price": Decimal128(lastTokenPrice)
    }
    collection_name_token.insert_one(currentTokenSupplyforDB)
    collection_name_price.insert_one(currentTokenPriceforDB)


def getDataBaseValues():
    global currentlocalprice
    currentlocalprice= Decimal(str(getCurrentTokenPrice()))
    global presentSupply 
    presentSupply= Decimal(str(getBaseTokensupply()))


if __name__ == '__main__':
    app.run(debug=True)