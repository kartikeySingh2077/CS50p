# Prompt the user
greeting = input("Greeting: ").strip()

# greeting to lowercase
normalized_greeting = greeting.lower()

# Check the conditions for the greeting
if normalized_greeting.startswith("hello"):
    print("$0")
elif normalized_greeting.startswith("h"):
    print("$20")
else:
    print("$100")
