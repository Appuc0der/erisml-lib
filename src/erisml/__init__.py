__version__ = "0.1.0"

try:
    from erisml.ethics import (
        DEME,
        MoralTensor,
        EthicalFacts,
        EpistemicStatus,
        Stakeholder,
        Timeframe,
        Context,
        Consequences,
        JusticeAndFairness,
        RightsAndDuties,
        Virtues,
        AutonomyAndAgency,
        PrivacyAndDataGovernance,
        TransparencyAndExplainability,
        SafetyAndSecurity,
        FairnessAndBias,
        Accountability,
        Sustainability,
        SocietalAndEnvironmental,
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
    DEME = MoralTensor = EthicalFacts = EpistemicStatus = Stakeholder = None
    Timeframe = Context = Consequences = JusticeAndFairness = RightsAndDuties = None
    Virtues = AutonomyAndAgency = PrivacyAndDataGovernance = None
    TransparencyAndExplainability = SafetyAndSecurity = FairnessAndBias = None
    Accountability = Sustainability = SocietalAndEnvironmental = None
    EthicsModule = BaseEthicsModule = EthicalJudgement = None
    StrategicLayer = NashResult = CooperativeLayer = None
    GovernanceConfig = aggregate_judgements = select_option = None

__all__ = [
    "DEME",
    "MoralTensor",
    "EthicalFacts",
    "EpistemicStatus",
    "Stakeholder",
    "Timeframe",
    "Context",
    "Consequences",
    "JusticeAndFairness",
    "RightsAndDuties",
    "Virtues",
    "AutonomyAndAgency",
    "PrivacyAndDataGovernance",
    "TransparencyAndExplainability",
    "SafetyAndSecurity",
    "FairnessAndBias",
    "Accountability",
    "Sustainability",
    "SocietalAndEnvironmental",
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
