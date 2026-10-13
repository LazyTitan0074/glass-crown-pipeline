import typer
typer.confirm = lambda *a, **k: True
import libriscribe.main as m
m.typer.confirm = lambda *a, **k: True

from libriscribe.agents.project_manager import ProjectManagerAgent

pm = ProjectManagerAgent(llm_client=None)
pm.load_project_data("leah_si_lara")
pkb = pm.project_knowledge_base
pm.initialize_llm_client(pkb.llm_provider, pkb.model)
print(f"provider={pkb.llm_provider} model={pkb.model} fallback={pkb.fallback_chain}", flush=True)
# style polish for ch1 (failed earlier on quota), then full ch2
try:
    pm.edit_style(1)
except Exception as e:
    print("style ch1 failed:", str(e)[:200], flush=True)
pm.write_and_review_chapter(2)
pm.checkpoint()
print("GATA CH2 + STYLE CH1", flush=True)
