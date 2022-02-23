# TiktokToDiscord Bot

This is a discord bot that can post the link of new Tiktok posts from a given creator into a discord channel

###  Configuration

Create a dotenv (.env) file and add the key USERNAME key with the value as the tiktok username you want to track

##### Example: USERNAME=user123

Optional Key value pairs are
1. DEBUG = True | False
2. WEBDRIVER_PORT = int
3. WINDOWS = True | False

### How to Run

#### 1. Run with Docker
    Start: docker-compose up
    
    Shutdown: docker-compose down

#### 2. Run Directly
1. Clone the git repository
2. Create python virtual environment
3. Install the python modules listed in requirements.txt
4. If on Windows set the WINDOWS environment variable  to True
5. Set up Selenium Server
6. Run Python main.py

##### Note: May get warning or error that uvicorn can not be installed on windows if this occurs remove uvicorn from requirements file and make sure windows env variable is set to True 
