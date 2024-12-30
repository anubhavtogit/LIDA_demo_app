# LIDA-Cohere CSV Visualizer

## Overview
LIDA-Cohere CSV Visualizer is an innovative project that leverages Microsoft's **Language Integrated Data Analytics (LIDA)** framework and **Cohere's Large Language Model (LLM)** to process CSV files, generate insights, and create visualizations. The goal is to simplify data exploration and enable intuitive understanding of datasets.

---

## Features
- **Upload CSV Files**: Seamlessly upload CSV files for analysis.
- **Generate Insights**: Utilize Cohere LLM for generating meaningful insights from the data.
- **Interactive Visualizations**: Create charts, graphs, and other visualizations using LIDA’s powerful tools.
- **User-Friendly Interface**: An intuitive interface for data processing and visualization.

---

## Tech Stack
- **Microsoft LIDA**: For data processing and visualization.
- **Cohere LLM**: For generating insights and summarizing datasets.
- **Python**: Backend scripting.
- **Streamlit**: Frontend for creating an interactive web interface.

---

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- Pip

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/lida-cohere-csv-visualizer.git
   cd lida-cohere-csv-visualizer
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API keys for **Cohere** and **Microsoft LIDA**:
   - **Cohere**: Obtain an API key from [Cohere’s platform](https://cohere.ai/).
   - **LIDA**: Follow the official [LIDA setup guide](https://learn.microsoft.com/en-us/lida/).
   - Add these keys to a `.env` file in the following format:
     ```env
     COHERE_API_KEY=your_cohere_api_key
     LIDA_API_KEY=your_lida_api_key
     ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```
5. Open your browser and navigate to `http://localhost:8501`.

---

## Usage
1. **Upload File**: Upload a CSV file using the provided interface.
2. **Process Data**: View the dataset’s structure and insights generated by Cohere LLM.
3. **Visualize**: Select from various visualization options (bar charts, line graphs, pie charts, etc.) powered by LIDA.

---

## Example Workflow
1. Upload a CSV file containing sales data.
2. Receive a summary from Cohere LLM, such as "The dataset contains sales data from Q1 to Q4, with key metrics like revenue, profit, and customer count."
3. Choose to visualize revenue trends over time using LIDA’s line chart.

---

## Contributing
We welcome contributions to enhance the project! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to the branch:
   ```bash
   git commit -m "Add feature-name"
   git push origin feature-name
   ```
4. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Acknowledgements
- **Microsoft LIDA** for data integration and visualization tools.
- **Cohere** for advanced natural language processing capabilities.
- **Streamlit** for the user-friendly web interface.

---

## Contact
For questions, suggestions, or issues, feel free to open an issue in this repository or contact:
- **Your Name**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [github.com/your-username](https://github.com/your-username)

---

Happy Visualizing!

