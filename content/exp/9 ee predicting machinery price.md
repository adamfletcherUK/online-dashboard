### Predicting the resale price of used machinery

#### Project Aims and Goals

The client wanted to determine factors which influenced the resale price of
construction equipment sold globally. The aim was to be able to predict the
resale price of used machinery all over the world in order to better optimise
sales prices for machine dealers.

#### Phase 1: Proof of Concept

The initial phase of the project involved:

- Data cleaning four different data sources
- Determining any leading indicators for final sale price
    - ensuring they were present in all datasets (or could be inferred)
- Making sure all historical sales were inflation adjusted to present day
- Imputing missing data (although some fields were not used for machine
  learning)
    - I used correlation between variables to predict missing values and thus
      thought that these samples used one variable twice
- Removing outlying results
    - I used a statistical approach that would bin samples and remove outliers
      based on population statistics and business rules
- Utilising machine learning to predict the resale values of construction
  equipment based on leading indicators.
    - The model utilised was a Random Forest Regression model as a first pass
    - It was chosen as it readily takes both categorical and continous variables
      witout much transformation and typically show high accuracies
    - Althought they do have a tendancy to overfit.
- Constructing a timeline graph showing how the price for an individual asset
  depreciates based on estimated annual usage.

For speed, it being a technology already available to the client and a lack of
front-end developers, we used Power BI to surface this information. I built a
dashboard allowing users to dig into the cleaned data.

I deployed an API endpoint using AWS Sagemaker allowing inference from our model
to be surfaces, we utilised a software package which "spoofed" Power BI into
thinking our API was an ODBC connection allowing it to push predictions to a
model (I would NOT recommend doing this, it was dreadfully slow)

For the timeline depreciation I utilised SciPy to model the relationship between
the machines usage and price to calculate some regression coeffcients, this was
then outputted to a file which Power BI imported, and the equation was
reproduced in DAX. This allowed end users to see ML predictions and interact
with them. Although not the most advanced approach, and not something we would
keep longterm, it was a great and fast way of getting models infont of the
client, especially with a lack of frontend developers.

### Phase 2: WebApp Development, ETL pipeline construction and Model Interation

The main user-facing difference when we moved into phase 2 was the welcomed
removal of Power BI and the building of a Node JS frontend by two dedicated
front end developers. This had the affect of allowing us to not only free up
time from building a dashboard, but also to use more powerful models.

A second outcome from the Pro

- The client wanted to determine factors influencing the resale price of
  machines to better optimise sales prices.
- Created a non-linear regression model to predict the price of an asset and how
  that price changes over time, which I deployed via a Flask API.
- Conducted validation activities to build user-confidence in predictions as the
  industry was typically not data-driven.
- Built a pricing index, modelling market trends over time, using regression to
  normalise sales to reference values.
- The business is now able to sell assets faster and at a more appropriate
  price. They are also able to predict depreciation price on new assets and
  factor in price of selling assets in project costings.