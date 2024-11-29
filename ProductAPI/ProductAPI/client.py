import requests

BASE_URL = "http://127.0.0.1:5000"

def add_product(name, description, price):
    url = f"{BASE_URL}/products"
    payload = {"name": name, "description": description, "price": price}
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Failed to create product:", response.json())

def list_products():
    url = f"{BASE_URL}/products"
    response = requests.get(url)
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Failed to retrieve products")

if __name__ == "__main__":
    # Test adding products
    add_product("Laptop", "A high-end gaming laptop", 1500.75)
    add_product("Smartphone", "A smartphone with a great camera", 800.99)

    # Test listing products
    list_products()
