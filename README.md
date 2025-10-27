# ✈️ AI Trip Planner

## Project Overview

The **AI Trip Planner** is a sophisticated travel planning agent designed to generate comprehensive, data-driven itineraries. Leveraging an advanced agentic workflow, it integrates real-time data on weather, prices, reservations, and locations to provide users with a detailed and accurate plan for their next trip.

This project showcases expertise in **Agentic Workflow Orchestration**, **Real-time Data Integration**, and **Performance Tracking** using industry-standard tools.

***

## ✨ Key Features

* **Agentic Workflow Orchestration:** Built with **LangGraph** to manage specialized worker agents (e.g., Weather Agent, Finance Agent) ensuring accurate, sequential tool utilization for focused data gathering.
* **Real-time Data Integration:** Uses dynamic function calling (tools) to check live data, including current weather, hotel prices, and restaurant availability.
* **Performance Monitoring:** Integrates **LangSmith** for end-to-end tracing, debugging, and experimentation to continuously improve agent performance and reliability.
* **Modular and Clean Code:** Structured for high maintainability, separating routing logic, agent definitions, and tool functions.
* **Comprehensive Output:** Generates a detailed plan including two itinerary options (Standard Tourist & Off-Beat Explorer), cost breakdowns, accommodation estimates, and local transport options.

***

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Agent Framework** | **LangChain** | Core library for building LLM applications. |
| **Orchestration** | **LangGraph** | Used for defining and managing the stateful, cyclic workflow graph. |
| **LLM Inference** | **GROQ** | High-speed LLM inference provider for rapid agent decision-making. |
| **Observability** | **LangSmith** | Essential for debugging, tracing calls, and tracking performance metrics. |
| **Frontend** | **Streamlit** | Simple, interactive web application interface for the agent. |
| **Backend/API** | **FastAPI** | Provides the scalable REST API endpoint for the agent service. |
| **Package Manager** | **`uv`** | Ultra-fast package installer and resolver. |

***

## 🚀 Setup & Installation

Follow these steps to get the AI Trip Planner running locally.

### Prerequisites

* Python 3.12+

Create a file named **`.env`** in the root directory of the project and populate it with your keys.

```dotenv
# --- LLM and Agent Framework Keys ---
GROQ_API_KEY=your_groq_key_here
LANGSMITH_API_KEY=your_langsmith_key_here

# --- Real-Time Data and Search Keys ---
GOOGLE_API_KEY=your_google_search_key_here
GPLACE_API_KEY=your_google_places_key_here
FOURSQUARE_API_KEY=your_foursquare_key_here
TAVILY_API_KEY=your_tavily_key_here
OPENWEATHERMAP_API_KEY=your_openweathermap_key_here

# --- Financial and Exchange Rate Keys ---
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
EXCHANGE_RATE_API_KEY=your_exchange_rate_key_here

### 1. Environment Setup

It is highly recommended to use the `uv` package manager for ultra-fast setup.

```bash
# Install uv (if you don't have it)
pip install uv

# Create and activate a virtual environment
uv venv

# Activate the environment (Linux/macOS)
source .venv/bin/activate
# Activate the environment (Windows)
# .venv\Scripts\activate

# Install dependencies from the requirements file
uv pip install -r requirements.txt

# Run the FastAPI backend service
# --reload is for developer hot-reloading
uvicorn main:app --reload --port 8000

# Run the Streamlit frontend (in a separte cmd)
streamlit run streamlit_app.py