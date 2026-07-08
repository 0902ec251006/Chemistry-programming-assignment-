def periodic_element_info():
    # Database of selected common elements
    elements = {
        "Na": {
            "name": "Sodium", "atomic_num": 11, "atomic_mass": "22.99 u", 
            "group": 1, "period": 3, "config": "[Ne] 3s1", "oxidation": "+1",
            "application": "Liquid sodium is used as a coolant in nuclear reactors."
        },
        "Fe": {
            "name": "Iron", "atomic_num": 26, "atomic_mass": "55.85 u", 
            "group": 8, "period": 4, "config": "[Ar] 3d6 4s2", "oxidation": "+2, +3",
            "application": "Primary constituent of steel used in structural engineering and infrastructure."
        },
        "Cl": {
            "name": "Chlorine", "atomic_num": 17, "atomic_mass": "35.45 u", 
            "group": 17, "period": 3, "config": "[Ne] 3s2 3p5", "oxidation": "-1",
            "application": "Extensively used in water purification and manufacturing PVC plastics."
        },
        "Cu": {
            "name": "Copper", "atomic_num": 29, "atomic_mass": "63.55 u", 
            "group": 11, "period": 4, "config": "[Ar] 3d10 4s1", "oxidation": "+1, +2",
            "application": "Widely used in electrical wiring and heat exchangers due to high conductivity."
        },
        "Al": {
            "name": "Aluminium", "atomic_num": 13, "atomic_mass": "26.98 u", 
            "group": 13, "period": 3, "config": "[Ne] 3s2 3p1", "oxidation": "+3",
            "application": "Used in aerospace structures and automotive components due to its low density and corrosion resistance."
        }
    }

    print("--- Interactive Periodic Element Information Program ---")
    symbol = input("Enter the chemical symbol of an element (e.g., Na, Fe, Cl, Cu): ").strip()
    
    # Capitalizing correctly (e.g., 'fe' or 'FE' becomes 'Fe')
    symbol = symbol.capitalize()

    if symbol in elements:
        el = elements[symbol]
        print(f"\nInformation for {el['name']} ({symbol}):")
        print(f"  • Atomic Number: {el['atomic_num']}")
        print(f"  • Atomic Mass: {el['atomic_mass']}")
        print(f"  • Group: {el['group']}")
        print(f"  • Period: {el['period']}")
        print(f"  • Electronic Configuration: {el['config']}")
        print(f"  • Common Oxidation State: {el['oxidation']}")
        print(f"  • Engineering Application: {el['application']}")
    else:
        print("\n[!] Element symbol not found in the database. Please try Na, Fe, Cl, Cu, or Al.")

if __name__ == "__main__":
    periodic_element_info()