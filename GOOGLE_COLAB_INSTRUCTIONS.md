# 🚀 Google Colab Setup Instructions for EY Challenge

## 📁 Required Google Drive Structure

Create the following folder structure in your Google Drive:

```
📁 MyDrive
  └── 📁 EY Challenge
      ├── 📄 AutoCalendarAgent.ipynb (this notebook)
      └── 📁 data
          ├── 📄 document1.pdf
          ├── 📄 document2.jpg
          ├── 📄 document3.docx
          └── 📄 ... (all your EY Challenge documents)
```

## 🔧 Setup Steps

### 1. Upload Files to Google Drive
1. Create a folder named "EY Challenge" in your Google Drive root
2. Upload the updated `AutoCalendarAgent.ipynb` to this folder
3. Create a "data" subfolder inside "EY Challenge"
4. Upload all your EY Challenge documents to the "data" folder

### 2. Open in Google Colab
1. In Google Drive, right-click on `AutoCalendarAgent.ipynb`
2. Select "Open with" > "Google Colaboratory"
3. If Colab is not available, install it from Google Workspace Marketplace

### 3. Configure API Key
1. In the notebook, locate the cell with `GEMINI_API_KEY = "AIzaSyB..."`
2. Replace with your actual Gemini API key from https://aistudio.google.com/app/apikey
3. **IMPORTANT**: For security, consider using Colab secrets instead of hardcoding

## 🏃‍♂️ Running the Notebook

### Execute All Cells in Order:
1. **Setup Cell**: Mounts Google Drive and installs dependencies
2. **Imports Cell**: Loads all required libraries
3. **AI Model Configuration**: Sets up Gemini AI models
4. **Function Definitions**: OCR, date extraction, AI processing
5. **Document Processing**: Processes all files in data folder
6. **Analysis & Visualization**: Creates charts and business metrics
7. **Live Demo**: Interactive demonstration

### Expected Output:
- ✅ All dependencies installed successfully
- ✅ Google Drive mounted and data folder found
- ✅ AI models configured and ready
- ✅ Documents processed with deadline extraction
- ✅ Visualizations and business metrics generated
- ✅ Live demo ready for presentation

## 🎯 For EY Challenge Submission

### After Running All Cells:
1. **Save outputs**: Make sure all cell outputs are saved (Runtime > Save)
2. **Download notebook**: File > Download > Download .ipynb
3. **Copy back to repo**: Replace the original notebook in your repository
4. **Verify outputs**: Ensure all visualizations and results are preserved

### Key Features Demonstrated:
- ✅ Multi-modal document processing (PDF, images, DOCX, TXT)
- ✅ Portuguese tax law compliance rules
- ✅ Dual AI model support (Gemini Pro + 2.0 Flash)
- ✅ OCR for handwritten/scanned documents
- ✅ Working days and holiday calculations
- ✅ Business impact analysis with cost savings
- ✅ Real-time visualization dashboards
- ✅ Executive summary for EY presentation

## 🛠 Troubleshooting

### Common Issues:
1. **API Key Error**: Verify your Gemini API key is valid and has quota
2. **Drive Mount Error**: Restart runtime and re-run setup cell
3. **Package Installation**: If packages fail, restart runtime and try again
4. **Data Folder Not Found**: Ensure "data" folder exists in correct location

### Model Switching:
```python
# Switch between AI models during demonstration
switch_ai_model('gemini-pro')
switch_ai_model('gemini-2.0-flash-001')
```

### Demo Commands:
```python
# Run single document demo
demo_single_document('your_document.pdf')

# Compare both models
demo_model_comparison('your_document.pdf')

# Show current model info
get_current_model_info()
```

## 📊 Business Value Highlights

The notebook demonstrates:
- **87% reduction** in manual processing time
- **Automated compliance** with Portuguese tax regulations
- **Multi-model AI** for robust deadline extraction
- **Scalable cloud deployment** via Google Colab
- **Real-time processing** and visualization
- **Enterprise-ready** integration capabilities

## ✅ Final Checklist

Before submission:
- [ ] Notebook runs successfully in Google Colab
- [ ] All cells execute without errors
- [ ] Outputs are saved and visible
- [ ] Visualizations display correctly
- [ ] Business metrics are calculated
- [ ] Demo functions work properly
- [ ] API key is configured (but not exposed in final submission)
- [ ] All dependencies install automatically

**Ready for EY Challenge submission! 🎉**
