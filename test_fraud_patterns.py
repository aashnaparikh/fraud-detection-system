"""
Test script for fraud patterns.
Run this from the project root directory.
"""

import sys
sys.path.insert(0, 'backend')

from data_generators.generator import TransactionGenerator
from data_generators.fraud_patterns import FraudPatternGenerator

if __name__ == "__main__":
    print("Testing Fraud Pattern Generator...")
    print("=" * 60)
    
    # Create base generator
    gen = TransactionGenerator(num_users=20, num_merchants=20)
    fraud_gen = FraudPatternGenerator(gen.users, gen.merchants)
    
    print("\n1. Testing Unusual Amount Fraud:")
    print("-" * 60)
    fraud_tx = fraud_gen.generate_unusual_amount()
    print(f"Amount: ${fraud_tx.amount:.2f}")
    print(f"Fraud Type: {fraud_tx.fraud_type}")
    print(f"Is Fraud: {fraud_tx.is_fraud}")
    
    print("\n2. Testing Geographic Anomaly:")
    print("-" * 60)
    fraud_tx = fraud_gen.generate_geographic_anomaly()
    user = next(u for u in gen.users if u.user_id == fraud_tx.user_id)
    print(f"User Home: ({user.home_lat:.2f}, {user.home_lon:.2f})")
    print(f"Transaction Location: ({fraud_tx.location_lat:.2f}, {fraud_tx.location_lon:.2f})")
    print(f"Fraud Type: {fraud_tx.fraud_type}")
    
    print("\n3. Testing High Frequency Fraud:")
    print("-" * 60)
    fraud_txs = fraud_gen.generate_high_frequency()
    print(f"Generated {len(fraud_txs)} rapid transactions")
    time_span = (fraud_txs[-1].timestamp - fraud_txs[0].timestamp).total_seconds()
    print(f"Time span: {time_span:.0f} seconds")
    
    print("\n4. Testing Card Testing Pattern:")
    print("-" * 60)
    fraud_txs = fraud_gen.generate_card_testing()
    print(f"Generated {len(fraud_txs)} small test transactions")
    amounts = [tx.amount for tx in fraud_txs]
    print(f"Amounts: ${min(amounts):.2f} to ${max(amounts):.2f}")
    
    print("\n5. Testing Time Anomaly:")
    print("-" * 60)
    fraud_tx = fraud_gen.generate_time_anomaly()
    print(f"Transaction time: {fraud_tx.timestamp.strftime('%I:%M %p')}")
    print(f"Fraud Type: {fraud_tx.fraud_type}")
    
    print("\n6. Testing Round Amount:")
    print("-" * 60)
    fraud_tx = fraud_gen.generate_round_amount()
    print(f"Amount: ${fraud_tx.amount:.2f} (suspiciously round)")
    print(f"Fraud Type: {fraud_tx.fraud_type}")
    
    print("\n7. Testing High Risk Category:")
    print("-" * 60)
    fraud_tx = fraud_gen.generate_high_risk_category()
    print(f"Category: {fraud_tx.merchant_category}")
    print(f"Amount: ${fraud_tx.amount:.2f}")
    print(f"Fraud Type: {fraud_tx.fraud_type}")
    
    print("\n" + "=" * 60)
    print("All fraud patterns tested successfully! ✓")
    print("=" * 60)
