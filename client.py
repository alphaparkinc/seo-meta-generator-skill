"""
seo-meta-generator-skill: Client SDK
Auto-generates Google-compliant SEO Title and Meta Description tags using product context.
"""
from __future__ import annotations
from typing import Optional


class SEOMetaGeneratorClient:
    """
    SDK for e-commerce SEO metadata generation.
    """

    def generate(
        self,
        product_name: str,
        category: str,
        keywords: list[str],
        brand_name: str = "",
    ) -> dict:
        kw_str = ", ".join(keywords[:2])
        
        # Build Title Tag (< 60 chars)
        title = f"{product_name} | Premium {category}"
        if brand_name:
            title = f"{title} by {brand_name}"
        if len(title) > 60:
            title = title[:57] + "..."

        # Build Meta Description (< 160 chars)
        desc = f"Shop high-quality {product_name}. Features top-rated solutions for {kw_str}."
        if brand_name:
            desc = f"{desc} Certified quality products from {brand_name}. Order today!"
        else:
            desc = f"{desc} Buy now and get fast shipping on all orders."

        if len(desc) > 160:
            desc = desc[:157] + "..."

        return {
            "seo_title": title,
            "meta_description": desc,
            "title_length": len(title),
            "description_length": len(desc),
        }
