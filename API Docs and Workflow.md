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
    

## 

### Generate an API workflow diagram

https://www.figma.com/file/GhL5PPbOrvt3edrTFrUGZh/WorkflowApp?node-id=0%3A1&t=NiqQw72JMPLJ0H6p-1

[https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FGhL5PPbOrvt3edrTFrUGZh%2FWorkflowApp%3Fnode-id%3D0%253A1%26t%3DNiqQw72JMPLJ0H6p-1](https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FGhL5PPbOrvt3edrTFrUGZh%2FWorkflowApp%3Fnode-id%3D0%253A1%26t%3DNiqQw72JMPLJ0H6p-1)