import random
import matplotlib.pyplot as plt

# Simulate a stream of stock prices (simplified)
def generate_stock_data(days=100, trend=0.05, volatility=0.2):
    prices = [100]  # starting price
    for _ in range(days - 1):
        daily_return = random.gauss(trend, volatility)
        new_price = prices[-1] * (1 + daily_return)
        prices.append(new_price)
    return prices

# Simulated online learning model (basic linear regression with SGD)
class OnlineLinearRegression:
    def __init__(self, learning_rate=0.0001):
        self.weight = 0.0
        self.bias = 0.0
        self.lr = learning_rate

    def predict(self, x):
        return self.weight * x + self.bias

    def update(self, x, y):
        y_pred = self.predict(x)
        error = y - y_pred
        self.weight += self.lr * error * x
        self.bias += self.lr * error

# Generate synthetic stock price data
prices = generate_stock_data()

# Online learning: predict today's price from yesterday's price
model = OnlineLinearRegression(learning_rate=0.0001)
predictions = []
for i in range(1, len(prices)):
    x = prices[i - 1]  # yesterday's price
    y = prices[i]      # today's price

    y_pred = model.predict(x)
    predictions.append(y_pred)

    # Update the model
    model.update(x, y)

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(prices[1:], label='Actual Price')
plt.plot(predictions, label='Online Predicted Price')
plt.title("Online Learning of Stock Prices (Simplified)")
plt.xlabel("Day")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
