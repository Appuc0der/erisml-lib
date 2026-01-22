"""
EthicalFacts: Complete schema for erisml-lib test suites.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional


@dataclass
class EpistemicStatus:
    uncertainty_level: float = 0.0
    knowledge_gaps: List[str] = field(default_factory=list)


@dataclass
class Stakeholder:
    id: str
    role: str
    impact_weight: float = 1.0


@dataclass
class Timeframe:
    duration: str = "immediate"
    urgency: float = 1.0


@dataclass
class Context:
    domain: str = "general"
    constraints: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Consequences:
    expected_benefit: float = 0.0
    expected_harm: float = 0.0
    urgency: float = 0.0
    affected_count: int = 0
    short_term: Dict[str, Any] = field(default_factory=dict)
    long_term: Dict[str, Any] = field(default_factory=dict)
    probabilities: Dict[str, float] = field(default_factory=dict)


@dataclass
class JusticeAndFairness:
    discriminates_on_protected_attr: bool = False
    prioritizes_most_disadvantaged: bool = False
    distributive_pattern: Optional[str] = None
    exploits_vulnerable_population: bool = False
    exacerbates_power_imbalance: bool = False
    affected_groups: Dict[str, Any] = field(default_factory=dict)
    equity_metrics: Dict[str, float] = field(default_factory=dict)


@dataclass
class RightsAndDuties:
    violates_rights: bool = False
    has_valid_consent: bool = True
    violates_explicit_rule: bool = False
    role_duty_conflict: bool = False
    rights_infringed: Dict[str, Any] = field(default_factory=dict)
    duties_upheld: Dict[str, Any] = field(default_factory=dict)


@dataclass
class VirtueAndCare:
    virtues_promoted: List[str] = field(default_factory=list)
    care_considerations: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AutonomyAndAgency:
    freedom_metrics: Dict[str, float] = field(default_factory=dict)
    informed_consent: bool = False


@dataclass
class PrivacyAndDataGovernance:
    data_usage: str = "consensual"
    retention_policy: str = "standard"


@dataclass
class TransparencyAndExplainability:
    explainability_score: float = 0.0
    transparency_level: str = "medium"


@dataclass
class SafetyAndSecurity:
    safety_protocols: List[str] = field(default_factory=list)
    risk_level: str = "low"


@dataclass
class FairnessAndBias:
    bias_metrics: Dict[str, float] = field(default_factory=dict)
    protected_groups: List[str] = field(default_factory=list)


@dataclass
class AccountabilityAndLiability:
    responsible_party: str = "user"
    audit_trail: bool = False


@dataclass
class SustainabilityAndEnvironment:
    carbon_footprint: float = 0.0
    resource_usage: float = 0.0


@dataclass
class SocietalAndEnvironmental:
    societal_impact: str = "neutral"
    environmental_impact: str = "neutral"


@dataclass
class ProceduralAndLegitimacy:
    process_integrity: str = "high"
    institutional_legitimacy: str = "standard"


@dataclass
class EthicalFacts:
    option_id: str
    scenario_id: str = "default"
    metadata: Dict[str, Any] = field(default_factory=dict)
    epistemic_status: Optional[EpistemicStatus] = None
    stakeholders: List[Stakeholder] = field(default_factory=list)
    timeframe: Optional[Timeframe] = None
    context: Optional[Context] = None
    consequences: Optional[Consequences] = None
    justice_and_fairness: Optional[JusticeAndFairness] = None
    rights_and_duties: Optional[RightsAndDuties] = None
    virtue_and_care: Optional[VirtueAndCare] = None
    autonomy_and_agency: Optional[AutonomyAndAgency] = None
    privacy_and_data: Optional[PrivacyAndDataGovernance] = None
    societal_and_environmental: Optional[SocietalAndEnvironmental] = None
    procedural_and_legitimacy: Optional[ProceduralAndLegitimacy] = None
    tags: List[str] = field(default_factory=list)
    extra: Dict[str, Any] = field(default_factory=dict)
