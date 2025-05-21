# 🧠 Fashion MNIST Classification with Optuna Hyperparameter Tuning (PyTorch)



> 🚀 This project demonstrates how to use **Optuna** for automated hyperparameter tuning to boost the performance of a PyTorch-based neural network on the **Fashion MNIST** dataset.

---

## 📌 Project Summary

This repository contains a complete pipeline for:

- Visualizing Fashion MNIST images
- Preprocessing and splitting data
- Defining a custom `Dataset` class for loading
- Building a fully connected neural network with dynamic architecture
- Automatically tuning hyperparameters using **Optuna**
- Comparing different optimizers (Adam, SGD, RMSProp)
- Evaluating model accuracy

---

## 🧠 Key Features

✅ Custom PyTorch `Dataset` class  
✅ Neural network built using `nn.Sequential`  
✅ Configurable layers, neurons, dropout  
✅ Supports **Adam, SGD, RMSprop** optimizers  
✅ Uses `CrossEntropyLoss` for classification  
✅ Dynamic **batch sizes**, **learning rates**, **dropouts**, and **hidden layers** via **Optuna**  
✅ Uses `train_test_split` from scikit-learn  
✅ GPU support using `cuda` if available  
✅ Visualization of first 16 images from dataset using `matplotlib`

---



## 🔍 Hyperparameters Tuned with Optuna

| Parameter         | Search Space                         |
|------------------|--------------------------------------|
| `num_hidden_layers` | 1 to 5                            |
| `neurons_per_layers` | 8 to 128 (step 8)               |
| `dropout_rate`      | 0.1 to 0.5 (step 0.1)            |
| `epochs`            | 10 to 100 (step 10)              |
| `lr` (learning rate)| 1e-5 to 1e-1 (log scale)         |
| `batch_size`        | 16, 32, 64, 128                   |
| `weight_decay`      | 1e-5 to 1e-3 (log scale)         |
| `optimizers`        | Adam, RMSprop, SGD               |

---

## 📊 Best Accuracy Result

Accuracy Obtained on test data of 10000 samples is 85%(APPROX.)

and that on 60000 samples is 90% (APPROX.)


## 🤝 Connect & Contribute

### 🔗 Ways to Get Involved:

- **Fork the Repository:** [Click here to fork](https://github.com/CGMAPS1/Mini-Project-Optuna-Pytorch-/fork) and try it out yourself!
- **Star the Repo:** ⭐ Show support by starring this project.
- **Raise Issues & PRs:** Found a bug or want to improve something? Open an [issue](https://github.com/CGMAPS1/Mini-Project-Optuna-Pytorch-/issues) or submit a pull request.
- **Explore the Code:** Clone the repo, run the experiments, and modify hyperparameters to see how performance changes.

### 👨‍💻 Let’s Connect!

Feel free to connect and reach out on [LinkedIn](www.linkedin.com/in/aditya-pratap-singh-admin) I'm always open to:

- 💡 Feedback & Suggestions  
- 🤝 Collaborations  
- 💼 Opportunities

> Every contribution matters. Let’s build and learn together! 🚀 
