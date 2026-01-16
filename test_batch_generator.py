"""
Test batch generation with fraud mix.
Run this from the project root directory.
"""

import sys
sys.path.insert(0, 'backend')

from data_generators.generator import TransactionGenerator

if __name__ == "__main__":
    print("Testing Transaction Generator with Fraud Patterns...")
    print("=" * 70)
    
    generator = TransactionGenerator(num_users=50, num_merchants=30)
    
    # Generate 20 transactions
    print("\nGenerating 20 sample transactions:")
    print("=" * 70)
    
    transactions = generator.generate_batch(20)
    
    fraud_count = sum(1 for tx in transactions if tx.is_fraud)
    normal_count = len(transactions) - fraud_count
    
    print(f"\n📊 Statistics:")
    print(f"  Total transactions: {len(transactions)}")
    print(f"  Normal transactions: {normal_count} ({normal_count/len(transactions)*100:.1f}%)")
    print(f"  Fraudulent transactions: {fraud_count} ({fraud_count/len(transactions)*100:.1f}%)")
    
    if fraud_count > 0:
        print(f"\n🚨 Fraud Types Detected:")
        fraud_types = {}
        for tx in transactions:
            if tx.is_fraud:
                fraud_type = tx.fraud_type
                fraud_types[fraud_type] = fraud_types.get(fraud_type, 0) + 1
        
        for fraud_type, count in fraud_types.items():
            print(f"  - {fraud_type}: {count}")
    
    print("\n" + "=" * 70)
    print("Sample Transactions:")
    print("=" * 70)
    
    for i, tx in enumerate(transactions[:10], 1):
        fraud_marker = "🚨 FRAUD" if tx.is_fraud else "✓ Normal"
        print(f"\n{i}. {fraud_marker}")
        print(f"   ID: {tx.transaction_id[:16]}...")
        print(f"   Amount: ${tx.amount:.2f}")
        print(f"   Merchant: {tx.merchant_name} ({tx.merchant_category})")
        print(f"   Location: ({tx.location_lat:.2f}, {tx.location_lon:.2f})")
        if tx.is_fraud:
            print(f"   Fraud Type: {tx.fraud_type}")
