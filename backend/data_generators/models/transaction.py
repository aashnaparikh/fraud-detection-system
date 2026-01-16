"""
Transaction data models for fraud detection system.

This module defines the structure of transaction data that flows through
our fraud detection pipeline.
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
import json


@dataclass
class Transaction:
    """
    Represents a single financial transaction.
    
    Attributes:
        transaction_id: Unique identifier for the transaction
        timestamp: When the transaction occurred
        user_id: ID of the user making the transaction
        card_number: Masked credit card number (last 4 digits visible)
        merchant_id: ID of the merchant receiving payment
        merchant_name: Name of the merchant
        merchant_category: Type of merchant (e.g., 'restaurant', 'electronics')
        amount: Transaction amount in dollars
        currency: Currency code (e.g., 'USD')
        location_lat: Latitude of transaction location
        location_lon: Longitude of transaction location
        device_id: Device used for transaction
        ip_address: IP address of the transaction
        is_fraud: Whether this transaction is fraudulent (ground truth)
        fraud_type: Type of fraud if is_fraud is True
    """
    
    transaction_id: str
    timestamp: datetime
    user_id: str
    card_number: str
    merchant_id: str
    merchant_name: str
    merchant_category: str
    amount: float
    currency: str
    location_lat: float
    location_lon: float
    device_id: str
    ip_address: str
    is_fraud: bool
    fraud_type: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert transaction to dictionary format."""
        data = asdict(self)
        # Convert datetime to ISO format string
        data['timestamp'] = self.timestamp.isoformat()
        return data
    
    def to_json(self) -> str:
        """Convert transaction to JSON string."""
        return json.dumps(self.to_dict())


@dataclass
class User:
    """
    Represents a user in the system.
    
    Attributes:
        user_id: Unique user identifier
        name: User's full name
        email: User's email address
        phone: User's phone number
        home_lat: Latitude of user's home address
        home_lon: Longitude of user's home address
        typical_spending: User's typical transaction amount
        account_age_days: How long the account has existed
    """
    
    user_id: str
    name: str
    email: str
    phone: str
    home_lat: float
    home_lon: float
    typical_spending: float
    account_age_days: int


@dataclass
class Merchant:
    """
    Represents a merchant/store in the system.
    
    Attributes:
        merchant_id: Unique merchant identifier
        merchant_name: Name of the merchant
        category: Type of business (e.g., 'grocery', 'gas_station')
        location_lat: Latitude of merchant location
        location_lon: Longitude of merchant location
        average_transaction: Typical transaction amount at this merchant
    """
    
    merchant_id: str
    merchant_name: str
    category: str
    location_lat: float
    location_lon: float
    average_transaction: float
