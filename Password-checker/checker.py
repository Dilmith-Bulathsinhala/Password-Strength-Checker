import re

def check_password_strength(password):
    strength = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Increase the password length to at least 8 characters.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        suggestions.append("Include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Include at least one special character.")

    # Determine overall strength
    if strength == 5:
        return "Strong password!", suggestions
    elif 3 <= strength < 5:
        return "Medium strength password.", suggestions
    else:
        return "Weak password.", suggestions


# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    result, advice = check_password_strength(user_password)
    print(result)
    if advice:
        print("Suggestions to improve:")
        for suggestion in advice:
            print(f"- {suggestion}")
