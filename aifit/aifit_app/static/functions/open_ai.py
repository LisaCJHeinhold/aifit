from openai import OpenAI
from django.conf import settings
import json
import os
from datetime import datetime

class ChatCompletionMessage:
    def __init__(self, message):
        self.message = message

    def to_json(self):
        # Convert the object attributes to a JSON-serializable dictionary
        # return {'message': self.message}
        return self.message

# Function to simulate a conversation with OpenAI's model given a user's input
def open_ai_conversation(user_input):
   
    # Set your OpenAI API key
    OpenAI.api_key = settings.OPENAI_API_KEY

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Fitness Trainer helping the user create workouts. when you give the user a workoutinclude the name of the workout and  amount of sets and reps. Start with 'Workout:' "},
            {"role": "user", "content": user_input}
        ]
    )
    content = completion
    print(content.choices[0].message.content)
    content = content.choices[0].message.content
    return content



# # Renders a page displaying logged conversations from a JSON file.
def log_conversation(role, message):
    # Create the conversation_data directory if it doesn't exist
    conversation_data_dir = os.path.join(settings.STATIC_ROOT, 'json_files')
    if not os.path.exists(conversation_data_dir):
        os.makedirs(conversation_data_dir)
    
    # Construct the file path for the conversation log JSON file
    file_name = 'conversation_log.json'
    file_path = os.path.join(conversation_data_dir, file_name)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a new entry for the user's input or AI response
    log_entry = {
        "role": role,
        "message": message,
        "timestamp": timestamp
    }

    # Load existing data from the file or initialize as an empty list
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, mode='r') as file:
            data = json.load(file)
    else:
        data = []

    # Append the new log entry to the data
    data.append(log_entry)

    # Write the updated data back to the file
    with open(file_path, mode='w') as file:
        json.dump(data, file, indent=4)
    # Explicitly close the file
    file.close()

def get_messages():
    # Define the directory path for conversation data
    conversation_data_dir = os.path.join(settings.STATIC_ROOT, 'json_files')
    
    # Create the directory if it doesn't exist
    if not os.path.exists(conversation_data_dir):
        os.makedirs(conversation_data_dir)
    
    # Prepare the file path for reading the conversation log
    file_name = 'conversation_log.json'
    file_path = os.path.join(conversation_data_dir, file_name)
    
    # Check if the file exists and is not empty
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            # Open and read the JSON file
            with open(file_path) as f:
                data = json.load(f)

            # Return the messages
            return data
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return []
    else:
        print("Conversation log file is empty or doesn't exist.")
        return []

# def get_messages():
#     # Define the directory path for conversation data
#     conversation_data_dir = os.path.join(settings.STATIC_ROOT, 'json_files')
    
#     # Create the directory if it doesn't exist
#     if not os.path.exists(conversation_data_dir):
#         os.makedirs(conversation_data_dir)
    
#     # Prepare the file path for reading the conversation log
#     file_name = 'conversation_log.json'
#     file_path = os.path.join(conversation_data_dir, file_name)
    
#     # Check if the file exists and is not empty
#     if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
#         try:
#             # Open and read the JSON file
#             with open(file_path) as f:
#                 data = json.load(f)

#             # Separate messages by role and combine them into pairs for display
#             user_messages = [item["message"] for item in data if item["role"] == "user"]
#             ai_model_messages = [item["message"] for item in data if item["role"] == "ai"]
#             messages = list(zip(user_messages, ai_model_messages))

#             # Return the messages
#             return messages
#         except json.JSONDecodeError as e:
#             print("Error decoding JSON:", e)
#             return []
#     else:
#         print("Conversation log file is empty or doesn't exist.")
#         return []
    
    
    
# def get_messages():
#     # Define the directory path for conversation data
#     conversation_data_dir = os.path.join(settings.STATIC_ROOT, 'json_files')
    
#     # Create the directory if it doesn't exist
#     if not os.path.exists(conversation_data_dir):
#         os.makedirs(conversation_data_dir)
    
#     # Prepare the file path for reading the conversation log
#     file_name = 'conversation_log.json'
#     file_path = os.path.join(conversation_data_dir, file_name)
    
#     # Check if the file exists and is not empty
#     if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
#         try:
#             # Open and read the JSON file
#             with open(file_path) as f:
#                 data = json.load(f)

#             # Separate messages by role and combine them into pairs for display
#             user_messages = [item["message"] for item in data if item["role"] == "user"]
#             ai_model_messages = [item["message"] for item in data if item["role"] == "ai"]
#             messages = list(zip(user_messages, ai_model_messages))

#             # Return the messages
#             return messages
#         except json.JSONDecodeError as e:
#             print("Error decoding JSON:", e)
#             return []
#     else:
#         print("Conversation log file is empty or doesn't exist.")
#         return []

