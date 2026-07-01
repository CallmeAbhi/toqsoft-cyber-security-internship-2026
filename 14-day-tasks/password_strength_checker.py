import string
user_password = input("Enter your password: ")

def check_password_strength(user_password):
    suggestions = []
    strength=0
    length = len(user_password)
    match length:
        case 0:
            suggestions.append("Password cannot be empty.")
            length_status = "Very Weak"

        case 1 | 2 | 3:
            suggestions.append("Consider using at least 12 characters.")
            length_status = "Very Weak"

        case 4 | 5 | 6:
            strength += 0
            suggestions.append("Consider using at least 12 characters.")
            length_status = "Weak"

        case 7 | 8 | 9:
            strength += 0.5
            suggestions.append("Consider using at least 12 characters.")
            length_status = "Moderate"

        case _:
            strength += 1
            length_status = "Good"
    
    if any(char.isdigit() for char in user_password):
        num_status = "Present"
        strength += 1
    else:
        num_status = "Missing"
        suggestions.append("Consider adding numbers to your password for better security.")
    if any(char.isupper() for char in user_password):
        upper_status = "Present"
        strength += 1
    else:
        upper_status = "Missing"
        suggestions.append("Consider adding uppercase letters to your password for better security.")
    if any(char.islower() for char in user_password):
        lower_status = "Present"
        strength += 1
    else:
        lower_status = "Missing"
        suggestions.append("Consider adding lowercase letters to your password for better security.")
    if any(char in string.punctuation for char in user_password):
        punctuation_status = "Present"
        strength += 1
    else:
        punctuation_status = "Missing"
        suggestions.append("Consider adding Special Characters to your password for better security.")

    if strength <= 1:
        rating = "Very Weak"
    elif strength <= 2:
        rating = "Weak"
    elif strength <= 3:
        rating = "Moderate"
    elif strength <= 4:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return (
    f"\n========== Password Strength Report ==========\n"
    f"Password Length           : {length}, {length_status}\n"
    f"Number Status             : {num_status if 'num_status'  else 'No numbers'}\n"
    f"Uppercase Status          : {upper_status if 'upper_status'  else 'No uppercase letters'}\n"
    f"Lowercase Status          : {lower_status if 'lower_status'  else 'No lowercase letters'}\n"
    f"Special Characters Status : {punctuation_status if 'punctuation_status'  else 'No special characters'}\n"
    f"Suggestions               : {'; '.join(suggestions) if suggestions else 'Excellent! Your password satisfies all evaluated security checks.'}\n"
    f"Strength Score            : {strength}/5\n"
    f"Password Rating           : {rating}\n"
    f"=============================================="
)

print(check_password_strength(user_password))