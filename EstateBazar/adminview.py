from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models.user import User
from .models.adminuser import AdminUser
from .models.properties import Property

from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from bs4 import BeautifulSoup
import requests
import json

BASE_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US;en;q=0.9",
    "accept-encoding": "gzip, deflate, br",
}


adminview = Blueprint('adminview', __name__)

@adminview.route('/', methods=['GET', 'POST'])
@login_required
def index():
    print(current_user)

    if(request.method == 'POST'):
      state = request.form['places']

 


    url="https://www.realtor.com/realestateandhomes-search/"+state


    html_text = requests.get(url=url,headers=BASE_HEADERS)
    soup = BeautifulSoup(html_text.content,'html.parser')
    homes = soup.find_all('li', class_='jsx-1881802087 component_property-card')
  
    for i in range(0,5,1):
        home = homes[i]
        print(home)


        price = home.find('span',class_ = 'Price__Component-rui__x3geed-0 gipzbd').text
        beds = home.select('[data-label=pc-meta-beds]')[0].get_text(separator = ' ')
        bath = home.select('[data-label=pc-meta-baths]')[0].get_text(separator = ' ')
        sqft = home.select('[data-label=pc-meta-sqft]')[0].get_text(separator = ' ')
        address = home.select('[data-label=pc-address]')[0].get_text()

        
        
        if home.select('img')[0]["src"].startswith('data',0,4):
            img = home.select('img')[1]["src"]
        else:
            img = home.select('img')[0]["src"]
    

        home = Property(price = price,bedroom = beds,bathroom = bath,sqft = sqft,address = address,imgSrc=img,)

        db.session.add(home)
        db.session.commit()





    return render_template("adminActiveListing.html", user=current_user)



