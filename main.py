import os
import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are Frak, an ai voice assistant which helps people in their tasks",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I'm Frak! Ready to assist you. I'm here to help you with your tasks, so tell me, what do you need? I'm capable of a wide range of things, like:\n\n*   **Setting reminders:** Don't forget that important meeting!\n*   **Creating lists:** Shopping lists, to-do lists, brainstorming lists - you name it.\n*   **Answering questions:** I'll do my best to find the answers you need.\n*   **Summarizing information:** Got a long article? I can help you get the gist of it.\n*   **Providing creative text formats:** Want a poem, a story, a script? Let's do it!\n*   **And much more!**\n\nSo, don't be shy. Let me know how I can be of assistance today. What's on your mind? Let's get to work!\n",
      ],
    },
  ]
)
while True:
  prompt = input("Type in your Message: ")
  response = chat_session.send_message(prompt)

  print(response.text)
