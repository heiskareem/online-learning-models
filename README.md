# 📈 Online Learning for Stock Price Prediction (From Scratch)

This project demonstrates how **online learning** can be applied to a streaming data scenario using a **simplified stock price prediction task**. The model is implemented from scratch using a basic **linear regression with stochastic gradient descent (SGD)**. It learns and updates **one data point at a time**, mimicking how systems operate in real-time environments.

---

## 🎯 Objective
Predict today's stock price using only **yesterday's price** — and improve the model incrementally as new prices arrive.

---

## ⚙️ How It Works

### 🔁 Data Simulation
- We generate synthetic stock price data for 100 days.
- Prices follow a random walk with a slight upward trend and noise.

### 🧠 Online Learning Model
- A basic linear regression model is created with:
  - One weight (slope)
  - One bias (intercept)
- The model predicts today’s price using:
  ```python
  y_pred = weight * yesterday_price + bias
  ```
- After each prediction, it updates its parameters using one sample at a time.
  ```python
  error = actual_price - predicted_price
  weight += learning_rate * error * x
  bias += learning_rate * error
  ```

---

## 📉 Visualization
The output plot shows:
- The actual stock price over time (blue line)
- The predicted price from the online model (orange line)

As time progresses, the model **learns from its mistakes** and **begins to track the true stock price more closely**.

---

## 📌 Key Concepts Demonstrated
| Concept              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Online Learning**   | Updates model one sample at a time                                          |
| **Stochastic Gradient Descent (SGD)** | Lightweight, fast, and memory-efficient                           |
| **Streaming Data**    | Simulates real-time updates like in finance or IoT systems                  |
| **Adaptability**      | Model continuously adapts to new information without full retraining        |

---

## 📚 Example Use Cases
- Stock market prediction
- IoT sensor analytics
- News and sentiment streaming
- Real-time anomaly detection

---

## 🐍 Requirements
- Python 3.x
- matplotlib (for visualization)

---

## ✅ Output Snapshot
You will see a dynamic plot comparing actual vs predicted stock prices as the model learns in real time.

---

## ✍️ Author
KareemShaik.com
