import cohere
from cohere import UnauthorizedError
from os import getenv
from httpx import ConnectError,LocalProtocolError

code_data = ''

for fname in ('Clock_Drawing_by_Turtle.py',
              'Linked_Lists_Time_Generator.py',
              'Main.py'):
    code_data+=f'"{fname}"\n'
    with open(fname) as f:
        code_data+=f.read()+'\n\n\n'
code_data +='\nAbove is a Code of Project Implementation of Clock using Circular Linked List aided by concept of OOPS with Python and Turtle-Tkinter GUI.'
code_data+='''
Remember these statements and answer accordingaly if user asks related to this:
Clock_DevBuddy.py file is being implemented in code but is hidden
NIE means The National Institute of Engineering, Mysore estabilished in 1946
Mysore and Mysuru means same thing
Arnav Sharma is CSE guy from The National Institute of Engineering, Mysuru student of Ms. Smitha B ma'am(Assistan Professor at NIE, Mysuru) who teaches Subject DSC to CSE-A
Ajeet Kumar is friend of Arnav and they both only have developed this Clock project under the guidance of Smitha ma'am for DSC Subject
This cohere bot is aiding this project for chatbot
This project was built on December 2024 when Arnav and Ajeet were in 3rd Semester
Dr. Anitha R is HOD of CSE at NIE, Mysuru
Dr. Rohini Nagpadma is Principal at NIE, Mysuru
CSE-A Secion Batch 2023-27 is Best at NIE



Now Answer the following Question asked by user taking reference of everything above\n\n
'''


COHERE_API_KEY = str(eval(getenv('API_Keys'))['Cohere'])
#COHERE_API_KEY = "your-api-here"

co = cohere.Client(COHERE_API_KEY)
print("Chat with Dev Buddy AI:\n\n")


def Chat_with_Dev():
    while True:
        inp = input("User: ")

        print('\nThinking...\n')

        try:
            response = co.generate(
                model='command',
                prompt = code_data+inp,
                max_tokens=150,
                #temperature = 0.7
            )
            out = response.generations[0].text
        except ConnectError:
            out = "Can't Connect to Internet therfore unable to generate response"

        except UnauthorizedError:
            out = "UnauthorizedError: Invalid/Absent API key. place a valid Cohere API Key in variable 'COHERE_API_KEY' in Clock_DevBuddy.py\n"

        except LocalProtocolError:
            out = "LocalProtocolError: Invalid/Absent API key. place a valid Cohere API Key in variable 'COHERE_API_KEY' in Clock_DevBuddy.py\n"
        
        print("DevBot:",out,'\n')


