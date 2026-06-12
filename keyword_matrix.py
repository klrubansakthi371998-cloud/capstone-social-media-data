keywords = {
    "AI": [
        "chatgpt",
        "openai",
        "gemini",
        "machine learning",
        "artificial intelligence"
    ],

    "Cloud": [
        "aws",
        "azure",
        "gcp",
        "cloud computing"
    ],

    "Data Analytics": [
        "python",
        "sql",
        "tableau",
        "power bi",
        "data analysis"
    ]
}

print("Keyword Matrix Created")

for category, words in keywords.items():
    print(f"\n{category}:")
    for word in words:
        print("-", word)