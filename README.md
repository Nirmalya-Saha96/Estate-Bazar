# ESTATE BAZAR

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
- All sold records are stored in BlockChain Smart Contract for creating a non-fungible token

### Security

- All the payment transactions are done in ETHEREUM BLOCKCHAIN
- Once the estate is sold the record get's written in the BlockChain
- providing an unalterable selling records.
- and safe payment methods by Smart Contract to remove Frauds.

### Create a basic workflow of your app

https://user-images.githubusercontent.com/81407181/216064318-cd665149-ae07-4f32-b795-dc9ddb8305ac.mp4

[https://www.figma.com/file/UkyElEZqTRxFKWucGtnLbE/Untitled?node-id=0%3A1&t=iCrAQe43HMIWG3I3-1](https://www.figma.com/file/UkyElEZqTRxFKWucGtnLbE/Untitled?node-id=0%3A1&t=iCrAQe43HMIWG3I3-1)

### DOCUMENTATIONS 

***[Idea Creation](https://silent-option-8b8.notion.site/Ideation-Document-Template-48522144e607483fbd42788a707e3c93)***

***[Bachend And DB Design](https://silent-option-8b8.notion.site/Create-the-Backend-and-DB-Design-Planning-9322fc3f5bc04029a61cdb1910bc74a9)***

***[API Documentation](https://silent-option-8b8.notion.site/API-Docs-and-Workflow-54c042f3574040ed94bf881457d3316d)***


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

### Create ERD diagram of your database using dbdiagram.io

![db diagram.jpeg](Create%20the%20Backend%20and%20DB%20Design%20Planning%209322fc3f5bc04029a61cdb1910bc74a9/db_diagram.jpeg)


## API Docs and Workflow

### Decide on different API end points that you require for the app

#### End points for Admin

1. Route: /admin_signup
    
    Method: POST
    
2. Route: /admin_login
    
    Method: POST
    
3. Route: /get_all_properties
    
    Method: GET
    
4. Route: /property_sold_history
    
    Method: GET
    
5. Route: /inactive_bidding
    
    Method: GET
    
6. Route: /active_bidding
    
    Method: GET
    
7. Route: /fetch_client_details
    
    Method: GET
    
8. Route: /update_bid_status
    
    Method: PUT
    
9. Route: /update_payment_status
    
    Method: PUT
    
10. Route: /payment
    
    Method: POST
    
11. Route: /add_property
    
    Method: POST
    

#### End points for Client

1. Route: /signup
    
    Method: POST
    
2. Route: /login
    
    Method: POST
    
3. Route: /live_property_details
    
    Method: GET
    
4. Route: /current_bidding_price
    
    Method: GET
    
5. Route: /post_bid
    
    Method: POST
    
6. Route: /buy_history
    
    Method: GET
    

### Design individual API input parameters and response formats

#### Admin

1. Route: /signup_admin
    
    Method: POST
    
    Request: email, username, password
    
    Response: “Signed Up”
    
2. Route: /login_admin
    
    Method: POST
    
    Request: admin id, password
    
    Response: “Logged In”
    
3. Route: /get_all_properties
    
    Method: GET
    
    Request: email-id, password, admin id
    
    Response: All properties available to the admin
    
4. Route: /property_sold_history
    
    Method: GET
    
    Request: start date, end date, admin id
    
    Response: List of properties sold that day
    
5. Route: /inactive_bidding
    
    Method: GET
    
    Request: property id
    
    Response: Property details
    
6. Route: /active_bidding
    
    Method: GET
    
    Request: property id
    
    Response: Property details
    
7. Route: /fetch_client_details
    
    Method: GET
    
    Request: client id
    
    Response: Client details
    
8. Route: /update_bid_status
    
    Method: PUT
    
    Request: property id, bid status
    
    Response: property details
    
9. Route: /update_payment_status
    
    Method: PUT
    
    Request: property id, is_sold
    
    Response: Property details
    
10. Route: /payment
    
    Method: POST
    
    Request: transaction id, client id, property id, price
    
    Response: payment details
    
11. Route: /add_property
    
    Method: POST
    
    Request: state
    
    Response: “Property added successfully”
    

#### User

1. Route: /signup
    
    Method: POST
    
    Request: client email, username, password
    
    Response: “Signed Up”
    
2. Route: /login
    
    Method: POST
    
    Request: email, password
    
    Response: “Logged In”
    
3. Route: /live_property_details
    
    Method: GET
    
    Request: is active status=true
    
    Response: List of properties
    
4. Route: /current_bidding_price
    
    Method: GET
    
    Request: property id
    
    Response: current price
    
5. Route: /post_bid
    
    Method: POST
    
    Request: price
    
    Response: Bid position, price
    
6. Route: /buy_history
    
    Method: GET
    
    Request: user id
    
    Response: List of properties
    

### Generate an API workflow diagram

https://www.figma.com/file/GhL5PPbOrvt3edrTFrUGZh/WorkflowApp?node-id=0%3A1&t=NiqQw72JMPLJ0H6p-1

[https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FGhL5PPbOrvt3edrTFrUGZh%2FWorkflowApp%3Fnode-id%3D0%253A1%26t%3DNiqQw72JMPLJ0H6p-1](https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FGhL5PPbOrvt3edrTFrUGZh%2FWorkflowApp%3Fnode-id%3D0%253A1%26t%3DNiqQw72JMPLJ0H6p-1)
