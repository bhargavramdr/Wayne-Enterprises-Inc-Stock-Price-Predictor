# Wayne-Enterprises-Inc-Stock-Price-Predictor
About 97 accurate predictor of  next five days stock trend. Deployed using Flask.


**Mr Wayne has a lot on his plate. He doesn't have to time to fret about his companies stock price. He has many other things to take care.
So, We are going to build him a predictor which will let him know the trend of his stocks for next days.**


**In this project we take the last five days stock trend as a basis to project the next five days trend.**


Here's how the site looks:

![Screenshot (97)](https://user-images.githubusercontent.com/72303641/137005982-bf24eff7-fd50-4d18-8e35-c259743dfb73.png)

**Importing necessary libraries
We are going to use linear regression.**
 ![image](https://user-images.githubusercontent.com/72303641/138639157-84072d06-cff3-4467-bb55-87b348492dda.png)

 
 
**Data Preparation
Now I will write a function that will prepare the dataset so that we can fit it easily in the Linear Regression model**
 ![image](https://user-images.githubusercontent.com/72303641/138639124-75e682ba-4e0e-4393-9e13-253528e9b93d.png)


**We are using NIFTY – 50 data. For fun I had changed it to Wayne stock data.**


**Applying Machine Learning for Stock Price Prediction
Now I will split the data and fit into the linear regression model:**
 ![image](https://user-images.githubusercontent.com/72303641/138639246-922921d7-0642-4ea0-b766-0033c535c5ce.png)


**Now let’s predict the output and have a look at the prices of the stock prices:**

![image](https://user-images.githubusercontent.com/72303641/138639270-c43c4cbe-0803-45f8-b192-1d7608b73927.png)



