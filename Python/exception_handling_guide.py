
"""
Comprehensive Guide to Python Exception Handling
---------------------------------------------

This module demonstrates Python exception handling from basics to advanced concepts,
including real-world examples and best practices.
"""

import logging
import time
from contextlib import contextmanager

# Basic Exception Handling
def basic_exception_demo():
    """Basic try-except demonstration"""
    print("\n=== Basic Exception Handling ===")
    
    # Simple try-except
    try:
        x = int("not a number")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    
    # Multiple exceptions
    try:
        numbers = [1, 2, 3]
        print(numbers[10] / 0)
    except IndexError as e:
        print(f"Index Error: {e}")
    except ZeroDivisionError as e:
        print(f"Division Error: {e}")
    except Exception as e:
        print(f"Generic Error: {e}")

# Advanced Exception Handling
def advanced_exception_demo():
    """Advanced exception handling with else and finally"""
    print("\n=== Advanced Exception Handling ===")
    
    try:
        with open("nonexistent.txt") as f:
            data = f.read()
    except FileNotFoundError as e:
        print(f"File Error: {e}")
    else:
        print("File processing successful")
    finally:
        print("Cleanup operations here")

# Custom Exceptions
class CustomError(Exception):
    """Custom exception class"""
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

def custom_exception_demo():
    """Demonstrate custom exceptions"""
    print("\n=== Custom Exceptions ===")
    
    def process_age(age):
        if age < 0:
            raise CustomError("Age cannot be negative", 1001)
        if age > 150:
            raise CustomError("Age seems invalid", 1002)
        return f"Age {age} is valid"
    
    try:
        print(process_age(-5))
    except CustomError as e:
        print(f"Error {e.error_code}: {e.message}")

# Context Managers
@contextmanager
def timer():
    """Custom context manager to measure execution time"""
    start = time.time()
    yield
    end = time.time()
    print(f"Execution time: {end - start:.2f} seconds")

# Real-world Examples
class DatabaseConnection:
    """Mock database connection for demonstration"""
    def __init__(self):
        self.connected = False
    
    def connect(self):
        self.connected = True
        print("Database connected")
    
    def disconnect(self):
        self.connected = False
        print("Database disconnected")
    
    def query(self, sql):
        if not self.connected:
            raise ConnectionError("No database connection")
        if "DROP" in sql.upper():
            raise PermissionError("DROP operations not allowed")
        return "Query executed successfully"

def database_operations_demo():
    """Demonstrate exception handling in database operations"""
    print("\n=== Database Operations Example ===")
    
    db = DatabaseConnection()
    
    try:
        # Attempt operations without connection
        db.query("SELECT * FROM users")
    except ConnectionError as e:
        print(f"Connection Error: {e}")
        db.connect()
    
    try:
        # Attempt dangerous operation
        db.query("DROP TABLE users")
    except PermissionError as e:
        print(f"Permission Error: {e}")
    finally:
        db.disconnect()

# Retry Decorator with Exception Handling
def retry(max_attempts=3, delay=1):
    """Decorator to retry failed operations"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    print(f"Attempt {attempts} failed: {e}. Retrying...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_operation():
    """Simulate an unreliable operation"""
    import random
    if random.random() < 0.7:
        raise ConnectionError("Random network error")
    return "Success!"

def main():
    """Run all demonstrations"""
    # Basic demos
    basic_exception_demo()
    advanced_exception_demo()
    custom_exception_demo()
    
    # Context manager demo
    print("\n=== Context Manager Demo ===")
    with timer():
        time.sleep(1)
    
    # Database operations demo
    database_operations_demo()
    
    # Retry decorator demo
    print("\n=== Retry Decorator Demo ===")
    try:
        result = unreliable_operation()
        print(f"Operation result: {result}")
    except ConnectionError as e:
        print(f"Operation finally failed after 3 attempts: {e}")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Run demonstrations
    main()
