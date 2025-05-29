"""
EY AI Challenge - Deadline Manager Agent Backend
Core processing engine extracted from AutoCalendarAgent.ipynb
"""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path

import google.generativeai as genai
import holidays
from dateutil.relativedelta import relativedelta
from PyPDF2 import PdfReader

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyB1XJV_CWEu9zojtETnViNEhwoFa8CF-FE"
genai.configure(api_key=GEMINI_API_KEY)


class DeadlineManagerAgent:
    """AI-powered deadline manager for Portuguese tax obligations"""

    def __init__(self):
        self.portuguese_holidays = holidays.Portugal()
        self.reference_date = datetime.now()

    def extract_text_from_image(self, image_path_or_file, use_mock_ocr=True):
        """Extract text from image using OCR (mock implementation for demo)"""
        try:
            if use_mock_ocr:
                # Mock OCR based on filename patterns for demo
                filename = getattr(
                    image_path_or_file, "name", str(image_path_or_file)
                ).lower()
                return self._mock_ocr_by_filename(filename)
            else:
                # Real OCR implementation would go here
                # import pytesseract
                # image = Image.open(image_path_or_file)
                # text = pytesseract.image_to_string(image, lang='por+eng')
                # return text.strip()
                pass
        except Exception as e:
            return f"Error processing image: {e}"

    def extract_text_from_pdf(self, pdf_path_or_file):
        """Extract text from PDF document"""
        try:
            if hasattr(pdf_path_or_file, "read"):
                # It's a file-like object
                reader = PdfReader(pdf_path_or_file)
            else:
                # It's a file path
                reader = PdfReader(pdf_path_or_file)

            text_parts = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)

            extracted_text = "\n".join(text_parts)

            # If minimal text extracted, use mock content for demo
            if len(extracted_text.strip()) < 50:
                filename = getattr(
                    pdf_path_or_file, "name", str(pdf_path_or_file)
                ).lower()
                return self._mock_pdf_content_by_filename(filename)

            return extracted_text

        except Exception as e:
            return f"Error processing PDF: {e}"

    def _mock_ocr_by_filename(self, filename):
        """Mock OCR results based on filename patterns"""
        filename = filename.lower()

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

    def _mock_pdf_content_by_filename(self, filename):
        """Mock PDF content based on filename patterns"""
        filename = filename.lower()

        if "aviso" in filename and "obrigacao" in filename:
            return """
            AVISO DE OBRIGAÇÃO DECLARATIVA EM FALTA

            Autoridade Tributária e Aduaneira

            Exmo(a). Senhor(a),

            Vimos por este meio informar que não foi entregue a declaração IVA
            referente ao período de [período], devendo a mesma ser entregue
            até ao final do trimestre seguinte.

            Data: {date}
            """.format(date=datetime.now().strftime("%Y-%m-%d"))
        elif "notificacao" in filename and "inspecao" in filename:
            return """
            NOTIFICAÇÃO DE INÍCIO DE INSPEÇÃO TRIBUTÁRIA

            Nos termos do artigo 52.º do CPPT, notifica-se que deverá
            responder no prazo de 15 dias úteis a partir da presente notificação.

            Data: {date}
            """.format(date=datetime.now().strftime("%Y-%m-%d"))
        elif "rejeicao" in filename:
            return """
            NOTIFICAÇÃO DE REJEIÇÃO

            A sua submissão foi rejeitada. Deve proceder à correção e
            reenvio no prazo de 15 dias úteis a partir desta notificação.

            Data: {date}
            """.format(date=datetime.now().strftime("%Y-%m-%d"))
        elif "despacho" in filename and "indeferimento" in filename:
            return """
            DESPACHO DE INDEFERIMENTO

            O seu pedido foi indeferido. Pode apresentar recurso no prazo
            de 30 dias úteis a partir da presente notificação.

            Data: {date}
            """.format(date=datetime.now().strftime("%Y-%m-%d"))
        else:
            return f"Documento fiscal - {filename}"

    def add_working_days(self, start_date, num_days):
        """Add working days to a date, skipping weekends and Portuguese holidays"""
        current_date = start_date
        days_added = 0

        while days_added < num_days:
            current_date += timedelta(days=1)
            if (
                current_date.weekday() < 5
                and current_date not in self.portuguese_holidays
            ):
                days_added += 1

        return current_date

    def apply_portuguese_tax_rules(self, text, reference_date=None):
        """Apply specific Portuguese tax deadline rules"""
        ref = reference_date or self.reference_date
        text_lower = text.lower()

        # Modelo 22 (IRS) - due by July 31st
        if "modelo 22" in text_lower or (
            "irs" in text_lower and ("modelo" in text_lower or "deadline" in text_lower)
        ):
            deadline = datetime(ref.year, 7, 31)
            if deadline < ref:
                deadline = datetime(ref.year + 1, 7, 31)
            return {
                "deadline": deadline,
                "rule": "Modelo 22 - IRS deadline",
                "priority": "high",
                "legal_basis": "CIRS - Código do IRS",
                "confidence": "high",
            }

        # IES - due by April 15th
        if "ies" in text_lower:
            deadline = datetime(ref.year, 4, 15)
            if deadline < ref:
                deadline = datetime(ref.year + 1, 4, 15)
            return {
                "deadline": deadline,
                "rule": "IES deadline",
                "priority": "high",
                "legal_basis": "CIRS - Informação Empresarial Simplificada",
                "confidence": "high",
            }

        # Modelo 30 (Retenções na fonte) - monthly, 20th of following month
        if (
            "modelo 30" in text_lower
            or "retenções na fonte" in text_lower
            or "retencao na fonte" in text_lower
            or "retencao" in text_lower
        ):
            next_month = ref.replace(day=1) + relativedelta(months=1)
            deadline = next_month.replace(day=20)
            return {
                "deadline": deadline,
                "rule": "Modelo 30 - Monthly retention deadline",
                "priority": "medium",
                "legal_basis": "CIRS - Retenções na fonte",
                "confidence": "high",
            }

        # IVA declarations - quarterly deadlines
        if "iva" in text_lower and (
            "declaracao" in text_lower or "declaração" in text_lower
        ):
            quarters = [(3, 31), (6, 30), (9, 30), (12, 31)]
            for month, day in quarters:
                deadline = datetime(ref.year, month, day)
                if deadline > ref:
                    return {
                        "deadline": deadline,
                        "rule": "IVA quarterly declaration",
                        "priority": "high",
                        "legal_basis": "CIVA - Código do IVA",
                        "confidence": "high",
                    }
            # If all quarters passed, use first quarter of next year
            deadline = datetime(ref.year + 1, 3, 31)
            return {
                "deadline": deadline,
                "rule": "IVA quarterly declaration",
                "priority": "high",
                "legal_basis": "CIVA - Código do IVA",
                "confidence": "high",
            }

        # SAF-T - monthly, 25th of following month
        if "saf-t" in text_lower:
            next_month = ref.replace(day=1) + relativedelta(months=1)
            deadline = next_month.replace(day=25)
            return {
                "deadline": deadline,
                "rule": "SAF-T monthly deadline",
                "priority": "medium",
                "legal_basis": "Portaria n.º 321-A/2007",
                "confidence": "high",
            }

        # DMR (Declaração Mensal de Remunerações) - 10th of following month
        if (
            "dmr" in text_lower
            or "declaração mensal de remunerações" in text_lower
            or "declaracao mensal" in text_lower
        ):
            next_month = ref.replace(day=1) + relativedelta(months=1)
            deadline = next_month.replace(day=10)
            return {
                "deadline": deadline,
                "rule": "DMR monthly deadline",
                "priority": "medium",
                "legal_basis": "Código do Trabalho",
                "confidence": "high",
            }

        # Working days patterns - "X dias úteis"
        working_days_pattern = r"(\d+)\s+dias?\s+úteis"
        match = re.search(working_days_pattern, text_lower)
        if match:
            days = int(match.group(1))
            deadline = self.add_working_days(ref, days)
            return {
                "deadline": deadline,
                "rule": f"{days} working days from notification",
                "priority": "urgent",
                "legal_basis": "CPPT - Código de Procedimento e de Processo Tributário",
                "confidence": "high",
            }

        # Regular days pattern - "prazo de X dias"
        days_pattern = r"prazo\s+(?:de\s+)?(\d+)\s+dias?"
        match = re.search(days_pattern, text_lower)
        if match:
            days = int(match.group(1))
            deadline = ref + timedelta(days=days)
            return {
                "deadline": deadline,
                "rule": f"{days} days from notification",
                "priority": "urgent",
                "legal_basis": "CPPT - Código de Procedimento e de Processo Tributário",
                "confidence": "high",
            }

        return None

    def process_with_gemini_ai(self, text, reference_date=None):
        """Use Gemini AI to extract deadline information when rule-based approach fails"""
        try:
            model = genai.GenerativeModel("gemini-pro")
            ref = reference_date or self.reference_date

            prompt = f"""
            You are a Portuguese tax deadline expert. Analyze this text and extract deadline information.

            Reference date: {ref.strftime("%Y-%m-%d")}
            Text: "{text}"

            Based on Portuguese tax law (CPPT, CIRS, CIVA), identify:
            1. The specific tax obligation mentioned
            2. The deadline calculation rule
            3. The exact deadline date
            4. Priority level (urgent/high/medium/low)
            5. Legal basis for the deadline

            Return ONLY a valid JSON object with:
            {{
                "deadline": "YYYY-MM-DD",
                "rule": "description of the rule applied",
                "priority": "urgency level",
                "legal_basis": "relevant legal framework",
                "confidence": "high/medium/low"
            }}

            If no deadline can be determined, return {{"error": "No deadline found"}}.
            """

            response = model.generate_content(prompt)
            response_text = response.text.strip()

            # Try to extract JSON from response
            if "{" in response_text and "}" in response_text:
                start = response_text.find("{")
                end = response_text.rfind("}") + 1
                json_str = response_text[start:end]

                try:
                    result = json.loads(json_str)
                    if "deadline" in result and "error" not in result:
                        deadline_dt = datetime.strptime(result["deadline"], "%Y-%m-%d")
                        return {
                            "deadline": deadline_dt,
                            "rule": result.get("rule", "Gemini AI analysis"),
                            "priority": result.get("priority", "medium"),
                            "legal_basis": result.get("legal_basis", "AI inference"),
                            "confidence": result.get("confidence", "medium"),
                        }
                except json.JSONDecodeError as e:
                    return {"error": f"JSON parsing error: {e}"}

            return {"error": "Could not parse deadline from AI response"}

        except Exception as e:
            return {"error": f"Gemini AI error: {e!s}"}

    def process_document(self, text, reference_date=None, use_ai_fallback=True):
        """Main processing function that combines rule-based and AI approaches"""
        ref = reference_date or self.reference_date

        # First try rule-based approach
        rule_result = self.apply_portuguese_tax_rules(text, ref)
        if rule_result:
            rule_result["processing_method"] = "rule_based"
            rule_result["processed_at"] = datetime.now()
            return rule_result

        # Fallback to AI if enabled
        if use_ai_fallback:
            ai_result = self.process_with_gemini_ai(text, ref)
            if "deadline" in ai_result:
                ai_result["processing_method"] = "ai_inference"
                ai_result["processed_at"] = datetime.now()
                return ai_result

        return {
            "error": "No deadline could be determined",
            "processing_method": "failed",
            "processed_at": datetime.now(),
        }

    def process_file(self, file_path_or_object, reference_date=None):
        """Process a file (PDF or image) and extract deadline information"""
        try:
            # Determine file type
            if hasattr(file_path_or_object, "name"):
                filename = file_path_or_object.name
                file_type = (
                    file_path_or_object.type
                    if hasattr(file_path_or_object, "type")
                    else None
                )
            else:
                filename = str(file_path_or_object)
                file_type = None

            # Extract text based on file type
            text = ""
            if file_type and file_type.startswith("image"):
                text = self.extract_text_from_image(file_path_or_object)
            elif file_type == "application/pdf" or filename.lower().endswith(".pdf"):
                text = self.extract_text_from_pdf(file_path_or_object)
            elif filename.lower().endswith((".jpg", ".jpeg", ".png", ".jfif")):
                text = self.extract_text_from_image(file_path_or_object)
            else:
                return {"error": f"Unsupported file type: {file_type or filename}"}

            if not text or text.startswith("Error"):
                return {"error": f"Could not extract text from file: {text}"}

            # Process the extracted text
            result = self.process_document(text, reference_date)

            # Add file metadata
            result["filename"] = filename
            result["file_type"] = file_type or "unknown"
            result["extracted_text"] = text[:500] + "..." if len(text) > 500 else text

            return result

        except Exception as e:
            return {"error": f"File processing error: {e!s}"}

    def batch_process_folder(self, folder_path, reference_date=None):
        """Process all supported files in a folder"""
        folder = Path(folder_path)
        if not folder.exists():
            return {"error": f"Folder not found: {folder_path}"}

        results = []
        supported_extensions = [".pdf", ".jpg", ".jpeg", ".png", ".jfif"]

        for file_path in folder.iterdir():
            if (
                file_path.suffix.lower() in supported_extensions
                and not file_path.name.startswith(".")
            ):
                result = self.process_file(file_path, reference_date)
                results.append(result)

        return {
            "total_files": len(results),
            "successful_extractions": len([r for r in results if "deadline" in r]),
            "results": results,
            "processed_at": datetime.now(),
        }

    def calculate_business_metrics(self, results, hourly_rate=75):
        """Calculate business impact metrics"""
        if isinstance(results, dict) and "results" in results:
            results_list = results["results"]
        else:
            results_list = results

        total_docs = len(results_list)
        successful = len([r for r in results_list if "deadline" in r])

        # Time savings calculation
        manual_time_per_doc = 15  # minutes
        ai_time_per_doc = 2  # minutes
        time_saved_per_doc = manual_time_per_doc - ai_time_per_doc

        total_time_saved_hours = (total_docs * time_saved_per_doc) / 60
        cost_savings = total_time_saved_hours * hourly_rate

        # Risk reduction
        missed_deadlines_prevented = successful * 0.15  # 15% would be missed manually
        avg_penalty_per_missed = 500  # EUR
        risk_reduction_value = missed_deadlines_prevented * avg_penalty_per_missed

        return {
            "total_documents": total_docs,
            "successful_extractions": successful,
            "success_rate": (successful / total_docs * 100) if total_docs > 0 else 0,
            "time_saved_hours": total_time_saved_hours,
            "cost_savings": cost_savings,
            "risk_reduction_value": risk_reduction_value,
            "total_value": cost_savings + risk_reduction_value,
            "processing_capacity_per_hour": 60 / ai_time_per_doc,
            "annual_value_projection": (cost_savings + risk_reduction_value) * 52,
        }


# Convenience functions for direct use
def create_agent():
    """Create a new DeadlineManagerAgent instance"""
    return DeadlineManagerAgent()


def process_text(text, reference_date=None):
    """Quick function to process text"""
    agent = create_agent()
    return agent.process_document(text, reference_date)


def process_file(file_path, reference_date=None):
    """Quick function to process a file"""
    agent = create_agent()
    return agent.process_file(file_path, reference_date)


def process_folder(folder_path, reference_date=None):
    """Quick function to process all files in a folder"""
    agent = create_agent()
    return agent.batch_process_folder(folder_path, reference_date)


# Example usage and testing
if __name__ == "__main__":
    # Test the agent
    agent = DeadlineManagerAgent()

    # Test with sample text
    test_cases = [
        "To Do: IES ACE - enviar declaração até 15 de abril",
        "To Do: SAF-T - entregar ficheiro até dia 25 do mês seguinte",
        "Deve responder no prazo de 15 dias úteis a partir desta notificação",
        "To Do: Declaração IVA - prazo trimestral",
    ]

    print("🧠 EY AI Challenge - Deadline Manager Agent Backend Test")
    print("=" * 60)

    for i, text in enumerate(test_cases, 1):
        print(f"\nTest {i}: {text}")
        result = agent.process_document(text)

        if "deadline" in result:
            print(f"✅ Deadline: {result['deadline'].strftime('%Y-%m-%d')}")
            print(f"   Rule: {result['rule']}")
            print(f"   Priority: {result['priority']}")
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")

    print(f"\n{'=' * 60}")
    print("✅ Backend testing complete!")
