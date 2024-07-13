## Python LangChainの自作LLMchainを、Next.js・ReactのチャットAIアプリにしたい！【NLUX】 

[**→　Zennの記事本文はこちら**](https://zenn.dev/vel/articles/daaf85d203b258). 

--- 

### セットアップ

バックエンドとフロントエンドのセットアップは, 別々のターミナルで行ってください. 

#### バックエンド

LLMは高速安価な[**Groq**](https://groq.com)のAPIを用いて呼び出しています. [**→ API Keyの設定**](https://console.groq.com/keys)が必要です. 

```
$ cd backend
$ pip install -r requirements.txt
$ export GROQ_API_KEY=<your-api-key-here>
$ python server.py
```

ブラウザで [**`http://127.0.0.1:8083/chat/playground/`**](http://127.0.0.1:8083/chat/playground/) を開くと, 動作確認できます. 

#### フロントエンド

```
$ cd frontend
$ npm install
$ npm run dev
```

ブラウザで [**`http://localhost:5173`**](http://localhost:5173) を開くと, 動作確認できます. 
