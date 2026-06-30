from pathlib import Path

ROOT = Path(__file__).parent

content = {
    "biography/faculty_bio.md": """# Faculty Biography

Jake Macdonald is a Hybrid Systems Architect, founder of the HACR Hybrid Observatory, and an independent researcher based in Kelowna, British Columbia, Canada.

His work focuses on AI governance, observability, systems resilience, and boundary-based approaches to complex engineering systems. Through open-source software and interdisciplinary research, he develops practical frameworks for accountability, recoverability, consequence analysis, and governance in intelligent systems.
""",

    "biography/executive_summary.md": """# Executive Summary

This portfolio documents an active independent research program focused on observability and governability in complex systems.

The work includes open-source software, research frameworks, computational investigations, teaching material, and published research outputs connected through ORCID, GitHub, and Zenodo.
""",

    "software/hacr.md": """# HACR Hybrid Observatory

Repository:

https://github.com/macess888-cmyk/HACR_Hybrid_Observatory

The HACR Hybrid Observatory is an open-source research platform focused on observability, governance boundaries, accountability, consequence analysis, recoverability, and resilient system architectures.

Status: Active research platform.
""",

    "publications/orcid.md": """# Research Profiles and Publications

ORCID:

https://orcid.org/0009-0000-6513-7049

Selected Works:

1. Geometric Foundations of Invariant Corridors and Governance: A Unified Framework with Empirical Validation v3.3  
DOI: 10.5281/zenodo.18822553  
Contributors: Jake Macdonald; Massimo Medesani

2. OpenGoldenRatio (OGR) v0.1 — Containment-First Multi-Agent Governance Protocol  
DOI: 10.5281/zenodo.18969396  
Contributor: Jake Macdonald
""",

    "teaching/teaching_statement.md": """# Teaching Statement

Teaching emphasizes critical thinking, evidence-based systems reasoning, explicit assumptions, reproducibility, and responsible communication of uncertainty.

Students are encouraged to distinguish observation from interpretation, evidence from decision-making, and exploratory frameworks from established results.

Proposed teaching areas include AI governance, fail-safe and fail-closed architectures, observability in complex systems, smart infrastructure, intelligent transportation systems, and human decision-making in autonomous systems.
"""
}

for path, text in content.items():
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(text, encoding="utf-8")

print("Portfolio content updated.")