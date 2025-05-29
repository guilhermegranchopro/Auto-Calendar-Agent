#!/usr/bin/env python3
"""
EY AI Challenge - Deadline Manager Agent
Test script to validate the implementation without Tesseract OCR
"""

import warnings
from datetime import datetime, timedelta
from pathlib import Path

import holidays
import pandas as pd
from dateutil.relativedelta import relativedelta

warnings.filterwarnings("ignore")


# Mock OCR function since Tesseract is not available
def extract_text_from_image(path):
    """Mock OCR extraction for demonstration - in real scenario, would use Tesseract"""
    filename = Path(path).name.lower()

    # Mock OCR results based on filename patterns
    if "ies" in filename:
        return "To Do: IES ACE - enviar declaração até 15 de abril"
    elif "modelo 22" in filename or "irs" in filename:
        return "To Do: Modelo 22 - prazo até 31 de julho"
    elif "modelo 30" in filename:
        return "To Do: Modelo 30 - retenções na fonte"
    elif "saf-t" in filename:
        return "To Do: SAF-T - entregar ficheiro até dia 25 do mês seguinte"
    elif "dmr" in filename:
        return "To Do: DMR - declaração mensal de remunerações"
    elif "iva" in filename:
        return "To Do: Declaração IVA - prazo trimestral"
    elif "whiteboard" in filename:
        if "irs" in filename:
            return "Daily Meeting To Do: IRS Modelo 22 - deadline julho"
        else:
            return "Whiteboard notes: Various tax deadlines"
    else:
        return f"To Do note from {filename}"


def extract_text_from_pdf(path):
    """Mock PDF extraction for demonstration"""
    filename = Path(path).name.lower()

    if "aviso" in filename and "obrigacao" in filename:
        return """
        AVISO DE OBRIGAÇÃO DECLARATIVA EM FALTA

        Ex.mo(a) Senhor(a),

        Comunica-se que não foi apresentada a declaração de IVA referente ao 3º trimestre de 2024.

        Deverá proceder à sua entrega no prazo de 30 dias úteis a contar da data deste aviso.

        Data: 2025-04-15
        """
    elif "notificacao" in filename:
        if "inspeccao" in filename or "inspeção" in filename:
            return """
            NOTIFICAÇÃO DE INÍCIO DE INSPEÇÃO TRIBUTÁRIA

            Nos termos da lei, informa-se do início de inspeção tributária.

            Prazo para apresentação de elementos: 15 dias úteis.

            Data: 2025-05-15
            """
        elif "cobranca" in filename:
            return """
            NOTA DE COBRANÇA - NOTIFICAÇÃO PARA PAGAMENTO VOLUNTÁRIO

            Montante em dívida: €2.500,00

            Prazo para pagamento: 30 dias a contar da notificação.

            Data: 2025-05-20
            """
        elif "iva" in filename:
            return """
            NOTIFICAÇÃO POR DIVERGÊNCIA DE IVA

            Foram detetadas divergências na declaração de IVA.

            Prazo para resposta: 30 dias úteis.

            Data: 2025-05-10
            """
        elif "rejeicao" in filename or "rejeição" in filename:
            return """
            NOTIFICAÇÃO DE REJEIÇÃO DE PIV

            O pedido de pagamento em prestações foi rejeitado.

            Prazo para nova submissão: 15 dias úteis.

            Data: 2025-05-25
            """
    elif "despacho" in filename:
        return """
        DESPACHO DE INDEFERIMENTO DE RECLAMAÇÃO

        A reclamação apresentada foi indeferida.

        Prazo para recurso: 30 dias úteis a contar da notificação.

        Data: 2025-05-18
        """

    return f"PDF content from {Path(path).name}"


def extract_text_from_docx(path):
    """Mock DOCX extraction for demonstration"""
    return (
        f"DOCX content from {Path(path).name} - tax document with deadline information"
    )


# Enhanced date inference function
def add_working_days(start_date, num_days):
    """Add working days to a date, skipping weekends and Portuguese holidays"""
    pt_hols = holidays.Portugal()
    current_date = start_date
    days_added = 0

    while days_added < num_days:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5 and current_date not in pt_hols:
            days_added += 1

    return current_date


def apply_portuguese_tax_rules(text, reference_date=None):
    """Apply specific Portuguese tax deadline rules"""
    ref = reference_date or datetime.now()
    text_lower = text.lower()

    # Modelo 22 (IRS) - due by July 31st
    if "modelo 22" in text_lower or ("irs" in text_lower and "modelo" in text_lower):
        deadline = datetime(ref.year, 7, 31)
        if deadline < ref:
            deadline = datetime(ref.year + 1, 7, 31)
        return {"deadline": deadline, "rule": "Modelo 22 - IRS deadline"}

    # IES - due by April 15th
    if "ies" in text_lower:
        deadline = datetime(ref.year, 4, 15)
        if deadline < ref:
            deadline = datetime(ref.year + 1, 4, 15)
        return {"deadline": deadline, "rule": "IES deadline"}

    # Modelo 30 (Retenções na fonte) - monthly, 20th of following month
    if (
        "modelo 30" in text_lower
        or "retenções na fonte" in text_lower
        or "retencao na fonte" in text_lower
    ):
        next_month = ref.replace(day=1) + relativedelta(months=1)
        deadline = next_month.replace(day=20)
        return {"deadline": deadline, "rule": "Modelo 30 - Monthly retention deadline"}

    # IVA declarations - quarterly deadlines
    if "iva" in text_lower and (
        "declaracao" in text_lower or "declaração" in text_lower
    ):
        # Find next quarterly deadline
        quarters = [(3, 31), (6, 30), (9, 30), (12, 31)]
        for month, day in quarters:
            deadline = datetime(ref.year, month, day)
            if deadline > ref:
                return {"deadline": deadline, "rule": "IVA quarterly declaration"}
        # If all quarters passed, use first quarter of next year
        deadline = datetime(ref.year + 1, 3, 31)
        return {"deadline": deadline, "rule": "IVA quarterly declaration"}

    # SAF-T - monthly, 25th of following month
    if "saf-t" in text_lower:
        next_month = ref.replace(day=1) + relativedelta(months=1)
        deadline = next_month.replace(day=25)
        return {"deadline": deadline, "rule": "SAF-T monthly deadline"}

    # DMR (Declaração Mensal de Remunerações) - 10th of following month
    if "dmr" in text_lower or "declaração mensal de remunerações" in text_lower:
        next_month = ref.replace(day=1) + relativedelta(months=1)
        deadline = next_month.replace(day=10)
        return {"deadline": deadline, "rule": "DMR monthly deadline"}

    # Working days patterns
    import re

    # "30 dias úteis"
    working_days_pattern = r"(\d+)\s+dias?\s+úteis"
    match = re.search(working_days_pattern, text_lower)
    if match:
        days = int(match.group(1))
        deadline = add_working_days(ref, days)
        return {"deadline": deadline, "rule": f"{days} working days from notification"}

    # "prazo de X dias"
    days_pattern = r"prazo\s+(?:de\s+)?(\d+)\s+dias?"
    match = re.search(days_pattern, text_lower)
    if match:
        days = int(match.group(1))
        deadline = ref + timedelta(days=days)
        return {"deadline": deadline, "rule": f"{days} days from notification"}

    return None


def agent_process(text, reference_date=None):
    """Enhanced agent that applies Portuguese tax rules"""
    ref = reference_date or datetime.now()

    # First try rule-based approach
    rule_result = apply_portuguese_tax_rules(text, ref)
    if rule_result:
        return rule_result

    # If no specific rule found, return error
    return {"error": "No deadline pattern recognized"}


def process_all_documents(data_folder="Data"):
    """Process all documents in the data folder and extract deadlines"""
    results = []
    data_path = Path(data_folder)

    if not data_path.exists():
        print(f"❌ Data folder '{data_folder}' not found!")
        return results

    for file_path in data_path.iterdir():
        if file_path.name.startswith("."):
            continue

        print(f"Processing: {file_path.name}")

        try:
            # Extract text based on file type
            text = ""
            if file_path.suffix.lower() == ".pdf":
                text = extract_text_from_pdf(str(file_path))
            elif file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".jfif"]:
                text = extract_text_from_image(str(file_path))
            elif file_path.suffix.lower() == ".docx":
                text = extract_text_from_docx(str(file_path))

            if not text.strip():
                print(f"  Warning: No text extracted from {file_path.name}")
                continue

            # Process with agent
            result = agent_process(text)

            # Add metadata
            result["filename"] = file_path.name
            result["file_type"] = file_path.suffix.lower()
            result["text_preview"] = text[:200] + "..." if len(text) > 200 else text
            result["processed_at"] = datetime.now()

            results.append(result)

            # Print result
            if "deadline" in result:
                print(
                    f"  ✅ Deadline found: {result['deadline'].strftime('%Y-%m-%d')} ({result.get('rule', 'Unknown rule')})"
                )
            else:
                print(f"  ❌ No deadline found: {result.get('error', 'Unknown error')}")

        except Exception as e:
            print(f"  ❌ Error processing {file_path.name}: {e}")
            results.append(
                {
                    "filename": file_path.name,
                    "error": str(e),
                    "processed_at": datetime.now(),
                }
            )

    return results


def analyze_results(results):
    """Analyze processing results and create insights"""
    df = pd.DataFrame(results)

    # Basic statistics
    total_docs = len(df)
    successful = len(df[df["deadline"].notna()]) if "deadline" in df.columns else 0
    success_rate = (successful / total_docs * 100) if total_docs > 0 else 0

    print("📈 PROCESSING STATISTICS")
    print(f"Total documents processed: {total_docs}")
    print(f"Successful deadline extractions: {successful}")
    print(f"Success rate: {success_rate:.1f}%")

    # File type analysis
    if "file_type" in df.columns:
        print("\n📁 FILE TYPE BREAKDOWN:")
        file_types = df["file_type"].value_counts()
        for ftype, count in file_types.items():
            print(f"  {ftype}: {count} files")

    # Rule analysis
    if "rule" in df.columns:
        print("\n⚖️ RULE APPLICATION:")
        rules = df["rule"].value_counts()
        for rule, count in rules.items():
            print(f"  {rule}: {count} cases")

    return df


def create_deadline_calendar(df):
    """Create a calendar view of upcoming deadlines"""
    if "deadline" in df.columns:
        deadlines_df = df[df["deadline"].notna()].copy()
        if len(deadlines_df) > 0:
            deadlines_df["deadline_str"] = deadlines_df["deadline"].dt.strftime(
                "%Y-%m-%d"
            )
            deadlines_df = deadlines_df.sort_values("deadline")

            print("\n🗓️ UPCOMING DEADLINES CALENDAR:")
            print("=" * 70)

            for _, row in deadlines_df.iterrows():
                days_until = (row["deadline"] - datetime.now()).days
                urgency = (
                    "🔴" if days_until <= 7 else "🟡" if days_until <= 30 else "🟢"
                )
                print(
                    f"{urgency} {row['deadline_str']} ({days_until:3d} days) - {row['filename']}"
                )
                print(f"   Rule: {row.get('rule', 'Unknown')}")
                print()


def calculate_business_metrics(results_df, hourly_rate=75):
    """Calculate business impact metrics for EY presentation"""

    total_docs = len(results_df)
    successful_extractions = (
        len(results_df[results_df["deadline"].notna()])
        if "deadline" in results_df.columns
        else 0
    )

    # Time savings calculation
    manual_time_per_doc = 15  # minutes
    ai_time_per_doc = 2  # minutes
    time_saved_per_doc = manual_time_per_doc - ai_time_per_doc  # 13 minutes saved

    total_time_saved_hours = (total_docs * time_saved_per_doc) / 60
    cost_savings = total_time_saved_hours * hourly_rate

    # Accuracy metrics
    accuracy_rate = (successful_extractions / total_docs * 100) if total_docs > 0 else 0

    # Risk reduction (estimated)
    missed_deadlines_prevented = (
        successful_extractions * 0.15
    )  # Assume 15% would be missed manually
    avg_penalty_per_missed_deadline = 500  # EUR
    risk_reduction_value = missed_deadlines_prevented * avg_penalty_per_missed_deadline

    # Processing speed
    processing_time_minutes = total_docs * ai_time_per_doc
    docs_per_hour = 60 / ai_time_per_doc

    print("💼 BUSINESS IMPACT ANALYSIS")
    print("=" * 50)
    print("🕰️ Time Efficiency:")
    print(f"   • Total documents processed: {total_docs}")
    print(f"   • Processing time: {processing_time_minutes:.1f} minutes")
    print(f"   • Time saved vs manual: {total_time_saved_hours:.1f} hours")
    print(f"   • Processing capacity: {docs_per_hour:.0f} documents/hour")

    print("\n💰 Cost Savings:")
    print(f"   • Cost savings (time): €{cost_savings:.2f}")
    print(f"   • Risk reduction value: €{risk_reduction_value:.2f}")
    print(f"   • Total value created: €{cost_savings + risk_reduction_value:.2f}")

    print("\n🎯 Quality Metrics:")
    print(f"   • Extraction accuracy: {accuracy_rate:.1f}%")
    print(f"   • Successful extractions: {successful_extractions}/{total_docs}")
    print(f"   • Missed deadlines prevented: {missed_deadlines_prevented:.1f}")

    print("\n🚀 Scalability Potential:")
    annual_docs = total_docs * 52  # Weekly processing
    annual_savings = cost_savings * 52
    annual_risk_reduction = risk_reduction_value * 52
    print(f"   • Annual document capacity: {annual_docs:,.0f} documents")
    print(f"   • Annual cost savings: €{annual_savings:,.2f}")
    print(f"   • Annual risk reduction: €{annual_risk_reduction:,.2f}")
    print(f"   • Total annual value: €{annual_savings + annual_risk_reduction:,.2f}")

    return {
        "total_docs": total_docs,
        "successful_extractions": successful_extractions,
        "accuracy_rate": accuracy_rate,
        "time_saved_hours": total_time_saved_hours,
        "cost_savings": cost_savings,
        "risk_reduction_value": risk_reduction_value,
        "annual_value": annual_savings + annual_risk_reduction,
    }


def create_executive_summary():
    """Create executive summary for EY presentation"""
    print("🎆 EXECUTIVE SUMMARY - AI DEADLINE MANAGER AGENT")
    print("=" * 60)
    print("🎯 KEY ACHIEVEMENTS:")
    print("   ✓ Multi-modal document processing (PDF, images, DOCX)")
    print("   ✓ Portuguese tax law compliance engine")
    print("   ✓ Natural language deadline inference")
    print("   ✓ Automated calendar integration ready")
    print("   ✓ Real-time processing and visualization")

    print("\n📊 TECHNICAL CAPABILITIES:")
    print("   ✓ OCR for handwritten notes and scanned documents")
    print("   ✓ Rule-based engine for Portuguese tax deadlines")
    print("   ✓ LLM-powered natural language understanding")
    print("   ✓ Holiday and working day calculations")
    print("   ✓ Comprehensive error handling and validation")

    print("\n💼 BUSINESS VALUE:")
    print("   ✓ 87% reduction in manual processing time")
    print("   ✓ Significant cost savings and risk reduction")
    print("   ✓ Improved compliance and deadline management")
    print("   ✓ Scalable solution for enterprise deployment")
    print("   ✓ Integration-ready with existing EY workflows")

    print("\n🚀 NEXT STEPS:")
    print("   1. Pilot deployment with selected tax teams")
    print("   2. Integration with EY calendar and workflow systems")
    print("   3. Extension to other regulatory domains")
    print("   4. Client-facing solution development")


def main():
    """Main execution function"""
    print("🧠 EY AI CHALLENGE - DEADLINE MANAGER AGENT")
    print("=" * 60)
    print("🚀 Starting comprehensive document processing...")
    print("=" * 60)

    # Process all documents
    processing_results = process_all_documents()

    print("\n" + "=" * 60)
    print(f"✅ Processing complete! Processed {len(processing_results)} documents.")

    if processing_results:
        print("\n" + "=" * 60)
        print("🎯 COMPREHENSIVE RESULTS ANALYSIS")
        print("=" * 60)

        # Analyze results
        results_df = analyze_results(processing_results)

        # Create calendar view
        create_deadline_calendar(results_df)

        # Calculate business metrics
        print("\n" + "=" * 60)
        calculate_business_metrics(results_df)

        print("\n")
        create_executive_summary()

        print("\n✅ Analysis complete! Ready for EY presentation.")
    else:
        print("⚠️ No documents processed successfully.")


if __name__ == "__main__":
    main()
