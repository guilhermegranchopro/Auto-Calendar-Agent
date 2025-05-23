![alt text](https://github.com/EYAIChallenge/Overview/blob/main/Banner-EY-1280x640.jpg "EY AI Challenge")

<h1 align="center"> <img src="https://github.com/EYAIChallenge/Overview/blob/main/EY_Logo_Beam_RGB_White_Yellow.png" width="40" alt="Logo"/> AI Challenge 2025 | Auto Calendar Deadline Manager Agent Challenge </h1>

---

## 🧠 Description

In this challenge, your team will support **Tax Service** client by designing an **AI-powered agent** capable of managing and interpreting deadlines from **diverse input channels**.  

Tax professionals regularly receive time-sensitive obligations through various means:
- Scanned letters from tax authorities  
- Client emails  
- WhatsApp messages  
- SMS  
- Handwritten notes
- [...]

Your goal is to develop a solution that can **ingest multimodal inputs**, **extract or infer relevant deadlines**, and produce **structured output** to enhance:
- Operational efficiency  
- Risk reduction  
- Regulatory compliance  

Many real-world deadlines are **not explicitly stated**. For example:  
> “You must reply within 5 business days from the date of this notification.”

Your AI agent must:
- Determine the **base date**
- Apply **Portuguese legal logic** (e.g., *Código de Procedimento e de Processo Tributário*, *Código do Procedimento Administrativo*)  
- Produce an **accurate due date**

This simulates a **real consulting engagement** where you must deliver both a prototype and a strategic pitch to showcase its business value.

---

## 🗃️ Dataset

You will receive **25 multimodal inputs**, including:
- 📄 10 scanned letters  
- ✉️ 10 plain text emails  
- 📱 10 WhatsApp screenshots  
- ✍️ 10 handwritten notes or scribbles  

Each document contains **explicit or implicit tax-related deadlines**, often requiring nuanced interpretation.

---

## 🧭 Consulting Mindset Expectations

- **Legal Logic Designers**  
  Create a system that understands procedural rules and deadline logic from **Portuguese tax law**.

- **Multi-Modal Integrators**  
  Unify **text, image**, and possibly **audio** inputs to produce **actionable intelligence**.

- **Efficiency Catalysts**  
  Build tools that **save time**, **reduce manual error**, and **streamline EY’s deadline management**.

- **Strategic Communicators**  
  Present your solution as a **business asset** that can be **adopted and scaled** by tax professionals.

---

## 📦 Deliverables

- ✅ A **working prototype** of your AI-powered deadline assistant  
- ✅ **Modular, clean, and well-documented code**  
- ✅ A **consulting-style presentation** to EY executives  
- ✅ *(Optional)* (Optional) It’s a major plus if your presentation includes a brief live demo to showcase how the solution works in practice, you can even present over it.  
- ✅ *(Optional)* Provide metrics like:
  - ⏱ Average processing time  
  - ❌ Error rate reduction  
  - 📚 Legal coverage scope  

<h2 align="center"> ⚠️ **Important Submission Requirement** ⚠️ </h2>
<h3> ✅ Before the 4-hour deadline</h3>

Submit a **zip folder** with:
- The **Google Colab notebook** (with all cells run & outputs shown)
- **Screenshots** of any external tools or visualizations you used
- **Email it to**: [eyaichallenge@pt.ey.com](mailto:eyaichallenge@pt.ey.com)  
- **Subject**: `AutoCalendarDeadlineManagerAgent – GroupName`  
- Include **group member names** in the email  
- 📁 Only **one submission per group**

---

## 💡 Tips for Competitors

- **Understand the Business Challenge**  
  Research what types of obligations exist (e.g., notifications from AT), and how deadlines are calculated.

- **Design for Ambiguity**  
  Handle **incomplete inputs**, **conflicting messages**, and **uncertainty**

- **Combine Rule Engines + LLMs**  
  Combine deterministic logic (rules, calendars, holiday lookups) with natural language understanding.

- **Visualize Time**  
  Consider timeline visualizations like:
  - 📅 Calendar views  
  - 📊 Gantt charts  
  - 🚨 Deadline alerts  

- **Validate Relentlessly**  
  Address:
  - ❗ False positives  
  - 🤖 Mesread text  
  - 🔄 Conflicting data sources  

---

## 🛠 Tech & Tools

🚨 **Mandatory**:  
It is mandatory to develop the solution in Google Colab using Python.

Other than that, you are completely free to choose your own:

- **🔧 Libraries**  
  `LangChain`, `Pandas`, OCR(`Tesseract`), `dateparser`, `calendar` APIs, etc.

- **📈 Visualization Tools**  
  `Streamlit`, `Dash`, `Power BI`, etc.

- **🤖 AI Assistants**  
  `ChatGPT`, `GitHub Copilot`, `Gemini`, etc.

> 💥 Use any tools that enhance **speed, accuracy, or creativity**

---

## ⏱ Time Management & Rules

- ⏳ You have **4 hours** to complete the challenge  
  🔒 **No extensions**

- 🗣 Present your solution in a **5-minute pitch**, simulating a client-facing demo

- 👥 Each group is allowed:
  - `1` **technical support** session (up to 5 minutes)  
  - `1` **business guidance** session (up to 5 minutes)

> 🚫 Assistants won’t provide direct solutions  
> 🧠 They’re here to **help you think and overcome blockers**

---

## 💬 Final Thought

This challenge reflects a growing need in professional services: automating complexity. Your solution has the potential to not only increase compliance accuracy, but also free up human capital for higher-value tasks. Think like consultants — design something practical, strategic, and future-ready.

---

### 🏁 Brought to you by **EY AI Challenge**
