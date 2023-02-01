## Create the Backend and DB Design Planning

### Decide on the fundamental entities of your app

#### **User**

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

#### Admin App

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

### Decide on data points you will collect from the user

#### User

- username
- name
- email
- encrypted password

#### Properties

- area
    - square-feet
    - bedrooms
    - bathrooms
- price
- address-location
- state
- image-source

#### Property Valuation

- area
    - square-foot
    - bedrooms
    - bathrooms
- address-location
- state
- condition

#### Realtime auction

- bidding amount

#### Payment Transaction

- bid id
- payment mode
- price
- client id
- transaction id

### Admin

- username
- email
- encrypted password
- name

#### Scrapped Properties

- number of records
- state where hosted on-sale properties required

## Create ERD diagram of your database using dbdiagram.io

![db diagram.jpeg](Create%20the%20Backend%20and%20DB%20Design%20Planning%209322fc3f5bc04029a61cdb1910bc74a9/db_diagram.jpeg)