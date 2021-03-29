"""Decision tree classifier"""
from __future__ import absolute_import

import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

from tools.import_data import get_data, data_prep


# Import data
data = get_data()

x_train, x_test, y_train, y_test = data_prep(data)

# Model definition
tree = DecisionTreeClassifier(
    max_depth=3
)

# Fit model
tree.fit(x_train, y_train)

# Test model
y_pred = tree.predict(x_test)


# Show tree
plot_tree(tree)
plt.show()
