![banner](banner.png)

# Infinity Search
This is the code for [infinitysearch.co](https://infinitysearch.co), our privacy search
engine. Our service is now completely open source. 

This project contains the code for our front-end and back-end and does not include any of our web services code. We are currently 
working on a web crawler and indexer that will also be open source but it will be hosted in a different repository. 
It is also not currently implemented in Infinity Search. 

# How It Works
For the web application, we use Flask. For the search results, we use the Microsoft Cognitive Services Search API and
the DuckDuckGo Instant Answers API. We will have more detailed information about how
our system works in the future. 

# Usage

### Note
to run this on your own as is, you'll need to subscribe to the microsoft cognitive services search API and put your account info 
into a file called accounts.py. Their is an example of what this files looks like at [example_accounts.py](/example_accounts.py).


If you are using different results, then you will need to adjust [WebsiteAPI/PublicAPI](/WebsiteAPI/PublicAPI.py) and
add your custom way of displaying results from your source. 

### Requirements
Runtime: Python3.7 

### For Running Infinity Search Locally

```shell script
# pip install the required dependencies
pip3.7 install -r requirements.txt
```

Run wsgi.py and then go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### For Running AWS Serverless with AWS 
Install serverless and get your AWS account setup. Then all you 
need to do is configure your serverless.yml file and then run:
```shell script
serverless deploy
```

### For Running Infinity Search On Your Own Server

If you are doing it this way, it is the same way as deploying any 
flask application. For more information about deploying Flask apps, 
you can go [here](https://flask.palletsprojects.com/en/1.1.x/deploying).


## Documentation 
There is currently not much documentation but as this project 
grows, it can be found in the [docs folder](/docs).

## Contributing to Infinity Search
All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome. 
More information about what we need to be done can be found in our [TODO file](/docs/TODO.md).

## Forking Our Project
This project is open source under the [Apache 2.0 License](/LICENSE) and anyone is welcome to fork our project and use it for their own 
purposes.
