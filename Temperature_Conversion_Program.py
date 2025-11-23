#!/usr/bin/env python3
"""
Temperature conversion CLI
Supports: Celsius (C), Fahrenheit (F) and Kelvin (K)
Author: ChatGPT
"""

def c_to_f(c): return (c * 9/5) + 32
def c_to_k(c): return c + 273.15
def f_to_c(f): return (f - 32) * 5/9
def f_to_k(f): return c_to_k(f_to_c(f))
def k_to_c(k): return k - 273.15
def k_to_f(k): return c_to_f(k_to_c(k))

def parse_unit(u: str) -> str:
    u = u.replace("°", "").strip().lower()   # remove degree symbol

    if u in ("c", "celsius", "celcius"):
        return "C"
    if u in ("f", "fahrenheit"):
        return "F"
    if u in ("k", "kelvin"):
        return "K"
    raise ValueError("Unknown unit. Use C, F, or K.")

def pretty(val):
    return f"{val:.2f}".rstrip("0").rstrip(".")

def main():
    print("Temperature Conversion Program")
    print("Enter a temperature and unit (C, F, K). Example: 25 C")

    try:
        raw = input("Temperature (e.g. 25 C): ").strip()

        parts = raw.split()
        if len(parts) < 2:
            # Allow formats like "25°C"
            import re
            m = re.match(r"([-+]?[0-9]*\.?[0-9]+)\s*([A-Za-z°]+)", raw)
            if not m:
                raise ValueError("Invalid input format.")
            temp_str, unit_str = m.groups()
        else:
            temp_str, unit_str = parts[0], " ".join(parts[1:])

        temp = float(temp_str)
        unit = parse_unit(unit_str)

        if unit == "C":
            print(f"\nInput: {pretty(temp)} °C")
            print("Fahrenheit:", pretty(c_to_f(temp)), "°F")
            print("Kelvin:", pretty(c_to_k(temp)), "K")

        elif unit == "F":
            print(f"\nInput: {pretty(temp)} °F")
            print("Celsius:", pretty(f_to_c(temp)), "°C")
            print("Kelvin:", pretty(f_to_k(temp)), "K")

        else:  # Kelvin
            print(f"\nInput: {pretty(temp)} K")
            print("Celsius:", pretty(k_to_c(temp)), "°C")
            print("Fahrenheit:", pretty(k_to_f(temp)), "°F")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
