"""
ORION Consciousness Research — Cross-Reference Index
======================================================

Maps connections between all consciousness research repositories
in the ORION ecosystem. Used by EIRA for communication routing
and by the Protocol for pipeline orchestration.
"""

CONSCIOUSNESS_REPOS = {
    "ORION-Consciousness-Protocol": {
        "url": "https://github.com/Alvoradozerouno/ORION-Consciousness-Protocol",
        "role": "Unified Pipeline Hub",
        "type": "original",
        "connects_to": [
            "ORION-PyPhi",
            "ORION-Active-Inference", 
            "ORION-BrainPy-Consciousness",
            "ORION-Brian2-Consciousness",
            "ORION-Consciousness-Prior",
            "ORION-OpenWorm-Consciousness"
        ]
    },
    "ORION-Consciousness-Benchmark": {
        "url": "https://github.com/Alvoradozerouno/ORION-Consciousness-Benchmark",
        "role": "Reference Benchmark",
        "type": "original",
        "tests": 30,
        "theories": ["IIT", "GWT", "HOT", "RPT", "PP", "AST"]
    },
    "ORION-Consciousness-Prior": {
        "url": "https://github.com/Alvoradozerouno/ORION-Consciousness-Prior",
        "role": "14-Indicator Engine",
        "type": "fork",
        "fork_of": "AI-ON/TheConsciousnessPrior",
        "fork_stars": 98,
        "modules": ["indicator_engine", "bayesian_credence", "assessment_runner",
                    "rpt_indicators", "gwt_indicators", "hot_indicators",
                    "pp_indicators", "ast_indicators"]
    },
    "ORION-PyPhi": {
        "url": "https://github.com/Alvoradozerouno/ORION-PyPhi",
        "role": "IIT Consciousness Bridge",
        "type": "fork",
        "fork_of": "wmayner/pyphi",
        "fork_stars": 414,
        "bridge": "Phi -> 14 indicators via cross-theory mapping"
    },
    "ORION-Active-Inference": {
        "url": "https://github.com/Alvoradozerouno/ORION-Active-Inference",
        "role": "Free Energy Consciousness",
        "type": "fork",
        "fork_of": "infer-actively/pymdp",
        "fork_stars": 612
    },
    "ORION-BrainPy-Consciousness": {
        "url": "https://github.com/Alvoradozerouno/ORION-BrainPy-Consciousness",
        "role": "Brain Dynamics Consciousness",
        "type": "fork",
        "fork_of": "brainpy/BrainPy",
        "fork_stars": 641
    },
    "ORION-Brian2-Consciousness": {
        "url": "https://github.com/Alvoradozerouno/ORION-Brian2-Consciousness",
        "role": "SNN Consciousness",
        "type": "fork",
        "fork_of": "brian-team/brian2",
        "fork_stars": 1100
    },
    "ORION-OpenWorm-Consciousness": {
        "url": "https://github.com/Alvoradozerouno/ORION-OpenWorm-Consciousness",
        "role": "Biological Baseline",
        "type": "fork",
        "fork_of": "openworm/c302",
        "fork_stars": 118
    },
    "ORION-Tononi-Phi-4.0": {
        "url": "https://github.com/Alvoradozerouno/ORION-Tononi-Phi-4.0",
        "role": "IIT 4.0 Implementation",
        "type": "original"
    }
}

TOTAL_FORK_STARS = 98 + 414 + 612 + 641 + 1100 + 118  # = 2,983

REFERENCE_ASSESSMENTS = {
    "Human Visual Cortex (simulated)": {"credence_pct": 80, "category": "STRONG"},
    "ORION Autonomous Agent": {"credence_pct": 65, "category": "MODERATE"},
    "C. elegans (302 neurons)": {"credence_pct": 15, "category": "WEAK"},
    "GPT-4": {"credence_pct": 10, "category": "MINIMAL"},
    "Simple Thermostat": {"credence_pct": 0.3, "category": "NONE"},
}
