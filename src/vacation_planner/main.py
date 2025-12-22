#!/usr/bin/env python
"""
AI-Powered Vacation Planner - Main Entry Point

This module provides the command-line interface for the vacation planner,
handling user inputs and orchestrating the multi-agent crew to deliver
professional-level vacation planning.
"""

import sys
import warnings

from datetime import datetime
from vacation_planner.crew import VacationPlanner
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def get_comprehensive_inputs():
    """
    Gather comprehensive user inputs for personalized vacation planning.
    
    This function democratizes expert travel planning by making it accessible
    through simple, conversational inputs while gathering all necessary details
    for comprehensive planning.
    
    Returns:
        dict: Comprehensive vacation planning inputs
    """
    print("\n" + "="*70)
    print("🌴 AI-POWERED VACATION PLANNER 🌴")
    print("Professional-Level Travel Planning for Everyone")
    print("="*70 + "\n")
    
    inputs = {}
    
    # Destination preferences
    print("📍 DESTINATION PREFERENCES")
    print("-" * 70)
    
    inputs['topic'] = input("Destination name (e.g., Lima, London, etc): ").strip() or "Lima"
    
    destination_types = [
        "beach", "mountain", "city", "cultural", "adventure", 
        "relaxation", "nature", "historical", "mixed"
    ]
    print(f"Available types: {', '.join(destination_types)}")
    inputs['destination_type'] = input("Destination type (e.g., beach, mountain, city): ").strip() or "beach"
    
    # Duration
    print("\n📅 TRIP DURATION")
    print("-" * 70)
    inputs['duration'] = input("Trip duration (e.g., 7 days, 2 weeks): ").strip() or "7 days"
    
    # Travel dates
    print("\n🗓️  TRAVEL DATES")
    print("-" * 70)
    inputs['travel_dates'] = input("Preferred travel dates (e.g., June 2025, Summer 2025): ").strip() or "flexible"
    
    # Personal interests
    print("\n🎯 INTERESTS & PREFERENCES")
    print("-" * 70)
    print("Examples: snorkeling, local cuisine, museums, hiking, photography, nightlife")
    inputs['interests'] = input("Your interests: ").strip() or "local cuisine, sightseeing, relaxation"
    
    # Travel style
    print("\n🎨 TRAVEL STYLE")
    print("-" * 70)
    styles = ["relaxed", "moderate", "packed", "luxury", "budget-friendly", "adventurous"]
    print(f"Available styles: {', '.join(styles)}")
    inputs['travel_style'] = input("Travel style: ").strip() or "moderate"
    
    # Summary
    print("\n" + "="*70)
    print("📋 PLANNING SUMMARY")
    print("="*70)
    for key, value in inputs.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print("="*70 + "\n")
    
    confirm = input("Proceed with vacation planning? (yes/no): ").strip().lower()
    if confirm not in ['yes', 'y']:
        print("Planning cancelled. Goodbye!")
        sys.exit(0)
    
    return inputs

def run():
    """
    Run the vacation planner crew with user inputs.
    
    This function orchestrates the entire vacation planning process,
    coordinating multiple AI agents to deliver a comprehensive,
    professional-level vacation plan.
    """
    print("\n🚀 Initializing AI Vacation Planner...")
    
    # Get user inputs
    inputs = get_comprehensive_inputs()
    
    # inputs = {
    #     'topic': 'Lima',
    #     'destination_type': 'beach',
    #     'duration': '7 days',
    #     'travel_dates': 'June 2025',
    #     'interests': 'snorkeling, local cuisine, relaxation, photography',
    #     'dietary_restrictions': 'none',
    #     'accessibility_needs': 'none',
    #     'travel_style': 'moderate'
    # }
    
    print("\n🤖 Activating AI Agents...")
    print("  ✓ Vacation Research Specialist")
    print("  ✓ Vacation Planning Architect")
    
    print("\n⏳ Planning your perfect vacation... This may take 5-10 minutes.")
    print("   The agents are working hard to:")
    print("   • Research destinations and gather real-time information")
    print("   • Create optimized day-by-day itineraries")
    print("   • Add authentic local experiences")
    print("   • Optimize your budget for maximum value")

    try:
        # Initialize and run the crew
        result = VacationPlanner().crew().kickoff(inputs=inputs)
        
        print("\n" + "="*70)
        print("✅ VACATION PLAN COMPLETED!")
        print("="*70 + "\n")
        
        # Save results
        output_file = f"vacation_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(output_file, 'w') as f:
            f.write(str(result))
        
        print(f"📄 Full plan saved to: {output_file}")
        
        print("\n" + "="*70)
        print("🎉 Your personalized vacation plan is ready!")
        print("="*70 + "\n")
        
        # Display summary
        print(result)
    except Exception as e:
        print(f"\n❌ Error during planning: {str(e)}")
        print("\nPlease check your:")
        print("  • AWS credentials and Bedrock access")
        print("  • Internet connection")
        print("  • Environment variables (.env file)")
        sys.exit(1)
        # raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for improved performance.
    
    Args:
        n_iterations: Number of training iterations
        filename: File to save training results
    """
    inputs = {
        'topic': 'Lima',
        'destination_type': 'beach',
        'duration': '7 days',
        'travel_dates': 'flexible',
        'interests': 'water sports, local cuisine',
        'travel_style': 'moderate'
    }
    
    try:
        VacationPlanner().crew().train(
            n_iterations=int(sys.argv[1]) if len(sys.argv) > 1 else 2,
            filename=sys.argv[2] if len(sys.argv) > 2 else "training_results.pkl",
            inputs=inputs
        )
        
        print("\n✅ Training completed successfully!")
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay a specific task execution.
    
    Args:
        task_id: ID of the task to replay
    """
    try:
        task_id = sys.argv[1] if len(sys.argv) > 1 else None
        if not task_id:
            print("❌ Please provide a task_id to replay")
            print("Usage: crewai replay <task_id>")
            sys.exit(1)
        
        VacationPlanner().crew().replay(task_id=task_id)
        print(f"\n✅ Replayed task {task_id} successfully!")
    except Exception as e:
        raise Exception(f"Replay error: {e}")

def test():
    """
    Test the crew execution.
    
    Args:
        n_iterations: Number of test iterations
        model_name: Model to use for testing
    """
    inputs = {
        'topic': 'Lima',
        'destination_type': 'city',
        'duration': '5 days',
        'travel_dates': 'Spring 2025',
        'interests': 'museums, food tours, architecture',
        'travel_style': 'relaxed'
    }
    
    try:
        VacationPlanner().crew().test(
            n_iterations=int(sys.argv[1]) if len(sys.argv) > 1 else 3,
            openai_model_name=sys.argv[2] if len(sys.argv) > 2 else 'gpt-4',
            inputs=inputs
        )
        print("\n✅ Testing completed successfully!")
    except Exception as e:
        raise Exception(f"Testing error: {e}")
