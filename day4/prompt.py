import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
# load_dotenv()
load_dotenv("notepad.env")
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("not found")
client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    print(ans)

bprompt='''this is a user complain my  is not working
#role:you are a support assistant for laptop/pc
#task:classify my problem
#constraint:only claassify problem in three format namely billing ,technical,management
#output format : ans in not more than 100 words
#zero shot
#fallback :any problem other than classified problem ans it is not applicable

fix this problem'''
print(llm_ans(bprompt))