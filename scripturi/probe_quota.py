import json, os, sys, urllib.request
sys.stdout.reconfigure(encoding="utf-8")

def load_env(p):
    d = {}
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if line and "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            d[k.strip()] = v.strip().strip("'\"")
    return d

env = load_env(r"C:\Users\bizoi\libriscribe-roman\.env")
out = {}

def probe(name, fn):
    try:
        out[name] = fn()
    except Exception as e:
        out[name] = "DOWN: " + str(e)[:160]

def google(model):
    def go():
        import urllib.request
        key = env.get("GOOGLE_AI_STUDIO_API_KEY", "")
        body = json.dumps({"contents": [{"parts": [{"text": "Reply with OK."}]}], "generationConfig": {"maxOutputTokens": 5}}).encode()
        req = urllib.request.Request(
            "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent?key=%s" % (model, key),
            data=body, headers={"Content-Type": "application/json"})
        r = urllib.request.urlopen(req, timeout=30)
        j = json.load(r)
        return "OK: " + json.dumps(j.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "?"))[:60]
    return go

def openai_compat(name, url, key, model):
    def go():
        body = json.dumps({"model": model, "messages": [{"role": "user", "content": "Reply with OK."}], "max_tokens": 5, "temperature": 0}).encode()
        req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json", "Authorization": "Bearer " + key})
        r = urllib.request.urlopen(req, timeout=30)
        j = json.load(r)
        return "OK: " + str(j.get("choices", [{}])[0].get("message", {}).get("content", "?"))[:60]
    return go

def openrouter_quota():
    key = env.get("OPENROUTER_API_KEY", "")
    req = urllib.request.Request("https://openrouter.ai/api/v1/auth/key", headers={"Authorization": "Bearer " + key})
    r = urllib.request.urlopen(req, timeout=30)
    j = json.load(r)["data"]
    return "limit=%s usage=%s free=%s" % (j.get("limit"), j.get("usage"), j.get("limit") is None)

probe("gemini-flash-lite", google("gemini-2.5-flash-lite"))
probe("gemini-flash", google("gemini-2.5-flash"))
probe("openrouter-quota", openrouter_quota)
probe("mistral-8b", openai_compat("m8b", "https://api.mistral.ai/v1/chat/completions", env.get("MISTRAL_API_KEY", ""), "ministral-8b-latest"))
probe("mistral-small", openai_compat("ms", "https://api.mistral.ai/v1/chat/completions", env.get("MISTRAL_API_KEY", ""), "mistral-small-latest"))
probe("groq-20b", openai_compat("g20", "https://api.groq.com/openai/v1/chat/completions", env.get("BEDROCK_MANTLE_API_KEY", ""), "openai/gpt-oss-20b"))
probe("groq-120b", openai_compat("g120", "https://api.groq.com/openai/v1/chat/completions", env.get("BEDROCK_MANTLE_API_KEY", ""), "openai/gpt-oss-120b"))

for k, v in out.items():
    print(k, "=>", v)
