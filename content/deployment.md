# How This Website Is Deployed

## Interface
The front end of this website is using [StreamLit](https://streamlit.io/), a simple python interface to make dashboards
and quick Machine Learning tools.

Although not as flashy as traditional tools to build production ready webpages, I have chosen to use streamlit primarily
as a mechanism to learn this tool for data science projects.

The majority of the text in these pages will be rendered markdown templates, making updating the contents and formatting
relatively simple

## DevOps

The app is deployed using [Heroku](https://www.heroku.com/) as it is a user-friendly deployment tool for non-DevOps
people.

There is integration to deploy Test, Dev and Prod environments.

Currently I have set the Staging environment to automatically redeploy following
a codebase commit to the main branch on gitub.

Prod is protected to particular releases that I push manually when I have happy
with Dev.

There are two dev environments, which I use to test branches with new features -
they are currently manually deployed.

## Testing and CI/CD

[![Build Status](https://travis-ci.com/adamfletcherUK/online-dashboard.svg?branch=main)](https://travis-ci.com/adamfletcherUK/online-dashboard)

The webapp also contains some testing and CI/CD

For build testing and running the code bases test suit I have
utilised [Travis CI](https://www.travis-ci.com/)
which builds a test environment and runs the test suit whenever I commit to
Github.

NB. As I am just starting up the website, the test suits is limited and
automatically passes.

### Code Linting

I am currently implementing code linting to improve the readability of the
codebase, as well as instilling software best practices to myself.