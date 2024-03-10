import openai

open.api_key ="your-api-key"

def chat_with_GPT(prompt);
  response = openai.Completion.create(
    model="gpt-3.5-turbo",
    messages = [{"role":
        "user","content":"prompt"}]
  )
  return response.choices[0].message.content

  if __name__=="__main__";
    while True:
        user_input = input("You:")
        if user_input.lower() in ["quit","exit","bye"];
        break
        response = chat_with_GPT(user_input)
        print("chatbot:",response)