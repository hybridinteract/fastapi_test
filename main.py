from fastapi import FastAPI
from models import Product
from database import session,engine
import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI app!"}

products = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Phone", description="Smartphone", price=499.99, quantity=50),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=30),
    Product(id=4, name="Monitor", description="4K UHD Monitor", price=299.99, quantity=20),
]

@app.get("/products")
def get_products():
    db=session()
    db.query()

    return products

@app.get("/products/{id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@app.post("/products")
def create_product(product:Product):
    products.append(product)
    return product

@app.put("/products/{id}")
def update_product(product_id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==product_id:
            products[i]=product
            return "product added successfully"
    return{"error":"product not f"}

@app.delete("/products/")
def delete_product(product_id: int):
    global products
    # Find product
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted successfully"}
    
    # If not found
    return {"error": "Product not found"}
