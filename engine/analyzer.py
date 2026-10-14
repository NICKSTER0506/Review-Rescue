"""
Review Analyzer: Sentiment, Rating, and Operational Extraction
"""

import re
from typing import Dict, Any

class ReviewAnalyzer:
    @staticmethod
    def analyze(review_text: str, rating: int = None) -> Dict[str, Any]:
        """
        Analyzes customer review text and determines sentiment, tone strategy, and key friction points.
        """
        text_lower = review_text.lower()
        
        # Detect rating if not provided
        inferred_rating = rating
        if inferred_rating is None:
            if any(w in text_lower for w in ["terrible", "worst", "rude", "horrible", "disaster", "never again", "waste", "scam"]):
                inferred_rating = 1
            elif any(w in text_lower for w in ["poor", "slow", "cold", "mediocre", "disappointed"]):
                inferred_rating = 2
            elif any(w in text_lower for w in ["okay", "average", "decent", "fine"]):
                inferred_rating = 3
            elif any(w in text_lower for w in ["good", "nice", "friendly", "helpful"]):
                inferred_rating = 4
            else:
                inferred_rating = 5

        # Classify strategy
        if inferred_rating <= 2:
            strategy = "de_escalation"
            priority = "HIGH (Damage Control)"
        elif inferred_rating == 3:
            strategy = "neutral_recovery"
            priority = "MEDIUM (Service Refinement)"
        else:
            strategy = "seo_amplification"
            priority = "STANDARD (Community Growth)"

        # Extract potential operational pain points
        issues = []
        if any(w in text_lower for w in ["wait", "slow", "forever", "line", "hour", "delay"]):
            issues.append("Wait Times / Speed of Service")
        if any(w in text_lower for w in ["rude", "attitude", "ignored", "server", "waiter", "staff", "manager"]):
            issues.append("Staff Behavior / Customer Service")
        if any(w in text_lower for w in ["cold", "undercooked", "burnt", "dirty", "taste", "quality", "broken"]):
            issues.append("Product / Food Quality")
        if any(w in text_lower for w in ["expensive", "overpriced", "bill", "charged", "refund"]):
            issues.append("Pricing & Billing Clarity")

        if not issues:
            issues = ["General Customer Experience"]

        return {
            "rating": inferred_rating,
            "strategy": strategy,
            "priority": priority,
            "issues": issues,
            "char_count": len(review_text)
        }
