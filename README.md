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
   pip install turtle
   ```

4. Generate a Cohere API key from [Cohere's Website](https://dashboard.cohere.com/api-keys). Copy the key and either paste it into the Clock_DevBuddy.py file at the designated location as a string assigned to the variable COHERE_API_KEY, or save it in the system environment variables. In the latter case, use a Python dictionary format as shown below, with a key named 'Cohere' and the corresponding value being the generated API key:

   ```python
   {"Cohere":"<your-api-key>"}
   ```

---

## Usage

1. Run the main file to start the clock:
   
   ```bash
   python Main.py
   ```

2. The clock will render an analog display with ticking functionality, and the chatbot will provide assistance or additional information as required.

---

## Features

- **Circular Linked List**: Implements timekeeping logic using nodes to represent hours, minutes, and seconds.
- **Graphical Display**: Renders a dynamic clock using the Turtle library.
- **OOP Design**: Encapsulation of clock logic in modular components.
- **Chatbot Integration**: Assists with project details and troubleshooting via the Cohere API.

---

This project was built in December 2024.
