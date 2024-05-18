## Testing:


### Manual testing

Below are tables of manual testing carried out by myself.

#### Homepage:

| Feature tested  | Action     | Expected Outcome         | Result                    |
|-----------------|------------|--------------------------|---------------------------|
|Logo             |Left click  |Redirect to home page     |Pass                       |
|Register Button  |Left click  |Redirect to Register page |Pass                       |
|Social links     |Left click  |Redirect to link clicked  |Pass                       |

#### Recipes:

| Feature tested  | Action     | Expected Outcome                                       | Result|
|-----------------|------------|--------------------------------------------------------|-------|
|Logo             |Left click  |Redirect to home page                                   |Pass   |
|Recipe Filter    |Left click  |Show recipes of selection                               |Pass   |
|View recipe BTN  |Left click  |Open recipe detials in a new page                       |Pass   |
|Edit recipe BTN  |Left click  |Opens edit recipe with fields filled with previous data |Pass   |
|Delete reipe BTN |Left click  |Trigger confirmation modal                              |Pass   |
|Social links     |Left click  |Redirect to link clicked                                |Pass   |

#### Add recipes:

| Feature tested  | Action     | Expected Outcome           | Result  |
|-----------------|------------|----------------------------|---------|
|Logo             |Left click  |Redirect to home page       |Pass     |
|Category Clicker |Left click  |Drop down menu of categories|Pass     |
|Submit BTN       |Left click  |Submit form to DB           |Pass     |
|Social links     |Left click  |Redirect to link clicked    |Pass     |

#### Account page:

| Feature tested  | Action     |Expected Outcome          | Result    |
|-----------------|------------|--------------------------|-----------|
|Logo             |Left click  |Redirect to home page     |Pass       |
|Edit BTN         |Left click  |Redirect to edit profile  |Pass       |
|Delete BTN       |Left click  |Trigger delete modal      |Pass       |
|Social links     |Left click  |Redirect to link clicked  |Pass       |


#### Admin page:

| Feature tested    | Action     | Expected Outcome             | Result   |
|-------------------|------------|------------------------------|----------|
|Logo               |Left click  |Redirect to home page         |Pass      |
|Add category BTN   |Left click  |Redirect to Add category form |Pass      |
|Edit category BTN  |Left click  |Redirect to edit category form|Pass      |
|Delete category BTN|Left click  |Redirect to edit category form|Pass      |
|Social links       |Left click  |Redirect to link clicked      |Pass      |

#### Forms:

| Feature tested    | Action                | Expected Outcome   | Result   |
|-------------------|-----------------------|--------------------|----------|
|Register form      |Fill fields and submit |Submits form to DB  |Pass      |
|Edit account form  |Fill fields and submit |Submits form to DB  |Pass      |
|Add recipe form    |Fill fields and submit |Submits form to DB  |Pass      |
|Edit recipe form   |Fill fields and submit |Submits form to DB  |Pass      |
|Add category form  |Fill fields and submit |Submits form to DB  |Pass      |
|Edit category form |Fill fields and submit |Submits form to DB  |Pass      |

### Validator testing:

#### HTML:

HTML error:
![Html-error](/static/images/test-img/html-error.png)

I had one error when checking html code through [w3c](https://validator.w3.org/). This was due to a stray div in one of my templates, to find this issue I right clicked the page and then clicked view page source to locate the stray div to see the surrounding code then I was able to see which template this was in.

HTML Correction:
![HTML-correct](/static/images/test-img/html-check.png)

#### CSS:

CSS error:
![CSS-error](/static/images/test-img/css-error.png)

CSS Input check:
![CSS-error](/static/images/test-img/css-error.png)

I had 1 error when checking CSS code through [w3c](https://jigsaw.w3.org/css-validator/). This is due to the materialize library I am using, I tried to correct this issue with a manual CSS rule but this was unsuccessful. Due to my time constraints I didn't investigate this any further and removed the style rule.

I knew the issue was through the library however I used direct input just for piece of mind as shown above.



### Lighthouse reports

#### Home page:

![home-desk](/static/images/test-img/home-lh.png)
![home-mob](/static/images/test-img/home-mob.png)

#### Recipes:

![recipes-desk](/static/images/test-img/recipe-lh.png)
![recipes-mob](/static/images/test-img/recipe-lh.png)

#### View recipe:

![view recipe-desk](/static/images/test-img/vr-lh.png)
![view recipe-desk](/static/images/test-img/vr-mob.png)

#### Register:

![register-desk](/static/images/test-img/reg-lh.png)
![register-mob](/static/images/test-img/reg-mob.png)

#### Log in:

![login-desk](/static/images/test-img/login-lh.png)
![login-mob](/static/images/test-img/login-mob.png)

#### Add recipe:

![Add recipes-desk](/static/images/test-img/ar-lh.png)
![Add recipes-mob](/static/images/test-img/ar-mob.png)

#### Account page:

![account-desk](/static/images/test-img/account-lh.png)
![account-mob](/static/images/test-img/account-mob.png)

#### Admin:

![admin-desk](/static/images/test-img/admin-lh.png)
![admin-mob](/static/images/test-img/admin-mob.png)


 

### Browsers & devices tested

- I have tested the site on Chrome, FireFox, Edge & safari with no issues.
- I tested the site accross multiple device platforms ranging from my Desktop pc to a galaxy fold (Smallest screensize availabe) with no issues or layout errors found.
  
### Responsiveness

