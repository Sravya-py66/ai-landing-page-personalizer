import streamlit as st

st.set_page_config(page_title="AI Landing Page Generator", layout="centered")

def fetch_page_content(url):
    # Simulated content (since no scraping)
    return "Welcome to our store. We sell high-quality shoes for everyday use."

# Reuse your functions
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

def analyze_page(page):
    return {
        "content": page,
        "length": len(page)
    }

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
### 🎯 {headline}

{content}

---

🚀 **{cta}**

---
Optimized based on: **{intent}**
"""

# UI
st.title("🚀 AI Landing Page Personalizer")
st.write("Generate optimized landing pages based on ad intent")

ad_input = st.text_input("📢 Ad Creative", placeholder="e.g. Get 50% discount on shoes!")

url = st.text_input("🔗 Landing Page URL", placeholder="https://example.com")

if st.button("✨ Generate Page"):
    ad_data = analyze_ad(ad_input)
    original_content = fetch_page_content(url)
    page_data = analyze_page(original_content)
    
    output = personalize(ad_data, page_data)
    
    st.subheader("🔵 Original Landing Page")
    st.write(original_content)

    st.subheader("🟢 Personalized Landing Page")
    st.markdown(output)
