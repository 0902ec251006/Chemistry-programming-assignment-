def plastic_identifier():
    # Database matching resin codes 1 through 7
    recycling_db = {
        1: {
            "name": "PETE / PET (Polyethylene Terephthalate)",
            "products": "Soft drink bottles, water bottles, salad dressing jars, peanut butter jars.",
            "recyclability": "Highly Recyclable. Universally accepted by curbside programs.",
            "remarks": "Intended for single-use. Repeated reuse increases the risk of leaching and bacterial growth."
        },
        2: {
            "name": "HDPE (High-Density Polyethylene)",
            "products": "Milk jugs, detergent bottles, shampoo bottles, grocery bags, recycling bins.",
            "recyclability": "Highly Recyclable. Widely accepted everywhere.",
            "remarks": "Very safe plastic; carries a low risk of chemical leaching into food or liquids."
        },
        3: {
            "name": "PVC (Polyvinyl Chloride)",
            "products": "Plumbing pipes, cable insulation, window frames, medical tubing, credit cards.",
            "recyclability": "Rarely Recycled. Seldom accepted by municipal recycling programs.",
            "remarks": "Contains toxic chemicals (phthalates) during lifecycle. Highly hazardous if burned."
        },
        4: {
            "name": "LDPE (Low-Density Polyethylene)",
            "products": "Squeeze bottles, shopping bags, dry cleaning bags, cling wraps, bread bags.",
            "recyclability": "Recyclable in select locations. Plastic bags usually require special drop-off points.",
            "remarks": "Relatively safe plastic, though thin films easily clog commercial sorting machinery."
        },
        5: {
            "name": "PP (Polypropylene)",
            "products": "Yogurt containers, syrup bottles, medicine bottles, straws, car bumpers.",
            "recyclability": "Increasingly Recycled. Accepted by many curbside programs now.",
            "remarks": "High melting point makes it safe for hot liquids. Highly durable and heat-resistant."
        },
        6: {
            "name": "PS (Polystyrene / Styrofoam)",
            "products": "Disposable coffee cups, plastic cutlery, take-out containers, packing peanuts.",
            "recyclability": "Hardly Recycled. Generally rejected due to low structural density and high transport costs.",
            "remarks": "Can leach styrene (a suspected carcinogen) when heated. Environmentally notorious for fragmenting."
        },
        7: {
            "name": "OTHER (Miscellaneous Plastics like Polycarbonate, Acrylic, Nylon, or Bioplastics)",
            "products": "Baby bottles, 5-gallon water jugs, safety glasses, electronic casings, fiberglass.",
            "recyclability": "Traditionally Non-Recycled. Only specialized industrial operations take them.",
            "remarks": "A catch-all category. Bisphenol A (BPA) is often found in older polycarbonate formulations."
        }
    }

    while True:
        print("\n--- Identification of Common Plastics Using Recycling Codes ---")
        print("1. Code 1 (PETE)")
        print("2. Code 2 (HDPE)")
        print("3. Code 3 (PVC)")
        print("4. Code 4 (LDPE)")
        print("5. Code 5 (PP)")
        print("6. Code 6 (PS)")
        print("7. Code 7 (OTHER)")
        print("8. Exit Program")
        
        try:
            choice = int(input("\nEnter a recycling code (1-7) or 8 to Exit: "))
            
            if choice == 8:
                print("Exiting program. Thank you!")
                break
            elif choice in recycling_db:
                data = recycling_db[choice]
                print("\n==================================================")
                print(f"Recycling Code: [{choice}]")
                print(f"• Polymer Name:        {data['name']}")
                print(f"• Common Products:     {data['products']}")
                print(f"• Recyclability:       {data['recyclability']}")
                print(f"• Environmental Notes: {data['remarks']}")
                print("==================================================")
            else:
                print("\n[!] Code out of range. Please choose a valid number between 1 and 8.")
        except ValueError:
            print("\n[!] Invalid input format. Please enter an integer value.")

if __name__ == "__main__":
    plastic_identifier()