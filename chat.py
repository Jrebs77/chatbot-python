import os
from openai import OpenAI

cliente = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def conversar_com_gpt():
    while True:
        user_impuut = input("Você: ")
        
        if user_impuut.lower() == "sair":
            print("Chat Bot : Até logo!")
            break
        completion = cliente.chat.completions.create(
            messages= [  
                {"role": "user", "content": user_impuut}
                content
            ],
            model= "gpt-4o-mini",

            reply = completion.choices[0].message.content
            print("Chat Bot :", reply) 




    
conversar_com_gpt()        
        
