#!/usr/bin/env python3
"""
Debug the specific failing patterns
"""

import re
from datetime import datetime

def debug_patterns():
    """Debug the failing patterns"""
    
    # Test the problematic patterns individually
    test_cases = [
        "Prazo até 15 de abril de 2025 para IES",
        "Entrega em 15-03-2025"
    ]
    
    # Portuguese month names mapping
    months_pt = {
        'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4,
        'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8,
        'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12,
        'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4,
        'mai': 5, 'jun': 6, 'jul': 7, 'ago': 8,
        'set': 9, 'out': 10, 'nov': 11, 'dez': 12
    }
    
    patterns = [
        (r"prazo\s+até\s+(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})", "prazo até pattern"),
        (r"entrega\s+em\s+(\d{1,2})-(\d{1,2})-(\d{4})", "entrega em pattern"),
    ]
    
    for text in test_cases:
        print(f"Testing: {text}")
        text_lower = text.lower()
        print(f"Lowercase: {text_lower}")
        
        for pattern, name in patterns:
            matches = re.findall(pattern, text_lower)
            print(f"  {name}: {matches}")
            
            if matches:
                match = matches[0]
                if name == "prazo até pattern":
                    day, month_name, year = match
                    month = months_pt.get(month_name.lower(), None)
                    print(f"    Day: {day}, Month: {month_name} -> {month}, Year: {year}")
                    if month:
                        deadline = datetime(int(year), month, int(day))
                        print(f"    Result: {deadline}")
                elif name == "entrega em pattern":
                    day, month, year = match
                    print(f"    Day: {day}, Month: {month}, Year: {year}")
                    deadline = datetime(int(year), int(month), int(day))
                    print(f"    Result: {deadline}")
        print()

if __name__ == "__main__":
    debug_patterns()
