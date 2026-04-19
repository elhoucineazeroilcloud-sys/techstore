from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "TechStore API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 999},
        {"id": 2, "name": "Mouse", "price": 29},
        {"id": 3, "name": "Keyboard", "price": 49},
    ]
