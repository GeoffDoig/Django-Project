# Full-Stack Development Django Project

## Issue Tracker Web Application
[![Build Status](https://www.travis-ci.org/GeoffDoig/Django-Project.svg?branch=master)](https://www.travis-ci.org/GeoffDoig/Django-Project)

The Issue Tracker Web Application is designed to let users raise any issues they may have or request any features they would like
to see developed for a one-off fee. In the spirit of collaboration, users can leave comments on any issue documenting their
experience, or add their vote to either a bug that they have experienced or a feature that they would also like to see developed.
To further encourage the sense of community within the application, a blog section is provided for users to leave posts on any 
subject matter, in order to stimulate further discussion on any topic of interest.

As a user of the Issue Tracker Web Application :-
   * I want to be able to raise issues I encounter regarding bugs in programs.
   * I want to be able to suggest features I would like to see developed.
   * I would like to be able to leave comments on any issue and read other users comments.
   * I would like to be involved in an online community and take part in discussions on a variety of subjects.

Wireframes for the Issue Tracker Web Application can be found [here](/Wireframes)

### Features

Once a user has signed up for an account with the Issue Tracker, a unique personal profile page is created for the user.
The user is encouraged through the application to complete their profile page to enhance their experience of the application.
Providing a profile picture personalises the site for the user and this is used within the application blog to personalise posts.

Completing the personal details of the profile will allow the user to speed up the checkout process, since these details will be
pre-populated on the checkout page, meaning the user will only have to complete their card details to submit their payment and 
complete the checkout process.

### Technologies Used

[HMTL5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
   * Used to define the web application.

[Bootstrap4](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
   * A modern responsive front-end framework used to apply styles and colours to, and provide a responsive layout for the web application.

[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
   * Used to provide additional styling, spacing and colours to the web application.

[jQuery](https://jquery.com/)
   * Javascript library used to target specific HTML elements with javascript functions.

[Python](https://www.python.org/)
   * Used to code the application's logic and data processing needs.

[Django](https://docs.djangoproject.com/en/1.11/)
   * A Python web framework.

### Testing

__Automated Testing__

Automated tests have been written to confirm the correct operation of models, forms and views within each separate application of the
Issue Tracker Web Application. These tests can be run be typing 'python3 manage.py test' into the command line. The effectiveness of the
tests written is monitored by the coverage package, which runs the tests and produces a report indicating how much of the code has been
tested and what remains to be tested. This report can be viewed by running the 'index.html' file from the 'htmlcov' folder (currently at 90%).
Continuous Integration testing is provided by the Travis application and shows at the top of this file that the build is currently passing.

__Manual Testing__

The Issue Tracker Web Application has been extensively tested in a manual environment, to check the correct functionality of each page
as well as layout and responsiveness on a variety of different screen sizes.

   1. The Home Page is displayed on loading and displays text and images for the application, with buttons to link to view the issues, the blog
      or to sign up for an account. All buttons direct to the correct pages and the layout is correct on different screen sizes. Statistical
      information relating to all user activity across the Issue Tracker Web Application is displayed in the form of a pie chart.
   2. The Issues page displays all the issues on the application oredered by date. Individual issues are colour-coded according to their status.
      Clicking the 'Create New Issue' button at the bottom of the page, at this stage, will direct the user to log in to their account
      or sign up for an account if they don't already have one. Clicking on a specific Issue title displays full details of that issue
      and any associated comments and then prompts the user to log in or sign up for an account.
   3. The Blog page displays all the posts on the blog ordered by date. Clicking the 'Create New Post' button at the bottom of the page, 
      at this stage, will direct the user to log in or sign up for an account. The full blog post can read by clicking the 'read more' button.
   4. The Sign Up page displays a registration form for the application. Fields cannot be left blank and a message is displayed to prompt the user
      to complete the form. Successful registration directs the user to the Issues page and displays a success message.
   5. Should the user already have an account, the log in page is accessed directly from the link on the navigation bar at the top of the page.
      Fields on the log in form cannot be left blank and a message is displayed to prompt the user to complete the form. Successful log in directs
      the user to the Issues page and displays a success message.
   6. The Issues page displays as before, but now clicking the 'Create New Issue' button directs the user to the new issue page where a new issue
      can be logged to the application. Individual issues can be accessed as before, however, the user has access to the voting system to register
      their agreement with the issue and is provided with the ability to leave their own comments in reply to the issue.
   7. Registering agreement with a feature the user would also like to see developed, adds a one-off charge to the user's account and is displayed
      next to the cart link in the navigation bar at the top of the page. Clicking this link displays the cart contents and the payment due,
      with the option to remove the request should the user have a change of mind. Clicking the 'Checkout' button directs the user to the checkout
      page to process payment for the requested feature.
   8. The Checkout page displays the feature(s) the user is being charged for and provides forms for the user to complete their personal details
      and card details in order for the payment to be processed. If the user has completed their profile, the personal details section is already
      completed. Clicking 'Submit Payment' processes the payment through Stripe and directs the user back to the Issues page displaying a success
      message.
   9. The Profile page is accessed from the link on the navigation bar at the top of the page and displays the user's personal details and current
      image used as the profile picture. Statistical information relating to the specific user's activity across the Issue Tracker Web Application
      is displayed in the form of a bar chart with key. Clicking the 'Update your Profile Now' button, reveals a form with which the user can add
      or change/update their personal details and profile picture. When completed, a success message is displayed.
   10. Logging out of the Issue Tracker Web Application is achieved by clicking on the link in the navigation bar at the top of the page and returns
       the user to the Home page.

### Deployment

The Issue Tracker Web Application is deployed on Heroku at https://gd-issue-tracker.herokuapp.com/

AWS S3 was used to serve all the static and media files for the Issue Tracker Web Application. An account was set up with AWS and an S3 bucket
created to provide modern, easily scalable storage for the application's static and media files. The AWS secret access key and access key id
provided, were added to Heroku's Config Vars. The 'collectstatic' function was also disabled in Heroku's Config Vars to prevent static files
being loaded from the Github source code.

For Heroku deployment, a Postgres database is used, instead of the SQLite3 database used in Django during development. The Postgres database
url provided to access this database is added to Heroku's Config Vars. 

The Django secret key and the Stripe publishable and secret keys used in both development and production environments are also added to 
Heroku's Config Vars. A requirements.txt file and a Procfile are created and added to the Github source code prior to deployment on Heroku.

### Credits

__Content__

The sample additional text used in issues and blog posts to provide extra content was copied from :-
   * [Wikipedia - New Zealand](https://en.wikipedia.org/wiki/New_Zealand)
   * [Wikipedia - Celts](https://simple.wikipedia.org/wiki/Celts)
   * [Wikipedia- Leeds Rhinos](https://en.wikipedia.org/wiki/Leeds_Rhinos)

__Media__

The photos and images used in the application were obtained from searches carried out on Google.

__Acknowledgements__

Code Institute tutorials and walk-through projects were used as the basis for the user registration and authentication pages, 
the cart and checkout pages and the blog for the Issue Tracker Web Application.
