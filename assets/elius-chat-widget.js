/**
 * Elius Chat Widget
 * Add this script to your GitHub Pages site to enable the AI chatbot
 */

(function() {
  const WEBHOOK_URL = 'https://n8n.srv1311127.hstgr.cloud/webhook/elius-chat';

  // Styles
  const styles = `
    #elius-chat-container {
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 9999;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
    }

    #elius-chat-button {
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    #elius-chat-button:hover {
      transform: scale(1.1);
      box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }

    #elius-chat-button svg {
      width: 28px;
      height: 28px;
      fill: white;
    }

    #elius-chat-window {
      display: none;
      position: absolute;
      bottom: 80px;
      right: 0;
      width: 380px;
      height: 500px;
      background: #1a1a2e;
      border-radius: 16px;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
      flex-direction: column;
      overflow: hidden;
    }

    #elius-chat-window.open {
      display: flex;
    }

    #elius-chat-header {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    #elius-chat-header-avatar {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255,255,255,0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
    }

    #elius-chat-header-info h3 {
      margin: 0;
      font-size: 16px;
      font-weight: 600;
    }

    #elius-chat-header-info p {
      margin: 2px 0 0 0;
      font-size: 12px;
      opacity: 0.8;
    }

    #elius-chat-close {
      margin-left: auto;
      background: none;
      border: none;
      color: white;
      cursor: pointer;
      font-size: 24px;
      line-height: 1;
      opacity: 0.8;
    }

    #elius-chat-close:hover {
      opacity: 1;
    }

    #elius-chat-messages {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .elius-message {
      max-width: 85%;
      padding: 12px 16px;
      border-radius: 16px;
      font-size: 14px;
      line-height: 1.5;
    }

    .elius-message.bot {
      background: #2d2d44;
      color: #e0e0e0;
      align-self: flex-start;
      border-bottom-left-radius: 4px;
    }

    .elius-message.user {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      align-self: flex-end;
      border-bottom-right-radius: 4px;
    }

    .elius-message.typing {
      display: flex;
      gap: 4px;
      padding: 16px 20px;
    }

    .elius-message.typing span {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #667eea;
      animation: typing 1.4s infinite ease-in-out;
    }

    .elius-message.typing span:nth-child(2) { animation-delay: 0.2s; }
    .elius-message.typing span:nth-child(3) { animation-delay: 0.4s; }

    @keyframes typing {
      0%, 60%, 100% { transform: translateY(0); }
      30% { transform: translateY(-8px); }
    }

    #elius-chat-input-container {
      padding: 16px;
      background: #16162a;
      display: flex;
      gap: 10px;
    }

    #elius-chat-input {
      flex: 1;
      padding: 12px 16px;
      border: 1px solid #3d3d5c;
      border-radius: 24px;
      background: #1a1a2e;
      color: white;
      font-size: 14px;
      outline: none;
      transition: border-color 0.3s;
    }

    #elius-chat-input:focus {
      border-color: #667eea;
    }

    #elius-chat-input::placeholder {
      color: #666;
    }

    #elius-chat-send {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.2s;
    }

    #elius-chat-send:hover {
      transform: scale(1.05);
    }

    #elius-chat-send:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }

    #elius-chat-send svg {
      width: 20px;
      height: 20px;
      fill: white;
    }

    @media (max-width: 480px) {
      #elius-chat-window {
        width: calc(100vw - 40px);
        height: calc(100vh - 120px);
        bottom: 70px;
        right: -10px;
      }
    }
  `;

  // HTML template
  const template = `
    <div id="elius-chat-container">
      <div id="elius-chat-window">
        <div id="elius-chat-header">
          <div id="elius-chat-header-avatar">🤖</div>
          <div id="elius-chat-header-info">
            <h3>Elius</h3>
            <p>AI Assistant</p>
          </div>
          <button id="elius-chat-close">&times;</button>
        </div>
        <div id="elius-chat-messages">
          <div class="elius-message bot">
            Hi! I'm Elius, Dr. Attardo's AI assistant. Ask me about his experience, skills, publications, or anything else!
          </div>
        </div>
        <div id="elius-chat-input-container">
          <input type="text" id="elius-chat-input" placeholder="Ask about Elia's experience..." />
          <button id="elius-chat-send">
            <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
          </button>
        </div>
      </div>
      <button id="elius-chat-button">
        <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.17L4 17.17V4h16v12z"/><path d="M7 9h10v2H7zm0-3h10v2H7z"/></svg>
      </button>
    </div>
  `;

  // Initialize
  function init() {
    // Add styles
    const styleSheet = document.createElement('style');
    styleSheet.textContent = styles;
    document.head.appendChild(styleSheet);

    // Add HTML
    document.body.insertAdjacentHTML('beforeend', template);

    // Get elements
    const container = document.getElementById('elius-chat-container');
    const chatWindow = document.getElementById('elius-chat-window');
    const chatButton = document.getElementById('elius-chat-button');
    const closeButton = document.getElementById('elius-chat-close');
    const messagesContainer = document.getElementById('elius-chat-messages');
    const input = document.getElementById('elius-chat-input');
    const sendButton = document.getElementById('elius-chat-send');

    // Toggle chat
    chatButton.addEventListener('click', () => {
      chatWindow.classList.toggle('open');
      if (chatWindow.classList.contains('open')) {
        input.focus();
      }
    });

    closeButton.addEventListener('click', () => {
      chatWindow.classList.remove('open');
    });

    // Send message
    async function sendMessage() {
      const message = input.value.trim();
      if (!message) return;

      // Add user message
      addMessage(message, 'user');
      input.value = '';
      sendButton.disabled = true;

      // Show typing indicator
      const typingId = showTyping();

      try {
        const response = await fetch(WEBHOOK_URL, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: message }),
        });

        const data = await response.json();
        removeTyping(typingId);
        addMessage(data.response || data.output || 'Sorry, I could not process that request.', 'bot');
      } catch (error) {
        console.error('Chat error:', error);
        removeTyping(typingId);
        addMessage('Sorry, I encountered an error. Please try again later.', 'bot');
      }

      sendButton.disabled = false;
    }

    function addMessage(text, type) {
      const messageDiv = document.createElement('div');
      messageDiv.className = `elius-message ${type}`;
      messageDiv.textContent = text;
      messagesContainer.appendChild(messageDiv);
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function showTyping() {
      const typingDiv = document.createElement('div');
      typingDiv.className = 'elius-message bot typing';
      typingDiv.id = 'typing-' + Date.now();
      typingDiv.innerHTML = '<span></span><span></span><span></span>';
      messagesContainer.appendChild(typingDiv);
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
      return typingDiv.id;
    }

    function removeTyping(id) {
      const typingDiv = document.getElementById(id);
      if (typingDiv) typingDiv.remove();
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') sendMessage();
    });
  }

  // Start when DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
