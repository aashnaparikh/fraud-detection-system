"""
Fraud pattern generators.

This module contains functions to generate different types of fraudulent
transaction patterns for testing the fraud detection system.
"""

import random
import uuid
from datetime import datetime, timedelta
from typing import List

from .models.transaction import Transaction, User, Merchant
from .config import US_LAT_RANGE, US_LON_RANGE


class FraudPatternGenerator:
    """Generates various types of fraudulent transaction patterns."""
    
    def __init__(self, users: List[User], merchants: List[Merchant]):
        """
        Initialize fraud pattern generator.
        
        Args:
            users: List of user objects
            merchants: List of merchant objects
        """
        self.users = users
        self.merchants = merchants
    
    def generate_unusual_amount(self) -> Transaction:
        """
        PATTERN 1: Unusual Amount Fraud
        
        Transaction amount is 10-20x higher than user's typical spending.
        Example: User normally spends $50, suddenly charges $1,000
        
        Real-world: Stolen card used for expensive purchase
        """
        user = random.choice(self.users)
        merchant = random.choice(self.merchants)
        
        # Amount is 10-20x the user's typical spending
        unusual_amount = round(user.typical_spending * random.uniform(10, 20), 2)
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            user_id=user.user_id,
            card_number=f"****-****-****-{random.randint(1000, 9999)}",
            merchant_id=merchant.merchant_id,
            merchant_name=merchant.merchant_name,
            merchant_category=merchant.category,
            amount=unusual_amount,
            currency="USD",
            location_lat=user.home_lat + random.uniform(-0.5, 0.5),
            location_lon=user.home_lon + random.uniform(-0.5, 0.5),
            device_id=f"DEVICE_{random.randint(1000, 9999)}",
            ip_address=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            is_fraud=True,
            fraud_type="unusual_amount"
        )
        
        return transaction
    
    def generate_geographic_anomaly(self) -> Transaction:
        """
        PATTERN 2: Geographic Anomaly
        
        Transaction occurs far from user's home location.
        Example: User lives in New York, transaction in California
        
        Real-world: Stolen card used in different state/country
        """
        user = random.choice(self.users)
        merchant = random.choice(self.merchants)
        
        # Generate location far from user's home (different region)
        # Add 10-30 degrees latitude/longitude difference
        far_lat = user.home_lat + random.uniform(10, 30) * random.choice([-1, 1])
        far_lon = user.home_lon + random.uniform(10, 30) * random.choice([-1, 1])
        
        # Clamp to valid ranges
        far_lat = max(US_LAT_RANGE[0], min(US_LAT_RANGE[1], far_lat))
        far_lon = max(US_LON_RANGE[0], min(US_LON_RANGE[1], far_lon))
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            user_id=user.user_id,
            card_number=f"****-****-****-{random.randint(1000, 9999)}",
            merchant_id=merchant.merchant_id,
            merchant_name=merchant.merchant_name,
            merchant_category=merchant.category,
            amount=round(random.uniform(100, 500), 2),
            currency="USD",
            location_lat=far_lat,
            location_lon=far_lon,
            device_id=f"DEVICE_{random.randint(5000, 9999)}",  # Different device
            ip_address=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            is_fraud=True,
            fraud_type="geographic_anomaly"
        )
        
        return transaction
    
    def generate_high_frequency(self) -> List[Transaction]:
        """
        PATTERN 3: High Frequency Fraud
        
        Multiple transactions in a very short time period.
        Example: 10 transactions in 2 minutes
        
        Real-world: Fraudster rushing to make purchases before card is blocked
        """
        user = random.choice(self.users)
        num_transactions = random.randint(8, 15)  # 8-15 rapid transactions
        transactions = []
        
        base_time = datetime.now()
        
        for i in range(num_transactions):
            merchant = random.choice(self.merchants)
            # Transactions within 5 minutes
            time_offset = timedelta(seconds=random.randint(0, 300))
            
            transaction = Transaction(
                transaction_id=str(uuid.uuid4()),
                timestamp=base_time + time_offset,
                user_id=user.user_id,
                card_number=f"****-****-****-{random.randint(1000, 9999)}",
                merchant_id=merchant.merchant_id,
                merchant_name=merchant.merchant_name,
                merchant_category=merchant.category,
                amount=round(random.uniform(50, 300), 2),
                currency="USD",
                location_lat=user.home_lat + random.uniform(-1, 1),
                location_lon=user.home_lon + random.uniform(-1, 1),
                device_id=f"DEVICE_{random.randint(1000, 9999)}",
                ip_address=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                is_fraud=True,
                fraud_type="high_frequency"
            )
            transactions.append(transaction)
        
        return transactions
    
    def generate_card_testing(self) -> List[Transaction]:
        """
        PATTERN 4: Card Testing
        
        Multiple small transactions to test if card is active.
        Example: $1.00, $2.00, $3.00 charges at different merchants
        
        Real-world: Fraudster testing stolen cards before big purchase
        """
        user = random.choice(self.users)
        num_tests = random.randint(5, 10)
        transactions = []
        
        base_time = datetime.now()
        
        for i in range(num_tests):
            merchant = random.choice(self.merchants)
            time_offset = timedelta(minutes=random.randint(0, 30))
            
            # Small amounts for testing
            test_amount = round(random.uniform(0.50, 5.00), 2)
            
            transaction = Transaction(
                transaction_id=str(uuid.uuid4()),
                timestamp=base_time + time_offset,
                user_id=user.user_id,
                card_number=f"****-****-****-{random.randint(1000, 9999)}",
                merchant_id=merchant.merchant_id,
                merchant_name=merchant.merchant_name,
                merchant_category=merchant.category,
                amount=test_amount,
                currency="USD",
                location_lat=user.home_lat + random.uniform(-0.3, 0.3),
                location_lon=user.home_lon + random.uniform(-0.3, 0.3),
                device_id=f"DEVICE_{random.randint(1000, 9999)}",
                ip_address=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                is_fraud=True,
                fraud_type="card_testing"
            )
            transactions.append(transaction)
        
        return transactions
    
    def generate_time_anomaly(self) -> Transaction:
        """
        PATTERN 5: Time Anomaly
        
        Transaction at unusual hour for the user.
        Example: Transaction at 3 AM when user typically shops 9 AM - 9 PM
        
        Real-world: Stolen card used while victim is asleep
        """
        user = random.choice(self.users)
        merchant = random.choice(self.merchants)
        
        # Generate transaction in middle of night (1 AM - 5 AM)
        base_time = datetime.now().replace(hour=random.randint(1, 5), minute=random.randint(0, 59))
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            timestamp=base_time,
            user_id=user.user_id,
            card_number=f"****-****-****-{random.randint(1000, 9999)}",
            merchant_id=merchant.merchant_id,
            merchant_name=merchant.merchant_name,
            merchant_category=merchant.category,
            amount=round(random.uniform(100, 800), 2),
            currency="USD",
            location_lat=user.home_lat + random.uniform(-2, 2),
            location_lon=user.home_lon + random.uniform(-2, 2),
            device_id=f"DEVICE_{random.randint(5000, 9999)}",
            ip_address=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            is_fraud=True,
            fraud_type="time_anomaly"
        )
        
        return transaction
    
    def generate_round_amount(self) -> Transaction:
        """
        PATTERN 6: Round Amount Fraud
        
        Suspicious round amounts that indicate manual entry.
        Example: Exactly $100.00, $500.00, $1000.00
        
        Real-world: Fraudster manually entering amounts (not real purchases)
        """
        user = random.choice(self.users)
        merchant = random.choice(self.merchants)
        
        # Exactly round amounts
        round_amounts = [100.00, 200.00, 250.00, 500.00, 750.00, 1000.00, 1500.00]
        amount = random.choice(round_amounts)
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            user_id=user.user_id,
            card_number=f"****-****-****-{random.randint(1000, 9999)}",
            merchant_id=merchant.merchant_id,
            merchant_name=merchant.merchant_name,
            merchant_category=merchant.category,
            amount=amount,
            currency="USD",
            location_lat=user.home_lat + random.uniform(-1, 1),
            location_lon=user.home_lon + random.uniform(-1, 1),
            device_id=f"DEVICE_{random.randint(1000, 9999)}",
            ip_address=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            is_fraud=True,
            fraud_type="round_amount"
        )
        
        return transaction
    
    def generate_high_risk_category(self) -> Transaction:
        """
        PATTERN 7: High Risk Category
        
        Large purchase in typically fraudulent categories.
        Example: $3,000 at jewelry store, $5,000 in electronics
        
        Real-world: Categories often targeted by fraudsters
        """
        user = random.choice(self.users)
        
        # Filter for high-risk merchants
        high_risk_categories = ['electronics', 'jewelry', 'online_retail']
        high_risk_merchants = [m for m in self.merchants if m.category in high_risk_categories]
        
        if not high_risk_merchants:
            merchant = random.choice(self.merchants)
        else:
            merchant = random.choice(high_risk_merchants)
        
        # Large amount
        amount = round(random.uniform(2000, 5000), 2)
        
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            user_id=user.user_id,
            card_number=f"****-****-****-{random.randint(1000, 9999)}",
            merchant_id=merchant.merchant_id,
            merchant_name=merchant.merchant_name,
            merchant_category=merchant.category,
            amount=amount,
            currency="USD",
            location_lat=user.home_lat + random.uniform(-3, 3),
            location_lon=user.home_lon + random.uniform(-3, 3),
            device_id=f"DEVICE_{random.randint(5000, 9999)}",
            ip_address=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            is_fraud=True,
            fraud_type="high_risk_category"
        )
        
        return transaction
    
    def generate_random_fraud(self) -> Transaction:
        """
        Generate a random fraud pattern.
        
        Returns:
            A fraudulent transaction of random type
        """
        fraud_generators = [
            self.generate_unusual_amount,
            self.generate_geographic_anomaly,
            self.generate_time_anomaly,
            self.generate_round_amount,
            self.generate_high_risk_category
        ]
        
        generator = random.choice(fraud_generators)
        return generator()


if __name__ == "__main__":
    # Test fraud patterns
    from .generator import TransactionGenerator
    
    print("Testing Fraud Pattern Generator...")
    print("=" * 60)
    
    # Create base generator
    gen = TransactionGenerator(num_users=20, num_merchants=20)
    fraud_gen = FraudPatternGenerator(gen.users, gen.merchants)
    
    print("\n1. Testing Unusual Amount Fraud:")
    print("-" * 60)
    fraud_tx = fraud_gen.generate_unusual_amount()
    print(f"Amount: ${fraud_tx.amount:.2f} (User typical: $50-500)")
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
    print(f"Time span: {(fraud_txs[-1].timestamp - fraud_txs[0].timestamp).total_seconds():.0f} seconds")
    
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
