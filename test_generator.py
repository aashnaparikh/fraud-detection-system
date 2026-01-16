"""
Test script for transaction generator.
Run this from the project root directory.
"""

import sys
sys.path.insert(0, 'backend')

from data_generators.generator import TransactionGenerator

if __name__ == "__main__":
    print("Testing Transaction Generator...")
    print("=" * 70)
    
    generator = TransactionGenerator(num_users=10, num_merchants=10)
    
    # Generate 5 sample transactions
    print("\nGenerating 5 sample transactions:")
    print("=" * 70)
    
    for i in range(5):
        transaction = generator.generate_transaction()
        print(f"\nTransaction {i+1}:")
        print(f"  ID: {transaction.transaction_id}")
        print(f"  User: {transaction.user_id}")
        print(f"  Merchant: {transaction.merchant_name} ({transaction.merchant_category})")
        print(f"  Amount: ${transaction.amount:.2f}")
        print(f"  Location: ({transaction.location_lat:.2f}, {transaction.location_lon:.2f})")
        print(f"  Fraud: {transaction.is_fraud}")
        if transaction.is_fraud:
            print(f"  Fraud Type: {transaction.fraud_type}")
