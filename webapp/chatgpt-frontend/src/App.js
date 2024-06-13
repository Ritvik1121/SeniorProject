import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (input.trim()) {
      const userMessage = { sender: 'user', text: input };
      setMessages([...messages, userMessage]);

      try {
        const response = await axios.post('http://localhost:5000/chat', {
          message: input,
        });

        const botMessage = { sender: 'bot', text: response.data.response };
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      } catch (error) {
        const botMessage = { sender: 'bot', text: 'Error communicating with server' };
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      }
      setInput('');
    }
  };

  return (
    <div className="App">
      <h1 className="title">MedLearnAI</h1>  
      
      <div className="chat-container">
        <div className="messages">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;

