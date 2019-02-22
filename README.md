# Azure ML SDK - Fashion MNIST

In this workshop we will look at the life-cycle of your projects: from data, to model and model to consumption in the real world. You can follow along with code samples shared, as well as use these examples to help you replicate this workshop with your own projects after the event. 

Feedback on the content below is welcome 😊👍 please reach out to me on [Twitter: @AmyKateNicho](https://twitter.com/AmyKateNicho) or submit an [issue/pull request on github](https://github.com/amynic/azureml-sdk-fashion/)

### Always remember to delete your resources - [click here to see how](#deleting-your-resources)

## The base dataset and model

The example model used in the code below is how to classify clothing into categories such as dresses, t-shirts, sandals, trainers etc. The dataset used is the Fashion MNIST dataset from Zalando the online fashion brand, find out more about this dataset here: https://github.com/zalandoresearch/fashion-mnist 

## What is Azure Machine Learning?
Azure Machine Learning is a platform for developing and deploying your machine learning models. Use your favourite frameworks, libraries and tools to build and deploy your machine learning experiments with the help of the cloud.  [https://docs.microsoft.com/en-us/azure/machine-learning/service/overview-what-is-azure-ml](https://docs.microsoft.com/en-us/azure/machine-learning/service/overview-what-is-azure-ml/?WT.mc_id=aisummit-github-amynic)


## Installation and Setup
You have many options for development environments to use with Azure Machine Learning - so take a look at the one your used to using or looking to setup: [https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-choose-a-dev-environment](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-choose-a-dev-environment/?WT.mc_id=aisummit-github-amynic)

Once you have chosen an environment - follow the instructions here to configure this environment: [https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-configure-environment](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-configure-environment/?WT.mc_id=aisummit-github-amynic)

For these samples specifically I have tested:
* [Data Science Virtual Machine](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-configure-environment#azure-notebooks-and-data-science-virtual-machine/?WT.mc_id=aisummit-github-amynic) in Azure 
* [Jupyter setup on your own machine](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-configure-environment#azure-notebooks-and-data-science-virtual-machine/?WT.mc_id=aisummit-github-amynic)





## Code Files Order

The code files below are listed in order of demonstration and reusability
* [FashionMNISTImageClassification-Model.ipynb](https://github.com/amynic/azureml-sdk-fashion/blob/master/FashionMNISTImageClassification-model.ipynb)
* [Fashion MNIST Image Classification - Azure ML SDK Training.ipynb](https://github.com/amynic/azureml-sdk-fashion/blob/master/Fashion%20MNIST%20Image%20Classification%20-%20Azure%20ML%20SDK%20Training.ipynb)
* [Fashion MNIST Image Classification - Azure ML SDK Deployment.ipynb](https://github.com/amynic/azureml-sdk-fashion/blob/master/Fashion%20MNIST%20Image%20Classification%20-%20Azure%20ML%20SDK%20Deployment.ipynb)


### Fashion MNIST Image Classification - Model
In the Fashion MNIST model notebook you will see the code for a standard Keras and Tensorflow Convolutional Neural Network (CNN). This symbolises the fact that the Azure ML SDK can be used and intergrated with any model, no matter what framework or setup you are using.

If you run this code on your local machine, its likely to run slowly as it churns through 60,000 training images 24 times. Therefore with the Azure ML SDK I will show you how to setup your target compute and use a GPU machine to train the model quicker

Run through this code to see what the model does and whats it predicting

### Fashion MNIST Image Classification - Azure ML SDK Training

In this Fashion MNIST notebook we introduce how to instrument your training process with the Azure ML SDK. 

This code will show how Azure ML SDK can support your machine learning project with:
* A central repository for your machine learning project
* Creating a cloud computer target and running your training in the cloud
* Whilst running your training in the cloud, add logging to the code to see in real time in your notebook the outputs and progress of the training on the remote compute in the cloud
* Saving your large datasets to azure storage so your training models can mount the data to the assigned training compute and have a 'one-source-of-truth' dataset for all your data science team to be using
* Finally registering this model with versioning so others can leverage it easily

### Fashion MNIST Image Classification - Azure ML SDK Deployment

In this Fashion MNIST notebook we introduce how to take the models you have registered and versioned, deploy them to production and monitor them 

This code will show how Azure ML SDK can support your machine learning project with:
* creating a training and scoring script for your model
* creating a bespoke environment for your model to run in (libraries and packages to install)
* setting up a container service to host your model
* deploying your model to the cloud container service
* retrieving the service scoring URL for your hosted model
* sending test data to your hosted model to be scored and returned to compare for the accuracy of your model on your validation set


# Deleting your Resources

Make sure you delete the compute when you are not using it to save money

A couple of options ...

## Delete the compute items
* make sure you delete the batch AI cluster and any container instances you created in your resource group.
* Go to your resource group in the Azure Portal (left panel 'resource groups' and select your resource group name)
* Next select the compute resources (such as the 'batch AI' cluster) and choose delete
* ![delete batch ai](/images/deleteresources1.JPG)

## Delete the whole resource group
* Or you can delete all resources created
*  Go to your resource group in the Azure Portal (left panel 'resource groups' and select your resource group name)
* Select 'Delete Resource group'
* confirm by writing the resource group name in the box
*  ![delete resource group](/images/deleteresources2.JPG)


## Shutdown/Delete the Virtual Machine
* finally you can shutdown your Virtual machine (VM)
* In the Azure portal - navigate to the virtual machines tab
* select the VM you created
* click 'shutdown' or 'delete'
*  ![shutdown vm](/images/deleteresources3.JPG)

