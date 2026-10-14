# ReviewRescue

> The Open-Source AI Reputation Copilot & Review Engine for Small Businesses
> Built for the Hacktoberfest 2026 (HF26) DEV Challenge Week 2: Side Hustle

ReviewRescue is a lightweight, zero-RAM CLI tool designed to help small businesses and freelance reputation managers turn Google Maps and Yelp customer reviews into high-converting customer retention and local SEO growth.

---

## The Side Hustle Problem

Over 30 million small businesses worldwide (restaurants, dental clinics, auto mechanics, contractors, boutique salons) depend on Google Maps and Yelp reviews for their daily revenue.
- 1-star reviews left unanswered destroy customer trust and decrease local walk-in traffic by up to 22%.
- 5-star reviews left without strategic keyword replies waste valuable local SEO ranking potential.
- Small business owners lack the time, energy, and diplomatic vocabulary to write calm de-escalation responses after a grueling 12-hour workday.

Freelance digital marketers charge between $150 and $300 per month per client to manage and reply to local reviews. ReviewRescue empowers any freelancer, agency owner, or solo founder to run a high-margin reputation management side hustle from a standard laptop with zero software subscription overhead.

---

## Features

- **Automated Rating & Sentiment Classification**: Automatically audits reviews and determines whether damage control or SEO amplification is required.
- **Conflict De-escalation Engine (1-2 Stars)**: Produces empathetic, calm, and non-defensive public replies that de-escalate public drama and transition dispute resolutions to private phone/email channels.
- **Local SEO Keyword Injection (4-5 Stars)**: Naturally weaves in targeted service keywords (e.g. "wood-fired pizza in downtown", "emergency pipe repair", "licensed pediatric dentist") to boost Google Maps local ranking.
- **Brand Tone Profiles**:
  - `warm`: Neighborhood cafes, bakeries, boutique shops, family practices.
  - `professional`: Medical clinics, law firms, accounting, B2B services.
  - `direct`: Plumbing, HVAC contractors, auto mechanics, emergency trades.
- **Internal Action Extraction**: Pinpoints the operational friction point (Wait Times, Staff Behavior, Product Quality, Billing) for internal staff remediation.
- **0 MB RAM Overhead**: Pure lightweight Python client with zero memory burden on low-spec hardware.

---

## Quick Start

### 1. Installation

```bash
git clone https://github.com/NICKSTER0506/Review-Rescue.git
cd Review-Rescue
pip install -r requirements.txt
```

### 2. Interactive Wizard Mode

```bash
python reviewrescue.py
```

Follow the guided terminal prompts to enter the business details, review text, and select your preferred tone.

### 3. Command Line Mode

```bash
# De-escalate a critical 1-star restaurant review
python reviewrescue.py --business "Trattoria Bella" --type "Italian Restaurant" --file demo_samples/angry_1star_review.txt --rating 1 --tone warm

# Boost local SEO keywords on a glowing 5-star plumbing review
python reviewrescue.py --business "Austin Pro Plumbing" --type "Plumbing Contractor" --file demo_samples/glowing_5star_review.txt --rating 5 --tone direct --keywords "burst pipe repair, licensed Austin plumber, 24/7 emergency"
```

---

## Architecture

```
Customer Review (Google Maps / Yelp / File / Direct Text)
     │
     ▼
Review Analyzer (Rating Detection & Operational Issue Extraction)
     │
     ▼
Prompt & Strategy Engine (De-escalation vs. SEO Keyword Amplification)
     │
     ▼
Open-Weight AI Inference (Llama-3.2 / Qwen-2.5 / Mistral)
     │
     ▼
Rich Terminal Dashboard & Formatted Public Response Card
```

---

## Why Open Innovation Matters

1. **Zero Marginal Operating Cost**: Proprietary cloud APIs charge ongoing token subscriptions that eat into small business service margins. By leveraging open-weight models (`Llama-3.2-3B-Instruct`, `Qwen-2.5-Coder`, `Mistral-7B`), a solo freelancer can service dozens of local businesses with 100% gross profit margins.
2. **Accessible on Budget Hardware**: Built and tested on a 6GB RAM laptop. Using a lightweight client harness against open inference endpoints ensures zero memory freezing or local hardware limitations.
3. **Customer Data Privacy**: Sensitive customer complaint details and internal business operational notes remain strictly within user-controlled workflows without vendor telemetry lock-in.
4. **Tone Customization without Moderation Pitfalls**: Proprietary model guardrails frequently misinterpret heated customer review text as policy violations. Open-weight models allow nuanced de-escalation of angry customer rants without unexpected API refusals.

---

## License

MIT License. Built for Hacktoberfest 2026.
