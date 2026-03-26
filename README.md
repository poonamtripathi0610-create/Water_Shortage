# 💧 Water Shortage Prediction System

An AI- and ML-powered project that predicts **water availability** based on environmental and demographic factors. The system includes data analysis, model training (in a Jupyter Notebook), and an interactive **Streamlit web application** for real-time prediction.

---

## 📁 Project Structure

```
water_shortage/
│
├── app.py                          # Streamlit web application for predictions
├── water_shortage_analysis..ipynb  # Jupyter Notebook: EDA, data preprocessing & ML training
├── water_model.pkl                 # Pre-trained ML model (serialized with joblib)
├── water_data.xls                  # Generated dataset (Temperature, Population, Reservoir Level)
├── chennai_water.xls               # Real-world Chennai water supply data by zone/ward
├── climate.xls                     # Daily climate data (Date, Rain, Temp Max, Temp Min)
├── rainfall.xls                    # Monthly/annual rainfall data (1901 onwards)
└── water_shortage.zip              # Archive of project files
```

---

## 🔬 Project Workflow

### 1. Data Generation (`water_data`)
A synthetic dataset of **200 records** is programmatically generated using NumPy with:

| Feature          | Range                  |
|------------------|------------------------|
| Temperature (°C) | 15 – 45                |
| Population       | 10,000 – 1,000,000     |
| Reservoir Level  | 10 – 100 (%)           |

The **target variable** – `Water_Availability` – is computed using:

```
Water_Availability = -0.3 × Temperature + 0.7 × Reservoir_Level - 0.00005 × Population
```

This dataset is exported as `water_data.csv/xls`.

---

### 2. Real-World Datasets

| File               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `chennai_water.xls`| Ward-level water supply capacity and domestic consumption data for Chennai  |
| `climate.xls`      | Daily climate records: Date, Rainfall, Max Temp, Min Temp (from 1951)      |
| `rainfall.xls`     | Month-wise and annual total rainfall records (from 1901 onwards)           |

These datasets are loaded, cleaned (handling nulls), and merged for comprehensive analysis.

---

### 3. Data Preprocessing (Notebook)

Steps performed in the Jupyter Notebook:
- **Load** all four datasets using `pandas`
- **Strip column name whitespace** using `.str.strip()`
- **Drop rows with missing values** (`.dropna()`)
- **Forward-fill missing values** (`fillna(method='ffill')`)
- **Select only numeric columns** (`.select_dtypes(include=['number'])`)
- **Reset and merge indexes** for alignment
- **Normalize column names**: lowercase and replace spaces with underscores

---

### 4. Exploratory Data Analysis (EDA)

The notebook visualizes the cleaned dataset using:
- **Histograms** of all numeric features to understand distributions
- **Scatter plots** and **heatmaps** for feature relationships and correlation analysis
- **Bar charts** to visualize feature-level impact on water availability

Key columns analyzed:
```
['temperature', 'population', 'reservoir_level', 'water_availability']
```

---

### 5. Model Training (Notebook)

The notebook trains a **Machine Learning regression model** on the `water_data` features:

- **Features (X):** `temperature`, `population`, `reservoir_level`
- **Target (y):** `water_availability`

Steps:
1. Train/test split of the dataset
2. Model fitting (regression-based algorithm)
3. Model evaluation using standard metrics
4. **Model serialization** using `joblib` → saved as `water_model.pkl`

---

### 6. Streamlit Web Application (`app.py`)

An interactive dashboard allowing real-time water availability prediction.

#### 🖥️ Features

| Feature                    | Details                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------|
| **Interactive Sliders**    | Sidebar sliders let users input Temperature, Population, Reservoir Level, and Rainfall               |
| **Input Data Display**     | Shows a table of the entered input values                                                            |
| **Prediction Display**     | Displays the predicted Water Availability score                                                      |
| **Risk Classification**    | Interprets the prediction into 3 risk levels                                                         |
| **Feature Visualization**  | A bar chart displays the relative values of each input feature                                       |

#### 🚦 Risk Level Interpretation

| Prediction Score | Status                        |
|-----------------|-------------------------------|
| > 50            | ✅ Good Water Availability     |
| 20 – 50         | ⚠️ Moderate Water Availability |
| < 20            | ❌ High Risk of Water Shortage  |

#### 🔢 Input Parameters (Slider Ranges)

| Parameter         | Min    | Max       | Default  |
|-------------------|--------|-----------|----------|
| Temperature (°C)  | 10.0   | 50.0      | 30.0     |
| Population        | 10,000 | 1,000,000 | 500,000  |
| Reservoir Level % | 0.0    | 100.0     | 50.0     |
| Rainfall (mm)     | 0.0    | 500.0     | 100.0    |

> **Note:** The model was originally trained without the `rainfall` feature. The app has a fallback that drops `rainfall` if the loaded model does not accept it — ensuring backward compatibility.

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.7+
- pip

### Install Dependencies

```bash
pip install streamlit pandas numpy joblib matplotlib seaborn scikit-learn
```

### Run the Web Application

```bash
streamlit run app.py
```

Open your browser and go to: [http://localhost:8501](http://localhost:8501)

### Run the Notebook

Launch Jupyter and open the notebook:

```bash
jupyter notebook "water_shortage_analysis..ipynb"
```

---

## 🧪 Tech Stack

| Technology      | Purpose                                      |
|-----------------|----------------------------------------------|
| Python          | Core programming language                    |
| pandas          | Data loading, cleaning, and manipulation     |
| NumPy           | Synthetic data generation and math ops       |
| matplotlib      | Data visualization                           |
| seaborn         | Statistical plots and heatmaps               |
| scikit-learn    | Machine learning model training              |
| joblib          | Model serialization and loading              |
| Streamlit       | Interactive web application framework        |
| Jupyter Notebook| Exploratory analysis and model training      |

---

## 🔄 End-to-End Data Flow

```
Raw Data Sources                 Jupyter Notebook                 Streamlit App
──────────────────               ─────────────────                ─────────────
chennai_water.xls  ──►           Load Datasets        ──►
climate.xls        ──►           Clean & Merge        ──►         Load water_model.pkl
rainfall.xls       ──►           EDA & Visualization  ──►
water_data.xls     ──►           Train ML Model       ──►         User Inputs via Sliders
                                 Save water_model.pkl ──►         Predict Water Availability
                                                                   Display Risk Level + Chart
```

---

## 📊 Sample Prediction Scenario

| Input               | Value   |
|---------------------|---------|
| Temperature         | 35°C    |
| Population          | 600,000 |
| Reservoir Level     | 40%     |
| Rainfall            | 80mm    |
| **Predicted Score** | ~8.5    |
| **Status**          | ⚠️ Moderate Water Availability |

---

## 📝 Notes

- The model is trained on **synthetic data** derived from a mathematical formula; predictions are approximations.
- Real-world accuracy would require training on verified historical water supply and demand data.
- The `rainfall` column was added as a new feature post-training; the app gracefully handles this with a try/except block.

---

## 📌 Future Improvements

- Train on larger, verified real-world datasets
- Add more environmental features (humidity, groundwater level, etc.)
- Integrate time-series forecasting for seasonal water availability
- Add map visualization for geographic water availability

---

*AI-based Water Resource Management System 💡*
