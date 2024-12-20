# Dosa Management REST API

This project is a REST API backend for managing a dosa restaurant. It provides CRUD (Create, Read, Update, Delete) functionality for three main entities: `customers`, `items`, and `orders`. The API is built using **FastAPI** and uses **SQLite** as the database.

## Features

1. **Customers Management**
   - Add a new customer.
   - Retrieve customer details by ID.
   - Update existing customer details.
   - Delete a customer by ID.

2. **Menu Items Management**
   - Add new items to the menu.
   - Retrieve item details by ID.
   - Update existing item details.
   - Delete a menu item by ID.

3. **Order Management**
   - Place a new order by linking customers and items.
   - Retrieve order details by ID.
   - Update order details.
   - Delete an order by ID.

4. **Interactive API Documentation**
   - Automatically generated Swagger UI and Redoc are available for testing.

## Prerequisites

- Python 3.9 or higher
- Pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Dosa_management_REST_API
   ```

2. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn pydantic sqlite3
   ```

3. Initialize the database:
   ```bash
   python init_db.py
   ```

4. Run the FastAPI server:
   ```bash
   python -m uvicorn main:app --reload
   ```

## Usage

### Access the API

1. Open your browser and navigate to the Swagger UI:
   ```
   http://127.0.0.1:8000/docs
   ```
   Use this interactive interface to test API endpoints.

2. Alternatively, use a tool like **Postman** or `curl` commands to test the API directly.

### Example Endpoints

#### Customers
- **POST /customers**: Create a new customer.
- **GET /customers/{id}**: Retrieve a customer by ID.
- **PUT /customers/{id}**: Update a customer's details.
- **DELETE /customers/{id}**: Delete a customer by ID.

#### Items
- **POST /items**: Add a new menu item.
- **GET /items/{id}**: Retrieve an item by ID.
- **PUT /items/{id}**: Update an item's details.
- **DELETE /items/{id}**: Delete an item by ID.

#### Orders
- **POST /orders**: Place a new order.
- **GET /orders/{id}**: Retrieve an order by ID.
- **PUT /orders/{id}**: Update an order's details.
- **DELETE /orders/{id}**: Delete an order by ID.

### Example `curl` Commands

#### Add a Customer
```bash
curl -X POST "http://127.0.0.1:8000/customers" -H "Content-Type: application/json" -d '{"name": "Alice Brown", "phone": "111-222-3333"}'
```

#### Retrieve an Item
```bash
curl -X GET "http://127.0.0.1:8000/items/1"
```

#### Place an Order
```bash
curl -X POST "http://127.0.0.1:8000/orders" -H "Content-Type: application/json" -d '{"customer_id": 1, "item_id": 1, "timestamp": 1700000000, "notes": "Extra spicy"}'
```

## Project Structure
```
Dosa_management_REST_API/
├── db.sqlite          # SQLite database file
├── example_orders.json # Sample data file (if applicable)
├── init_db.py         # Script to initialize the database
├── main.py            # FastAPI application
├── README.md          # Documentation file
```

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
- **Yeshwanth Kotha**