# 🌴 AI-Powered Vacation Planner
## Your Personal Travel Companion Powered by Amazon Bedrock

---

## 🎯 Project Overview

**AI-Powered Vacation Planner** is an intelligent, autonomous travel planning application that leverages cutting-edge artificial intelligence to transform the way people plan their dream vacations. By combining the power of **Amazon Bedrock's Nova Pro model** with **CrewAI's multi-agent orchestration** and **Amazon Bedrock AgentCore capabilities**, this application delivers personalized, comprehensive vacation itineraries tailored to individual preferences, budgets, and interests.

Gone are the days of spending countless hours researching destinations, comparing hotels, and planning daily activities. Our AI agents work collaboratively to handle the entire planning process—from initial research to creating detailed day-by-day itineraries—all while considering your unique travel style and requirements.

---

## 🚀 Project Objectives

### Primary Objective
Create an intuitive, AI-driven application that simplifies vacation planning by automating research, recommendation, and itinerary creation processes, enabling travelers to focus on what matters most: enjoying their trip.

### Specific Goals

1. **Democratize Expert Travel Planning**
   - Make professional-level vacation planning accessible to everyone
   - Eliminate the need for expensive travel agents
   - Provide 24/7 availability for instant vacation planning

2. **Personalization at Scale**
   - Deliver highly customized travel recommendations based on user preferences
   - Adapt to different budgets, from backpacker to luxury travel
   - Consider individual interests, dietary restrictions, and accessibility needs

3. **Comprehensive Information Aggregation**
   - Gather real-time information from multiple sources
   - Research destinations, attractions, restaurants, and accommodations
   - Provide up-to-date pricing, availability, and travel advisories

4. **Intelligent Itinerary Generation**
   - Create optimized day-by-day schedules
   - Balance activities with relaxation time
   - Consider geographical proximity and logical routing
   - Include realistic time estimates and transportation options

5. **User-Friendly Experience**
   - Offer both command-line and web-based interfaces
   - Provide interactive, conversational AI interactions
   - Enable easy modifications and refinements to plans

---

## 🏗️ Technical Architecture

Here it will be the architecture diagram...

---

## 🚀 Quick Start Guide

Get your AI-Powered Vacation Planner running in 5 minutes!

### Table of Contents
- [Prerequisites](#prerequisites)
- [Local Environment Setup](#local-environment-setup)
- [Project Setup](#project-setup)
- [Running the Project](#running-the-project)

### Prerequisites

Before you begin, ensure you have the following installed:

1. [VSCode](https://code.visualstudio.com/download)
2. [Python 3.11.9](https://www.python.org/downloads/) (Recommended: 3.10 to 3.13)
3. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
4. **AWS IAM Role**
   - Set up IAM role for AWS CLI with appropriate permissions
   - Ensure access to Amazon Bedrock models (verify from AWS Console)

### Local Environment Setup

#### Step 1: Clone the repository

Clone the repository in the desired local path.

#### Step 2: CrewAI Installation

Open the terminal and type the following:

1. **Install `uv`:**

```bash
pip install uv
```

2. **Run the following command to install CrewAI CLI:**

```bash
uv tool install crewai
```

3. **Update your shell:**

```bash
uv tool update-shell
```

4. **Verify that crewai is installed, run:**

```bash
uv tool list
```

### Project Setup

#### Configure Environment Variables

Create/update the `.env` file with the following:

```env
# AWS Credentials
AWS_PROFILE=my_aws_cli_profile
AWS_REGION_NAME=my_aws_cli_region_name

# Model Configuration
MODEL=bedrock/us.amazon.nova-pro-v1:0
EMBEDDING_MODEL=amazon.titan-embed-text-v2:0

# Serper API Key
SERPER_API_KEY=my_serper_api_key

# OpenAI API Key (if needed)
OPENAI_API_KEY=my_openai_api_key
```

**Important:** Ensure you have access to the Bedrock model from the AWS Console.

#### Install dependencies**

Go to the folder on which the project was cloned and type the following:

```bash
# Lock dependencies
crewai install

# Add additional required packages
uv add boto3
uv add streamlit
```

### Running the Project

**Option 1. Command Line Execution:**

```bash
crewai run
```

**Option 2. Streamlit UI:**

```bash
source .venv/bin/activate
streamlit run streamlit_ui.py
```

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact & Support

- **Project Maintainer:** Jano Camacho
- **LinkedIn:** https://www.linkedin.com/in/jano-camacho-vicente-96716893/
- **Support:** jandro.training@gmail.com

---

<div align="center">

### 🌟 Star this project if you find it useful!

**Let's make vacation planning accessible, enjoyable, and intelligent for everyone.**

Made with ❤️ using Amazon Bedrock, CrewAI, and Streamlit

</div>

---

## 🎯 Vision Statement

> "We envision a world where planning a vacation is as exciting as the trip itself—where artificial intelligence empowers everyone to explore new destinations with confidence, discover hidden gems with ease, and create unforgettable memories without the stress of planning."

---

- **Version:** 1.0.0  
- **Last Updated:** December 2025
- **Status:** Active Development 🚀