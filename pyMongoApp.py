import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://uuuuuuu:pppppppp@cluster0.lwl1o.mongodb.net/?retryWrites=true&w=majority")
#uuuuu = username   ppppppp=password


db = client.test
collection = db.test_collection
print(db.test_collection)

new_posts = [{
    "cliente": "Paulo",
    "cpf": 12312312312,
    "endereco": "Rua Um, 100 - São Paulo/SP",
    "conta":[{
        "tipo": "poupanca",
        "agencia": "0001",
        "numero": "12345",
        "saldo": 2318.14
    },
    {
        "tipo": "corrente",
        "agencia": "0001",
        "numero": "12346",
        "saldo": 4342.14
    }]
},
{
    "cliente": "Pedro",
    "cpf": 12312323434,
    "endereco": "Rua Dois, 102 - São Paulo/SP",
    "conta":[{
        "tipo": "poupanca",
        "agencia": "0001",
        "numero": "12347",
        "saldo": 218.15
    },
    {
        "tipo": "corrente",
        "agencia": "0001",
        "numero": "12348",
        "saldo": 442.17
    }]
}]





posts = db.posts
print("ok1")
results = posts.insert_many(new_posts)
print("ok2")
print(results.inserted_ids)

print("Recuperando dados...")
print(db.posts.find_one({"cliente": "Pedro"}))