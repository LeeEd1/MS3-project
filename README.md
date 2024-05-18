# Tasty Trove

![Site accross devices](/static/images/readme-img/amiresponsive.png)
Tasty Trove was founded with the intention of fostering a community where food enthusiasts can freely share their favorite recipes, gain culinary inspiration, and explore diverse cuisines. Our platform encourages users to connect with like-minded individuals, discover new flavors, and embark on culinary adventures together.

## UX:

### Site purose

At Tasty Trove, our goal is  to help you discover, share and enjoy delicious recipes from around the world. Whether you're a seasoned chef or a kitchen novice, our platform is your go-to destination for finding tasty dishes, getting inspired and connecting with fellow food lovers!

### Site goal

The site goal is to become a popular online recipe sharing hub for foodies around the world. We aim to provide a vibrant community-driven platform that inspires creativity in the kitchen and encourage culinary exploration. At Tasty Trove we aim to make cooking more accessible and enjoyable for everyone.

### Audience

The site audience is aimed at anybody willing and able, even children with parental guidance.

### Communication

The communication of the page is designed to be easily understandable for any user. It features clear buttons, a user friendly modal pop up and employs easy to read fonts with distinctly displayed colors, aiming for universal accessability.

### Registered user goals

- Discover new recipes.
- Share their own Recipes.
- Learning new cuisines and cooking skills.
- Be able to update an existing recipe if they have found a way to make it better.
- Delete a recipe if they no longer wish to share it.

### New user goals

- Be able to easily navigate the site.
- Browse existing recipes.
- Be able to register if interested.
- Be able to log out after browsing 

### Future user goals

- To be able to like a recipe.
- To be able to comment on a recipe.

### Admin user

- As an admin I want to be able to Edit or Delete any recipe.
- Add or Remove any category.

## Design:

### Wireframes

Please refer to [WIREFRAMES.md](WIREFRAMES.md)

### Typography

MedievalSharp was selected for the heading of my page with gothic selected for the body of my page. All fonts obtained from googlefonts.

### Color scheme

My color scheme was orange black and white as shown below:

![Home/Recipes Wireframes](/static/images/readme-img/colors.png)

### Images

I do not hold any rights to the images that are uploaded as they are uploaded via photo URL
and this page is for educational purposes only!

### Responsiveness

While creating my page I fully utilized [Materialize Css](https://materializecss.com/) for my responsive design. 

## Features

### Landing Page:

![Landing page](/static/images/readme-img/landing-page.png)
Above is the landing page the new/registered user will see which features a full navbar to browse accessible pages and if a new user the necessary links to register if interested.


### Recipes page:

![Recipes page](/static/images/readme-img/recipes-newuser.png)
Above is the recipes page new user will see.

![Recipes page](/static/images/readme-img/recipes-user.png)
Above is the recipes page existing user will see which features a different nav bar and edit/delete if you own the recipe.

### Register page:

![Register page](/static/images/readme-img/register.png)
Above is the register page for the user to join if interested.

### Add recipe page:

![Add recipe page](/static/images/readme-img/add-recipe.png)
Above is the Add recipe page for registered users.

### Account page:

![Account page](/static/images/readme-img/account.png)
Above is the account page where the user can view/edit their details.

### Admin page:

![Admin page](/static/images/readme-img/admin.png)
Above is the admin page which is only accessible to the user Admin.

![Admin page](/static/images/readme-img/admin-add.png)
Above is the Add category form which is only accessible to the user Admin.

### Nav bar:

![Navbar](/static/images/readme-img/new-nav.png)
Above is the navbar new users will see. New users will be able to browse recipes then register if interested.

![Navbar](/static/images/readme-img/nav-bar.png)
Above is the navbar existing user will see, however the admin tab is only accessible if your admin. This collapses on smaller devices.

### Footer:

![Footer](/static/images/readme-img/footer.png)
The page is also equipped with a footer with social icons for more viewing pleaure.

### Modals:

![Modal](/static/images/readme-img/modal.png)
Modal example, there are 3 in total which are delete recipe/delete account or delete category, however the delete category is only accesible to admins. Each modal is the same but the text inside corresponds with the button that is clicked.

### Database design:

![Db design](/static/images/readme-img/db-lucid.png)
Above is my database design which I created using Lucic Chart, I am using mongoDB which is a non-relational database.

## Testing:

Please refer to [TESTING.md](TESTING.md)

### Bugs

While creating Treasure trove I was continuously using dev tools throughout to check for design issues/bugs and corrected them as I found them. To my knowlege there are no known bugs to date.


## Technologies used:

### languages

- ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
- ![Jquery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
- ![PYTHON](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Frameworks, libraries & programs used.

- Materialize - Responsive design and most of css.
- Font Awesome - Too add icons to the page.
- Git Pod - Too create my project
- Git hub - To store my repository
- Heroku - To deploy my app
- MongoDB - To store all my information for the website
- Am I Responsive - To view site on all devices
- Google fonts - For the fonts MedievalSharp and Gothic
- Balsamiq - For my wireframes
- Snipping tool - for all my snippets for readme.

## Deployment

### MongoDB

I chose to use [MongoDB](https://www.mongodb.com) as its non-relational database.

To set up the Database URI, I followed these steps:
- I Navigate to the Cluster(myFirstCluster) and clicked on collections.
- I then created a new DB called Tasty Trove.
- I set up 3 collections (Users, Recipes, Categories)
- I Clicked on the connect button and selected connect your application
- I copied the connection string and replaced the password with my password.
- The connection string was then stored in my env.py file and I used it as a connection variable when deploying my App.


### Heroku Deployment

To deploy your app on [Heroku](https://www.heroku.com/platform), follow these steps:

- Sign up for a Heroku account.
- Click on the New button and select Create New App.
- Choose a unique name for your app.
- Select a region and click Create App. Chose the nearest region to you.
- Choose your connection method, I chose to do automatic deployment from a GitHub repository.
- Check your GitHub profile is visible, and search for the repository.
- Once the repository is found, click Connect.
- Navigate to the Settings tab and click Reveal Config Vars.
- Then duplicate your env.py file in the Fields provided.
- After adding all config vars, return to the Deploy tab and click Enable Automatic Deploys. Select the branch to deploy and click Deploy.
- Once the deployment is complete, click "Open App" to view the live site.

Heroku needs a requirements.txt and Procfile for the app to work.

Commands to install both files are:

- pip3 install -r requirements.txt
- echo web: python app.py > Procfile

After installing the requirements.txt you will need to run this command:
- pip3 freeze --local > requirements.txt (Ensuring you are updating this file every time you install packages by running this command again)

You will also need to create an env.py as follows:

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("MONGO_DBNAME", "Your own value")
os.environ.setdefault("MONGO_URI", "Your own value")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "Your own value")`

### Content

- [Color Hex](https://www.color-hex.com/color-palette/64222) For my color choices.
- [Font Awesome](https://fontawesome.com/) For my icons.
- [Google fonts](https://fonts.google.com/) For my fonts.

## Media

I do not hold any rights to any images displayed on this site as they are uploaded by photo URL, this site is purely educational purposes only.

### People

- I would like to thank my mentor [Spencer barriball](https://github.com/5pence) for His support throughout my first and second project has been immense and greatly appreciated.
- I would like to thank my friend [Nicholas Mobey](https://www.linkedin.com/in/nicolas-mobey-79149049) for His support constantly throughout my projects pushing me on when the going gets tough and guiding me where it's neeeded.
- I would like to thank the [CI Tutor support](https://learn.codeinstitute.net/ci_support/level5diplomainwebappdevelopment/tutor) for their ongoing support throughout my projects.
- I would like to also take the time to thank [Code Institute](https://codeinstitute.net/) as a whole, I have faced a very difficult few months in my home life and recieved nothing but support from CI student care and for that I am very greatful.