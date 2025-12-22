# Student Performance Predictor

A simple Python project that predicts whether a student is likely to pass or fail based on study hours, sleep hours, and previous marks using **Logistic Regression**.

---

## 📌 Features

- Predicts **PASS/FAIL** for a student.
- Provides **confidence probability** for the prediction.
- Uses **NumPy** for data handling and **Scikit-Learn** for machine learning.
- Simple **terminal-based interface** (no GUI required).

---

## 🛠 Technologies Used

- **Python 3**
- **NumPy** – for array handling
- **Scikit-Learn** – for Logistic Regression
- **tkinter** (optional, if GUI added later)

---

## 🔹 How it Works

1. The dataset consists of:
   - Hours studied
   - Hours slept
   - Previous marks  
   - Label: 1 (Pass), 0 (Fail)

2. Logistic Regression model is trained on the dataset.

3. User provides inputs for a new student:
   - Hours studied
   - Hours slept
   - Previous marks

4. Model predicts if the student will pass or fail and outputs **confidence probability**.

---

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/15-day-AIML-challenge.git
