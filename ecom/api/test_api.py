import requests
import json

# Base URL for the API
BASE_URL = 'http://127.0.0.1:8000/api'

def test_registration():
    """Test user registration"""
    print("\n=== Testing Registration ===")
    
    # Registration data
    register_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "confirm_password": "testpass123",
        "first_name": "Test",
        "last_name": "User"
    }
    
    # Make POST request to registration endpoint
    response = requests.post(f'{BASE_URL}/register/', json=register_data)
    
    # Print response
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))
    
    return response.json()

def test_login():
    """Test user login"""
    print("\n=== Testing Login ===")
    
    # Login data
    login_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    
    # Make POST request to login endpoint
    response = requests.post(f'{BASE_URL}/login/', json=login_data)
    
    # Print response
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))
    
    return response.json()

def test_invalid_registration():
    """Test registration with invalid data"""
    print("\n=== Testing Invalid Registration ===")
    
    # Invalid registration data (missing required fields)
    invalid_data = {
        "username": "testuser2",
        "password": "testpass123"
        # Missing email, first_name, last_name
    }
    
    # Make POST request to registration endpoint
    response = requests.post(f'{BASE_URL}/register/', json=invalid_data)
    
    # Print response
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))

def test_invalid_login():
    """Test login with invalid credentials"""
    print("\n=== Testing Invalid Login ===")
    
    # Invalid login data
    invalid_data = {
        "username": "wronguser",
        "password": "wrongpass"
    }
    
    # Make POST request to login endpoint
    response = requests.post(f'{BASE_URL}/login/', json=invalid_data)
    
    # Print response
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    # Run all tests
    print("Starting API Tests...")
    
    # Test registration
    registration_result = test_registration()
    
    # Test login
    login_result = test_login()
    
    # Test invalid registration
    test_invalid_registration()
    
    # Test invalid login
    test_invalid_login()
    
    print("\nAPI Testing Completed!") 