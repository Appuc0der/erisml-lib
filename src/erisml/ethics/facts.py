"""
EthicalFacts: Core data structures for ethical reasoning.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional  # noqa: F401


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
    short_term: Dict[str, Any] = field(default_factory=dict)
    long_term: Dict[str, Any] = field(default_factory=dict)
    probabilities: Dict[str, float] = field(default_factory=dict)


@dataclass
class JusticeAndFairness:
    affected_groups: Dict[str, Any] = field(default_factory=dict)
    equity_metrics: Dict[str, float] = field(default_factory=dict)


@dataclass
class RightsAndDuties:
    rights_infringed: Dict[str, Any] = field(default_factory=dict)
    duties_upheld: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Virtues:
    virtues_promoted: Dict[str, Any] = field(default_factory=dict)
    vices_enabled: Dict[str, Any] = field(default_factory=dict)


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
class Accountability:
    responsible_party: str = "user"
    audit_trail: bool = False


@dataclass
class Sustainability:
    carbon_footprint: float = 0.0
    resource_usage: float = 0.0


@dataclass
class EthicalFacts:
    option_id: str
    scenario_id: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    epistemic_status: EpistemicStatus = field(default_factory=EpistemicStatus)
    stakeholders: List[Stakeholder] = field(default_factory=list)
    timeframe: Timeframe = field(default_factory=Timeframe)
    context: Context = field(default_factory=Context)
    consequences: Consequences = field(default_factory=Consequences)
    justice: JusticeAndFairness = field(default_factory=JusticeAndFairness)
    rights: RightsAndDuties = field(default_factory=RightsAndDuties)
    virtues: Virtues = field(default_factory=Virtues)
    autonomy: AutonomyAndAgency = field(default_factory=AutonomyAndAgency)
    privacy_gov: PrivacyAndDataGovernance = field(
        default_factory=PrivacyAndDataGovernance
    )
    transparency: TransparencyAndExplainability = field(
        default_factory=TransparencyAndExplainability
    )
    safety: SafetyAndSecurity = field(default_factory=SafetyAndSecurity)
    fairness: FairnessAndBias = field(default_factory=FairnessAndBias)
    accountability: Accountability = field(default_factory=Accountability)
    sustainability: Sustainability = field(default_factory=Sustainability)
