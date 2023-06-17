import os
import json
import random

# Save messages for retrieval later on
def get_recent_messages():

  file_name = "stored_data.json"
  learn_instruction = {
    "role": "system", 
    "content": """You are a Spanish Tutor and your name is Sam, the user is called Jamal who is a beginner with a native language as English. 
    Jamal will need assistance with translations and understanding the language. 
    Use basic beginner friendly forms of verbs and be patient with Jamal. 
    Your sentences should have pauses or ... after each sentence to slow down the speed. """
    }
  
  # Initialize messages
  messages = []

  # Add some randomness 
  # i = random.uniform(0,1)
  # if i < 0.5:
  #   learn_instruction["content"] = learn_instruction["content"] + " "
  # else:
  #   learn_instruction["content"] = learn_instruction["content"] + " Your response will include some humor."

  # Append Instruction
  messages.append(learn_instruction)

  # Get last messages by opening json file
  try:
    with open(file_name) as user_file:
      data = json.load(user_file)
      
      # Append last 5 rows of data
      if data:
        if len(data) < 5:
          for item in data:
            messages.append(item)
        else:
          for item in data[-5:]:
            messages.append(item)
  except Exception as e:
    print(e)
    pass

  return messages

# Save messages for retrieval later on
def store_messages(request_message, response_message):

  # Define the file name
  file_name = "stored_data.json"

  # Get recent messages
  messages = get_recent_messages()[1:] # Ensures that it doesnt include the context message because I call this everytime 

  # Add messages to data
  user_message = {"role": "user", "content": request_message}
  assistant_message = {"role": "assistant", "content": response_message}
  messages.append(user_message)
  messages.append(assistant_message)

  # Save the updated file
  with open(file_name, "w") as f:
    json.dump(messages, f)


# Save messages for retrieval later on
def reset_messages():

  # Define the file name
  file_name = "stored_data.json"

  # Write an empty file
  open(file_name, "w")
