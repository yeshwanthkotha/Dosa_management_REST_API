from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Pydantic models for validation
class Customer(BaseModel):
    name: str
    phone: str

class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    customer_id: int
    item_id: int
    timestamp: int
    notes: str | None = None

# SQLite helper function
def get_db_connection():
    conn = sqlite3.connect("db.sqlite")
    conn.row_factory = sqlite3.Row
    return conn

# CRUD Endpoints for Customers
@app.post("/customers")
def create_customer(customer: Customer):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (customer.name, customer.phone))
        conn.commit()
        customer_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Phone number must be unique")
    conn.close()
    return {"id": customer_id, **customer.dict()}

@app.get("/customers/{id}")
def get_customer(id: int):
    conn = get_db_connection()
    customer = conn.execute("SELECT * FROM customers WHERE id = ?", (id,)).fetchone()
    conn.close()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return dict(customer)

@app.put("/customers/{id}")
def update_customer(id: int, customer: Customer):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET name = ?, phone = ? WHERE id = ?", (customer.name, customer.phone, id))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Customer not found")
    conn.close()
    return {"id": id, **customer.dict()}

@app.delete("/customers/{id}")
def delete_customer(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = ?", (id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Customer not found")
    conn.close()
    return {"detail": "Customer deleted successfully"}

# CRUD Endpoints for Items
@app.post("/items")
def create_item(item: Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (item.name, item.price))
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return {"id": item_id, **item.dict()}

@app.get("/items/{id}")
def get_item(id: int):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items WHERE id = ?", (id,)).fetchone()
    conn.close()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return dict(item)

@app.put("/items/{id}")
def update_item(id: int, item: Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET name = ?, price = ? WHERE id = ?", (item.name, item.price, id))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.close()
    return {"id": id, **item.dict()}

@app.delete("/items/{id}")
def delete_item(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.close()
    return {"detail": "Item deleted successfully"}

# CRUD Endpoints for Orders
@app.post("/orders")
def create_order(order: Order):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (customer_id, item_id, timestamp, notes) VALUES (?, ?, ?, ?)",
        (order.customer_id, order.item_id, order.timestamp, order.notes),
    )
    conn.commit()
    order_id = cursor.lastrowid
    conn.close()
    return {"id": order_id, **order.dict()}

@app.get("/orders/{id}")
def get_order(id: int):
    conn = get_db_connection()
    order = conn.execute("SELECT * FROM orders WHERE id = ?", (id,)).fetchone()
    conn.close()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return dict(order)

@app.put("/orders/{id}")
def update_order(id: int, order: Order):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE orders SET customer_id = ?, item_id = ?, timestamp = ?, notes = ? WHERE id = ?",
        (order.customer_id, order.item_id, order.timestamp, order.notes, id),
    )
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Order not found")
    conn.close()
    return {"id": id, **order.dict()}

@app.delete("/orders/{id}")
def delete_order(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE id = ?", (id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Order not found")
    conn.close()
    return {"detail": "Order deleted successfully"}
