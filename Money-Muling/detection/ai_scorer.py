import numpy as np
import networkx as nx
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

_MODEL = None
_SCALER = None

LABELS = {0: "Low", 1: "Medium", 2: "High"}
COLORS = {0: "green", 1: "amber", 2: "red"}

def _extract_features(node_data, all_nodes, all_edges):
    G = nx.DiGraph()
    for e in all_edges:
        G.add_edge(e["source"], e["target"])
        
    in_d = node_data.get("in_degree", 0)
    out_d = node_data.get("out_degree", 0)
    total = in_d + out_d
    
    in_ring = 1 if node_data.get("in_ring") else 0
    suspicious = 1 if node_data.get("suspicious") else 0
    num_patterns = len(node_data.get("patterns", []))
    score = node_data.get("score", 0)
    
    pr = nx.pagerank(G, alpha=0.85) if len(G) > 0 else {}
    node_id = node_data["id"]
    pagerank_val = pr.get(node_id, 0) * 1000
    
    k_val = min(50, len(G))
    try:
        bc = nx.betweenness_centrality(G, k=k_val) if len(G) > 0 else {}
    except:
        bc = {}
    betweenness = bc.get(node_id, 0) * 1000
    
    if total > 0:
        flow_imbalance = abs(in_d - out_d) / total
    else:
        flow_imbalance = 0
        
    return np.array([
        score, in_d, out_d, total, in_ring, suspicious, num_patterns,
        pagerank_val, betweenness, flow_imbalance
    ], dtype=float)

def _build_synthetic_model():
    rng = np.random.default_rng(42)
    n = 2000
    X = rng.uniform(0, 1, (n, 10))
    
    y = np.zeros(n, dtype=int)
    y[X[:, 0] > 0.74] = 2
    y[(X[:, 0] > 0.39) & (X[:, 0] <= 0.74)] = 1
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_scaled, y)
    
    return clf, scaler

def get_model():
    global _MODEL, _SCALER
    if _MODEL is None or _SCALER is None:
        _MODEL, _SCALER = _build_synthetic_model()
    return _MODEL, _SCALER

def score_accounts(analysis_result):
    model, scaler = get_model()
    
    nodes = analysis_result.get("graph", {}).get("nodes", [])
    edges = analysis_result.get("graph", {}).get("edges", [])
    
    results = []
    
    for node in nodes:
        features = _extract_features(node, nodes, edges)
        features_scaled = scaler.transform([features])
        
        proba = model.predict_proba(features_scaled)[0]
        pred_class = np.argmax(proba)
        max_proba = proba[pred_class]
        
        confidence = round(max_proba * 100, 1)
        suspicion_score = node.get("score", 0)
        
        results.append({
            "account_id": node["id"],
            "ai_risk_label": LABELS[pred_class],
            "ai_risk_color": COLORS[pred_class],
            "ai_confidence": confidence,
            "suspicion_score": suspicion_score
        })
        
    results.sort(key=lambda x: x["suspicion_score"], reverse=True)
    return results
