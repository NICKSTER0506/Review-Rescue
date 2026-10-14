"""
Reputation Responder: Prompt Engineering & Response Formulation
Generates tailored public responses, SEO injections, and internal action items.
"""

from typing import Dict, Any, Tuple

TONE_PROFILES = {
    "warm": {
        "name": "Warm & Community-Focused",
        "desc": "Great for neighborhood cafes, bakeries, boutique shops, and family practices.",
        "instruction": "Adopt an affectionate, highly personal, and humble tone. Emphasize neighborhood roots and community gratitude."
    },
    "professional": {
        "name": "Corporate & Polished",
        "desc": "Ideal for medical clinics, law offices, real estate agencies, and B2B services.",
        "instruction": "Maintain a calm, authoritative, polite, and strictly professional tone. Avoid slang, uphold company dignity and client privacy."
    },
    "direct": {
        "name": "Direct & Solution-Oriented",
        "desc": "Best for plumbers, auto repair shops, contractors, and home trade services.",
        "instruction": "Be straightforward, accountable, and action-oriented. Focus on swift resolution and dependable craftsmanship."
    }
}

class ReputationResponder:
    @staticmethod
    def build_prompts(
        business_name: str,
        business_type: str,
        review_text: str,
        rating: int,
        tone: str = "warm",
        keywords: str = ""
    ) -> Tuple[str, str]:
        """
        Builds the system and user prompt for open-weight models.
        """
        tone_data = TONE_PROFILES.get(tone, TONE_PROFILES["warm"])
        
        system_prompt = (
            "You are ReviewRescue, an expert AI customer reputation manager and local SEO strategist for small businesses.\n"
            "Your job is to craft responses to public Google Maps and Yelp reviews that:\n"
            "1. Protect the business's public reputation and maintain customer trust.\n"
            "2. For negative reviews (1-2 stars): De-escalate with genuine empathy, take accountability, never get defensive or argumentative, and move the resolution offline (provide [Manager Contact Placeholder]).\n"
            "3. For positive reviews (4-5 stars): Express genuine gratitude, boost customer retention, and naturally weave in local SEO service keywords without sounding robotic.\n"
            "4. For mixed reviews (3 stars): Validate the pros, address the cons gracefully, and invite them back to experience improvements.\n\n"
            f"TONE PROFILE: {tone_data['name']}\n"
            f"TONE INSTRUCTION: {tone_data['instruction']}\n\n"
            "FORMATTING GUIDELINE:\n"
            "- First section: '### Primary Response (Ready to Post)' -> The exact public response to paste on Google/Yelp.\n"
            "- Second section: '### Alternative Short Response' -> A punchy 2-sentence version for quick SMS or Instagram replies.\n"
            "- Third section: '### Internal Action Items' -> 2-3 specific bullet points for staff/management to prevent this issue or double down on what worked.\n"
            "- Do not include robotic preamble (e.g., 'Sure, here is your output:'). Jump straight into the sections."
        )

        user_prompt = (
            f"BUSINESS NAME: {business_name}\n"
            f"BUSINESS TYPE: {business_type}\n"
            f"STAR RATING: {rating}/5 stars\n"
            f"LOCAL SEO KEYWORDS TO WEAVE IN: {keywords if keywords else 'standard industry services'}\n\n"
            f"CUSTOMER REVIEW TEXT:\n\"{review_text}\""
        )

        return system_prompt, user_prompt
