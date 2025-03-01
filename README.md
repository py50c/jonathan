# AI Illness Detector & Study Timer  

## Overview  
This project contains two Python programs:  

1. **AI Illness Detector** – A medical chatbot powered by **Google Gemini AI** that predicts illnesses from symptoms, provides **home remedies**, and asks follow-up questions like a doctor.  
2. **Study Timer with ASCII Art** – A countdown timer that visually displays time using **ASCII art** and alerts users when their study session ends.  

## Features  

### 🤖 **AI Illness Detector**  
- ✅ Predicts possible **illnesses** based on symptoms.  
- ✅ Requests at least **three symptoms** for accuracy.  
- ✅ Asks **follow-up questions** to refine the diagnosis.  
- ✅ Provides **home remedies** and **first aid tips**.  
- ✅ Uses **Google Gemini AI** for medical responses.  
- ✅ Customizable **color interface** using `rich`.  

### ⏳ **Study Timer**  
- ✅ Accepts **study duration** in minutes.  
- ✅ Displays real-time **ASCII countdown** using `art`.  
- ✅ Alerts users when time is up with **pyfiglet**.  
- ✅ Supports **continuous study sessions**.  

## Prerequisites  

- Python 3.7+  
- Required Packages:  
  ```sh
  pip install google-generativeai rich art pyfiglet colorama
