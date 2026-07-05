"""
example_usage.py -- Demonstrates SEOMetaGeneratorClient
"""
from client import SEOMetaGeneratorClient

def main():
    client = SEOMetaGeneratorClient()
    result = client.generate(
        product_name="HydraGlow Vitamin C Serum",
        category="skincare",
        keywords=["glow skin", "brighten dark spots"],
        brand_name="GlowStore"
    )
    print("[SEO Metadata Result]")
    print(f"Title ({result['title_length']} chars): {result['seo_title']}")
    print(f"Meta Description ({result['description_length']} chars): {result['meta_description']}")

if __name__ == "__main__":
    main()
