import google.generativeai as genai

genai.configure(api_key="AIzaSyCXMEMW-0pwMuIKQgqOSan38jRChbAIbuE")

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

