import { AiChat } from '@nlux/react';
import { useChatAdapter } from '@nlux/langchain-react';
import '@nlux/themes/nova.css';

export default function App() {
  return (<AiChat adapter={useChatAdapter({
    url: 'http://127.0.0.1:8083/chat',
    // Host IP address, port number, and path name must match to the server
  })} />);
};
