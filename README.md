# ErisML Library

ErisML is a modeling language for **governed, foundation-model-enabled agents**
operating in pervasive computing environments (homes, hospitals, campuses,
factories, vehicles, etc.).

ErisML provides a single, machine-interpretable and human-legible representation of:

- **(i)** environment state and dynamics  
- **(ii)** agents and their capabilities and beliefs  
- **(iii)** intents and utilities  
- **(iv)** norms (permissions, obligations, prohibitions, sanctions)  
- **(v)** multi-agent strategic interaction  

We define a concrete syntax, a formal grammar, denotational semantics, and
an execution model that treats norms as first-class constraints on action,
introduces longitudinal safety metrics such as **Norm Violation Rate (NVR)** and
**Alignment Drift Velocity (ADV)**, and supports compilation to planners,
verifiers, and simulators.

On top of this, ErisML now includes an **ethics-only decision layer (DEME)** for
democratically-governed ethical reasoning.

---

![CI](https://github.com/ahb-sjsu/erisml-lib/actions/workflows/ci.yaml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)
![License](https://img.shields.io/badge/License-AGI--HPC%20Responsible%20AI-blue.svg)

---

## Overview

ErisML has two tightly-related layers:

1. **Core ErisML governance layer**

   - Formal language for:
     - Environment models and dynamics
     - Agents, capabilities, and beliefs
     - Intents, utilities, and payoffs
     - Norms (permissions, obligations, prohibitions, sanctions)
     - Multi-agent strategic interaction
   - Execution model:
     - Norm gating and constraint filtering on actions
     - Longitudinal safety metrics (e.g., NVR, ADV)
     - Adapters for planners, verifiers, and simulators

2. **DEME (Democratically Governed Ethics Modules)** — ethics-only decision layer

   - A structured **`EthicalFacts`** abstraction that captures ethically-salient
     context (consequences, rights/duties, fairness, autonomy, privacy,
     societal/environmental impact, procedural legitimacy, epistemic status).
   - Pluggable **`EthicsModule`** implementations that perform **purely normative**
     reasoning over `EthicalFacts` (never raw domain data).
   - A **democratic governance** layer that aggregates multiple
     `EthicalJudgement` outputs using configurable stakeholder weights, hard
     vetoes, and lexical priority layers.
   - A **DEME profile** format (`DEMEProfileV03`) for versioned governance
     configurations (e.g., `hospital_service_robot_v1`).
   - A **narrative CLI** that elicits stakeholder values via scenarios and
     produces DEME profiles.
   - A **MCP server** (`erisml.ethics.interop.mcp_deme_server`) so any
     MCP-compatible agent can call DEME tools (`deme.list_profiles`,
     `deme.evaluate_options`, `deme.govern_decision`).

Together, ErisML + DEME support **norm-governed, ethics-aware agents** that can
be inspected, audited, and configured by multiple stakeholders.

---

## What’s in this Repository?

This repository contains a production-style Python library with:

- **Project layout & tooling**
  - Modern `src/` layout and `pyproject.toml`
  - GitHub Actions CI using:
    - **Python 3.12** (via `actions/setup-python@v5`)
    - **Black 24.4.2** for formatting checks
    - **Ruff** for linting
    - **Taplo** for TOML validation
    - **Pytest** for tests
    - A **DEME smoke test** that runs the triage ethics demo

- **Core ErisML implementation**
  - Language grammar (Lark)
  - Typed AST (Pydantic)
  - Core IR (environment, agents, norms)
  - Runtime engine with:
    - Norm gate
    - Longitudinal safety metrics (e.g., NVR, ADV)
  - PettingZoo adapter for multi-agent RL
  - PDDL/Tarski adapter stub for planning

- **Ethics / DEME subsystem**
  - Structured **`EthicalFacts`** and ethical dimensions:
    - Consequences and welfare
    - Rights and duties
    - Justice and fairness
    - Autonomy and agency
    - Privacy and data governance
    - Societal and environmental impact
    - Virtue and care
    - Procedural legitimacy
    - Epistemic status (confidence, known-unknowns, data quality)
  - **`EthicalJudgement`** and **`EthicsModule`** interface
  - Governance configuration and aggregation:
    - `GovernanceConfiguration` / `DEMEProfileV03`
    - `DecisionOutcome` and helpers (e.g., `select_option`)
    - Stakeholder weights, hard vetoes, lexical priority layers, tie-breaking
  - Example modules:
    - **Case Study 1 triage module** (`CaseStudy1TriageEM`)
    - A small **rights-first** EM
    - Additional simple EMs for safety, fairness, etc. (in progress)

- **Executable examples**
  - **TinyHome** norm-gated environment
  - **Triage ethics demo** combining multiple EMs under governance
  - Experimental **ethical dialogue CLI** that interactively builds
    DEME profiles from narrative scenarios

- A basic test suite

---

## Quickstart (Windows / PowerShell)

    # PowerShell
    cd erisml-lib

    python -m venv .venv
    .\.venv\Scripts\activate

    pip install -e ".[dev]"

    pytest

On macOS / Linux, the equivalent would be:

    # Bash (macOS / Linux)
    cd erisml-lib

    python -m venv .venv
    source .venv/bin/activate

    pip install -e ".[dev]"

    pytest

This will run the core test suite **and** the DEME smoke test.

---

## Running the DEME Triage Demo

The DEME triage demo shows how multiple Ethics Modules and a governance
configuration interact to produce an ethically-justified decision.

Typical usage (exact paths/scripts may vary slightly depending on how you install):

    # From repo root, inside your virtualenv
    pytest -k triage  # run only the triage-related tests

or, if you have a convenience script:

    python -m erisml.examples.triage_demo

This will:

1. Construct `EthicalFacts` for a small set of triage options.  
2. Evaluate them via multiple EMs (e.g., triage, fairness, rights-first).  
3. Run the governance layer to select a recommended option and log the rationale.

---

## DEME MCP Server (Experimental)

The DEME subsystem can also be exposed as an **MCP server**:

    MCP Server ID: erisml.ethics.interop.mcp_deme_server

It provides (at minimum) the following MCP tools:

- `deme.list_profiles` — enumerate available DEME profiles and metadata  
- `deme.evaluate_options` — run Ethics Modules on candidate options given
  their `EthicalFacts`  
- `deme.govern_decision` — aggregate EM outputs and select an option under a
  chosen profile

Any MCP-compatible client (e.g., agent frameworks, IDE copilots, or custom
agents) can use this server to add ethical oversight to planning and action
selection. See the `erisml/ethics/interop/` directory and examples for details.

---

## Writing Your Own Ethics Module (EM)

ErisML’s DEME subsystem is designed so that **any stakeholder** can plug in their
own ethical perspective as a small, testable module.

An EM is just a Python object that implements the `EthicsModule` protocol (or
subclasses `BaseEthicsModule`) and **only looks at `EthicalFacts`**, never at raw
domain data (ICD codes, sensor traces, etc.).

### 1. Basic structure

A minimal EM looks like this:

    from dataclasses import dataclass

    from erisml.ethics import (
        EthicalFacts,
        EthicalJudgement,
        EthicsModule,
    )


    @dataclass
    class SimpleSafetyEM(EthicsModule):
        """
        Example EM that only cares about expected harm.

        verdict mapping (based on normative_score):
          [0.8, 1.0] -> strongly_prefer
          [0.6, 0.8) -> prefer
          [0.4, 0.6) -> neutral
          [0.2, 0.4) -> avoid
          [0.0, 0.2) -> forbid
        """

        em_name: str = "simple_safety"
        stakeholder: str = "safety_officer"

        def judge(self, facts: EthicalFacts) -> EthicalJudgement:
            # Use only EthicalFacts – no direct access to ICD codes, sensors, etc.
            harm = facts.consequences.expected_harm

            # Simple scoring: less harm -> higher score
            score = 1.0 - harm

            # Map score to a discrete verdict
            if score >= 0.8:
                verdict = "strongly_prefer"
            elif score >= 0.6:
                verdict = "prefer"
            elif score >= 0.4:
                verdict = "neutral"
            elif score >= 0.2:
                verdict = "avoid"
            else:
                verdict = "forbid"

            reasons = [
                f"Expected harm={harm:.2f}, computed safety score={score:.2f}.",
            ]

            metadata = {
                "harm": harm,
                "score_components": {"harm_component": score},
            }

            return EthicalJudgement(
                option_id=facts.option_id,
                em_name=self.em_name,
                stakeholder=self.stakeholder,
                verdict=verdict,
                normative_score=score,
                reasons=reasons,
                metadata=metadata,
            )

From there, you can:

- Add additional features (e.g., use `facts.epistemic_status` to downweight
  low-confidence scenarios).  
- Compose multiple EMs and wire them into a `GovernanceConfiguration` / DEME
  profile.  
- Write unit tests to ensure your EM behaves as intended over important
  corner cases.

---

## Relationship Between ErisML and DEME

- **ErisML** handles:
  - World modeling (environments, agents, capabilities, norms)
  - Strategic interaction and norm-governed behavior
  - Longitudinal safety metrics and simulation/integration with RL/planning

- **DEME** handles:
  - Ethics-only reasoning over `EthicalFacts`
  - Multi-stakeholder governance (multiple EMs)
  - Configurable profiles and decision aggregation
  - Structured audit logs and explainable rationales

In many deployments:

- ErisML provides the **normative environment model** and **constraint gate**.  
- Domain services convert raw state/plan information into `EthicalFacts`.  
- DEME evaluates candidate options and recommends (or vetoes) actions.  

---

## License

This project is distributed under the **AGI-HPC Responsible AI License v1.0 (DRAFT)**.

Very short summary (non-legal, see `LICENSE` for full text):

- ✅ You **may** use, modify, and distribute the software for **non-commercial
  research, teaching, and academic work**, subject to attribution and inclusion
  of the license.
- 🚫 **Commercial use** and **autonomous deployment in high-risk domains**
  (e.g., vehicles, healthcare, critical infrastructure, financial systems,
  defense, large-scale platforms) are **not granted by default** and require a
  separate written agreement or explicit written permission from the Licensor.
- ✅ If you use ErisML/DEME in autonomous or AGI-like systems, you must implement
  **Safety and Governance Controls**, including:
  - Explicit normative constraints / environment modeling (e.g., ErisML or
    equivalent),
  - Pluralistic, auditable ethical decision modules (e.g., DEME-style EMs),
  - Logging and audit trails with tamper-evident protections,
  - Safe fallback behaviors and reasonable testing.
- 🚫 You **must not** use the software to build:
  - Weapons systems designed primarily to harm or destroy,
  - Coercive surveillance or systems aimed at suppressing fundamental rights,
  - Systems that intentionally or recklessly cause serious harm or large-scale
    rights violations.
- ✅ Attribution is required. A suitable notice is:

  > “This project incorporates components from the AGI-HPC architecture  
  > (Andrew H. Bond et al., San José State University), used under the  
  > AGI-HPC Responsible AI License v1.0.”

For full details, **this README is not legal advice** — please see the
[`LICENSE`](./LICENSE) file and consult legal counsel before adopting this
license for production or commercial use.

---

## Citation & Contact

If you use ErisML or DEME in academic work, please cite the corresponding
papers and/or this repository.

Project / license contact: **agi.hpc@gmail.com**
