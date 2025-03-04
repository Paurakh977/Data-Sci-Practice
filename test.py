# None
# __library_transactions: Dict[str, Dict[str, Dict[str, int]]] = {}  # date: {action: {category: count}}

books: dict[str, list[dict[str, any]]] = {}  # key: category, value: list of book details

UNIVERSAL_BORROW_HISTORY={
    "2025-01-02":[
        {
           "User_id":"u123",
           "book_id":"ISBN1213",
           "borrow_period":"4",
           "Book_category" : "comics"
        },
        {
           "User_id":"u223",
           "book_id":"ISBN313",
           "borrow_period":"4",
           "Book_category" : "Fiction" 
        },
    ],
    
    "2025-01-03":[
        {
           "User_id":"u123",
           "book_id":"ISBN213",
           "borrow_period":"2",
           "Book_category" : "Science"
        },
        {
           "User_id":"u253",
           "book_id":"ISBN713",
           "borrow_period":"4",
           "Book_category" : "Philosophy" 
        },
        
    ]
}

# key will be date and value will be list of dict 
self_borrow_history = {
    "2025-01-02": [
        {   
            "book": "Book obj itself",
            "book_id": "ISBN98632",
            "borrow_period": 2,
            "book_category": "Science",
            "library": "Arts Library"
        },
        {   
            "book": "Book obj itself",
            "book_id": "ISBN998632",
            "borrow_period": 4,
            "book_category": "Fiction",
            "library": "Science Library"
        }
    ],
    "2025-01-03":[
        {   
           "book": "Book obj itself",
           "book_id":"ISBN213",
           "borrow_period":"2",
           "Book_category" : "Science"
        },
        {
           "book": "Book obj itself",
           "User_id":"u253",
           "book_id":"ISBN713",
           "borrow_period":"4",
           "Book_category" : "Philosophy" 
        },
        
    ]
    
}

# Standardized return history (keys standardized and borrow_period as int)
self_book_return_history = {
    "2025-01-03": [
        {
            "book": "Book obj itself",  # If you have an object, this could be a reference
            "book_id": "ISBN0291",
            "fine": 20,
            "borrow_period": 8,
            "condition_on_return": "good",
            "library": "Arts Library"
        },
        {
            "book": "Book obj itself",
            "book_id": "ISBN0321",
            "borrow_period": 2,
            "condition_on_return": "Average",
            "library": "College Library"
            # 'fine' is optional here
        }
    ]
}

def get_transactions():
    transactions = {}
    
    # Process borrow history
    for key_date, value_list in self_borrow_history.items():
        # Optionally create a copy of each record to avoid modifying the original data
        processed_list = []
        for item in value_list:
            new_item = item.copy()  # Create a shallow copy
            new_item.update({"type": "borrow"})
            processed_list.append(new_item)
        
        if key_date not in transactions:
            transactions[key_date] = processed_list
        else:
            transactions[key_date].extend(processed_list)
            
    # Process return history
    for key_date, value_list in self_book_return_history.items():
        processed_list = []
        for item in value_list:
            new_item = item.copy()
            new_item.update({"type": "return"})
            processed_list.append(new_item)
        
        if key_date not in transactions:
            transactions[key_date] = processed_list
        else:
            transactions[key_date].extend(processed_list)
    
    return transactions

            
            
            
        
        