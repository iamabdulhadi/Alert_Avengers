#!/usr/bin/env python3
"""
Setup script for SQL Query App
This script initializes the database and installs dependencies
"""

import subprocess
import sys
import os
from database import init_db

def install_dependencies():
    """Install required Python packages"""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing dependencies: {e}")
        return False
    return True

def setup_database():
    """Initialize the SQLite database with sample data"""
    print("Setting up database...")
    try:
        init_db()
        print("✓ Database initialized successfully")
    except Exception as e:
        print(f"✗ Error setting up database: {e}")
        return False
    return True

def create_env_file():
    """Create a sample .env file"""
    print("Creating environment file...")
    env_content = """# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE=https://api.openai.com/v1

# Note: Replace 'your_openai_api_key_here' with your actual OpenAI API key
"""
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✓ .env file created successfully")
        print("  Please update the .env file with your OpenAI API key")
    except Exception as e:
        print(f"✗ Error creating .env file: {e}")
        return False
    return True

def main():
    """Main setup function"""
    print("=== SQL Query App Setup ===")
    print()
    
    success = True
    
    # Install dependencies
    if not install_dependencies():
        success = False
    
    print()
    
    # Setup database
    if not setup_database():
        success = False
    
    print()
    
    # Create environment file
    if not create_env_file():
        success = False
    
    print()
    
    if success:
        print("🎉 Setup completed successfully!")
        print()
        print("Next steps:")
        print("1. Update the .env file with your OpenAI API key")
        print("2. Run the application with: streamlit run app.py")
    else:
        print("❌ Setup encountered errors. Please check the output above.")
        sys.exit(1)

if __name__ == "__main__":
    main()

