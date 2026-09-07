import json
from datetime import datetime


def save_report(password, score, strength, entropy, resistance,
                sha256_hash, salt, salted_hash):

    report = {
        "project": "Advanced Password Security Analyzer",
        "generated_at": datetime.now().isoformat(),
        "analysis": {
            "password_length": len(password),
            "security_score": f"{score}/6",
            "strength": strength,
            "entropy_bits": entropy,
            "crack_resistance": resistance
        },
        "hashing": {
            "algorithm": "SHA-256",
            "sha256_hash": sha256_hash,
            "salt": salt,
            "salted_sha256": salted_hash
        },
        "security_note": (
            "This report was generated using a TEST password. "
            "No real credentials should be used."
        )
    }

    output_file = "results/security_report.json"

    with open(output_file, "w") as file:
        json.dump(report, file, indent=4)

    return output_file
