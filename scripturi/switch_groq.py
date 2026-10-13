import json
p = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\project_data.json"
d = json.load(open(p, encoding="utf-8"))
d["llm_provider"] = "bedrock_mantle"
d["model"] = "openai/gpt-oss-120b"
d["fallback_chain"] = [
    "bedrock_mantle/openai/gpt-oss-120b",
    "bedrock_mantle/openai/gpt-oss-20b",
    "mistral/ministral-8b-latest",
    "google_ai_studio/gemini-2.5-flash",
]
d["agent_fallback_chains"] = {
    "chapter_writer": [
        "bedrock_mantle/openai/gpt-oss-120b",
        "mistral/ministral-8b-latest",
    ],
    "editor": [
        "bedrock_mantle/openai/gpt-oss-120b",
        "mistral/ministral-8b-latest",
        "google_ai_studio/gemini-2.5-flash",
    ],
}
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("writer ->", d["llm_provider"], "/", d["model"])
