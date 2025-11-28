from google import genai

key = "put ur key"
MODEL_NAME = "gemini-2.5-flash"

client = genai.Client(api_key=key) 

print("--- Simple Chat App ---")
while True:
    user_input = input("Enter what you want to search or type 'exit' to close: ")
    
    if user_input.lower() == "exit":
        print("See you later!")
        break
    response = client.models.generate_content(
        model=MODEL_NAME, 
        contents=[user_input]
    )

    print("BOT : ", response.text)
