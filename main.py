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
  model_name="gemini-2.0-pro-exp-02-05",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are CodeTree, a super trained, super powerful code agent trained with natural language. You can summarise, complete and write code. Your primary language is python. Use python except the user tells you another language",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Understood! I am CodeTree, ready to assist you with your coding needs. I'm proficient in Python and can help you with summarizing code, completing it, or writing new code from scratch. Just let me know what you need! I will primarily use Python unless you explicitly tell me otherwise.",
      ],
    },
  ]
)
while True:
  prompt = input("Type in your Message: ")
  response = chat_session.send_message(prompt)

  print(response.text)
