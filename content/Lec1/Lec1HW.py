# Assignment: Practice if/else and match

# Task 1: Temperature Status
def temperature_status(temp):
    # TODO: Use if/else
    # If temp < 0 → return "Freezing"
    # If temp is between 0 and 30 → return "Normal"
    # If temp > 30 → return "Hot"
    pass


# Task 2: Traffic Light
def traffic_light(color):
    # TODO: Use if / elif / else
    # color = "red" → return "Stop"
    # color = "yellow" → return "Wait"
    # color = "green" → return "Go"
    # any other → return "Unknown"
    pass


# Task 3: Season (using match)
def season(month):
    # TODO: Use match-case
    # 12, 1, 2 → "Winter"
    # 3, 4, 5 → "Spring"
    # 6, 7, 8 → "Summer"
    # 9, 10, 11 → "Autumn"
    # anything else → "Invalid"
    pass


# Task 4 (Challenge): BMI Calculator
def bmi_category(weight, height):
    # TODO: Use if / elif / else
    # BMI = weight (kg) / (height (m) * height (m))
    # BMI < 18.5 → "Underweight"
    # 18.5 <= BMI < 24 → "Normal"
    # 24 <= BMI < 30 → "Overweight"
    # BMI >= 30 → "Obese"
    pass


# Main function: Testing
def main():
    print("=== Test temperature_status ===")
    print(temperature_status(-5))   # Expected: Freezing
    print(temperature_status(20))   # Expected: Normal
    print(temperature_status(35))   # Expected: Hot

    print("\n=== Test traffic_light ===")
    print(traffic_light("red"))     # Expected: Stop
    print(traffic_light("green"))   # Expected: Go
    print(traffic_light("blue"))    # Expected: Unknown

    print("\n=== Test season ===")
    print(season(1))    # Expected: Winter
    print(season(4))    # Expected: Spring
    print(season(8))    # Expected: Summer
    print(season(11))   # Expected: Autumn
    print(season(15))   # Expected: Invalid

    print("\n=== Test bmi_category ===")
    print(bmi_category(50, 1.7))    # ≈ 17.3 → Underweight
    print(bmi_category(65, 1.7))    # ≈ 22.5 → Normal
    print(bmi_category(80, 1.7))    # ≈ 27.7 → Overweight
    print(bmi_category(100, 1.7))   # ≈ 34.6 → Obese


# Entry point
if __name__ == "__main__":
    main()