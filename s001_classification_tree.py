"""Decision tree classifier"""
from __future__ import absolute_import

import matplotlib.pyplot as plt
from scikitplot.metrics import plot_confusion_matrix
from sklearn.tree import DecisionTreeClassifier, plot_tree

from s000_import_data import get_data, data_prep


# Import data
data = get_data()

x_train, x_test, y_train, y_test = data_prep(data)

# Model definition
tree = DecisionTreeClassifier()

# Fit model
tree.fit(x_train, y_train)

# Test model
y_pred = tree.predict(x_test)

# Confusion matrix
plot_confusion_matrix(y_test, y_pred)
plt.show()

# Show tree
plot_tree(tree)
plt.show()