# Jenas Creations

Jenas Creations is an online homemade jewellery store. This e-commerce application allows shoppers to browse products that are on offer for sale from Four categories, bracelets, necklaces, earrings and phone charms. Shoppers can also create a custom product, choosing the category, material, colour scheme, personalisation and add a charm if they would like as well as including any additional details they feel are needed in order to make their product unique and a treasured piece in their collection. The application allows shoppers to add products and a custom order to their bag, checkout and receive email conformation of their order, as well as additional features such as leaving reviews on products, contact admin with any queries and search for specific products.   

A live version of the project can be accessed here: [Jenas Creations](https://jenas-creations-ad878282c6a4.herokuapp.com/)

<img src="../docs/readme_images/jenas-creations-mockup.png">

# User Experience Design

## User Demographic

This website is intended for:

* Users that have a keen interest homemade jewellery.
* Users that would like to purchase homemade jewellery.
* Users that would like to have a custom order made for them.
* Users that are interested in browsing an online store and adding items to their bag.  

## User Stories

As a User of this website:

* I want to browse a selection of products available. 
* I want to be able to give my preferences for a custom order. 
* I want to purchase homemade jewellery. 
* I want to be able to leave a review of the product I purchased.
* I want to be able to contact site admin with any inquires I may have.
* I want to be able to manage my reviews.
* I want to be able to save my delivery information. 
* I want to be able to see my order history. 

## Entity Relationship Diagram

The entity relationship diagram for this application was generated from Django. A link to the tutorial on how to generate the diagram can be found in the credits section. Some considerations with this entity relationship diagram include the foreign key relationships. A foreign key relationship links Two tables, the column of One table is linked to the primary key of another table, allowing that table to access the information stored in the table with the foreign key relationship. Some key foreign key relationships in this entity relationship diagram is the relationship between user profile and order, connecting a user to an order. Orderlineitem table has Three foreign key relationships to custom order, order and product. Both custom order and product have a foreign key relationship to the category table and product has a foreign key relationship to the review table, ensuring the reviews are left for a specific product. 

<img src="../docs/readme_images/erd.png">

## Wireframes

Wireframes were produced for the home, products, product detail, shopping bag, checkout and checkout success pages. These wireframes where used for reference when building the site, some aspects of the wireframes have changed as the website was being produced.

### Home

<img src="../docs/readme_images/wireframe-home.png">

### Products

<img src="../docs/readme_images/wireframe-products.png">

### Product Detail

<img src="../docs/readme_images/wireframe-product-detail.png">

### Shopping Bag

<img src="../docs/readme_images/wireframe-shopping-bag.png">

### Checkout

<img src="../docs/readme_images/wireframe-checkout.png">

### Checkout Success 

<img src="../docs/readme_images/wireframe-checkout-success.png">















# Credits 
Connecting social accounts: https://www.marinamele.com/user-authentication-with-google-using-django-allauth
Django order_by: https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending 
Django filter: https://www.w3schools.com/django/django_queryset_filter.php 
overflow-wrap: https://www.w3schools.com/cssref/css3_pr_overflow-wrap.php
Convert object: https://www.geeksforgeeks.org/convert-object-to-string-in-python/ 
positive integer field: https://www.geeksforgeeks.org/positiveintegerfield-django-models/
Clean method on django models: https://docs.djangoproject.com/en/5.0/ref/forms/validation/ 
Save method django: https://docs.djangoproject.com/en/5.0/topics/db/models/
Retrieving a single object with get(): https://docs.djangoproject.com/en/5.0/topics/db/queries/
Python get method call: https://www.w3schools.com/python/ref_dictionary_get.asp
Finding the average: https://docs.djangoproject.com/en/5.0/topics/db/aggregation/ 
Toasts: https://getbootstrap.com/docs/5.3/components/toasts/#events
Fix footer to bottom with flex: https://stackoverflow.com/questions/55541850/how-to-make-footer-stay-at-bottom-of-the-page-with-flex-box 
ERD: https://www.wplogout.com/export-database-diagrams-erd-from-django/





# Images

## Braceletes
https://i.etsystatic.com/27283872/r/il/525dc1/2804553214/il_fullxfull.2804553214_nhj2.jpg

https://i.pinimg.com/originals/f1/9c/aa/f19caa86a38c7a3e06748852d209178c.jpg

https://i.pinimg.com/originals/d0/0e/65/d00e65e5a757c741c6e2859c0bb02eb3.jpg

https://i.pinimg.com/originals/7d/16/4d/7d164df902d9ec8407acaeb8b191d08f.jpg

https://i.pinimg.com/originals/f9/6b/83/f96b83ad835da2d7a8b52ded28a5222b.jpg

https://i.pinimg.com/originals/59/66/72/59667237b23aa86ed09c79e6b5726f9b.jpg

https://assets0.mirraw.com/images/6934949/image_zoom.jpeg?1555137275

https://m.media-amazon.com/images/I/41Nnf+goGCL._AC_UL480_FMwebp_QL65_.jpg

https://m.media-amazon.com/images/I/51q0-VmHVyL._AC_UL480_FMwebp_QL65_.jpg

https://m.media-amazon.com/images/I/51OSJXrvY7L._AC_UL480_FMwebp_QL65_.jpg

## phone charms

https://m.media-amazon.com/images/I/41Dl58NBIyL._AC_SL1200_.jpg
https://m.media-amazon.com/images/I/61RB2XZksQL._AC_UY327_FMwebp_QL65_.jpg
https://m.media-amazon.com/images/I/41gFO23fydL._AC_UY327_FMwebp_QL65_.jpg
https://m.media-amazon.com/images/I/41KD2QtLx1L._AC_UY327_QL65_.jpg
https://m.media-amazon.com/images/I/41iIKG0OtFL._AC_UY327_QL65_.jpg

## earrings

https://tse2.mm.bing.net/th?id=OIP.GGT6wY-Ol-V8dXPSxEOASwHaF7&pid=Api&P=0&h=180
https://tse2.mm.bing.net/th?id=OIP.Z3xTA7IfeYTu3RI0N6NaGQHaHb&pid=Api&P=0&h=180
https://tse1.mm.bing.net/th?id=OIP.BsidtET6rAGPXQx6lQioJAHaId&pid=Api&P=0&h=180
https://tse2.mm.bing.net/th?id=OIP.fm7hSfSuuAy4EflCxy1IwAHaHa&pid=Api&P=0&h=180
https://tse3.mm.bing.net/th?id=OIP.RtMWbbyhw076mNZRqglcLwHaGL&pid=Api&P=0&h=180

## necklaces
https://tse1.explicit.bing.net/th?id=OIP.ar88vVAbALTNiKY85s_TqAHaFj&pid=Api&P=0&h=180

https://tse1.explicit.bing.net/th?id=OIP.S25_e6wwy0Lr7vZEhdsOjQHaHa&pid=Api&P=0&h=180
https://tse1.mm.bing.net/th?id=OIP.vBH6ZjmBCKl8-Hc33gAmEgHaHa&pid=Api&P=0&h=180
https://tse4.mm.bing.net/th?id=OIP.okybC0DHVP6FJ8Tx5x2hOQHaJ5&pid=Api&P=0&h=180
https://tse1.mm.bing.net/th?id=OIP.4lPxe2gW9elzY-YwdHp6uwHaJ4&pid=Api&P=0&h=180




