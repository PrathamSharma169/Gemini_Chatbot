import google.generativeai as genai
import os
API_KEY = os.environ.get("API_KEY")

genai.configure(api_key=API_KEY)

for i in genai.list_models():
    print(i.name)

def read(message):
    for chunk in message :
        chunk.text.replace('*',"")
        print(chunk.text)

model=genai.GenerativeModel("gemini-pro")

history=[]

chat= model.start_chat(history=history)

chat.send_message("you are Pratham's assistant ")

def chatting(text):
    res=chat.send_message(text)
    read(res) 


# message= model.generate_content("hello")

# for chunk in message :
#     chunk.text.replace('*',"")
#     print(chunk.text)

if __name__=="__main__":
    text="true"
    while(text!="exit"):
        text=input("user: ")
        chatting(text)

