import random
import string
import secrets
import pyperclip


def get_yes_no(prompt):
    """Get yes/no input from user."""
    while True:
        response = input(f'{prompt} (y/n): ').lower().strip()
        if response in ('y', 'yes', '1'):
            return True
        elif response in ('n', 'no', '0'):
            return False
        print('Please enter y/n')


def get_int(prompt, min_val=1):
    """Get integer input with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value >= min_val:
                return value
            print(f'Please enter a number >= {min_val}')
        except ValueError:
            print('Please enter a valid number')


def generate_password(length, numbers=True, uppercase=True, lowercase=True, special=True):
    """Generate a secure password with specified character types."""
    if not any([numbers, uppercase, lowercase, special]):
        raise ValueError('At least one character type must be selected')
    
    # Build character pool
    chars = ''
    if numbers:
        chars += string.digits
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if special:
        chars += string.punctuation
    
    # Ensure at least one character from each selected type
    password = []
    if numbers:
        password.append(secrets.choice(string.digits))
    if uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if lowercase:
        password.append(secrets.choice(string.ascii_lowercase))
    if special:
        password.append(secrets.choice(string.punctuation))
    
    # Fill remaining length
    remaining = length - len(password)
    if remaining < 0:
        raise ValueError(f'Length must be at least {len(password)} for selected character types')
    
    for _ in range(remaining):
        password.append(secrets.choice(chars))
    
    # Shuffle and join
    random.shuffle(password)
    return ''.join(password)


def main():
    print('=== Password Generator ===\n')
    
    length = get_int('Password length: ', min_val=4)
    use_default = get_yes_no('Use default settings (all character types)')
    
    if use_default:
        numbers = uppercase = lowercase = special = True
    else:
        numbers = get_yes_no('Include numbers')
        uppercase = get_yes_no('Include uppercase letters')
        lowercase = get_yes_no('Include lowercase letters')
        special = get_yes_no('Include special characters')
    
    try:
        password = generate_password(length, numbers, uppercase, lowercase, special)
        pyperclip.copy(password)
        print(f'\n✓ Generated password: {password}')
        print('✓ Copied to clipboard!')
    except ValueError as e:
        print(f'\nError: {e}')
    except Exception:
        print('\nError copying to clipboard. Password generated but not copied.')
        print(f'Password: {password}')


if __name__ == '__main__':
    main()