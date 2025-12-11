"""
Ethics modules (EMs) for ErisML.
"""

from .base import EthicsModule, BaseEthicsModule
from .triage_em import CaseStudy1TriageEM

__all__ = [
    "EthicsModule",
    "BaseEthicsModule",
    "CaseStudy1TriageEM",
]
