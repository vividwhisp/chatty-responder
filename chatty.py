import json

try:
   with open("data/knowledge.json", "r") as file:
    knowledge = json.load(file)
except FileNotFoundError:
   print("Error : Knowledge.json not found")
except json.JSONDecodeError:
   print("Error : knowledge.json is invalid json")

while True:
    user_input = input("YOU: ").lower()
    
    if user_input in ["exit", "bye"]:
        bot_response = "Goodbye! Have a nice day"
        print("YOUR DAD:", bot_response)
        break
    elif user_input.strip()=="":
       print("Please type somerthing")
       continue
    # If input exists in knowledge
    elif user_input in knowledge:
        bot_response = knowledge[user_input]
        print("YOUR DAD:", bot_response)

    # If input not found
    else:
    

     new_response = input("Teach me: What should I reply to that?\n").strip()

    # Add to knowledge
     if new_response:
       knowledge[user_input] = new_response
       bot_response=new_response

    # Save updated knowledge to file
       try:
        with open("data/knowledge.json", "w") as file:
            json.dump(knowledge, file, indent=4)
        print("Thanks! I’ve learned that.")
       except Exception as e:
        print("Failed to save new knowledge:", e)
     else:
        bot_response = "TEACH ME DAWGG!!"
        print(bot_response)

    # Log the chat
    try:
     with open("logs/chatlog.txt", "a") as log_file:
        log_file.write(f"You: {user_input}\n")
        log_file.write(f"YOUR DAD: {bot_response}\n")
    except Exception as e:
       print("Logging error: ",e)
