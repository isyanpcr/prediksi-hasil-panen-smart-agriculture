# Smart Agriculture Crop Prediction using Machine Learning

This project is a machine learning-based smart agriculture system developed to predict irrigation needs and crop condition using environmental sensor data. The project utilizes data preprocessing, exploratory data analysis (EDA), feature engineering, and multiple machine learning models to support precision agriculture and improve farming decision-making.

The system helps farmers predict irrigation requirements based on soil conditions, environmental factors, and seedling growth stages.

---

## Project Title

“Crop Yield Prediction Using Smart Agriculture Sensor Data”

---

## Background

Precision agriculture using IoT sensors and data analytics provides significant opportunities to improve crop prediction accuracy. Accurate predictions help farmers and policymakers plan agricultural inputs, reduce crop failure risks, and improve food security through more efficient resource allocation.

This project focuses on utilizing smart agriculture sensor data such as:
- Soil Type
- Moisture Index (MOI)
- Temperature
- Humidity
- Seedling Stage

to predict irrigation requirements and crop conditions before harvesting.

The project is highly relevant to Indonesia, where agricultural productivity still depends heavily on manual field decisions. This system aims to support small and medium-scale farmers through data-driven recommendations.

---

## Objectives

- Develop a machine learning model for predicting irrigation needs using smart agriculture sensor data.
- Identify the most influential features affecting prediction results.
- Provide practical recommendations for farmers based on prediction outcomes.
- Support precision agriculture implementation using data analytics and machine learning.

---

## Dataset Information

### Dataset Title
Smart Agriculture Dataset

### Dataset Source
Kaggle

### Dataset Link
https://www.kaggle.com/datasets/chaitanyagopidesi/smart-agriculture-dataset/data

### Dataset Size
- 16,411 records
- 768 KB

---

## Dataset Features

| Feature | Description |
|---|---|
| crop ID | Unique identifier for each crop/sample |
| soil_type | Type of soil where the crop grows |
| Seedling Stage | Growth stage of the crop |
| MOI | Soil Moisture Index |
| temp | Environmental temperature (°C) |
| humidity | Air humidity (%) |
| result | Irrigation requirement label |

### Target Label
- 1 = Requires Irrigation
- 0 = Does Not Require Irrigation

### Data Types
#### Numerical Features
- MOI
- temp
- humidity
- result

#### Categorical Features
- crop ID
- soil_type
- Seedling Stage

---

## Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

### Machine Learning Models
- Decision Tree
- Random Forest
- K-Nearest Neighbor (KNN)
- XGBoost

---

## Exploratory Data Analysis (EDA)

The project includes several EDA stages:

- Basic statistical analysis
- Feature distribution visualization
- Correlation heatmap analysis
- Outlier identification
- Class imbalance analysis

### Key Insights

- The dataset contains no missing values.
- The target class distribution is imbalanced.
- MOI is the most influential feature for irrigation prediction.
- Temperature and humidity also contribute significantly.
- Soil type and seedling stage provide important contextual information.

---

## Data Preprocessing

Several preprocessing techniques were applied:

### Handling Missing Values
The dataset contains no missing values.

### Encoding Categorical Features
Label Encoding was used for:
- crop ID
- soil_type
- Seedling Stage

### Feature Scaling
StandardScaler was applied to:
- MOI
- temp
- humidity

### Feature Selection
SelectKBest with mutual information was used to identify important features.

### Train-Test Split
Dataset split ratio:
- 80% Training Data
- 20% Testing Data

---

## Machine Learning Models

### Decision Tree
Decision Tree achieved:
- Accuracy: 0.994

### Random Forest
Random Forest achieved:
- Accuracy: 0.988

### K-Nearest Neighbor (KNN)
KNN achieved:
- Accuracy: 0.947

### XGBoost
XGBoost showed excellent performance:
- Accuracy: 1.00
- ROC-AUC: 0.9999

---

## Model Evaluation

Evaluation metrics used:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

The models demonstrated excellent classification performance for smart agriculture prediction tasks.

---

## Deployment Features

### Prediction Form

The prediction form allows users to input:
- Crop Type
- Soil Type
- Seedling Stage
- MOI
- Temperature
- Humidity

The system predicts:
- No Irrigation Needed
- Irrigation Needed
- High Irrigation Priority

The application also stores prediction history using a local database.

---

## Dashboard Features

The dashboard provides:
- Dataset statistics
- Class distribution visualization
- Feature importance analysis
- Model comparison charts
- Confusion matrix visualization
- Prediction monitoring

The dashboard is designed to help users understand model performance and agricultural conditions interactively.

---

## Best Model Result

Based on evaluation results:

| Model | Accuracy |
|---|---|
| Random Forest | 0.9868 |
| Decision Tree | 0.9625 |
| KNN | 0.9509 |

Random Forest was selected as the best model due to its stability, robustness, and high accuracy.

---

## Most Influential Features

The most important features identified by the Random Forest model are:
- Soil Type
- Seedling Stage
- MOI (Moisture Index)
- Temperature

These features strongly influence irrigation prediction results.

---

## Limitations

- Model performance depends heavily on historical data patterns.
- Real-time field testing has not yet been implemented.
- The project does not include real-time location and temporal analysis.
- Additional external validation is still required.

---

## Future Improvements

Potential future developments include:
- Real-time IoT integration
- Real-time environmental monitoring
- Advanced imbalance handling techniques
- More interactive dashboards
- Automatic recommendation systems for farmers
- Integration with mobile applications

---

## Project Scope

### Included
- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Machine learning modeling
- Model evaluation
- Dashboard visualization
- Prediction system deployment

### Not Included
- Additional field data collection
- Real-time location-based analysis
- Real-time sensor deployment

---

## Installation

Clone the repository:

```bash
git clone https://github.com/username/smart-agriculture-prediction.git
```

Go to project directory:

```bash
cd smart-agriculture-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## Project Structure

```bash
smart-agriculture-prediction/
│
├── dataset/
├── models/
├── notebooks/
├── app/
├── static/
├── templates/
├── requirements.txt
└── README.md
```

---

## Conclusion

This project successfully developed a machine learning-based smart agriculture prediction system using environmental sensor data. Random Forest achieved the best performance with an accuracy of 0.9868, demonstrating that machine learning can effectively support precision agriculture and irrigation decision-making.

The project also highlights the importance of proper preprocessing, feature engineering, and model selection in building reliable prediction systems for agriculture.

---

## License

This project was developed for academic and educational purposes.
