# Machine Learning Algorithms

Welcome to the **Machine Learning Algorithms** repository! This repository contains various fundamental machine learning algorithms implemented in Python using Jupyter Notebooks.

## Repository Overview
This repository includes the following algorithms:

1. **Find-S Algorithm** - A simple algorithm for learning the most specific hypothesis from a given dataset.  
   **Complexity:** O(n * m), where n is the number of training examples and m is the number of attributes.

2. **Linear Regression Algorithm** - A statistical method used to model relationships between dependent and independent variables.  
   **Complexity:** O(n * m^2) for normal equation; O(n * m) for gradient descent.

3. **Candidate Elimination Algorithm** - An algorithm used in concept learning to find the version space.  
   **Complexity:** O(n * h), where n is the number of training examples and h is the hypothesis space size.

4. **Decision Tree Algorithm** - A supervised learning algorithm used for classification and regression tasks.  
   **Complexity:** O(n * m log m), where n is the number of examples and m is the number of features.

5. **K-Nearest Neighbor (KNN)** - A non-parametric algorithm used for classification and regression based on feature similarity.  
   **Complexity:** O(n * m) for training (storing data) and O(k * m) for query time, where k is the number of neighbors.

6. **Perceptron for OR Gate** - A single-layer perceptron implementation for simulating an OR gate.  
   **Complexity:** O(n * m), where n is the number of training examples and m is the number of attributes.

7. **Naive Bayes Algorithm** - A probabilistic classifier based on Bayes' theorem, used for classification tasks.  
   **Complexity:** O(n * m), where n is the number of training examples and m is the number of features.

8. **K-Means Algorithm** - An unsupervised learning algorithm used for clustering data points into K clusters.  
   **Complexity:** O(n * k * i), where n is the number of data points, k is the number of clusters, and i is the number of iterations.

## Getting Started
### Prerequisites
To run these notebooks, ensure you have the following installed:
- Python 3.x
- Jupyter Notebook
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

You can install the necessary libraries using:
```bash
pip install numpy pandas scikit-learn matplotlib
```

### Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/patelmj04/machine-learning-algorithms.git
   ```
2. Navigate to the repository:
   ```bash
   cd machine-learning-algorithms
   ```
3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Open any `.ipynb` file and run the cells to execute the algorithm.

## Contributing
Contributions are welcome! If you'd like to improve the implementations or add new algorithms, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
**Mit Patel**  
GitHub: [patelmj04](https://github.com/patelmj04)

Happy coding! 🚀

