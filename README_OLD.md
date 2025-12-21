# Bedrock AgentCore - Vacation Planner

A CrewAI-powered vacation planning application using Amazon Bedrock and Streamlit UI.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Virtual Environment Setup](#virtual-environment-setup)
- [Installation](#installation)
- [Project Setup](#project-setup)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Streamlit UI](#streamlit-ui)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have the following installed:

1. **VSCode**
   - Download: https://code.visualstudio.com/download

2. **Python 3.11.9** (Recommended: 3.10 to 3.13)
   - Download: https://www.python.org/downloads/

3. **AWS CLI**
   - Installation Guide: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

4. **AWS IAM Role**
   - Set up IAM role for AWS CLI with appropriate permissions
   - Ensure access to Amazon Bedrock models (verify from AWS Console)

## Virtual Environment Setup

It's recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects.

### Step 1: Install virtualenv

```bash
# Install virtualenv globally
pip install virtualenv
```

### Step 2: Create Virtual Environment

Navigate to your project directory and create a virtual environment:

```bash
# Create a virtual environment named '.venv'
virtualenv .venv
```

### Step 3: Activate Virtual Environment

**On Windows:**
```bash
# Command Prompt
.venv\Scripts\activate

# PowerShell
.venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

You should see `(.venv)` appear in your terminal prompt, indicating the virtual environment is active.

### Step 4: Install Packages from Requirements File

```bash
# Install all required packages from requirements.txt
pip install -r requirements.txt
```

### Step 5: Verify Installation

```bash
# List all installed packages
pip list
```

### Deactivating Virtual Environment

When you're done working on the project:

```bash
deactivate
```

## Project Setup

### 1. Configure Environment Variables

Create/update the `.env` file with the following:

```env
# AWS Credentials
AWS_REGION_NAME=us-west-2

# Model Configuration
MODEL=bedrock/us.amazon.nova-pro-v1:0
```

**Important:** Ensure you have access to the Bedrock model from the AWS Console.




.........3. Create Project............
crewai create crew vacation_planner
Select 8
Bedrock Model in .env  -----> Should have access to Model (Check from console)
Set Access Key, Secret Key, region-us.west-2
Update Agent and Task details in YAML
Add Tools to Agents in Crew.py 
Update Agent and Task details in Crew.py
Add input in main.py

...........Run the Project.....................
Lock dependencies --- > crewai install (uv lock file)
uv add boto3
Run Command --- > crewai run
............................................

.......5. UI Install - Streamlit..........

.......# Changes in case of errors using Amazon Bedrock....https://docs.crewai.com/en/concepts/agents..........

#1 Imports
from crewai import LLM

#2 Define and plug in the values for LLM and SerperDev
serper_dev_tool=SerperDevTool(api_key='9951ae7963727fd049c8ba2bfff0f8a6799cf2c7')
llm = LLM (model='bedrock/us.amazon.nova-pro-v1:0') # Donot add region attribute(not supported by Bedrock Nova as it is cross region)

#3 @agents - for both Agnets
llm=llm
.....................................

.........Add Streamlit UI......
# Add streamlit file.py
# Import class VacationPlanner() in Streamlit file
uv add streamlit

.....Run Streamlit on Local...........
# Run Streamlit File ---- > Streamlit run StreamlitUI.py
