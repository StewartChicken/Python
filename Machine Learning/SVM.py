import numpy as np

w = None
b = None

def fit(data_points):
    data = data_points
    opt_dict = {}

    transforms = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

    all_data = []
    for yi in data:
        for feature_set in data[yi]:
            for feature in feature_set:
                all_data.append(feature)

    max_feature_value = max(all_data)
    min_feature_value = min(all_data)

    step_sizes = [max_feature_value * 0.1, max_feature_value * 0.01, max_feature_value * 0.001]

    b_range_multiple = 5
    b_multiple = 5

    latest_optimum = max_feature_value * 10

    for step in step_sizes:
        w = np.array([latest_optimum], [latest_optimum])
        optimized = False
        while not optimized:
            for b in np.arange(-1 * (max_feature_value * b_range_multiple),
                max_feature_value * b_range_multiple, step * b_multiple):
                    for transformation in transforms:
                        w_t = w * transformation
                        found_option = True
                        for i in data:
                           for xi in data[i]:
                               yi = i
                               if not yi * (np.dot(w_t, xi) + b) >= 1:
                                   found_option = False

                        if(found_option):
                           opt_dict[np.linalg.norm(w_t)] = [w_t, b]

            if w[0] < 0:
                optimized = True
                print('Optimized a step')
            else:
                w = w - step
        norms = sorted([n for n in opt_dict])
        opt_choice = opt_dict[norms[0]]

        w = opt_choice[0]
        b = opt_choice[1]
        latest_optimum = opt_choice[0][0] + step * 2

def predict(features):
    classification = np.sign(np.dot(np.array(features), w) + b)
    return classification






