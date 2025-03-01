#import syst
import google.generativeai as genai
from rich import print
from rich.text import Text
import os
col = input("What colour do you want you interface ? \n ANSWER :")
os.system("clear")
print(Text("THIS IS AN ILLNESS DETECTOR\n....\n ", style = f" {col} bold"))
genai.configure(api_key= "Enter Your API KEY here")
# Create the model
generation_config = {
"temperature": 1,
"top_p": 0.7,
"top_k": 40,
"max_output_tokens": 2000,
"response_mime_type": "text/plain",
}
model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config,system_instruction = "You start your respinse with 'AI doctor : '.You are an illness predictor, and your job is to generate a list of possible illnesses in a very appealing way that won't make the terrify the user from the symptoms assed to you,if input is not sounding like a symptom you can suggest symptoms close to the input for the user, three symptoms must be passed to you if not you tell them again to pass three  .\ninput would be passed as a string but you should return output as plain text.\n\nmake sure the possible illness you give are very close enough or even accurate to the symptoms\nAlso ask further questions like a doctor and take down every user input that would help narrow down what the illness is make your response not more than 60 words, give possible illness, possible home remedies  and possible first aid procedures then ask precise questions to get the accurate illness like a doctor would\n also arrange your response to be user friendly interactive and easy to understand ")

chat_session = model.start_chat(

history=[

]

)
count = 0
print(Text("Enter three symptoms your are feeling : ",style = f"{col} bold"))
response = chat_session.send_message(input("....\n\nUSER : "))
print(Text(response.text,style = f"{col} bold"))
while count < 7:
	interact = chat_session.send_message(input("ANSWER : "))
	print("\n\n")
	print(Text(interact.text,style = f"{col} bold "))

