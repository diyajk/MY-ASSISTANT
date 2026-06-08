import google.genai as genai

# Paste your Gemini API key here
API_KEY = input("Enter your Gemini API Key: ")

client = genai.Client(api_key=API_KEY)

# ---- PERSONALISE THIS PART ----
# Change the name, add facts about yourself, give it a role
SYSTEM_PROMPT = """You are my productivity assistant.
Your name is Max.
Help me plan my day, break down tasks, and stay focused.
Be direct and motivating."""
# --------------------------------

config = genai.types.GenerateContentConfig(
    system_instruction=SYSTEM_PROMPT,
    temperature=1.0,
)

# This gives the assistant memory of the conversation
chat_history = []

print("=" * 40)
print("  Nova is ready! Type 'quit' to exit.")
print("=" * 40)
print()

while True:
    user_input = input("You: ")
    
    if user_input.strip() == "":
        continue  # ignore empty messages
    
    if user_input.lower() == "quit":
        print("Nova: Goodbye! Have a great day!")
        break
    
    chat_history.append({"role": "user", "content": user_input})
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
        config=config
    )
    chat_history.append({"role": "assistant", "content": response.text})
    print(f"Nova: {response.text}")
    print()