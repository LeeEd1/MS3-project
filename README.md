# Tasty Trove

![Site accross devices]()
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
- To be able to comment on a recipe

## Design:

### Wireframes



### Typography

MedievalSharp was selected for the heading of my page with gothic selected for the body of my page. All fonts obtained from googlefonts.

### Color scheme

My color scheme was orange black and white as shown below:

### Images

I do not hold any rights to the images that are uploaded as they are uploaded via photo URL

## Features

### Landing Page




### Game board

Once the user clicks start game the game board is revealed and the timer starts the countdown. 
![here](assets/documentation/game-board.PNG)

### Modals

![Here](assets/documentation/modal-instructions.PNG)
![Here](assets/documentation/win-modal.PNG) 
![Here](assets/documentation/game-over.PNG)

Above are 3 modals the player will see in their journey through the game. The first is the instructions modal which pops up when the player clicks How to play, The second is the win modal which pops up if the player is successful, The third is the game over modal.

### Footer

I have also added social media links along with youtube for more viewing pleasure.

## Testing:



### Manual testing

Below is a table of manual testing carried out by myself.

| Feauture tested | Action     | Outcome               | Result                    |
|-----------------|------------|-----------------------|---------------------------|
|                 | Left click | Pop up modal          | Successfully opens modal  |
|Modal close BTN  | Left click | Close Modal           | Successfully close modal  |
|Start game BTN   | Left click | Start's Game          | Successfully Start's game |
|New game BTN     | Left click | Clear's game          | Successfully Clear's game |
|Social links     | Left click | Direct to desired link| Successfully loads link   |

### Validator testing 

- HTML files passed through w3c with no issues found, As shown below.
![HTMLw3c](assets/documentation/html-check.PNG)

- Css files passed through w3c with 1 issue found which was a link to fontawesome, this has been corrected as shown below.
![Csserror](assets/documentation/error-css.PNG)
![Csscheck](assets/documentation/css-check.PNG)

- I used Js hint to check my JavaScript code, no errors as shown below. I did however remove all unnecassary semi colon's as it suggested and corrected a typo in my global variable.
![JSHint](assets/documentation/js-hint.PNG)

### Lighthouse reports


| location | Result                                               |
|----------|------------------------------------------------------|
| Desktop  | ![Desktop](assets/documentation/lighthouse-desk.PNG) |
| Mobile   | ![Mobile](assets/documentation/lighthouse-mob.PNG)   |

The page has a full house on Desktop and nearly full on Mobile. 

### Browsers & devices tested

- I have tested the site on Chrome, FireFox, Edge & safari with no issues.
- I tested the site accross multiple device platforms ranging from my Desktop pc to a galaxy fold (Smallest screensize availabe) with no issues or layout errors found.
  
### Responsiveness

While working on this game, I underestimated the complexity of the task. It was only midway through the project that I began to regret my decision not to utilize bootstrap and Jquery. Although I successfully ensured the game's functionality accross various devices, I now realise that opting for libraries like Bootstrap and Jquery could have allowed me to implement a more intricate and sophisticated game.

### Bugs

After my final testing phases, There are no known bugs to date.

## Technologies used:

### languages

- ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

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