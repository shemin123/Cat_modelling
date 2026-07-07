def calculate_hazard(intensity):
    """Simple hazard intensity calculation."""
    return intensity * 1.2


if __name__ == "__main__":
    print("Hazard =", calculate_hazard(100))