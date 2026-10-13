import json
p = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\project_data.json"
d = json.load(open(p, encoding="utf-8"))
OR = "openrouter/nvidia/nemotron-3-super-120b-a12b:free"
d["llm_provider"] = "openrouter"
d["model"] = "nvidia/nemotron-3-super-120b-a12b:free"
d["fallback_chain"] = [
    OR,
    "google_ai_studio/gemini-2.5-flash",
    "mistral/ministral-8b-latest",
]
d["agent_fallback_chains"] = {
    "chapter_writer": [OR, "google_ai_studio/gemini-2.5-flash", "mistral/ministral-8b-latest"],
    "editor": ["mistral/ministral-8b-latest", "google_ai_studio/gemini-2.5-flash"],
}
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("writer ->", d["llm_provider"], "/", d["model"])
