#Linear Regression class which has the capability to output the slope, y-intercept, and coefficient of determination of a set of data

#Finds slope
def find_M(X, y):
    return (  (mean(X) * mean(y)) - (mean_mult(X, y))  ) / (  (mean(X) ** 2) - mean_power(X)  )

#Finds y-intercept
def find_B(X, y, slope):
    return mean(y) - slope * (mean(X))

#Returns the mean of all the X-values squared
def mean_power(X):
    product_sum = 0
    for i in X:
        product_sum += i ** 2;

    return (float)(product_sum) / (float)(len(X))

#Returns the mean of the product of all the X and y values
def mean_mult(X, y):
    product_sum = 0

    for i in range(len(X)):
        product_sum += X[i] * y[i]

    return (float)(product_sum) / (float)(len(X))

#Returns the mean of a list of data
def mean(data):
    sum = 0.0
    for point in data:
        sum += point
    return sum / len(data)

#Predicts Y coordinate from a user-input X-coordinate
def predict_YCoor(X, y, xCoor):
    slope = find_M(X, y)
    return (xCoor * slope) + find_B(X, y, slope)

#Finds the squared error between predicted and observed data lists
def squared_error(predicted, observed):
    sum = 0.0
    for i in range(len(predicted)):
        sum += (observed[i] - predicted[i]) ** 2

    return sum

#Calculates the squared error between the mean of the observed data and the list of observed data
def mean_squared_error(mean_value, observed):
    sum = 0.0

    for i in range(len(observed)):
        sum += (observed[i] - mean_value) ** 2

    return sum

#Calculates the coefficient of determination
def r_squared(predicted, observed):
    y_hat_squared_error = squared_error(predicted, observed)
    mean_value = mean(observed)

    y_mean_squared_error = mean_squared_error(mean_value, observed)

    return 1.0 - (y_hat_squared_error / y_mean_squared_error)

#Outputs the linear regression equation and the coefficient of determination
def get_data_info(X, y):
    m = find_M(X, y)
    b = find_B(X, y, m)

    predicted_points = []

    for point in range(len(X)):
        predicted_points.append(predict_YCoor(X, y, X[point]))

    R_2 = r_squared(predicted_points, y)

    print("The linear regression function of this data is: y^ = " + (str)(m) + "x + " + (str)(b) + " and the coefficient of determination is " + (str)(R_2))


