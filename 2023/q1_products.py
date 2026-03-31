import csv
import os


class Product:
    """Task 1.1: Product class"""
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return (f"ID: {self.product_id}, Name: {self.name}, "
                f"Category: {self.category}, Price: £{self.price:.2f}, "
                f"Stock: {self.stock}")


def LoadProducts(filename="products.csv"):
    """Task 1.1: Load products from CSV file"""
    products = {}
    
    if not os.path.exists(filename):
        print(f"Error: {filename} not found")
        return products
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            product_id = row[0]
            products[product_id] = Product(row[0], row[1], row[2], 
                                           float(row[3]), int(row[4]))
    
    print(f"Loaded {len(products)} products")
    return products


def DisplayAllProducts(products):
    """Task 1.1: Display all products"""
    print("\nAll Products:")
    print("-" * 100)
    
    for product in products.values():
        print(product)


def DisplayProductsByCategory(category, products):
    """Task 1.2: Display products by category"""
    found = []
    for product in products.values():
        if product.category.lower() == category.lower():
            found.append(product)
    
    if found:
        print(f"\nProducts in category '{category}':")
        for product in found:
            print(product)
    else:
        print(f"No products found in category '{category}'")
    
    return found


def DisplayProductsByPriceRange(min_price, max_price, products):
    """Task 1.2: Display products within price range"""
    found = []
    for product in products.values():
        if min_price <= product.price <= max_price:
            found.append(product)
    
    if found:
        print(f"\nProducts priced between £{min_price:.2f} and £{max_price:.2f}:")
        for product in found:
            print(product)
    else:
        print(f"No products found in price range £{min_price:.2f} - £{max_price:.2f}")
    
    return found


def SearchProductsByName(search_term, products):
    """Task 1.2: Search products by name (partial match)"""
    found = []
    search_lower = search_term.lower()
    
    for product in products.values():
        if search_lower in product.name.lower():
            found.append(product)
    
    if found:
        print(f"\nProducts matching '{search_term}':")
        for product in found:
            print(product)
    else:
        print(f"No products found matching '{search_term}'")
    
    return found


def AddNewProduct(product_id, name, category, price, stock, products):
    """Task 1.3: Add a new product"""
    if product_id in products:
        print(f"Product ID {product_id} already exists")
        return False
    
    products[product_id] = Product(product_id, name, category, price, stock)
    print(f"Added product: {name}")
    return True


def UpdateProductPrice(product_id, new_price, products):
    """Task 1.3: Update product price"""
    if product_id in products:
        old_price = products[product_id].price
        products[product_id].price = new_price
        print(f"Updated {products[product_id].name} price from £{old_price:.2f} to £{new_price:.2f}")
        return True
    
    print(f"Product {product_id} not found")
    return False


def UpdateProductStock(product_id, new_stock, products):
    """Task 1.3: Update product stock"""
    if product_id in products:
        old_stock = products[product_id].stock
        products[product_id].stock = new_stock
        print(f"Updated {products[product_id].name} stock from {old_stock} to {new_stock}")
        return True
    
    print(f"Product {product_id} not found")
    return False


def DeleteProduct(product_id, products):
    """Task 1.3: Delete a product"""
    if product_id in products:
        removed = products.pop(product_id)
        print(f"Deleted product: {removed.name}")
        return True
    
    print(f"Product {product_id} not found")
    return False


def SaveProducts(filename, products):
    """Task 1.4: Save all products to CSV file"""
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ProductID", "Name", "Category", "Price", "Stock"])
        
        for product in products.values():
            writer.writerow([product.product_id, product.name, product.category,
                           f"{product.price:.2f}", product.stock])
    
    print(f"Saved {len(products)} products to {filename}")


def CalculateTotalInventoryValue(products):
    """Task 1.4: Calculate total inventory value"""
    total = 0
    for product in products.values():
        total += product.price * product.stock
    
    print(f"Total inventory value: £{total:.2f}")
    return total


def GetLowStockProducts(threshold, products):
    """Task 1.4: Get products with stock below threshold"""
    low_stock = []
    for product in products.values():
        if product.stock < threshold:
            low_stock.append(product)
    
    if low_stock:
        print(f"\nLow stock products (below {threshold}):")
        for product in low_stock:
            print(product)
    else:
        print(f"No products with stock below {threshold}")
    
    return low_stock


def GetProductsByCategory(products):
    """Task 1.4: Get products grouped by category"""
    categories = {}
    
    for product in products.values():
        if product.category not in categories:
            categories[product.category] = []
        categories[product.category].append(product)
    
    for category, products_list in categories.items():
        print(f"\n{category}: {len(products_list)} products")
        for product in products_list:
            print(f"  - {product.name}: £{product.price:.2f}")
    
    return categories


def CalculateCategoryTotals(products):
    """Task 1.4: Calculate total value by category"""
    categories = {}
    
    for product in products.values():
        value = product.price * product.stock
        if product.category not in categories:
            categories[product.category] = 0
        categories[product.category] += value
    
    print("\nValue by category:")
    for category, total in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: £{total:.2f}")
    
    return categories


if __name__ == "__main__":
    products = LoadProducts("products.csv")
    
    if products:
        DisplayAllProducts(products)
        
        print("\n" + "=" * 80)
        print("Task 1.2: Search and Filter")
        print("=" * 80)
        DisplayProductsByCategory("Electronics", products)
        DisplayProductsByPriceRange(100, 500, products)
        SearchProductsByName("phone", products)
