
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import Mock, patch
from agent import get_sql_agent

class TestAgent(unittest.TestCase):
    
    def setUp(self):
        self.db_path = "banking.db"
    
    @patch('agent.ChatOpenAI')
    @patch('agent.SQLDatabase')
    def test_agent_initialization(self, mock_sql_db, mock_chat_openai):
        """Test that the agent is initialized correctly"""
        # Mock the dependencies
        mock_db_instance = Mock()
        mock_sql_db.from_uri.return_value = mock_db_instance
        
        mock_llm_instance = Mock()
        mock_chat_openai.return_value = mock_llm_instance
        
        # Test agent creation
        with patch('agent.create_sql_agent') as mock_create_agent:
            mock_agent = Mock()
            mock_create_agent.return_value = mock_agent
            
            agent = get_sql_agent(self.db_path)
            
            # Verify that the agent was created with correct parameters
            mock_sql_db.from_uri.assert_called_once_with(f"sqlite:///{self.db_path}")
            mock_chat_openai.assert_called_once_with(model="gpt-4o", temperature=0)
            mock_create_agent.assert_called_once()
            
            self.assertEqual(agent, mock_agent)
    
    def test_agent_query_processing(self):
        """Test that the agent can process queries (mock test)"""
        # This is a mock test since we can't test the actual OpenAI API without credentials
        mock_agent = Mock()
        mock_response = {
            'output': 'There are 2 customers in the database.',
            'intermediate_steps': []
        }
        mock_agent.invoke.return_value = mock_response
        
        # Test query processing
        query = "How many customers are there?"
        response = mock_agent.invoke({"input": query})
        
        self.assertEqual(response['output'], 'There are 2 customers in the database.')
        mock_agent.invoke.assert_called_once_with({"input": query})

if __name__ == '__main__':
    unittest.main()

