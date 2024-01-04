# Example main.py
from infrastructure.models.user_model import User

def main():
    # Example usage of User
    # user = User(name="John Doe", email="john@example.com")
    # user.save()
    user_id = User.get("John Doe")

    if user_id:
        print(f"retrieved user: {user_id}")
    else: 
        print("user not found")


if __name__ == "__main__":
    main()
