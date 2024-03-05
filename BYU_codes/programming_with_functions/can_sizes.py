from math import pi

def main():
    can_sizes = []
    while True:
        name = input("Enter the name of the can (or 'done' to finish): ")
        if name.lower() == "done":
            break
        radius = float(input("Enter the radius of the can: "))
        height = float(input("Enter the height of the can: "))
        cost = float(input("Enter the cost of the can: "))
        can_sizes.append({"name": name, "radius": radius, "height": height, "cost": cost})

    for can in can_sizes:
        volume = compute_volume(can["radius"], can["height"])
        surface_area = compute_surface_area(can["radius"], can["height"])
        can["volume"] = volume
        can["surface_area"] = surface_area
        can["storage_efficiency"] = compute_storage_efficiency(volume, surface_area)
        can["cost_efficiency"] = compute_cost_efficiency(volume, can["cost"])
        print(f"The volume of {can['name']} is {can['volume']:.2f}")
        print(f"The surface area of {can['name']} is {can['surface_area']:.2f}")
        print(f"The storage efficiency of {can['name']} is {can['storage_efficiency']:.2f}")
        print(f"The cost efficiency of {can['name']} is ${can['cost_efficiency']:.2f}")
        print()

        if can["name"] == "Can A" and compute_storage_efficiency(can["radius"], can["height"]) > 0.5:
            print(f"{can['name']} has the best storage efficiency so far.\n")
        if can["name"] == "Can A" and compute_cost_efficiency(can["volume"], can["cost"]) > 10:
            print(f"{can['name']} has the best cost efficiency so far.\n")
    if can_sizes:
        best_storage_efficiency = max(can["storage_efficiency"] for can in can_sizes)
        for can in can_sizes:
            if can["storage_efficiency"] == best_storage_efficiency:
                print(f"The can size with the best storage efficiency is {can['name']} with a value of {best_storage_efficiency:.2f}.")

        best_cost_efficiency = max(can["cost_efficiency"] for can in can_sizes)
        for can in can_sizes:
            if can["cost_efficiency"] == best_cost_efficiency:
                print(f"The can size with the best cost efficiency is {can['name']} with a value of {best_cost_efficiency:.2f}.")
    print()
    print_table(can_sizes)
    print()
    
def print_table(can_sizes):
    print(f"{'Name'.ljust(15)} | {'Storage Efficiency'.ljust(20)} | {'Cost Efficiency'.ljust(20)}")
    print("-" * 65)
    for can in can_sizes:
        storage_efficiency_formatted = format(can['storage_efficiency'], '.2f')
        cost_efficiency_formatted = "$" + ' ' + format(can['cost_efficiency'], '.2f')  # Add dollar sign to the formatted cost efficiency value
        print(f"{can['name'].ljust(15)} | {storage_efficiency_formatted.ljust(20)} | {cost_efficiency_formatted.ljust(20)}")

def compute_volume(radius, height):
    volume =  pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()