# Agent 1: Ad Analyzer
def analyze_ad(ad):
    ad = ad.lower()
    
    if "discount" in ad or "offer" in ad:
        intent = "promotion"
    elif "premium" in ad or "luxury" in ad:
        intent = "premium"
    else:
        intent = "general"
    
    return {
        "intent": intent,
        "headline": ad.capitalize()
    }


# Agent 2: Page Analyzer
def analyze_page(page):
    return {
        "content": page,
        "length": len(page)
    }


# Agent 3: Personalization Agent
def personalize(ad_data, page_data):
    intent = ad_data["intent"]
    headline = ad_data["headline"]
    content = page_data["content"]

    if intent == "promotion":
        cta = "🔥 Grab this limited-time discount now!"
        content += "\n\n💥 Special offer available for a limited time!"
    elif intent == "premium":
        cta = "✨ Experience premium quality today."
        content += "\n\n🌟 Designed for customers who value excellence."
    else:
        cta = "👉 Explore our collection today."

    return f"""
========================================
        PERSONALIZED LANDING PAGE
========================================

🎯 HEADLINE:
{headline}

📄 CONTENT:
{content}

🚀 CALL TO ACTION:
{cta}

----------------------------------------
Optimized based on Ad Intent: {intent}
----------------------------------------
"""

# MAIN FLOW

ad_input = input("Enter Ad Creative: ")
landing_page = input("Enter Landing Page Content: ")

ad_data = analyze_ad(ad_input)
page_data = analyze_page(landing_page)

output = personalize(ad_data, page_data)

print("\n--- FINAL OUTPUT ---\n")
print(output)
