# cs4501sp17group6

## Project 2 (due 2/15)
APIs
- index(): located at /studenthousing/, accepts GET but not POST requests
- listings(): located at /studenthousing/listings/, accepts GET but not POST requests, will display all information for all listings in the database
- listing_create(): located at /studenthousing/listings/new/, accepts POST but not GET requests, will accept form-specified key:value pairs and will return a success message and the new listing object
- listing_detail(): located at /studenthousing/listings/{id}/, where id is an integer. accepts both GET and POST requests. will accept form-specified key:value pairs to update an existing listing via a POST request, or will return information about listing with id=id (if it exists) via a GET request; will return an error message if no such listing exists, otherwise will return a message saying that it doesn’t exist
- listing_delete(): located at /studenthousing/listings/delete/{id}, using a GET request, will delete a listing if the listing’s ID passed in exists in the database; if a POST request is used, will send a message saying action is not allowed
- users(): located at /studenthousing/users/, accepts GET but not POST requests, will display all information for all users in the database
- user_create(): located at /studenthousing/users/new/, accepts POST but not GET requests, will accept form-specified key:value pairs and will return a success message and the new user object
- user_detail(): located at /studenthousing/users/{id}/, where id is a positive integer. accepts both GET and POST requests. will accept form-specified key:value pairs to update an existing user via a POST request, or will return information about user with id=id (if it exists) via a GET request; will return an error message if no such user exists
- user_delete(): located at /studenthousing/users/delete/{id}, where id is a positive integer. accepts GET but not POST requests. will delete the user with id=id if such a user exists





