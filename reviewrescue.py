#!/usr/bin/env python3
"""
ReviewRescue — Local Business Review & Reputation Copilot
Built for Hacktoberfest 2026 (HF26) DEV Challenge Week 2: Side Hustle
"""

import sys
import os
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.markdown import Markdown
from rich.table import Table
from rich import box

from engine.llm_client import OpenAIEngine
from engine.analyzer import ReviewAnalyzer
from engine.responder import ReputationResponder, TONE_PROFILES

console = Console()

BANNER = r"""[bold cyan]
  _____            _                 _____                             
 |  __ \          (_)               |  __ \                            
 | |__) |_____   ___  _____      __ | |__) |___  ___  ___ _   _  ___  
 |  _  // _ \ \ / / |/ _ \ \ /\ / / |  _  // _ \/ __|/ __| | | |/ _ \ 
 | | \ \  __/\ V /| |  __/\ V  V /  | | \ \  __/\__ \ (__| |_| |  __/ 
 |_|  \_\___| \_/ |_|\___| \_/\_/   |_|  \_\___||___/\___|\__,_|\___| 
[/bold cyan]"""

def print_header():
    console.print(BANNER)
    console.print(
        "[bold white]Local Business Reputation Copilot & Review Engine[/bold white] | "
        "[bold green]0 MB RAM Overhead[/bold green] | "
        "[bold yellow]Open-Source AI Core[/bold yellow]\n"
    )

def interactive_wizard():
    print_header()
    console.print("[bold cyan]Customer Review Assistant (Interactive Mode)[/bold cyan]\n")

    # 1. Business Info
    business_name = Prompt.ask("[bold yellow]Business Name[/bold yellow]", default="Luigi's Pizzeria")
    business_type = Prompt.ask("[bold yellow]Business Category[/bold yellow]", default="Italian Restaurant & Takeout")
    keywords = Prompt.ask("[bold yellow]Local SEO Keywords (comma-separated, optional)[/bold yellow]", default="fresh wood-fired pizza, pasta in downtown, catering")

    # 2. Review Text
    console.print("\n[bold yellow]Paste the customer review (Google Maps, Yelp, or TripAdvisor):[/bold yellow]")
    review_text = Prompt.ask(">")
    if not review_text.strip():
        console.print("[red]Review text cannot be empty.[/red]")
        sys.exit(1)

    # 3. Rating
    rating_input = Prompt.ask("[bold yellow]Customer Star Rating (1-5, press Enter to auto-detect)[/bold yellow]", default="auto")
    if rating_input.lower() == "auto":
        analysis = ReviewAnalyzer.analyze(review_text)
        rating = analysis["rating"]
        console.print(f"[dim]Auto-detected rating: {rating} stars ({analysis['priority']})[/dim]")
    else:
        try:
            rating = int(rating_input)
            rating = max(1, min(5, rating))
        except ValueError:
            rating = 3

    # 4. Tone
    console.print("\n[bold cyan]Select Brand Tone:[/bold cyan]")
    for k, v in TONE_PROFILES.items():
        console.print(f" • [bold yellow]{k}[/bold yellow]: {v['name']} — [dim]{v['desc']}[/dim]")
    tone = Prompt.ask("\nChoose Tone", choices=list(TONE_PROFILES.keys()), default="warm")

    # 5. Process
    process_and_display(business_name, business_type, review_text, rating, tone, keywords)

def process_and_display(business_name: str, business_type: str, review_text: str, rating: int, tone: str, keywords: str):
    analysis = ReviewAnalyzer.analyze(review_text, rating)
    
    # Overview Table
    table = Table(title="Review Audit Summary", box=box.ROUNDED, header_style="bold cyan")
    table.add_column("Property", style="bold white", width=18)
    table.add_column("Details", style="yellow")
    
    table.add_row("Business", f"{business_name} ({business_type})")
    table.add_row("Rating", f"{rating} / 5 Stars")
    table.add_row("Strategy", f"{analysis['strategy'].upper()} — {analysis['priority']}")
    table.add_row("Friction Points", ", ".join(analysis["issues"]))
    table.add_row("Tone Selected", TONE_PROFILES.get(tone, {}).get("name", tone))
    
    console.print(table)
    console.print("")

    system_prompt, user_prompt = ReputationResponder.build_prompts(
        business_name=business_name,
        business_type=business_type,
        review_text=review_text,
        rating=rating,
        tone=tone,
        keywords=keywords
    )

    with console.status("[bold green]Generating strategic public response using Open-Source AI...[/bold green]", spinner="dots"):
        engine = OpenAIEngine()
        response_text = engine.generate_response(system_prompt, user_prompt)

    console.print(
        Panel(
            Markdown(response_text),
            title=f"[bold green]ReviewRescue Strategy & Copy for {business_name}[/bold green]",
            border_style="cyan",
            padding=(1, 2)
        )
    )

    console.print("[bold yellow]Tip:[/bold yellow] Copy the primary response directly to Google Business Profile or Yelp manager dashboard.\n")

def main():
    parser = argparse.ArgumentParser(description="ReviewRescue — AI Reputation & Review Responder for Local Businesses")
    parser.add_argument("--business", "-b", type=str, help="Business name (e.g. 'Blue Harbor Dental')")
    parser.add_argument("--type", "-t", type=str, help="Business category (e.g. 'Dental Clinic')")
    parser.add_argument("--review", "-r", type=str, help="Customer review text")
    parser.add_argument("--file", "-f", type=str, help="File containing review text")
    parser.add_argument("--rating", type=int, choices=[1, 2, 3, 4, 5], help="Star rating (1 to 5)")
    parser.add_argument("--tone", choices=list(TONE_PROFILES.keys()), default="warm", help="Response tone profile")
    parser.add_argument("--keywords", "-k", type=str, default="", help="Local SEO keywords to weave into positive replies")

    args = parser.parse_args()

    # Launch interactive wizard if no review argument provided
    if not args.review and not args.file:
        interactive_wizard()
        return

    # CLI flag execution
    review_content = ""
    if args.file and os.path.isfile(args.file):
        with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
            review_content = f.read().strip()
    elif args.review:
        review_content = args.review.strip()

    if not review_content:
        console.print("[red]Error: Please provide review content via --review or --file[/red]")
        sys.exit(1)

    b_name = args.business or "Local Business"
    b_type = args.type or "Service Provider"
    
    if args.rating:
        rating = args.rating
    else:
        rating = ReviewAnalyzer.analyze(review_content)["rating"]

    print_header()
    process_and_display(b_name, b_type, review_content, rating, args.tone, args.keywords)

if __name__ == "__main__":
    main()
