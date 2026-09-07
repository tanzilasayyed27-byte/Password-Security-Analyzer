import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from password_analyzer import analyze_password


def test_common_password():
    score, strength, checks = analyze_password("password123")
    assert strength == "VERY WEAK"


def test_weak_password():
    score, strength, checks = analyze_password("hello")
    assert strength == "WEAK"


def test_strong_password():
    score, strength, checks = analyze_password("T3st!Secure#2026")
    assert strength == "STRONG"


def test_uppercase():
    score, strength, checks = analyze_password("Testpassword123!")
    assert any("uppercase" in check.lower() for check in checks)


def test_special_character():
    score, strength, checks = analyze_password("Testpassword123!")
    assert any("special" in check.lower() for check in checks)
