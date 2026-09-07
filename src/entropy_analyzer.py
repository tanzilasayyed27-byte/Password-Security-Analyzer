import math
import string


def calculate_entropy(password):
    pool = 0

    if any(c.islower() for c in password):
        pool += 26

    if any(c.isupper() for c in password):
        pool += 26

    if any(c.isdigit() for c in password):
        pool += 10

    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    if pool == 0:
        return 0

    return round(len(password) * math.log2(pool), 2)


def estimate_resistance(entropy):
    if entropy < 28:
        return "VERY LOW"
    elif entropy < 36:
        return "LOW"
    elif entropy < 60:
        return "MODERATE"
    elif entropy < 80:
        return "HIGH"
    else:
        return "VERY HIGH"


def main():
    print("=== Password Entropy & Crack-Resistance Analyzer ===")

    password = input("Enter a test password: ")

    entropy = calculate_entropy(password)
    resistance = estimate_resistance(entropy)

    print("\nSecurity Metrics")
    print("-" * 45)
    print(f"Password Length       : {len(password)}")
    print(f"Estimated Entropy     : {entropy} bits")
    print(f"Crack Resistance      : {resistance}")
    print("-" * 45)


if __name__ == "__main__":
    main()
