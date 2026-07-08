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
prompt="i love you"
# SYSTEM 
message_sys={
    "role":"system",
    "content":" give me a nickname as my name is eshu "
}
message_sys1={
    "role":"system",
    "content":"you are my strict office manager"
}
message={"role":role,
         "content":prompt}
messages=[message_sys1,message]
# TEMP
response=client.chat.completions.create(model=model,messages=messages,temperature=2)
# print(response)
print(response.choices[0].message.content)