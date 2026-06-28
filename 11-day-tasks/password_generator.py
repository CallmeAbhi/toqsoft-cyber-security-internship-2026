import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generate a random password with specified criteria.
    
    Args:
        length: Length of the password (default: 12)
        use_uppercase: Include uppercase letters (default: True)
        use_lowercase: Include lowercase letters (default: True)
        use_digits: Include digits (default: True)
        use_special: Include special characters (default: True)
    
    Returns:
        A random password string
    """
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character type must be selected")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===\n")
    
    try:
        length = int(input("Enter password length (default 12): ") or "12")
        
        use_upper = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
        use_lower = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
        use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
        use_special = input("Include special characters? (y/n, default y): ").lower() != 'n'
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"\nGenerated Password: {password}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
