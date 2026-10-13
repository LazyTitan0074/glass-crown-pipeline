import json
p = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\project_data.json"
d = json.load(open(p, encoding="utf-8"))
d["agent_fallback_chains"] = {
    "chapter_writer": ["mistral/ministral-8b-latest", "openrouter/qwen2.5:7b"],
    "editor": ["openrouter/qwen2.5:7b", "mistral/ministral-8b-latest",
               "google_ai_studio/gemini-2.5-flash"],
}
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("editor chain ->", d["agent_fallback_chains"]["editor"])
