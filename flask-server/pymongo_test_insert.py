import certifi

def get_database():    
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
    CONNECTION_STRING = "mongodb+srv://thankseve:feb48287@cluster0.hadh8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING,tlsCAFile=certifi.where())

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['Yelow_Token_Price']
    
# This is added so that many files can reuse the function get_database()


if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    collection_name = dbname["YelowCurrentTokenPrice"]
    collection_name2 = dbname['YellowCurrentTokenSupply']
    
    currentTokenSupply = {
        "CurrentTokenSupply":10**10
    }

    currentTokenPrice = {
        "price":0.7680000000114828485065834245
    }
    
    collection_name2.insert_one(currentTokenSupply)
    collection_name.insert_one(currentTokenPrice)

