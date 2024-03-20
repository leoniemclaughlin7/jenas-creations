# Testing

## Manual testing

###  Main navigation Bar

|Feature  | Expect  | Action | Result |
|--|--|--|--|
| Logo  | When the logo is clicked it will return the user to the home page |Clicked logo | pass
| All Products link| When clicked it will direct the user to the products page |Clicked All Products on the nav bar | pass
|Filter By dropdown link| When clicked it will open a dropdown that has Two options, Price (low to high) and Price (High to low)  |Clicked Filter By on the nav bar | pass
|Price (Low to high) link| When clicked it will direct the user to the products page with the products displayed by their price low to high |Clicked Price (low to high) on the nav bar | pass
|Price (High to low) link| When clicked it will direct the user to the products page with the products displayed by their price high to low |Clicked Price (High to low) on the nav bar | pass
| My Account dropdown link| When clicked it will open a dropdown that has Two options, Register and Login  |Clicked My Account on the nav bar | pass
|Register link |When clicked it will direct the user to the sign up page |Clicked Register link| pass
|Login link |When clicked it will direct the user to the sign in page |Clicked Login link| pass
|Search input - empty search |When an empty search is submitted an error message will appear detailing 'Please enter a search criteria!'  |Submitted an empty search criteria| pass
|Search input - Green |When a search criteria is submitted in this case 'Green' it will return all products with green in its name or description  |Submitted a 'Green' search criteria| pass
|Search input - Homemade |When a search criteria is submitted in this case 'Homemade' it will return all products with homemade in its name or description  |Submitted a 'Homemade' search criteria| pass
|Search results - Homemade |When a search criteria is submitted in this case 'Homemade' it will return a link to the main products page and detail how many products where found for the search query  |Submitted a 'Homemade' search criteria| pass
|Shopping bag icon |When clicked it will direct the user to the shopping bag page |Clicked the shopping bag icon on the nav bar| pass

### Category navigation bar 

|Feature  | Expect  | Action | Result |
|--|--|--|--|
|Bracelets link |When clicked it will direct the user to a list of all products that are of the bracelet category |Clicked the Bracelet link on the nav bar| pass
|Phone Charms link |When clicked it will direct the user to a list of all products that are of the phone charm category |Clicked the Phone Charm link on the nav bar| pass
|Earrings link |When clicked it will direct the user to a list of all products that are of the earrings category |Clicked the Earrings link on the nav bar| pass
|Necklaces link |When clicked it will direct the user to a list of all products that are of the necklace category |Clicked the Necklace link on the nav bar| pass
|Category link highlights |When clicked the current category that the user is browsing is highlighted in a dark pink colour |Clicked the category links on the nav bar| pass

### Logged in navigation bar

|Feature  | Expect  | Action | Result |
|--|--|--|--|
|My Account dropdown link |When logged in the My Account dropdown will show Profile and Logout when clicked |Clicked the My Account link on the nav bar| pass
|Profile link |When clicked it will direct the user to their profile |Clicked the Profile link on the nav bar| pass
|Logout link |When clicked it will direct the user to the logout page |Clicked the Logout link on the nav bar| pass

### Superuser navigation bar

|Feature  | Expect  | Action | Result |
|--|--|--|--|
|My Account dropdown link |When logged in as the superuser the My Account dropdown will show Admin Area, Profile and Logout when clicked |Clicked the My Account link on the nav bar| pass
|Admin Area link |When clicked it will direct the superuser to the admin area |Clicked the Admin Area link on the nav bar| pass

### Home page

|Feature  | Expect  | Action | Result |
|--|--|--|--|
|Shop Now button |When clicked it will direct the user to a list of all products |Clicked the Shop Now button| pass
|Custom Order button |When clicked it will direct the user to the custom order page |Clicked the Custom Order button| pass

### Products page

|Feature  | Expect  | Action | Result |
|--|--|--|--|
|Product image |When clicked it will direct the user to the product detail page |Clicked a product image| pass

### Products page - superuser

|Feature  | Expect  | Action | Result |
|--|--|--|--|
|Edit link |When a superuser is logged in an edit link will be displayed under each product, when clicked it will bring the superuser to the edit product page| clicked edit link | pass
|Delete link |When a superuser is logged in a delete link will be displayed under each product| Observed the delete link under each product | pass

### Product detail page
 
|Feature  | Expect  | Action | Result |
|--|--|--|--|
|Image clickable |When the image is clicked it will open in a new tab| Clicked image | pass
|Quantity selector - increment |When the increment button is clicked the quantity increases| Clicked the increment button on the quantity selector | pass
|Quantity selector - decrement |When the decrement button is clicked the quantity decreases| Clicked the decrement button on the quantity selector | pass
|Quantity selector - decrement disabled |When the quantity is 1 the decrement button on the quantity selector is disabled | Clicked the decrement button on the quantity selector when at 1 | pass
|Quantity selector - increment disabled |When the quantity is 50 the increment button on the quantity selector is disabled | Clicked the increment button on the quantity selector when at 50 | pass
|Keep Shopping button |When clicked the Keep Shopping button will direct the user to the all products page | Clicked the Keep Shopping button | pass
|Add to bag button |When clicked the Add to bag button will add the product to the users bag | Clicked the Add to bag button | pass
|Add to bag - shopping bag icon |When an item is added to the bag the price will increase under the shopping bag icon | Added product to bag and observed the shopping bag icon | pass
|Add to bag - toast |When an item is added to the bag a toast message will pop up detailing 'Product name has been added to your bag', the contents of the bag and a Go to Secure Checkout button | Added product to bag and observed the toast message | pass
|Secure Checkout button - toast |When the Go to Secure Checkout button is clicked it will direct the user to the shopping bag page| Clicked the Go to Secure Checkout button in the toast message | pass
|Increase quantity - toast message |When an item is added to the bag that is already in the bag the toast message will detail 'Updated product name to quantity x'| Add item to bag that is already in bag and observed the toast message | pass
|Reviews |Product reviews will be displayed below the product details| Observe the reviews section | pass

### Product detail - logged in user

|Feature  | Expect  | Action | Result |
|--|--|--|--|
|Leave a review |When user is logged in they can leave a review on a product | Review a product and clicked submit | pass
|Leave a review -  form validation |If a users submits a review with a required field left blank a message will detail 'Please fill in this field' | Leave message blank and clicked submit | pass
|Edit a review link |When user is logged in and they are the owner of the review they can edit the review. Clicking the edit link will open the edit review page | Clicked the edit link | pass 
|Edit a review - toast |When user is editing a review an information toast will pop up detailing 'You are editing a review posted by user' | Clicked the edit link and observed the toast message | pass 
|Editing a review |When on the edit review page the form should be prefilled with pervious review and can be updated when update is clicked| Clicked update on the edit review page | pass 
|Editing a review - success toast |When the review has been edited a success message will detail 'Successfully updated review'| Clicked update on the edit review page and observe toast message | pass
|Delete a review link |When user is logged in and they are the owner of the review they can delete the review. Clicking the delete link will remove the review | Clicked the delete link | pass 
|Delete a review - success toast |When the review has been deleted a success message will detail 'Review deleted!'| Clicked delete review and observe toast message | pass
|Average star rating |When a review is posted the star rating will contribute to the average rating displayed in the product detail| Add reviews and checked average star rating in product detail | pass

### Product detail  - superuser

|Feature  | Expect  | Action | Result |
|--|--|--|--|
|Edit link |When a superuser is logged in an edit link will be displayed under the price in the product detail page | Observed edit link | pass
|Delete link |When a superuser is logged in a delete link will be displayed under the price in the product detail page | Observed the delete link | pass

### Custom order page

|Feature  | Expect  | Action | Result |
|--|--|--|--|
|Custom order form |When form is filled in correctly and Place custom order is clicked a confirmation page will detail the price for the custom order | Filled in form and clicked Place custom order button | pass
|Custom order price |The price for the custom order will depend on the selections made by the user | Added different selections in the custom order form and checked the price differing | pass
|Custom order form - blank input validation |If Place custom order button is clicked with required fields left blank then a pop up will detail 'Please fill in this field' | Clicked Place custom order button and left colour scheme blank | pass
|Custom order form - Name validation |If Place custom order button is clicked with Personalised checked and the name field left blank then an error message will detail 'A name is required for personalised items' | Clicked Place custom order button and left name blank | pass
|All products button |When clicked the all products button will direct the user to the products page  | Clicked the all products button | pass
|Add to Bag button |When clicked the Add to Bag button will add the custom order to the bag and navigate to the shopping bag page | Clicked the Add to Bag button | pass
|Add to bag - toast |When a custom order is added to the bag a toast message will pop up detailing 'Custom order has been added to your bag', the contents of the bag and a Go to Secure Checkout button | Added custom order to bag and observed the toast message | pass
|Keep Shopping button |When clicked the Keep Shopping button will direct the user to the products page | Clicked the Keep Shopping button | pass
