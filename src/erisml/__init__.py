__version__ = "0.1.0"

try:
    from erisml.ethics import (
        DEME,
        MoralTensor,
        EthicalFacts,
        Consequences,
        JusticeAndFairness,
        RightsAndDuties,
        Virtues,
        AutonomyAndAgency,
        EthicsModule,
        BaseEthicsModule,
        EthicalJudgement,
        StrategicLayer,
        NashResult,
        CooperativeLayer,
        GovernanceConfig,
        aggregate_judgements,
        select_option,
    )  # noqa: F401
except ImportError:
    # Fallback for setup.py
    DEME = None
    MoralTensor = None
    EthicalFacts = None
    Consequences = None
    JusticeAndFairness = None
    RightsAndDuties = None
    Virtues = None
    AutonomyAndAgency = None
    EthicsModule = None
    BaseEthicsModule = None
    EthicalJudgement = None
    StrategicLayer = None
    NashResult = None
    CooperativeLayer = None
    GovernanceConfig = None
    aggregate_judgements = None
    select_option = None

__all__ = [
    "DEME",
    "MoralTensor",
    "EthicalFacts",
    "Consequences",
    "JusticeAndFairness",
    "RightsAndDuties",
    "Virtues",
    "AutonomyAndAgency",
    "EthicsModule",
    "BaseEthicsModule",
    "EthicalJudgement",
    "StrategicLayer",
    "NashResult",
    "CooperativeLayer",
    "GovernanceConfig",
    "aggregate_judgements",
    "select_option",
]
