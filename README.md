# Clock-using-CircularLL_and_AIAssistant

This project demonstrates a clock that ticks by leveraging the concept of a circular linked list. It uses Python's Turtle library to display the clock visually and incorporates object-oriented programming (OOP) principles to create both nodes for the circular linked list and the clock itself. Additionally, the Cohere API is utilized to enhance chatbot functionality and assist the users with their queries and troublshooted experience.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

---

## About the Project

This project showcases the integration of data structures and graphical interfaces through the following features:

- A clock interface that updates in real-time using a circular linked list to manage time.
- The Turtle library for rendering the clock face and hands.
- Object-oriented principles to encapsulate clock components and behavior.
- Chatbot functionality powered by the Cohere API for interactive guidance.
- The file Linked_Lists_Time_Generator.c is a C language implementation that mirrors the functionality and purpose of the Python file Linked_Lists_Time_Generator.py. While the Python file likely utilizes Python's dynamic and high-level constructs, the C file demonstrates the equivalent logic and structure in a more low-level and manually managed context.

---

## Tech Stack

- **Python**: Core programming language.
- **Turtle Library**: For graphical clock rendering.
- **Cohere API**: Enables chatbot integration for developer assistance.

---

## Installation

To install and run the Clock-Using-CircularLL_and_AIAssistant project, follow these steps:

1. Clone the repository:
   
   ```bash
   git clone https://github.com/ArnavSharma2908/Clock-Using-CircularLL_and_AIAssistant
   ```

2. Navigate to the project directory:
   
   ```bash
   cd Clock-using-CircularLL_and_AIAssistant
   ```

3. Ensure Python 3 is installed along with required modules and pip is functional:
   
   ```bash
   pip install cohere
   ```

4. Generate a Cohere API key from [Cohere's Website](https://dashboard.cohere.com/api-keys). Copy the key and either paste it into the Clock_DevBuddy.py file at the designated location as a string assigned to the variable COHERE_API_KEY and comment out any other declaration of variable COHERE_API_KEY, or save it in the system enviornment variables. In the latter case, use a Python dictionary format as shown below, with a key named 'Cohere' and the corresponding value being the generated API key:
   
   ```python
   {"Cohere":"<your-api-key>"}
   ```

---

## Usage

1. Run the main file to start the clock:
   
   ```bash
   python Main.py
   ```
   
   If the above command does not work in Terminal/Command Prompt then try running Main.py file from working directory by using Python IDLE or any other present IDE.
   If Dev Buddy AI Assistant is not working then try debugging API part in following ways mentioned:
   
   1) Check if generated Cohere API key is a valid and active Key from [Cohere](https://cohere.com/).
   2) If API Key is valid then check if API Key was pasted correctly in System enviornment variables in prescribed dictionary format as discussed earlier.
   3) If previous Step 2 is the issue then go for simpler method that was discussed earlier. Paste the generated API Key in Clock_DevBuddy.py at designated location and comment out the above line which is not needed or may throw error. This method is not recommended as it may expose user's API Key if code is shared without inspection and correction of such API Keys.

2. After following all the steps, the program will render an clock with analog display with ticking functionality, and the chatbot will provide assistance or additional information as required about Code and developers.

---

## Features

- **Circular Linked List**: Implements timekeeping logic using nodes to represent hours, minutes, and seconds.
- **Graphical Display**: Renders a dynamic clock using the Turtle library.
- **OOP Design**: Encapsulation of clock logic in modular components.
- **Chatbot Integration**: Assists with project details and troubleshooting via the Cohere API.

---

This project was built in December 2024.
