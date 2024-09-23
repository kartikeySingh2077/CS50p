# Prompt the user for their favorite anime genre
genre = input("Enter your favorite anime genre (Romance, Action, Fantasy): ").strip().lower()

# Suggest a waifu based on the genre
if genre == "romance":
    print("Suggested Waifu: Emilia from Re:Zero")
elif genre == "action":
    print("Suggested Waifu: Mikasa Ackerman from Attack on Titan")
elif genre == "fantasy":
    print("Suggested Waifu: Rem from Re:Zero")
else:
    print("Genre not recognized. Please choose from Romance, Action, or Fantasy.")
