# Eco-Travel Advisor

## Project Overview

Eco-Travel Advisor is a Rasa-based conversational chatbot developed for sustainable travel planning. The system collects key travel preferences through a multi-turn conversation and uses them to provide an eco-travel recommendation.

The chatbot can collect and remember:

- Travel destination
- Travel dates
- Budget
- Sustainability preference

It also includes:

- Rasa NLU for intent and entity recognition
- Conversation state management using slots
- A custom Python action for eco-travel recommendations
- Fallback handling for unclear or unsupported messages
- A simple web-based chat interface
- A REST connection between the web interface and the Rasa server

The project is designed as an academic prototype for the **Eco-Travel Advisor – Conversational Agent for Sustainable Tourism Planning using the Rasa Platform** assignment.

---

## Main Technologies

- Python 3.10
- Rasa Open Source 3.6.21
- Rasa SDK 3.6.2
- HTML
- CSS
- JavaScript
- Rasa REST channel

---

## Project Structure

```text
eco-travel-chatbot/
│
├── actions/
│   ├── __init__.py
│   └── actions.py
│
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
│
├── web/
│   └── index.html
│
├── config.yml
├── credentials.yml
├── domain.yml
├── endpoints.yml
├── README.md
└── models/
```

---

# How to Run the Project

## 1. Extract the ZIP File

Extract the project ZIP file to a convenient location, for example:

```text
Desktop\eco-travel-chatbot
```

Open the extracted folder in VS Code or Command Prompt.

---

## 2. Check Python Version

This project should be run with **Python 3.10**.

Check the installed version:

```bash
py -3.10 --version
```

Expected output should be similar to:

```text
Python 3.10.11
```

> Rasa 3.6.21 is not compatible with Python 3.13, so Python 3.10 should be used.

---

## 3. Create a Virtual Environment

From inside the project folder, run:

```bash
py -3.10 -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

After activation, the terminal should begin with:

```text
(venv)
```

---

## 4. Install the Required Packages

Upgrade pip first:

```bash
python -m pip install --upgrade pip
```

Install Rasa:

```bash
pip install rasa==3.6.21
```

Install the Rasa SDK:

```bash
pip install rasa-sdk==3.6.2
```

Confirm the installation:

```bash
rasa --version
```

The important versions should be:

```text
Rasa Version: 3.6.21
Rasa SDK Version: 3.6.2
Python Version: 3.10.x
```

---

## 5. Train the Rasa Model

Run:

```bash
rasa train
```

Wait until a message similar to the following appears:

```text
Your Rasa model is trained and saved at 'models/...tar.gz'
```

---

# Running the Complete Application

The application uses three local services. Keep all three terminals open while using the chatbot.

## Terminal 1 — Start the Custom Action Server

Open a terminal in the project folder, activate the virtual environment and run:

```bash
venv\Scripts\activate
rasa run actions
```

Wait until:

```text
Action endpoint is up and running on http://0.0.0.0:5055
```

Keep this terminal open.

---

## Terminal 2 — Start the Rasa Server

Open another terminal, activate the virtual environment and run:

```bash
venv\Scripts\activate
rasa run --enable-api --cors "*"
```

Wait until:

```text
Rasa server is up and running.
```

The Rasa server runs on:

```text
http://localhost:5005
```

Keep this terminal open.

---

## Terminal 3 — Start the Web Interface

Open a third terminal and run:

```bash
venv\Scripts\activate
python -m http.server 8000 -d web
```

The terminal should display:

```text
Serving HTTP on 0.0.0.0 port 8000
```

Now open a web browser and visit:

```text
http://localhost:8000
```

The Eco-Travel Advisor web interface should appear.

---

# Example Conversation

A typical conversation is:

```text
User: I want to plan a trip

Bot: Great! Where would you like to travel?

User: I want to go to Paris

Bot: What are your travel dates?

User: 10 October to 15 October

Bot: What is your approximate travel budget?

User: My budget is 600 euros

Bot: How important is sustainability to you: low, medium, or high?

User: High sustainability
```

The system then provides an eco-travel recommendation using the collected information.

Example recommendation:

```text
Destination: Paris
Travel dates: 10 October to 15 October
Budget: 600 euros
Sustainability preference: high

Recommended transport: train or other low-carbon public transport
Accommodation: an eco-certified hotel
Activities: walking, cycling and local cultural activities
```

---

# Fallback Handling

If the chatbot does not understand a message, it provides a clarification response such as:

```text
Sorry, I didn't understand that. Could you please rephrase your request?
```

This prevents the chatbot from automatically treating an unrelated message as a valid travel preference.

---

# Important Configuration Files

## `data/nlu.yml`

Contains example user messages used for intent classification and entity extraction.

## `data/stories.yml`

Defines example multi-turn conversation paths.

## `data/rules.yml`

Defines fixed conversation rules such as trip-planning steps and fallback behaviour.

## `domain.yml`

Contains:

- Intents
- Entities
- Slots
- Bot responses
- Custom action declarations

## `actions/actions.py`

Contains the custom Python recommendation logic.

## `credentials.yml`

Enables the REST channel used by the web interface.

## `endpoints.yml`

Connects the Rasa server to the custom action server running on port 5055.

## `web/index.html`

Contains the browser-based Eco-Travel Advisor chat interface.

---

# Troubleshooting

## `rasa` command is not recognised

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Then try:

```bash
rasa --version
```

---

## Rasa cannot be installed

Check that Python 3.10 is being used:

```bash
python --version
```

If another version appears, create the environment explicitly with:

```bash
py -3.10 -m venv venv
```

---

## Webpage opens but the chatbot does not respond

Check that both servers are running:

```text
Rasa server:   http://localhost:5005
Action server: http://localhost:5055
```

Also confirm that `credentials.yml` contains:

```yaml
rest:
```

---

## Custom recommendation does not appear

Check that the action server is running:

```bash
rasa run actions
```

Also confirm that `endpoints.yml` contains:

```yaml
action_endpoint:
  url: "http://localhost:5055/webhook"
```

---

## Changes do not appear after editing training files

Retrain the model:

```bash
rasa train
```

Then restart the Rasa server.

---

# Quick Start Summary

After the first installation and training, the project can normally be started with these three commands in three separate terminals:

### Terminal 1

```bash
venv\Scripts\activate
rasa run actions
```

### Terminal 2

```bash
venv\Scripts\activate
rasa run --enable-api --cors "*"
```

### Terminal 3

```bash
venv\Scripts\activate
python -m http.server 8000 -d web
```

Then open:

```text
http://localhost:8000
```

---

## Notes

- Keep all three terminal windows open while using the application.
- Python 3.10 is recommended for compatibility with the Rasa version used in this project.
- If the project is moved to another computer, create a new virtual environment rather than relying on a copied `venv` folder.
