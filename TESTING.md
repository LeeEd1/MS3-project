## Testing:

### User story testing:

#### New users:

|Story                                                                                      |Page          |Documentation                                                       | 
|-------------------------------------------------------------------------------------------|------------------------|----------------------------------------------------------|
|Clear Information on what the site is about and a button to register if interested         |Home page               |![Home](/static/images/readme-img/landing-page.png)       |
|Clear navigation menu which collapses on smaller devices                                   |Home Page               |![Nav2](/static/images/readme-img/new-nav.png)            |
|Recipes page has all the recipes listed clearly with a easy to use recipe filter at the top|Recipe page             |![Recipes](/static/images/readme-img/recipes-newuser.png) |
|Throughout the page there are informative prompts flash messages                           |All pages               |![Field-prompt](/static/images/test-img/flash.png)        |
|Throughout the page there are informative prompts for fields                               |All pages with forms    |![Field-prompt](/static/images/test-img/field-prompt.png) |
|The footer of the page was kept minimal just with socials links for viewing pleasure       |All pages               |![Footer](/static/images/readme-img/footer.png)           |

#### Existing users:

|Story                                                                                                     |Page          |Documentation                                                       | 
|----------------------------------------------------------------------------------------------------------|------------------------|----------------------------------------------------------|
|Clear Information on what the site is about and a button to View recipe                                   |Home page               |![Home](/static/images/readme-img/landing-page.png)       |
|Clear navigation menu which collapses on smaller devices                                                  |Home Page               |![Nav2](/static/images/readme-img/nav-bar.png)            |
|Recipes are listed clearly with a easy to use recipe filter at the top with edit/delete BTN if owner of recipe|Recipe page         |![Recipes](/static/images/readme-img/recipes-user.png)    |
|Add recipe page features a form that is easy to read where the user gets prompted with any errors in field|Add recipe page         |![Add recipe](/static/images/readme-img/add-recipe.png)   |
|Edit recipe page features a form that is pre filled with the data from DB                                 |Edit recipe page        |![Add recipe](/static/images/readme-img/er-form.png)      |
|Account page features a simple card that is easy to read where the user can delete or edit account        |Account page            |![Field-prompt](/static/images/readme-img/account.png)    |
|Throughout the page there are informative prompts flash messages (Text changes depending on action)       |All pages               |![Field-prompt](/static/images/test-img/flash.png)        |
|Throughout the page there are informative prompts for fields                                              |All pages with forms    |![Field-prompt](/static/images/test-img/field-prompt.png) |
|The footer of the page was kept minimal just with socials links for viewing pleasure                      |All pages               |![Footer](/static/images/readme-img/footer.png)           |

#### Admin user:
  
|Story                                                                                                     |Page                    |Documentation                                        | 
|----------------------------------------------------------------------------------------------------------|------------------------|-----------------------------------------------------|
|Admin page features current categories with option to add/edit or delete                                  |Admin page              |![Admin page](/static/images/readme-img/admin.png)   |
|Admin is also able edit/delete any recipe on the page not just their own                                  |Recipes page            |![Admin page](/static/images/test-img/admin-dlt.png) |

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

I had 1 error when checking CSS code through [w3c](https://jigsaw.w3.org/css-validator/). This is due to the materialize library I am using, I tried to correct this issue with a manual CSS rule but this was unsuccessful. Due to my time constraints I didn't investigate this any further and removed the style rule because I dont think this will cause any issues.

CSS Input check:
![CSS-error](/static/images/test-img/css-manual.png)

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

After going through my lighthouse tests I came accross a few issues mostly minor things like buttons and contrast which I have corrected to improve the scores.

I also had an issue with the contrast on my forms where by the text was not sufficient for all readers so I applied a global style rule to change the text to a darker colour on all forms to combat this issue as shown below.

label {
    color: rgb(77, 75, 75) !important;
}

After testing the recipes page on lighthouse I found that there was a significant drop in the scores on mobile mainly due to the way the images are being uploaded(By URL) as they can vary in size which I have no control over, To combat this issue I googled [This](https://www.google.com/search?q=how+can+i+improve+light+house+score+with+images+uploaded+by+url&sca_esv=aabad935989ed720&sca_upv=1&ei=mqdIZuezHrP97_UPvsiz2Ao&ved=0ahUKEwjn6LT7oZeGAxWz_rsIHT7kDKsQ4dUDCBA&uact=5&oq=how+can+i+improve+light+house+score+with+images+uploaded+by+url&gs_lp=Egxnd3Mtd2l6LXNlcnAiP2hvdyBjYW4gaSBpbXByb3ZlIGxpZ2h0IGhvdXNlIHNjb3JlIHdpdGggaW1hZ2VzIHVwbG9hZGVkIGJ5IHVybEjAkQFQAFjBjwFwB3gBkAEBmAHeAaAB4CqqAQY2OC4xLjG4AQPIAQD4AQGYAkSgAucnqAITwgIKEAAYgAQYQxiKBcICEBAAGIAEGLEDGEMYgwEYigXCAggQABiABBixA8ICCxAAGIAEGLEDGIMBwgIOEC4YgAQYsQMY0QMYxwHCAhEQLhiABBixAxjRAxiDARjHAcICDhAuGIAEGLEDGIMBGIoFwgIdEAAYgAQYtAIY1AMY5QIYtwMYigUY6gIYigPYAQHCAhYQABgDGLQCGOUCGOoCGIwDGI8B2AECwgIWEC4YAxi0AhjlAhjqAhiMAxiPAdgBAsICCxAAGIAEGJECGIoFwgILEC4YgAQYkQIYigXCAgUQABiABMICCxAuGIAEGNEDGMcBwgILEAAYgAQYsQMYigXCAhEQLhiABBixAxiDARjUAhiKBcICDhAAGIAEGLEDGIMBGIoFwgILEC4YgAQYsQMY1ALCAgQQABgDwgIIEC4YgAQYsQPCAgYQABgWGB7CAggQABgWGB4YD8ICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogTCAgUQIRigAcICBRAhGJ8FwgIEECEYFcICBxAhGKABGArCAgYQIRgVGAqYAwW6BgQIARgHugYGCAIQARgKkgcGNjUuMi4xoAfipAM&sclient=gws-wiz-serp) and checked out the list provided which I ended up using loading="lazy" and this corrected my issue on mobile devices. This rule defers the loading of an image that is not needed on the page immediately.

Wile doing lighthouse tests I picked up the side nav trigger issue "Links do not have a discernible name". To combat this issue I used the same approach I used with the social icons which I picked up back in project one when I had the same issue by using an aria-label.

### CI python linter:

![Python linter](/static/images/test-img/linter-result.png)

Above is the CI python linter score. I had quite a few errors to correct mainly white space and trailing white space, all errors have been fixed and is fully pep8 compliant. 
I also had a few errors with continuation lines and at first I was struggling to break them up properly so I used the power of google and landed on [this](https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python-split-up-a-long-line-of) thread and I was able to then clear all the errors found.

### JS Hint:

![Jshint](/static/images/test-img/js-hint.png)

I passed my file through js hint, the file only contains Jquery code and shows no erros however it states $ is undefined which is not an issue because it's related to jquery.

### Browsers & devices tested:

During my testing phases I have tested this site heavily on the devices that are in my household which are predominantly android and windows and I corrected issues as I found them.
I had issues with forms on galaxy fold with the forms overlapping which I have corrected to the best of my ability. The site has been tested on galaxy s22, galaxy zfold4, alienware m15 r6, galaxy tab s7 and a desk top pc which are all fully functional.

I have also tested this site on an iphone14 and have checked through developer tools all the available Apple devices, the only downside to me testing these through devtools is it doesnt hold the software that could potentially cause bugs however I should have found these bugs on the iphone14 I physically tested thanks to my sister.
  
