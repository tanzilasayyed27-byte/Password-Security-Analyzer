import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from password_analyzer import analyze_password
from entropy_analyzer import calculate_entropy, estimate_resistance
from hash_engine import generate_hash
from salt_engine import generate_salted_hash
from report_generator import save_report


def password_analysis():
    password = input("\nEnter TEST password: ")

    score, strength, checks = analyze_password(password)
    entropy = calculate_entropy(password)
    resistance = estimate_resistance(entropy)

    print("\n" + "=" * 55)
    print("PASSWORD SECURITY REPORT")
    print("=" * 55)

    print(f"Length              : {len(password)}")
    print(f"Security Score      : {score}/6")
    print(f"Password Strength   : {strength}")
    print(f"Entropy             : {entropy} bits")
    print(f"Resistance          : {resistance}")

    print("\nSecurity Checks:")
    for check in checks:
        print(f"  {check}")

    print("=" * 55)


def entropy_analysis():
    password = input("\nEnter TEST password: ")

    entropy = calculate_entropy(password)
    resistance = estimate_resistance(entropy)

    print("\n" + "=" * 55)
    print("ENTROPY & CRACK-RESISTANCE ANALYSIS")
    print("=" * 55)

    print(f"Password Length : {len(password)}")
    print(f"Entropy         : {entropy} bits")
    print(f"Resistance      : {resistance}")

    print("=" * 55)


def hashing_analysis():
    password = input("\nEnter TEST password: ")

    score, strength, checks = analyze_password(password)
    entropy = calculate_entropy(password)
    resistance = estimate_resistance(entropy)

    sha256_hash = generate_hash(password)
    salt, salted_hash = generate_salted_hash(password)

    print("\n" + "=" * 55)
    print("HASHING & SECURITY ANALYSIS")
    print("=" * 55)

    print(f"Strength        : {strength}")
    print(f"Score           : {score}/6")
    print(f"Entropy         : {entropy} bits")
    print(f"Resistance      : {resistance}")

    print("\nSHA-256 Hash:")
    print(sha256_hash)

    print("\nSalt:")
    print(salt)

    print("\nSalted SHA-256:")
    print(salted_hash)

    report_file = save_report(
        password,
        score,
        strength,
        entropy,
        resistance,
        sha256_hash,
        salt,
        salted_hash
    )

    print(f"\n✓ Security report saved to: {report_file}")
    print("=" * 55)


def main():
    while True:
        print("\n")
        print("=" * 55)
        print("     ADVANCED PASSWORD SECURITY ANALYZER")
        print("=" * 55)
        print("1. Password Strength Analysis")
        print("2. Entropy & Crack-Resistance Analysis")
        print("3. Hashing & Salting Analysis + Report")
        print("4. Exit")
        print("=" * 55)

        choice = input("Select an option: ")

        if choice == "1":
            password_analysis()

        elif choice == "2":
            entropy_analysis()

        elif choice == "3":
            hashing_analysis()

        elif choice == "4":
            print("\nExiting Password Security Analyzer...")
            break

        else:
            print("\nInvalid option. Please select 1-4.")


if __name__ == "__main__":
    main()
