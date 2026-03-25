import os

base = "c:/Users/HP/OneDrive/Desktop/fraudsheild"
mm_dir = os.path.join(base, "Money-Muling")
bc_dir = os.path.join(base, "blockchain")

checks = []

# 1
c1 = os.path.exists(os.path.join(mm_dir, "detection", "ai_scorer.py"))
checks.append(("CHECK 1: Money-Muling/detection/ai_scorer.py exists", c1))

# 2
c2 = os.path.exists(os.path.join(mm_dir, "detection", "web3_bridge.py"))
checks.append(("CHECK 2: Money-Muling/detection/web3_bridge.py exists", c2))

# 3
c3 = os.path.exists(os.path.join(bc_dir, "contracts", "FraudLedger.sol"))
checks.append(("CHECK 3: blockchain/contracts/FraudLedger.sol exists", c3))

# 4
c4 = os.path.exists(os.path.join(bc_dir, "scripts", "deploy.js"))
checks.append(("CHECK 4: blockchain/scripts/deploy.js exists", c4))

# Read app.py
app_py_path = os.path.join(mm_dir, "app.py")
try:
    with open(app_py_path, "r", encoding="utf-8") as f:
        app_content = f.read()
except:
    app_content = ""

# 5
c5 = "from detection.ai_scorer" in app_content
checks.append(("CHECK 5: 'from detection.ai_scorer' appears in app.py", c5))

# 6
c6 = "from detection.web3_bridge" in app_content
checks.append(("CHECK 6: 'from detection.web3_bridge' appears in app.py", c6))

# 7
c7 = "/api/ai-score" in app_content
checks.append(("CHECK 7: '/api/ai-score' route exists in app.py", c7))

# 8
c8 = "/api/submit-fraud" in app_content
checks.append(("CHECK 8: '/api/submit-fraud' route exists in app.py", c8))

# 9
c9 = "/api/ledger" in app_content
checks.append(("CHECK 9: '/api/ledger' route exists in app.py", c9))

# Read requirements.txt
req_path = os.path.join(mm_dir, "requirements.txt")
try:
    with open(req_path, "r", encoding="utf-8") as f:
        req_content = f.read()
except:
    req_content = ""

# 10
c10 = "scikit-learn" in req_content
checks.append(("CHECK 10: 'scikit-learn' in Money-Muling/requirements.txt", c10))

# 11
c11 = "web3" in req_content
checks.append(("CHECK 11: 'web3' in Money-Muling/requirements.txt", c11))

passed = 0
for name, val in checks:
    status = "PASS" if val else "FAIL"
    print(f"{name} -> {status}")
    if val: passed += 1

print(f"\n{passed}/11 checks passed.")
