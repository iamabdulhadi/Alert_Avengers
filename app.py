
import streamlit as st
import sqlite3
import pandas as pd
from agent import get_sql_agent
import os

# Set up the page configuration
st.set_page_config(
    page_title="SQL Query App",
    page_icon="🔍",
    layout="wide"
)

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

if 'agent' not in st.session_state:
    st.session_state.agent = get_sql_agent("banking.db")

def main():
    st.title("🔍 Natural Language to SQL Query Converter")
    st.markdown("This application converts natural language requests into SQL queries for banking transaction data.")

    # Sidebar with database information
    with st.sidebar:
        st.header("Database Information")
        st.markdown("""
        **Tables Available:**
        - `customers`: Customer information
        - `accounts`: Account details
        - `transactions`: Transaction records
        - `branches`: Branch information
        """)
        
        # Show sample queries
        st.header("Sample Queries")
        sample_queries = [
            "How many customers are there?",
            "Show me all transactions for John Doe",
            "What is the total balance across all accounts?",
            "List all deposits made in January 2023"
        ]
        
        for query in sample_queries:
            if st.button(query, key=f"sample_{query}"):
                st.session_state.user_input = query

    # Main chat interface
    st.header("Ask Questions About Banking Data")
    
    # Display conversation history
    for i, (user_msg, bot_msg) in enumerate(st.session_state.conversation_history):
        with st.container():
            st.markdown(f"**You:** {user_msg}")
            st.markdown(f"**Assistant:** {bot_msg}")
            st.divider()

    # User input
    user_input = st.text_input(
        "Enter your question about the banking data:",
        key="user_input",
        placeholder="e.g., Show me all customers with savings accounts"
    )

    if st.button("Submit Query") and user_input:
        with st.spinner("Processing your query..."):
            try:
                # Get response from the agent
                response = st.session_state.agent.invoke({"input": user_input})
                bot_response = response['output']
                
                # Add to conversation history
                st.session_state.conversation_history.append((user_input, bot_response))
                
                # Display the latest response
                st.success("Query processed successfully!")
                st.markdown(f"**Your Question:** {user_input}")
                st.markdown(f"**Response:** {bot_response}")
                
                # Try to extract and display any tabular data
                try:
                    # Check if the response contains SQL results
                    conn = sqlite3.connect('banking.db')
                    
                    # This is a simple approach - in a production system, you'd want to 
                    # extract the actual SQL query from the agent's intermediate steps
                    if "SELECT" in bot_response.upper():
                        st.info("The agent generated and executed a SQL query to answer your question.")
                    
                    conn.close()
                except Exception as e:
                    pass  # Continue without showing SQL details
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please try rephrasing your question or check if the database is properly initialized.")

    # Clear conversation button
    if st.button("Clear Conversation"):
        st.session_state.conversation_history = []
        st.experimental_rerun()

    # Database viewer (for debugging/verification)
    with st.expander("View Database Tables (for verification)"):
        conn = sqlite3.connect('banking.db')
        
        table_names = ['customers', 'accounts', 'transactions', 'branches']
        selected_table = st.selectbox("Select table to view:", table_names)
        
        if selected_table:
            df = pd.read_sql_query(f"SELECT * FROM {selected_table}", conn)
            st.dataframe(df)
        
        conn.close()

if __name__ == "__main__":
    main()

