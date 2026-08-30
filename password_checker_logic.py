import string


def check_password_strength(password: str) -> tuple[str, str]:

    if not password:
        return "Please enter a password", "#000000"

    
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    
    score = 0
    if length >= 8:
        score += 1
    if has_lower and has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    
    if length < 6 or score <= 1:
        return "Weak Password ", "#d9534f"  
    elif score in (2, 3):
        return "Medium Password ", "#f0ad4e"  
    else:
        return "Strong Password ", "#5cb85c"  