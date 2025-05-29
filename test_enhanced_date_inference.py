#!/usr/bin/env python3
"""
Test the enhanced date inference function specifically
"""

import sys
import os
from datetime import datetime, timedelta
from pathlib import Path
import re
import calendar

def test_enhanced_date_inference():
    """Test the enhanced date inference function"""
    
    # Mock the enhanced infer_deadline function
    def infer_deadline(text, base_date=None):
        """Enhanced deadline identification with Portuguese legal patterns."""
        base = base_date or datetime.now()

        # Enhanced regex patterns for common Portuguese date formats
        import re
        
        # Portuguese month names mapping
        months_pt = {
            'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4,
            'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8,
            'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12,
            'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4,
            'mai': 5, 'jun': 6, 'jul': 7, 'ago': 8,
            'set': 9, 'out': 10, 'nov': 11, 'dez': 12
        }
        
        # Multiple date pattern formats
        date_patterns = [
            # "até 31 de julho de 2025"
            (r"até\s+(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})", "dmy_name"),
            # "prazo até 15 de abril de 2025"
            (r"prazo\s+até\s+(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})", "dmy_name"),
            # "15 de abril de 2025"
            (r"(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})", "dmy_name"),
            # "31/12/2025"
            (r"(\d{1,2})/(\d{1,2})/(\d{4})", "dmy_slash"),
            # "2025-06-30"
            (r"(\d{4})-(\d{1,2})-(\d{1,2})", "ymd_dash"),
            # "31-12-2025"
            (r"(\d{1,2})-(\d{1,2})-(\d{4})", "dmy_dash"),
            # "dezembro 2025" (end of month)
            (r"(\w+)\s+de\s+(\d{4})", "my_name"),
            (r"(\w+)\s+(\d{4})", "my_name_simple")
        ]
        
        for pattern, format_type in date_patterns:
            matches = re.findall(pattern, text.lower())
            if matches:
                for match in matches:
                    try:
                        if format_type == "dmy_name":
                            # Day, month name, year format
                            day, month_name, year = match
                            month = months_pt.get(month_name.lower(), None)
                            if month:
                                deadline = datetime(int(year), month, int(day))
                                if deadline > base:
                                    return deadline
                        
                        elif format_type == "dmy_slash":
                            # DD/MM/YYYY format
                            day, month, year = match
                            deadline = datetime(int(year), int(month), int(day))
                            if deadline > base:
                                return deadline
                        
                        elif format_type == "ymd_dash":
                            # YYYY-MM-DD format
                            year, month, day = match
                            deadline = datetime(int(year), int(month), int(day))
                            if deadline > base:
                                return deadline
                        
                        elif format_type == "dmy_dash":
                            # DD-MM-YYYY format
                            day, month, year = match
                            deadline = datetime(int(year), int(month), int(day))
                            if deadline > base:
                                return deadline
                        
                        elif format_type in ["my_name", "my_name_simple"]:
                            # Month and year only - use last day of month
                            if format_type == "my_name":
                                month_name, year = match
                            else:
                                month_name, year = match
                            
                            month = months_pt.get(month_name.lower(), None)
                            if month:
                                # Get last day of the month
                                last_day = calendar.monthrange(int(year), month)[1]
                                deadline = datetime(int(year), month, last_day)
                                if deadline > base:
                                    return deadline
                    
                    except (ValueError, TypeError) as e:
                        continue
        
        return None

    # Test cases with expected results
    test_cases = [
        ("Modelo 22 - IRS deve ser entregue até 31 de julho de 2025", "2025-07-31"),
        ("Prazo até 15 de abril de 2025 para IES", "2025-04-15"),
        ("Deadline: 31/12/2025", "2025-12-31"),
        ("Data limite: 2025-06-30", "2025-06-30"),
        ("Entrega em 15-03-2025", "2025-03-15"),
        ("Vencimento em dezembro de 2025", "2025-12-31"),
        ("Prazo dezembro 2025", "2025-12-31"),
        ("No deadline in this text", None)
    ]
    
    base_date = datetime(2025, 5, 29)  # Current date
    
    print("🧪 Testing Enhanced Date Inference Function")
    print("=" * 60)
    
    total_tests = len(test_cases)
    passed_tests = 0
    
    for i, (text, expected) in enumerate(test_cases, 1):
        print(f"Test {i}: {text[:50]}...")
        result = infer_deadline(text, base_date)
        
        if expected is None:
            if result is None:
                print(f"    ✅ PASS: No deadline found (as expected)")
                passed_tests += 1
            else:
                print(f"    ❌ FAIL: Found deadline {result.strftime('%Y-%m-%d')} but expected None")
        else:
            if result:
                result_str = result.strftime('%Y-%m-%d')
                if result_str == expected:
                    print(f"    ✅ PASS: Found deadline {result_str}")
                    passed_tests += 1
                else:
                    print(f"    ❌ FAIL: Found {result_str}, expected {expected}")
            else:
                print(f"    ❌ FAIL: No deadline found, expected {expected}")
    
    print(f"\n📊 Results: {passed_tests}/{total_tests} tests passed ({passed_tests/total_tests*100:.1f}%)")
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! Enhanced date inference is working correctly.")
    else:
        print("⚠️ Some tests failed. The function may need further refinement.")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    test_enhanced_date_inference()
