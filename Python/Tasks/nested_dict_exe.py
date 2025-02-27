from collections import Counter
from icecream import ic

# Task Description:
# Create a function that generates a comprehensive analytics summary for each customer, including purchase behavior, browsing patterns, and support interaction metrics.

# Requirements:

# - Calculate total spending, average order value, and number of orders
# - Determine most frequently purchased product category
# - Calculate average product rating across all purchases
# - Analyze support ticket resolution times and satisfaction
# - Calculate days since account creation
# - Determine average browsing time per product

customer_data = {
    "metadata": {
        "company": "TechMart Solutions",
        "database_version": "3.5.1",
        "last_updated": "2025-01-15T08:30:22Z",
        "record_count": 2
    },
    "customers": [
        {
            "customer_id": "C1001",
            "personal_info": {
                "name": {
                    "first": "Emma",
                    "last": "Johnson",
                    "title": "Ms."
                },
                "contact": {
                    "email": "emma.johnson@example.com",
                    "phone": [
                        {"type": "home", "number": "555-123-4567"},
                        {"type": "mobile", "number": "555-987-6543"}
                    ],
                    "preferred_contact": "email"
                },
                "demographics": {
                    "age": 34,
                    "location": {
                        "address": "123 Main Street",
                        "city": "Austin",
                        "state": "TX",
                        "postal_code": "78701",
                        "coordinates": (30.2672, -97.7431)
                    },
                    "membership_level": "gold",
                    "account_creation": (2021, 3, 15)  # year, month, day
                }
            },
            "purchase_history": [
                {
                    "order_id": "O78945",
                    "date": "2024-11-28",
                    "items": [
                        {
                            "product_id": "P345",
                            "name": "Wireless Headphones",
                            "category": "Electronics",
                            "price": 89.99,
                            "quantity": 1,
                            "ratings": {"quality": 4.5, "value": 4.0, "durability": 4.2}
                        },
                        {
                            "product_id": "P789",
                            "name": "Smartphone Case",
                            "category": "Accessories",
                            "price": 24.99,
                            "quantity": 2,
                            "ratings": {"quality": 3.8, "value": 4.2, "durability": 3.5}
                        }
                    ],
                    "payment": {
                        "method": "credit_card",
                        "card_type": "Visa",
                        "transaction_id": "T12345678"
                    },
                    "shipping": {
                        "method": "standard",
                        "tracking_number": "SHP123456789",
                        "status": "delivered",
                        "delivery_date": "2024-12-03"
                    },
                    "total": 139.97
                },
                {
                    "order_id": "O79012",
                    "date": "2025-01-05",
                    "items": [
                        {
                            "product_id": "P123",
                            "name": "Smart Watch",
                            "category": "Electronics",
                            "price": 199.99,
                            "quantity": 1,
                            "ratings": {"quality": 4.8, "value": 4.1, "durability": 4.7}
                        }
                    ],
                    "payment": {
                        "method": "paypal",
                        "transaction_id": "T23456789"
                    },
                    "shipping": {
                        "method": "express",
                        "tracking_number": "SHP234567890",
                        "status": "in_transit",
                        "estimated_delivery": "2025-01-08"
                    },
                    "total": 199.99
                }
            ],
            "browsing_history": [
                {"product_id": "P456", "timestamp": "2025-01-12T14:23:45Z", "time_spent": 120},
                {"product_id": "P234", "timestamp": "2025-01-12T14:26:32Z", "time_spent": 45},
                {"product_id": "P789", "timestamp": "2025-01-13T10:12:31Z", "time_spent": 60}
            ],
            "recommendations": {
                "based_on_history": ["P567", "P890", "P234"],
                "based_on_similar_users": ["P678", "P901"],
                "seasonal_offers": ["P345", "P678"]
            },
            "support_interactions": [
                {
                    "ticket_id": "T1001",
                    "date": "2024-12-12",
                    "issue": "Order delayed",
                    "status": "resolved",
                    "satisfaction_rating": 4,
                    "resolution_time": 48  # hours
                }
            ]
        },
        {
            "customer_id": "C1002",
            "personal_info": {
                "name": {
                    "first": "Michael",
                    "last": "Chen",
                    "title": "Mr."
                },
                "contact": {
                    "email": "michael.chen@example.com",
                    "phone": [
                        {"type": "mobile", "number": "555-456-7890"}
                    ],
                    "preferred_contact": "mobile"
                },
                "demographics": {
                    "age": 28,
                    "location": {
                        "address": "456 Oak Avenue",
                        "city": "Seattle",
                        "state": "WA",
                        "postal_code": "98101",
                        "coordinates": (47.6062, -122.3321)
                    },
                    "membership_level": "silver",
                    "account_creation": (2022, 7, 8)
                }
            },
            "purchase_history": [
                {
                    "order_id": "O45678",
                    "date": "2024-12-15",
                    "items": [
                        {
                            "product_id": "P234",
                            "name": "Bluetooth Speaker",
                            "category": "Electronics",
                            "price": 59.99,
                            "quantity": 1,
                            "ratings": {"quality": 4.2, "value": 4.5, "durability": 3.9}
                        },
                        {
                            "product_id": "P567",
                            "name": "Laptop Stand",
                            "category": "Office Supplies",
                            "price": 29.99,
                            "quantity": 1,
                            "ratings": {"quality": 4.0, "value": 4.3, "durability": 4.1}
                        },
                        {
                            "product_id": "P890",
                            "name": "Wireless Mouse",
                            "category": "Accessories",
                            "price": 19.99,
                            "quantity": 1,
                            "ratings": {"quality": 4.1, "value": 4.4, "durability": 3.8}
                        }
                    ],
                    "payment": {
                        "method": "credit_card",
                        "card_type": "Mastercard",
                        "transaction_id": "T34567890"
                    },
                    "shipping": {
                        "method": "standard",
                        "tracking_number": "SHP345678901",
                        "status": "delivered",
                        "delivery_date": "2024-12-20"
                    },
                    "total": 109.97
                }
            ],
            "browsing_history": [
                {"product_id": "P123", "timestamp": "2025-01-14T15:45:23Z", "time_spent": 180},
                {"product_id": "P456", "timestamp": "2025-01-14T15:49:57Z", "time_spent": 90},
                {"product_id": "P789", "timestamp": "2025-01-14T16:02:11Z", "time_spent": 120},
                {"product_id": "P234", "timestamp": "2025-01-15T09:34:29Z", "time_spent": 75}
            ],
            "recommendations": {
                "based_on_history": ["P123", "P456"],
                "based_on_similar_users": ["P789", "P234"],
                "seasonal_offers": ["P567", "P890"]
            },
            "support_interactions": [
                {
                    "ticket_id": "T1002",
                    "date": "2024-12-18",
                    "issue": "Product information inquiry",
                    "status": "resolved",
                    "satisfaction_rating": 5,
                    "resolution_time": 2
                },
                {
                    "ticket_id": "T1003",
                    "date": "2025-01-10",
                    "issue": "Return request",
                    "status": "pending",
                    "resolution_time": None
                }
            ]
        }
    ]
}



   
