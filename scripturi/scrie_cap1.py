import time
import typer
typer.confirm = lambda *a, **k: True
import libriscribe.main as m
m.typer.confirm = lambda *a, **k: True

from libriscribe.agents.project_manager import ProjectManagerAgent

pm = ProjectManagerAgent(llm_client=None)
pm.load_project_data("leah_si_lara")
pkb = pm.project_knowledge_base
pkb.llm_provider = "google_ai_studio"
pkb.model = "gemini-2.5-flash"
# OpenRouter slugs 404 under the google provider — clear them, pacing handles limits.
pkb.fallback_chain = []
pkb.agent_fallback_chains = {}
pm.initialize_llm_client(pkb.llm_provider, pkb.model)

# Pacer: Gemini free tier here allows ~5 req/min. Sleep 15s before every call.
_orig = pm.llm_client.generate_content
def paced(prompt, max_tokens=2000, **kw):
    time.sleep(15)
    return _orig(prompt, max_tokens=max_tokens, **kw)
pm.llm_client.generate_content = paced
for agent in pm.agents.values():
    if getattr(agent, "llm_client", None) is pm.llm_client:
        pass  # agents share the same client instance
print(f"provider={pkb.llm_provider} model={pkb.model}", flush=True)
pm.write_and_review_chapter(1)
pm.checkpoint()
print("CAPITOLUL 1 GATA", flush=True)
