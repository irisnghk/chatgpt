import tkinter as tk
import openai

# Set OpenAI API key
openai.api_key = "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"

# Define function to get ChatGPT response
def get_response(prompt):
    keywords = ['iris', 'ng', 'owner']

    # Check if any of the keywords is present in the user's input
    if any(keyword in prompt.lower() for keyword in keywords):
        response = "Yes Iris is the data expert"
    else:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
    return response

# Define function to handle user input and ChatGPT response
def send_message(event=None):
    # Get user input
    user_message = user_input.get()
    # Display user input in chat window
    chat_log.insert(tk.END, "You: " + user_message + "\n")

    # Get ChatGPT response
    response = get_response(user_message)

    # If response is a string (i.e. a keyword was detected)
    if isinstance(response, str):
        bot_message_str = response
    else:
        # Convert bot_message to string
        bot_message_str = str(response.choices[0].text)

    # Display ChatGPT response in chat window
    chat_log.insert(tk.END, "ChatGPT: " + bot_message_str.strip() + "\n")
    # Clear user input field
    user_input.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("ChatGPT")

# Create chat log window
chat_log = tk.Text(root, width=50, height=20)
chat_log.pack()

# Create user input field and send button
user_input = tk.Entry(root, width=50)
user_input.pack(side=tk.LEFT, padx=5, pady=5)
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Bind enter key to send_message function
root.bind('<Return>', send_message)

# Start main event loop
root.mainloop()
