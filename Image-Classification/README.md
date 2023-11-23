# Image Identification in PyTorch

This project focuses on implementing a neural network (multi-layer perceptron) for classifying hand-written digits using PyTorch.

## Purpose
The goal is to develop a robust neural network model capable of accurately classifying hand-written digits. The implementation involves creating, training, and evaluating the neural network using the popular MNIST dataset.

## Project Structure
The project is structured into various sections, covering key aspects of the implementation.

### 1. Imports
The necessary libraries and modules are imported, including PyTorch components (`torch`, `torch.nn`, `torch.optim`), datasets, and optional visualization tools (`matplotlib`).

### 2. PyTorch Data Types
An introduction to PyTorch data types, emphasizing the use of tensors to represent multi-dimensional arrays.

### 3. Representing Images as Tensors
Explains the process of representing images as tensors, a crucial step for inputting data into the neural network.

### 4. Hyperparameters
Defines hyperparameters used in the project, such as learning rate and the number of hidden layer units.

### 5. Importing the Data
Demonstrates the importation of the MNIST dataset, along with data transformations and the use of `DataLoader` for efficient data handling.

### 6. Creating the Neural Network
Defines a simple neural network class (`SimpleNN`) with an explanation of the structure, including input, hidden, and output layers.

### 7. Creating an Instance of the Module
Instantiates a neural network from the defined class (`SimpleNN`).

### 8. Defining the Optimizer and Loss Function
Sets up the optimizer (Stochastic Gradient Descent) and loss function (Negative Log Likelihood) for model training.

### 9. Training/Validation Loop
Implements the training loop, including epochs, forward and backward passes, and model optimization. Also evaluates the model on the validation (test) dataset.

### 10. Using our Model
Demonstrates how to utilize the trained model for handwritten digit recognition, showcasing a sample image's prediction.

## Results
The project concludes by displaying the accuracy achieved by the model on the test dataset, indicating the success of the implemented neural network in classifying hand-written digits.

**Note**: This README provides an overview of the project structure and key components. For detailed code implementation, refer to the original code [here](https://github.com/Onyelechie/Artificial-Intelligence-Projects/blob/main/Image-Classification/Image_Identification_in_Pytorch.ipynb?short_path=515f21c).

