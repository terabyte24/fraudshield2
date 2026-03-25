# 🛡 FraudShield — Money Muling Detection Engine

### ⚡ Graph AI • 🤖 ML Risk Scoring • ⛓ Blockchain Ledger

> 🏆 ROBIX Hackathon 2026 · Financial Crime Detection · Graph Intelligence System

---

## 🌐 Project Overview

FraudShield is a **real-time financial fraud detection engine** that identifies:

* 🔁 Money mule rings
* 🔄 Smurfing (fan-in / fan-out)
* 🔗 Layered laundering chains

using a **graph-based architecture + AI + blockchain immutability**.

---

### 📊 Core Metrics

| Metric               | Value                      |
| -------------------- | -------------------------- |
| ⚡ Complexity         | O(V + E) (SCC-based)       |
| 🔍 Patterns Detected | 4+                         |
| ⏱ Processing Speed   | < 5 sec (10K txns)         |
| 🔐 Infrastructure    | Offline-first + Blockchain |

---

## ⚠️ Problem Statement

### 💸 Money Muling — A Critical Threat

Traditional fraud systems fail because:

* ❌ Rule-based detection misses multi-hop laundering
* ❌ Graph algorithms like `simple_cycles()` are too slow (O(2ⁿ))
* ❌ No prioritization → investigators overwhelmed
* ❌ No tamper-proof audit trail

---

## 💡 Our Solution

FraudShield introduces:

* 🧠 **Graph Intelligence (SCC instead of brute cycles)**
* 🤖 **AI Risk Scoring (RandomForest)**
* ⛓ **Blockchain Ledger (Hardhat Smart Contract)**
* 📊 **Interactive Visualization (Cytoscape.js)**

👉 Result: **Real-time, scalable, tamper-proof fraud detection**

---

## 🔄 System Workflow

```text
📂 CSV Upload
   ↓
🧪 Data Validation (Pandas)
   ↓
🔗 Graph Construction (NetworkX DiGraph)
   ↓
🛡 Whitelist Filtering (legit accounts removed)
   ↓
┌────────────────────────────────────┐
│ 🔍 Detection Algorithms            │
│ 1. 🔁 Cycle Detection (SCC)        │
│ 2. 🔄 Smurfing Detection           │
│ 3. 🔗 Layered Networks             │
│ 4. 📊 Hub Node Analysis            │
└────────────────────────────────────┘
   ↓
📊 Suspicion Scoring Engine (0–100)
   ↓
🤖 AI Risk Classification
   ↓
⛓ Blockchain Storage (Fraud Ledger)
   ↓
🌐 Dashboard Visualization
```

---

## 🧠 Detection Algorithms

### 🔁 1. Cycle Detection (Circular Routing)

* Algorithm: **Tarjan’s SCC**
* Complexity: **O(V + E)**
* Detects: A → B → C → A

✔ Score: +35

---

### 🔄 2. Smurfing (Fan-In / Fan-Out)

* Algorithm: **Sliding Window (72 hrs)**
* Fan-in: ≥ 5 → 1
* Fan-out: 1 → ≥ 5

✔ Score: +25

---

### 🔗 3. Layered Shell Networks

* Algorithm: **BFS traversal**
* Chain length ≥ 3 hops
* Shell nodes ≤ 3 transactions

✔ Score: +20

---

### 📊 4. Hub Node Detection

* Algorithm: **95th percentile degree**

✔ Score: +20

---

## 📊 Suspicion Score Model

```text
score = pattern_score + activity_boost
activity_boost = log(degree + 1) × 2 + log(flow + 1)
final_score = min(100, score)
```

---

### 🎯 Risk Levels

| Score     | Level       |
| --------- | ----------- |
| 🔴 75–100 | High Risk   |
| 🟡 40–74  | Medium Risk |
| 🟢 0–39   | Low Risk    |

---

## 🛡 False Positive Control

✔ Whitelist conditions:

* Degree ≥ 200
* Unique partner ratio ≥ 60%

👉 Prevents flagging:

* Payroll systems
* Merchants

---

## ⛓ Blockchain Ledger (Web3 Integration)

### 🔐 Smart Contract: FraudLedger

Stores:

* 🆔 Ring ID
* 🔑 Hash of accounts
* 📊 Risk Score
* ⏱ Timestamp
* 👤 Submitter

---

### ⚡ Features

* 🔐 Tamper-proof records
* 🔄 Cross-platform fraud sharing
* ⚡ Real-time verification

---

## 🤖 AI Risk Scoring Layer

Uses:

* 🌲 RandomForestClassifier
* 📊 10 feature inputs

### 🔍 Features:

* Degree metrics
* Pattern count
* Centrality
* Flow imbalance

---

## 📥 Input Format

| Field          | Type     |
| -------------- | -------- |
| transaction_id | String   |
| sender_id      | String   |
| receiver_id    | String   |
| amount         | Float    |
| timestamp      | DateTime |

---

## 📤 Output Format

```json
{
  "suspicious_accounts": [...],
  "fraud_rings": [...],
  "summary": {...}
}
```

---

## ⚡ Performance

| Dataset  | Time   |
| -------- | ------ |
| 500 txns | < 0.3s |
| 5K txns  | < 2.5s |
| 10K txns | < 5s   |

---

## 🚀 Setup

```bash
# Install backend
pip install -r requirements.txt

# Start blockchain
npx hardhat node

# Deploy contract
npx hardhat run scripts/deploy.js --network localhost

# Run app
python app.py
```

---

## 🌐 API Endpoints

| Method | Endpoint          |
| ------ | ----------------- |
| POST   | /analyze          |
| POST   | /download         |
| POST   | /api/submit-fraud |
| GET    | /api/ledger       |

---

## ⚠️ Limitations

* No real-time streaming
* Fixed 72-hour window
* Graph size limits in UI

---

## 👥 Team

| Role              | Name                |
| ----------------- | ------------------- |
| 👨‍💻 Team Leader | Saurabh Yadav       |
| 👨‍💻 Member      | Fahad Afzal Hussain |
| 👨‍💻 Member      | Aryan Gambheer      |
| 👨‍💻 Member      | Aditya Ranjan       |

---

## 🎯 Final Vision

> 🧠 **AI + Graph + Web3 Fraud Detection System**
> 🔗 **Decentralized Financial Security Infrastructure**

---

✨ Built for ROBIX Hackathon 2026
🚀 FraudShield v2.0 — Detect • Prevent • Secure
