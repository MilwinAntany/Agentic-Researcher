# 🧑‍🔬 Agentic Researcher – End-to-End AI-Powered Research Assistant

## 📌 Two-Line Overview

An AI-powered research assistant that automates topic exploration, question generation, and intelligent synthesis using Large Language Models (LLMs).
Built with modular architecture to support multiple providers like **Ollama** for lightweight and efficient inference.

---

## 🔍 Project Overview

This project provides an **end-to-end agentic research framework** where users can input a topic, and the system automatically generates research questions, reasons through them, and produces structured insights. It is designed to demonstrate how LLMs can assist in **automated research, planning, and knowledge synthesis**.

---

## ✨ Features

* 📖 Automated research planning and question generation
* 🧠 LLM-powered reasoning and intelligent synthesis
* 🔄 Modular system with interchangeable LLM providers (e.g., Ollama, OpenAI)
* ⚡ Lightweight and efficient execution with models like `phi3:mini`
* 📂 Structured output for further analysis and reporting

---

## 🏗️ System Modules

1. **Input Handler** – accepts user research topics
2. **Planner** – generates structured research questions using LLMs
3. **Reasoner** – processes each question and extracts insights
4. **LLM Utility** – abstraction layer for connecting to Ollama or other providers
5. **Orchestrator (Main Script)** – coordinates the entire workflow end-to-end

---

## 🖼️ System Architecture

```
User Input → Planner → LLM (Ollama/OpenAI) → Reasoner → Synthesized Research Output
```

---

## 🛠️ Technologies Used

* **Programming Language**: Python 3.11
* **Libraries**: Ollama Client, argparse, JSON, logging
* **Models**: phi3\:mini, mistral, or other Ollama-supported models
* **IDE**: PyCharm / VSCode

---

## 💻 Hardware Requirements

* Minimum 8 GB RAM (16 GB recommended for smooth inference)
* CPU: Multi-core (GPU optional, depending on model size)
* Disk Space: 5–10 GB (for model storage and dependencies)
* OS: Windows / macOS / Linux

---

## 🧪 Testing

* ✅ Unit testing for planner, reasoner, and utils modules
* ✅ Integration testing with Ollama LLM
* ✅ Error handling (e.g., model not found, API issues)
* ✅ End-to-end testing by running sample topics like *AI in healthcare diagnostics*

---

## 📊 Results

* Successfully generates **relevant research questions** for any given topic
* Provides **structured insights** using lightweight LLM models
* Demonstrates **modular integration** of different AI providers (OpenAI → Ollama migration tested)

---

## 🚀 Future Enhancements

* Add **web-based UI** for user interaction
* Expand to support **multiple simultaneous topics**
* Enhance reasoning with **multi-agent collaboration**
* Store research results in a **searchable knowledge base**
* Integrate with **vector databases (e.g., Pinecone, ChromaDB)** for long-term memory

---

## 📚 References

* [Ollama Documentation](https://ollama.ai)
* [LangChain](https://www.langchain.com/)
* [OpenAI API](https://platform.openai.com/)
* Research papers on **Agentic AI Systems** and **LLM Planning & Reasoning**

---
## 👨‍💻 Developed By
 
- Contact: antanymilwin@gmail.com
