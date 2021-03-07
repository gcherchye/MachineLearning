"""Decision tree classifier"""
from __future__ import absolute_import

from s000_import_data import get_data, data_prep


# Import data
data = get_data()

x_train, x_test, y_train, y_test = data_prep(data)

# Model definition
