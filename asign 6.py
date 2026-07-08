def corrosion_risk_assessment():
    print("--- Simple Corrosion Risk Assessment Program ---")
    
    try:
        humidity = float(input("Enter Relative Humidity (%): "))
        temperature = float(input("Enter Temperature (°C): "))
        ph = float(input("Enter pH level (0-14): "))
        salt_presence = input("Is salt present? (Yes/No): ").strip().lower()
        
        # Fundamental validation
        if not (0 <= ph <= 14) or not (0 <= humidity <= 100):
            print("\n[!] Invalid entry. Humidity must be 0-100% and pH must be 0-14.")
            return

        # Logical Conditions for Risk Classification
        # High Risk: Highly acidic/alkaline environments, or high humidity with salt
        if ph < 4.0 or ph > 10.0 or (humidity >= 70 and salt_presence == 'yes'):
            risk = "High"
            remarks = "Severe risk environment. Immediate protective coating or material substitution required."
        
        # Moderate Risk: Moderate humidity, mild pH imbalance, or salt presence under lower humidity
        elif (4.0 <= ph < 6.0) or (8.5 < ph <= 10.0) or (humidity >= 50) or (salt_presence == 'yes'):
            risk = "Moderate"
            remarks = "Corrosion likely over time. Regular monitoring and standard anti-corrosive measures advised."
        
        # Low Risk: Dry, neutral pH, and no salt accelerators
        else:
            risk = "Low"
            remarks = "Stable environment. Standard atmospheric corrosion rates apply."

        print("\n--- Assessment Result ---")
        print(f"Corrosion Risk Level: **{risk}**")
        print(f"Recommendation: {remarks}")

    except ValueError:
        print("\n[!] Invalid numeric input. Please restart and type valid values.")

if __name__ == "__main__":
    corrosion_risk_assessment()