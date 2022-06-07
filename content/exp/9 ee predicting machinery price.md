### Predicting the resale price of used machinery
#### Phase 1: Proof of Concept

The client wanted to determine factors which influenced the resale price of
construction equipment sold globally. The aim was to be able to predict the
resale price of used machinery all over the world in order to better optimise
sales prices for machine dealers.

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
    - It was chosen as it readily takes both categorical and continuous variables
      without much transformation and typically show high accuracies
    - Although they do have a tendency to over fit.
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
the machines usage and price to calculate some regression coefficients, this was
then outputted to a file which Power BI imported, and the equation was
reproduced in DAX. This allowed end users to see ML predictions and interact
with them. Although not the most advanced approach, and not something we would
keep long term, it was a great and fast way of getting models infont of the
client, especially with a lack of frontend developers.

### Phase 2: WebApp Development, ETL pipeline construction and Model Interation

The main user-facing difference when we moved into phase 2 was the welcomed
removal of Power BI and the building of a Node JS frontend by two dedicated
front end developers. This had the affect of allowing us to not only free up
time from building a dashboard, but also to use more powerful models.

A second outcome from the proof of concept was that the end-users did not like 
some behaviours the random forest regression model. As the model was 
multidimensional, there were many factors influencing a prediction. However,
the end users understood that as the machines got older and more used, it would 
decrease in value - and anything to the contrary was incorrect.

I pivoted away from the random forest regression model and instead aimed to 
create a non-linear SciPy model which generalised the relationship between age 
and usage against price, showing an initial exponential decay of price which 
eventually plateaued at a basal price. The valuable lesson I learnt here is 
that, even if you have the most complex and accurate model, if no one uses it - 
it's worthless. So better to have a less accurate model in production than an 
accurate model gathering dust.

This model also allowed for the construction of a machines price "Timeline", 
which predicted the machines price from manufacture date to 10 years in the 
future based on how much a user intended to use the machine - allowing them to 
determine if it was more profitable to sell or maintain that machine.

In addition to changing the machine learning model, we also overhauled the 
ETL/feature engineering pipeline and created an automated model retraining and
deployment pipeline. This entailed:
- Converting all the original Jupyter Notebooks into class functions which would be called in sequence
- Creating detailed logging statements during a pipeline run
- Parallelising high compute tasks through batching and multiprocessing tasks
- Making a Docker container for the ETL pipeline and creating a Flask API with an endpoint which triggered the pipeline.
- A DevOps engineer also: implemented CI/CD for the ETL pipeline, created a trigger for the pipeline when new data was uploaded to an S3 bucket.
- Created a second model training Flask API which triggered model training after the ETL pipeline successfully ran.
  - The output of which was a serialized joblib file containing model coefficients and performance stats of each regression model.
- This joblib file was again uploaded to S3 and utilised by a third Flask API which served predictions to the WebApp frontend.
  - It handled general price predictions
  - It constructed "Machine Timelines" showing a machines full price history

After deploying these pipelines, I conducted a plethora of validation activities
to build user-confidence in the predictions as the industry was not typically 
data driven.

We also built a pricing index model, aiming to model market trends over time. 
This utilised linear regressions to normalise sales which then allowed for price
comparisons over time - from this we were able to see if prices were increasing
or decreasing over time when accounting for specific variables.

From this project the business is now able to sell machines faster and at a more 
appropriate price. They are also able to predict depreciation price on new 
machines and factor in price of selling machines in project costings.