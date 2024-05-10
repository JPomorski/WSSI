import numpy as np
from collections import Counter


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None


class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):
        if not self.n_features:
            self.n_features = X.shape[1]
        else:
            self.n_features = min(X.shape[1], self.n_features)

        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        if depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split:
            counter = Counter(y)
            node_value = counter.most_common(1)[0][0]
            return Node(value=node_value)

        feat_idxs = np.random.choice(n_features, self.n_features, replace=False)

        best_feature, best_threshold = self._best_split(X, y, feat_idxs)
        left_indices, right_indices = self._split(X[:, best_feature], best_threshold)

        left_children = self._grow_tree(X[left_indices, :], y[left_indices], depth + 1)
        right_children = self._grow_tree(X[right_indices, :], y[right_indices], depth + 1)

        return Node(best_feature, best_threshold, left_children, right_children)

    def _best_split(self, X, y, feat_idxs):
        best_gain = -1
        index = None
        threshold = None

        for idx in feat_idxs:
            X_column = X[:, idx]
            thresholds = np.unique(X_column)

            for thr in thresholds:
                gain = self._information_gain(y, X_column, thr)

                if gain > best_gain:
                    best_gain = gain
                    index = idx
                    threshold = thr

        return index, threshold

    def _information_gain(self, y, X_column, threshold):
        parent_entropy = self._entropy(y)
        left_indices, right_indices = self._split(X_column, threshold)

        if len(left_indices) == 0 or len(right_indices) == 0:
            return 0

        n = len(y)
        n_left, n_right = len(left_indices), len(right_indices)

        left_entropy, right_entropy = self._entropy(y[left_indices]), self._entropy(y[right_indices])
        child_entropy = (n_left / n) * left_entropy + (n_right / n) * right_entropy

        information_gain = parent_entropy - child_entropy
        return information_gain

    @staticmethod
    def _split(X_column, split_thresh):
        left_indices = np.argwhere(X_column <= split_thresh).flatten()
        right_indices = np.argwhere(X_column > split_thresh).flatten()

        return left_indices, right_indices

    @staticmethod
    def _entropy(y):
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p * np.log(p) for p in ps if p > 0])

    def _traverse_tree(self, x, node):
        pass

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])
