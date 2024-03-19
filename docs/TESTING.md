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