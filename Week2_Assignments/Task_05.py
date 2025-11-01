
# Task 5: Mini Project – Prompt Logger

'''
1. Accepts a user input (simulating an AI prompt). 
2. Saves the prompt text in a file named prompt_history.txt. 
3. Each time you run the program, new prompts are appended with timestamps.
'''

print("\n--- Task 5: Prompt Logger ---")

import datetime

user_prompt = input("Enter your AI prompt: ")

# Append prompt with timestamp
with open("prompt_history.txt", "a") as file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{timestamp} --> {user_prompt}\n")

print("✅ Prompt saved successfully!")
