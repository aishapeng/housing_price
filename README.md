# Housing Prices Prediction
In this project, we have created a SAP Analytics Cloud dashboard that served as a guide for users to determine the worthiness of property investment in Malaysia. 
Additionally, this dashboard help users to determine which type of property investment is right for them. 

#### Dashboard Content - 
1. Overview of Malaysia Housing Market
2. Detailed View of Housing Prices in Penang
3. House Price Prediction

#### Data Source - 

The data was collected from the Department of Statistics Malaysia. 

#### Data Content -

The data contains the housing prices of each type of houses (eg. All type, Detached house, Semi-detached, High Rise) for each state within Malaysia between 2011 to 2021.


## Story 1 - Overview of Malaysia Housing Market
<ul>
  <li> This story began by providing an overview of the Housing Prices in Malaysia in 2021 compared to 2020, where red indicates a drop and green indicates a rise. These numerical indicators help users to identify the impact of COVID on the housing prices for each state and each particlaur type of house. 
</li> 
  <li> Next, we created a barchart to determine which state has the most expensive house in 2021.
</li> 
  <li> We also tabulated a ROI table that compares the ROI of different types of houses in different states. 
</li>
  <li> Lastly, we have built a time-series line chart that shows the trend of housing prices over the years and forecasts the house price in 2022. 
</li>
</ul>

NOTE: All charts are applicable to the filter, for flexible user interaction.

![image](https://user-images.githubusercontent.com/55709960/157467296-162760c0-b788-43db-a742-0e748148029d.png)


#### Key Takeaways:
- All type of houses has declined in KL compared to 2020. We can conclude that COVID has caused housing prices in KL to depreciate. While for Sabah, we observed a totally different trend. Almost all types of houses has shown appreciation in housing prices. Hence, we can conclude that COVID did not has any effect on the housing prices in Sabah.
- KL has the most expensive house in 2021. 
- Terraced house in Johor gave investors the highest ROI, followed by detached house in Kelantan and detached house in Penang.



## Story 2 - Detailed View of Housing Prices in Penang
<ul>
  <li>We used latlong.py to extract latitude and lonngitude of housing address using Google's API. 
</li>
  <li>We clustered the latitude and longitude with K-Means clustering (HousePrice_HeatMap.ipynb) to cluster the houses based on their areas.
</li>
  <li>The median of each clusters is used to calculate the installment per month to pay the housing loan in the specific area, followed by proposing the recommended salary to the users. 
</li>
</ul>
To sum up, this geographical map shows users the reality of how much they should earn per month in order to purchase a house in their desired location. 




![image](https://user-images.githubusercontent.com/55709960/157468021-6f23eee2-5e0f-44b4-95a2-ebd0063e23a2.png)


#### Key Takeaways:
- Timur Laut appears to be the most popular district among buyers. 
- In Timur Laut, landlords sought an average of RM 1.2mil for landed houses and RM 550,000 for high-rise houses.
- Seberang Perai Tengah as a relative bargain at RM 460,000 for landed houses and RM 240,000 for high- rise houses.



## Story 3 - House Price Prediction
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


Thanks for reading. 
