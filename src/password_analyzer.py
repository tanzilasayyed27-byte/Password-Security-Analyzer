import re


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "iloveyou"
}


def analyze_password(password):
    score = 0
    checks = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, "VERY WEAK", [
            "✗ Common password detected",
            "✗ Easily guessable password"
        ]

    if len(password) >= 8:
        score += 1
        checks.append("✓ At least 8 characters")
    else:
        checks.append("✗ Less than 8 characters")

    if len(password) >= 12:
        score += 1
        checks.append("✓ At least 12 characters")

    if re.search(r"[A-Z]", password):
        score += 1
        checks.append("✓ Contains uppercase letter")
    else:
        checks.append("✗ No uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
        checks.append("✓ Contains lowercase letter")
    else:
        checks.append("✗ No lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
        checks.append("✓ Contains number")
    else:
        checks.append("✗ No number")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
        checks.append("✓ Contains special character")
    else:
        checks.append("✗ No special character")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return score, strength, checks


def main():
    print("=== Advanced Password Security Analyzer ===")

    password = input("Enter a test password: ")

    score, strength, checks = analyze_password(password)

    print("\nSecurity Analysis:")
    print("-" * 45)

    for check in checks:
        print(check)

    print("-" * 45)
    print(f"Security Score: {score}/6")
    print(f"Password Strength: {strength}")

    if strength in ("WEAK", "VERY WEAK"):
        print("Recommendation: Use a longer and unique password.")
    else:
        print("Recommendation: Password meets the basic complexity checks.")


if __name__ == "__main__":
    main()
