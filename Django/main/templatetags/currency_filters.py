from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def format_short(value):
    try:
        val = float(value)
        abs_val = abs(val)
        sign = "-" if val < 0 else ""
        
        if abs_val >= 1_000_000_000:
            return f"{sign}{abs_val / 1_000_000_000:.2f}B"
        if abs_val >= 1_000_000:
            return f"{sign}{abs_val / 1_000_000:.2f}M"
        if abs_val >= 1_000:
            return f"{sign}{abs_val / 1_000:.2f}K"
            
        return f"{val:.0f}"
    except (ValueError, TypeError):
        return value