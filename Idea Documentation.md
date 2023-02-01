## Ideation Document 

### Problem that you are solving

Real Estate Auctioning is one of the most prominent activities in this world, but due to more virtual events, not all auctions can occur offline; hence, there is a need to make all auctions available virtually, so that buyers can get his dream property under one place.

Here in **ESTATE BAZAR** not ****only we provide the required marketplace but also, through out **AI algorithm** we provide suggestive prediction over valuation for breaking over and under valuation which is evident in these online events  

### Who are the users?

Target users are the buyers/brokers who want to buy estate properties at their preferred location at the best available price without searching thorough various other sites  

Through our AI ALGORITHM our target users gets expanded to users who does not have proper knowledge over valuation

### Mention top 3 features about your product

- Prices of the property are predicted by the **ARTIFICIAL NETURAL NETWORKS** machine-learning model to prevent over and under valuation.
- Seamless Real-time auction with low latency
- Scrapped on-sale hosted estate properties to provide the buyer with most possible option for their dream house at their preferred location

### Create a basic workflow of your app

[https://www.figma.com/file/UkyElEZqTRxFKWucGtnLbE/Untitled?node-id=0%3A1&t=iCrAQe43HMIWG3I3-1](https://www.figma.com/file/UkyElEZqTRxFKWucGtnLbE/Untitled?node-id=0%3A1&t=iCrAQe43HMIWG3I3-1)

### List down all the features that your app has

Our website provides two modules-

 1. Admin

1. Client

### ADMIN

- Authentication
    - Dedicated admin authentication and session storage using
    - **Flask-Login** and **Flask Session**
    - Hashing the password using **sha256 algorithm**
- Web Scrapping
    - Scrapping Real Estate on-sale hosted properties form different online websites
    - Listing those properties for live auction
    - Tech used: **Beautiful Soup**
- Managing Auction Lifecycle
    - Activating listed properties for live auctions
    - Managing biddings from buyers
    - Admin can view all analytics based on past sold records
- Sold History
    - View and analyze all the sold records of previous properties

### CLIENT - BIDDERS

- Real Estate Bidding
    - Viewing live auctions
    - Viewing all his purchased properties
    - Real-time auction bidding using **flask-socketio**
    - The Bidding Mechanism is in **Real-Time**.
    - Updating of Bidding Amount at low latency
    - as, any bid is placed the TIMER reset's at the end to TIMER the highest BIDDER wins the Auction
- Brought History
    - View all bought properties of the current user
- Predicting Valuation
    - Estimating real-estate valuation using **artificial neural networks**
    - Prediction based on ****[House price prediction dataset](https://www.kaggle.com/datasets/shree1992/housedata?resource=download)****
- Authentication
    - user authentication using **flask login**
    - Session storage using **Flask Session**
    - Hashing the password using **sha256 algorithm**
- Filters
    - based on states
- Payments
    - card payments