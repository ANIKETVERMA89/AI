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
role="user"

prompt1="heloo"
prompt2="write somwthong about time dialation"
prompt3="write essay on ml"
prompts=[prompt1,prompt2,prompt3]
for p in prompts:
    message={"role":role,
         "content":p}
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages,max_tokens=500)
    print(response.choices[0].message.content)

