# Prompt the user for their waifu's name
waifu_name = input("Enter your waifu's name: ")

# Prompt the user for the affection level
affection_level = int(input("Enter your affection level (1-100): "))

# Determine the affection message
if 80 <= affection_level <= 100:
    message = "Love"
elif 50 <= affection_level < 80:
    message = "Like"
else:
    message = "Neutral"

# Output the result
print(f"Affection for {waifu_name}: {message}")

