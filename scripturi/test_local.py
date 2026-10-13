import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
os.environ["OPENROUTER_BASE_URL"] = "http://localhost:11434/v1"
os.environ["OPENROUTER_API_KEY"] = "ollama-local"
os.environ["OPENROUTER_MODEL"] = "qwen2.5:7b"
sys.path.insert(0, r"C:\Users\bizoi\AppData\Roaming\Python\Python314\site-packages")
from libriscribe.utils.llm_client import LLMClient
c = LLMClient("openrouter")
out = c.generate_content("Reply with exactly: LOCAL OK", max_tokens=50)
print("LOCAL REPLY:", out[:200])
