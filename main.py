import numpy as np

# Benetton dataset
advertising = np.array([23, 26, 30, 34, 43, 48, 52, 57, 58])
sales = np.array([651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518])

# Calculate the mean of advertising and sales
mean_advertising = np.mean(advertising)
mean_sales = np.mean(sales)

# Calculate the parameters beta1 and beta0
numerator = np.sum((advertising - mean_advertising) * (sales - mean_sales))
denominator = np.sum((advertising - mean_advertising) ** 2)
beta1 = numerator / denominator
beta0 = mean_sales - beta1 * mean_advertising

print(f"Regression Equation: Sales = {beta0:.2f} + {beta1:.2f} * Advertising")

# Five new advertising
new_advertising_values = np.array([20, 35, 45, 55, 60])

# Predict sales for the new advertising values
predicted_sales = beta0 + beta1 * new_advertising_values

# Print the predictions
for i in range(len(new_advertising_values)):
    print(f"Predicted Sales for Advertising = {new_advertising_values[i]}: {predicted_sales[i]:.2f}")