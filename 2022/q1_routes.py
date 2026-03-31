import csv
import os


def LoadRoutesData():
    """Task 1.1: Load routes data from CSV"""
    routes_file = "routes.csv"
    
    if not os.path.exists(routes_file):
        print(f"Error: {routes_file} not found")
        return []
    
    routes = []
    with open(routes_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            routes.append({
                'route_id': row[0],
                'origin': row[1],
                'destination': row[2],
                'distance': float(row[3]),
                'duration': int(row[4]),
                'price': float(row[5])
            })
    
    print(f"Loaded {len(routes)} routes")
    return routes


def DisplayAllRoutes(routes):
    """Task 1.1: Display all routes"""
    print("\nAll Routes:")
    print("-" * 100)
    print(f"{'RouteID':<10} {'Origin':<15} {'Destination':<15} {'Distance':>10} {'Duration':>10} {'Price':>10}")
    print("-" * 100)
    
    for route in routes:
        print(f"{route['route_id']:<10} {route['origin']:<15} {route['destination']:<15} "
              f"{route['distance']:>10.2f} {route['duration']:>10} {route['price']:>10.2f}")


def FindRouteByID(route_id, routes):
    """Task 1.2: Find route by ID"""
    for route in routes:
        if route['route_id'] == route_id:
            return route
    return None


def FindRoutesByOrigin(origin, routes):
    """Task 1.2: Find all routes from a specific origin"""
    matching = []
    for route in routes:
        if route['origin'].lower() == origin.lower():
            matching.append(route)
    return matching


def FindRoutesByDestination(destination, routes):
    """Task 1.2: Find all routes to a specific destination"""
    matching = []
    for route in routes:
        if route['destination'].lower() == destination.lower():
            matching.append(route)
    return matching


def FindRoutesInPriceRange(min_price, max_price, routes):
    """Task 1.2: Find routes within price range"""
    matching = []
    for route in routes:
        if min_price <= route['price'] <= max_price:
            matching.append(route)
    return matching


def AddNewRoute(route_id, origin, destination, distance, duration, price, routes):
    """Task 1.3: Add a new route"""
    if FindRouteByID(route_id, routes):
        print(f"Route ID {route_id} already exists")
        return False
    
    new_route = {
        'route_id': route_id,
        'origin': origin,
        'destination': destination,
        'distance': distance,
        'duration': duration,
        'price': price
    }
    routes.append(new_route)
    print(f"Added route: {route_id} - {origin} to {destination}")
    return True


def DeleteRoute(route_id, routes):
    """Task 1.3: Delete a route by ID"""
    for i, route in enumerate(routes):
        if route['route_id'] == route_id:
            removed = routes.pop(i)
            print(f"Deleted route: {removed['route_id']}")
            return True
    print(f"Route {route_id} not found")
    return False


def UpdateRoutePrice(route_id, new_price, routes):
    """Task 1.3: Update route price"""
    route = FindRouteByID(route_id, routes)
    if route:
        old_price = route['price']
        route['price'] = new_price
        print(f"Updated route {route_id} price from £{old_price:.2f} to £{new_price:.2f}")
        return True
    print(f"Route {route_id} not found")
    return False


def SaveRoutesToFile(filename, routes):
    """Task 1.4: Save routes to CSV file"""
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['RouteID', 'Origin', 'Destination', 'Distance', 'Duration', 'Price'])
        
        for route in routes:
            writer.writerow([route['route_id'], route['origin'], route['destination'],
                           route['distance'], route['duration'], route['price']])
    
    print(f"Saved {len(routes)} routes to {filename}")


def CalculateTotalRevenue(routes, passengers_per_route):
    """Task 1.4: Calculate total revenue"""
    total = 0
    print("\nRevenue by route:")
    for route_id, passengers in passengers_per_route.items():
        route = FindRouteByID(route_id, routes)
        if route:
            revenue = route['price'] * passengers
            total += revenue
            print(f"  {route_id}: £{revenue:.2f}")
    
    print(f"\nTotal Revenue: £{total:.2f}")
    return total


def FindShortestRoute(routes, origin, destination):
    """Task 1.4: Find shortest route by distance"""
    matching_routes = []
    
    for route in routes:
        if (route['origin'].lower() == origin.lower() and 
            route['destination'].lower() == destination.lower()):
            matching_routes.append(route)
    
    if not matching_routes:
        return None
    
    shortest = min(matching_routes, key=lambda x: x['distance'])
    return shortest


def FindCheapestRoute(routes, origin, destination):
    """Task 1.4: Find cheapest route"""
    matching_routes = []
    
    for route in routes:
        if (route['origin'].lower() == origin.lower() and 
            route['destination'].lower() == destination.lower()):
            matching_routes.append(route)
    
    if not matching_routes:
        return None
    
    cheapest = min(matching_routes, key=lambda x: x['price'])
    return cheapest


if __name__ == "__main__":
    routes = LoadRoutesData()
    
    if routes:
        DisplayAllRoutes(routes)
        
        print("\n" + "=" * 80)
        print("Task 1.2: Find routes from London")
        print("=" * 80)
        london_routes = FindRoutesByOrigin("London", routes)
        for r in london_routes:
            print(f"{r['route_id']}: {r['origin']} to {r['destination']} - £{r['price']:.2f}")
