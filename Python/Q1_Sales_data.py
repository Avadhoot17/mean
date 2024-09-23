# Sample Sales Data with Demo Product Names
sales_data = [
    {"product_name": "Wireless Mouse",      "category": "Electronics",     "units_sold": 100,  "unit_price": 20.5},
    {"product_name": "Bluetooth Headphones", "category": "Electronics",   "units_sold": 250,  "unit_price": 25.5},
    {"product_name": "Office Chair",        "category": "Furniture",       "units_sold": 200,  "unit_price": 10.5},
    {"product_name": "Gaming Laptop",       "category": "Electronics",     "units_sold": 250,  "unit_price": 20.5},
    {"product_name": "Desk Organizer",      "category": "Office Supplies", "units_sold": 200,  "unit_price": 20.0}
]

# Function to calculate total sales
def calculate_total_sales(data):
    """Calculate the total sales amount from the sales data."""
    total_sales = 0  # Initialize total sales
    for item in data:
        # Calculate sales for each item and add to total
        total_sales += item["units_sold"] * item["unit_price"]
    return total_sales  # Return the total sales amount

# Function to calculate average sales per product
def calculate_average_sales(data):
    """Calculate the average sales per product."""
    total_sales = calculate_total_sales(data)  # Get total sales
    total_products = len(data)  # Get number of products
    # Calculate and return average sales per product
    return total_sales / total_products if total_products > 0 else 0

# Function to find the top-selling product
def find_top_selling_product(data):
    """Identify the product with the highest units sold."""
    top_product = None  # Initialize variable for top product
    max_units = 0  # Initialize maximum units sold
    for product in data:
        # Check if current product has more units sold than the max
        if product["units_sold"] > max_units:
            max_units = product["units_sold"]  # Update max units
            top_product = product  # Update top product
    # Return the name of the top product and its units sold
    return top_product["product_name"], max_units

# Function to calculate sales by category
def calculate_sales_by_category(data):
    """Calculate total sales for each category."""
    category_sales = {}  # Initialize dictionary to hold category sales
    for item in data:
        category = item["category"]  # Get the category of the item
        sales = item["units_sold"] * item["unit_price"]  # Calculate sales for the item
        # Check if category already exists in the dictionary
        if category in category_sales:
            category_sales[category] += sales  # Add to existing sales
        else:
            category_sales[category] = sales  # Initialize sales for new category

    return category_sales  # Return the dictionary with sales by category

# Running the Analysis 
total_sales = calculate_total_sales(sales_data)  # Get total sales
average_sales = calculate_average_sales(sales_data)  # Get average sales
top_product, top_units = find_top_selling_product(sales_data)  # Get top-selling product
sales_by_category = calculate_sales_by_category(sales_data)  # Get sales by category

# Printing the Results 
print(f"Total Sales: Rs{total_sales:.2f}")  # Print total sales formatted to 2 decimal places
print(f"Average Sales per Product: Rs{average_sales:.2f}")  # Print average sales
print(f"Top Selling Product: {top_product} ({top_units} units sold)")  # Print top product info
print("Sales by Category:")  # Print header for sales by category
for category, sales in sales_by_category.items():
    print(f"{category}: Rs{sales:.2f}")  # Print sales for each category formatted to 2 decimal places