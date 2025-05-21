import torch
import torch.nn as nn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset,DataLoader
from sklearn.model_selection import train_test_split
import torch.optim as  optim
import optuna


torch.manual_seed(12)#just for sake that the running code doesn't provides different sets of accuracy

device='cuda' if torch.cuda.is_available() else 'cpu'
print(device)

df=pd.read_csv(r"C:\Users\prata\Downloads\fashion-mnist_test.csv")
#print(df.head())
print(df.shape)


# Create a 4x4 grid of images
fig, axes = plt.subplots(4, 4, figsize=(10, 10))
fig.suptitle("First 16 Images", fontsize=16)

# Plot the first 16 images from the dataset
for i, ax in enumerate(axes.flat):
    img = df.iloc[i, 1:].values.reshape(28, 28)  # Reshape to 28x28
    ax.imshow(img, cmap='viridis')  # Viridis is a colorful, perceptually uniform colormap
    ax.axis('off')  # Remove axis for a cleaner look
    ax.set_title(f"Label: {df.iloc[i, 0]}")  # Show the label

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit the title
plt.show()

#splitting train and test data
x,y=df.iloc[:,1:].values,df.iloc[:,0].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

x_train=x_train/255.0
x_test=x_test/255.0

class fashiondataset(Dataset):
    def __init__(self,features,labels):
        self.features=torch.tensor(features,dtype=torch.float32)
        self.labels=torch.tensor(labels,dtype=torch.long)
      
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self,idx):
        return self.features[idx],self.labels[idx]
    
train_loader=fashiondataset(x_train,y_train)
test_loader=fashiondataset(x_test,y_test)

class Fashion(nn.Module):
    def __init__(self,input_dim, output_dim, num_hidden_layers, neurons_per_layer, dropout_rate):
        super().__init__()
        self.model=self._build_model(input_dim, output_dim, num_hidden_layers, neurons_per_layer, dropout_rate)
        
    def _build_model(self,input_dim, output_dim, num_hidden_layers, neurons_per_layer, dropout_rate):
        layers=[]
        for i in range(num_hidden_layers):
            layers+=[
                nn.Linear(input_dim,neurons_per_layer),
                nn.BatchNorm1d(neurons_per_layer),
                nn.ReLU(),
                nn.Dropout(dropout_rate)
            ]
            input_dim=neurons_per_layer
        layers.append(nn.Linear(neurons_per_layer,output_dim))
        return nn.Sequential(*layers)
    
    def forward(self,x):
        return self.model(x)
    
# Optuna Objective Function
def objective(trial):
    
    #Hyper-paramters to tune 
    num_hidden_layers=trial.suggest_int("num_hidden_layers",1,5)
    neurons_per_layer=trial.suggest_int("neurons_per_layers",8,128,step=8)
    dropout_rate=trial.suggest_float("dropout_rate",0.1,0.5,step=0.1)
    epochs=trial.suggest_int("epochs",10,100,step=10)
    lr=trial.suggest_float("lr",1e-5,1e-1,log=True)
    batch_size=trial.suggest_categorical("batch_size",[16,32,64,128])
    weight_decay=trial.suggest_float("weight_decay",1e-5,1e-3,log=True)
    optimizer_name=trial.suggest_categorical("optimizers",['Adam','RMSprop','SGD'])
    
    train_l=DataLoader(train_loader,batch_size=batch_size,shuffle=True)
    test_l=DataLoader(test_loader,batch_size=batch_size,shuffle=False)
    
    #model init
    input_dim=784
    output_dim=10
    
    model=Fashion(input_dim, output_dim, num_hidden_layers, neurons_per_layer, dropout_rate)
    model.to(device)
    # Check if model parameters exist
    for name, param in model.named_parameters():
        print(name, param.shape)  # Debug if needed
    
    #optimizer selection
    criterion=nn.CrossEntropyLoss()
    
    
    if optimizer_name=='Adam':
        optimizer=optim.Adam(model.parameters(),lr=lr,weight_decay=weight_decay)
    elif optimizer_name=='SGD':
        optimizer=optim.SGD(model.parameters(),lr=lr,weight_decay=weight_decay)
    else:
        optimizer=optim.RMSprop(model.parameters(),lr=lr,weight_decay=weight_decay)
        
    #training loop
    for epoch in range(epochs):
        for batch_features,batch_labels in train_l:
            batch_features=batch_features.to(device)
            batch_labels=batch_labels.to(device)
            
            optimizer.zero_grad()
            output=model(batch_features)#forward pass
            loss=criterion(output,batch_labels)#loss
            loss.backward()#backprop
            optimizer.step()#parameters update
    
    #evaluation loop        
    model.eval()
    correct = 0
    total = 0
    #evaulation will be performed on the test dataset
    with torch.no_grad():
        
        for batch_features,batch_labels in test_l:
            batch_features=batch_features.to(device)
            batch_labels=batch_labels.to(device)
            
            outputs=model(batch_features)
            _,pred=torch.max(outputs,1)
            total+=batch_features.shape[0]
            correct+=(pred==batch_labels).sum().item()
            
        accuracy=((correct/total)*100)
        return accuracy
            

if __name__ == "__main__":
    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=20)
    
    print("\nBest Accuracy:", study.best_value)
    print("Best Trial:", study.best_trial.number)
    print("Best Hyperparameters:", study.best_params)
    
        
