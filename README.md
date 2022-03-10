# Housing Prices Prediction
In this project, we created a SAC dashboard to provide an investment guide for Malaysian real estate market.
We created 2 pages - 
1. Overview of Malaysia housing market
2. Detailed Penang house price


## Malaysia Housing Market
<ul>
  <li>We tabulated a ROI table that compares the ROI of different types of houses in different states. 
</li>
  <li>There is also a time-series line chart that forecasts the house price.
</li>
</ul>

NOTE: All charts are applicable to the filter, for flexible user interaction.

![image](https://user-images.githubusercontent.com/55709960/157467296-162760c0-b788-43db-a742-0e748148029d.png)

## Penang housing market
<ul>
  <li>We used latlong.py to extract latitude and lonngitude of housing address using Google's API. 
</li>
  <li>We clustered the latitude and longitude with K-Means clustering (HousePrice_HeatMap.ipynb) to cluster the houses based on their areas.
</li>
  <li>The median of each clusters is used to calculate the instalment each month to buy a house in the area and suggest the recommennded salary.
</li>
</ul>

![image](https://user-images.githubusercontent.com/55709960/157468021-6f23eee2-5e0f-44b4-95a2-ebd0063e23a2.png)

## House Price Prediction
<ul>
  <li>We compare the regression model of SAC and gradient boost model trained by ourselves.
</li>
  <li>SAC does not provide data cleaning flexibility. 
</li>
  <li>We compare different data preparation methods (One Hot Encode, Ordinal data) to see which method is more suitable to create accurate predictions (HousePrice_OneHotEncode.ipynb, HousePrice_Ordinal.ipynb). 
</li>
  <li>We found that removing extreme values (outliers) from the dataset hugely increase our models prediction (HousePrice_RemoveOutlier.ipynb). 
</li>
  <li>Gradient Boost was the best performing model compared to other reggression models (Linear, Lasso, Random Forest, DT) with 85% R2 score.
</li>
</ul>

![image](https://user-images.githubusercontent.com/55709960/157468791-a8e5f4d8-24a8-402b-be47-c2709381339b.png)
