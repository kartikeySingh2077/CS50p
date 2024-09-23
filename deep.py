# deep.py

# Prompt the user for input
answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

# Normalize the input to lowercase and strip any extra whitespace
normalized_answer = answer.strip().lower()

# Check if the answer is 42,forty-two, forty two
if normalized_answer == "42" or normalized_answer == "forty-two" or normalized_answer == "forty two":
    print("Yes")
else:
    print("No")
