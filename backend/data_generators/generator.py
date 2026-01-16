"""
Synthetic transaction data generator.

This module generates realistic transaction data with both normal
and fraudulent patterns for testing the fraud detection system.
"""

import random
import uuid
from datetime import datetime, timedelta
from typing import List, Tuple
from faker import Faker

from .models.transaction import Transaction, User, Merchant
from .config import (
    MERCHANT_CATEGORIES,
    CATEGORY_SPENDING_RANGES,
    US_LAT_RANGE,
    US_LON_RANGE,
    FRAUD_PROBABILITY
)

fake = Faker()


class TransactionGenerator:
    """Generates realistic transaction data."""
    
    def __init__(self, num_users: int = 1000, num_merchants: int = 500):
        """
        Initialize the transaction generator.
        
        Args:
            num_users: Number of unique users to generate
            num_merchants: Number of unique merchants to generate
        """
        self.num_users = num_users
        self.num_merchants = num_merchants
        self.users: List[User] = []
        self.merchants: List[Merchant] = []
        
        # Generate initial data
        self._generate_users()
        self._generate_merchants()
    
    def _generate_users(self):
        """Generate a pool of users."""
        print(f"Generating {self.num_users} users...")
        
        for i in range(self.num_users):
            user = User(
                user_id=f"USER_{str(uuid.uuid4())[:8]}",
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                home_lat=random.uniform(*US_LAT_RANGE),
                home_lon=random.uniform(*US_LON_RANGE),
                typical_spending=random.uniform(50, 500),
                account_age_days=random.randint(30, 3650)  # 1 month to 10 years
            )
            self.users.append(user)
        
        print(f"✓ Generated {len(self.users)} users")
    
    def _generate_merchants(self):
        """Generate a pool of merchants."""
        print(f"Generating {self.num_merchants} merchants...")
        
        for i in range(self.num_merchants):
            category = random.choice(MERCHANT_CATEGORIES)
            avg_amount = sum(CATEGORY_SPENDING_RANGES[category]) / 2
            
            merchant = Merchant(
                merchant_id=f"MERCH_{str(uuid.uuid4())[:8]}",
                merchant_name=fake.company(),
                category=category,
                location_lat=random.uniform(*US_LAT_RANGE),
                location_lon=random.uniform(*US_LON_RANGE),
                average_transaction=avg_amount
            )
            self.merchants.append(merchant)
        
        print(f"✓ Generated {len(self.merchants)} merchants")
    
    def generate_normal_transaction(self) -> Transaction:
        """
        Generate a normal (non-fraudulent) transaction.
        
        Returns:
            A Transaction object representing a legitimate transaction
        """
        user = random.choice(self.users)
        merchant = random.choice(self.merchants)
        
        # Amount based on merchant category with some randomness
        min_amount, max_amount = CATEGORY_SPENDING_RANGES[merchant.category]
        amount = round(random.uniform(min_amount, max_amount), 2)
        
        # Location near user's home (within ~50 miles)
        location_lat = user.home_lat + random.uniform(-0.7, 0.7)
        location_lon = user.home_lon + random.uniform(-0.7, 0.7)
        
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
            location_lat=location_lat,
            location_lon=location_lon,
            device_id=f"DEVICE_{random.randint(1000, 9999)}",
            ip_address=fake.ipv4(),
            is_fraud=False,
            fraud_type=None
        )
        
        return transaction
    
    def generate_transaction(self) -> Transaction:
        """
        Generate a transaction (could be normal or fraudulent).
        
        Returns:
            A Transaction object
        """
        # Decide if this transaction should be fraudulent
        if random.random() < FRAUD_PROBABILITY:
            # We'll implement fraud patterns in the next step
            return self.generate_normal_transaction()
        else:
            return self.generate_normal_transaction()


if __name__ == "__main__":
    # Test the generator
    print("Testing Transaction Generator...")
    print("=" * 50)
    
    generator = TransactionGenerator(num_users=10, num_merchants=10)
    
    # Generate 5 sample transactions
    print("\nGenerating 5 sample transactions:")
    print("=" * 50)
    
    for i in range(5):
        transaction = generator.generate_transaction()
        print(f"\nTransaction {i+1}:")
        print(f"  ID: {transaction.transaction_id}")
        print(f"  User: {transaction.user_id}")
        print(f"  Merchant: {transaction.merchant_name} ({transaction.merchant_category})")
        print(f"  Amount: ${transaction.amount:.2f}")
        print(f"  Location: ({transaction.location_lat:.2f}, {transaction.location_lon:.2f})")
        print(f"  Fraud: {transaction.is_fraud}")
