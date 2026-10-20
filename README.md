<div align="center">

# 📊 Sales Intelligence Dashboard

### End-to-End Sales Analytics Dashboard with Streamlit, Plotly, and Pandas

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.24+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![Pandas](https://img.shields.io/badge/Pandas-2.2+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)

<br>

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-00D4AA?style=for-the-badge&logo=streamlit&logoColor=white)](https://data-dashboard-srt343-z8hpwmaamvsucqn5jc5a4c.streamlit.app/)
[![GitHub](https://img.shields.io/badge/📦_Source_Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Asrt3131/data-dashboard-srt343)
[![Instagram](https://img.shields.io/badge/Instagram-@project__srt343-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/project_srt343)

<br>

[**🌐 View Live Demo**](https://data-dashboard-srt343-z8hpwmaamvsucqn5jc5a4c.streamlit.app/) · [**📂 Source Code**](https://github.com/Asrt3131/data-dashboard-srt343) · [**📸 Instagram**](https://instagram.com/project_srt343)

</div>

---

## 📸 Preview

<div align="center">
  <img src="assets/demo-screenshot.png" alt="Dashboard Preview" width="90%">
</div>

> 💡 To add an image: take a screenshot of the dashboard, save it in the `assets/` folder as `demo-screenshot.png`, and push it.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎯 Analysis & Visualization
- 📊 **6 Live KPIs** (Sales, Profit, Orders, Customers, Profit Margin, Avg Order Value)
- 📦 **Bar chart** of sales by category
- 🗺️ **Choropleth map** of US states
- 🔥 **Heatmap** of sales (Month × Year)
- 💸 **Discount impact analysis** on average profit
- 🏆 **Top 10 best-selling products**

</td>
<td width="50%">

### ⚙️ Technical & Architecture
- 📑 **4 separate pages** with `st.navigation`
- 🎨 **Custom dark theme** with CSS and `config.toml`
- ⚡ **Smart caching** with `@st.cache_data`
- 🔍 **Data explorer** with `st.form` and CSV download
- 🧹 **ETL pipeline** with Feature Engineering
- 📦 **Modular code** (reusable chart functions)

</td>
</tr>
</table>

---

## 🖥 Dashboard Pages

| Page | Icon | Description |
|------|-------|-------|
| **Overview** | 📊 | Key KPIs + category chart + regional profit share |
| **Trends** | 📈 | Sales time series + heatmap + best-selling products |
| **Geography** | 🗺️ | US states map + top 15 states ranking |
| **Data Explorer** | 🔍 | Advanced filters + raw data view + CSV download |

---

## 🛠 Technologies

<div align="center">

| Technology | Version | Purpose |
|:---------:|:-----:|--------|
| 🐍 **Python** | 3.12 | Core language |
| 🎈 **Streamlit** | 1.40+ | Dashboard framework |
| 📊 **Plotly** | 5.24+ | Interactive charts |
| 🐼 **Pandas** | 2.2+ | Data processing |
| 🔢 **NumPy** | 1.26+ | Numerical computing |

</div>

---

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Asrt3131/data-dashboard-srt343.git
cd data-dashboard-srt343

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run app.py
