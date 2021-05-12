

# Visitor story testing

| Test Case | User Story                                                             | Expected Result                                                                                                    | Actual Result |
|-----------|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------|
| 1.0       | As a visitor I want to easily view the dictionary                      | Visitor enters page URL and the main dictionary page opens                                                         | Pass          |
| 1.1       | (subtest)                                                              | All words render on the page                                                                                       | Pass          |
| 1.2       | (subtest)                                                              | All other elements render on the page (navigation bar, footer, serach bar & links)                                 | Pass          |
| 2.0       | As a visitor I want to search for specific words                       | Search bar is rendered on the page                                                                                 | Pass          |
| 2.1       | (subtest)                                                              | Visitor can enter text in the serach bar                                                                           | Pass          |
| 2.2       | (subtest)                                                              | Clicking on the search button initiates serach and results are displayed on page                                   | Pass          |
| 2.3       | (subtest)                                                              | If no results, visitor is informed that the search returned no results                                             | Pass          |
| 3.0       | As a visitor I want to find out more information about this dictionary | Visitor clicks on "About" link and is taken to the about page                                                      | Pass          |
| 4.0       | As a visitor I want to register for an account                         | Visitor clicks on the register link and is taken to the register page                                              | Pass          |
| 4.1       | (subtest)                                                              | Visitor can enter information in the imput fields                                                                  | Pass          |
| 4.2       | (subtest)                                                              | Form validation requires the visitor to enter username of minimum 5 characters                                     | Pass          |
| 4.3       | (subtest)                                                              | Form validation checks that the password was entered correctly twice                                               | Pass          |
| 4.4       | (subtest)                                                              | If registration successful, visitor is informed they are now registered                                            | Pass          |
| 4.5       | (subtest)                                                              | If the username is already taken, visitor is asked to choose another username and redirected back to register page | Pass          |
| 5.0       | As a visitor I want to easily navigate the page                        | Pagination is present on the dictionary page                                                                       | Pass          |
| 5.1       | (subtest)                                                              | Clicking on any page number takes the visitor to that specific page                                                | Pass          |
| 5.2       | (subtest)                                                              | Clicking on the "Previous" and "Next buttons increments the page by one                                            | Pass          |


# Registered User story testing
| Test Case | User Story                                           | Expected Result                                                                                                     | Actual Result |
|-----------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------|
| 1.0       | As a user I want to log in                           | User clicks on "Log In" link and is taken to the login page                                                         | Pass          |
| 1.1       | (subtest)                                            | User enters correct username and password and is then taken to their user dashboard                                 | Pass          |
| 1.2       | (subtest)                                            | User enters incorrect username and is informed that the username or password is incorrect                           | Pass          |
| 1.3       | (subtest)                                            | User enters incorrect password and is informed that the username or password is incorrect                           | Pass          |
| 2.0       | As a user I want to submit a new word                | Submit new word button is present on the user dashboard and the "User Tools" dropdown menu                          | Pass          |
| 2.1       | (subtest)                                            | Clicking either the button or the link takes the user to the submit new word form                                   | Pass          |
| 2.2       | (subtest)                                            | User is required to fill in all fields of the form                                                                  | Pass          |
| 2.3       | (subtest)                                            | User clicks on the "submit" button and is redirected back to their dashboard                                        | Pass          |
| 2.4       | (subtest)                                            | User can cancel the submission and is returned to the dashboard                                                     | Pass          |
| 2.5       | (subtest)                                            | User is informed that they submitted a new word successfully                                                        | Pass          |
| 2.6       | (subtest)                                            | If the word exists, user is informed that the word exists and asked to add another word                             | Pass          |
| 2.7       | (subtest)                                            | On the dashboard, the user will see the new word they submitted in the "Pending Approval" section of the dashboard  | Pass          |
| 3.0       | As a user I want to see the status of my submissions | User clicks on "Profile Dashboard" link in the "User Tools" dropdown and is taken to their dashboard                | Pass          |
| 3.1       | (subtest)                                            | Acordion renders and all submitted words populate                                                                   | Pass          |
| 3.2       | (subtest)                                            | Words are categorised in "Approved" and "Pending Approval"                                                          | Pass          |
| 4.0       | As a user I want to edit words                       | In the "Pending Approval" section, user can see the "Edit" button                                                   | Pass          |
| 4.1       | (subtest)                                            | Clicking the "Edit" button takes the user to the edit word page                                                     | Pass          |
| 4.2       | (subtest)                                            | All fields are populated with the current data                                                                      | Pass          |
| 4.3       | (subtest)                                            | User is able to change the data                                                                                     | Pass          |
| 4.4       | (subtest)                                            | User can submit the new data                                                                                        | Pass          |
| 4.5       | (subtest)                                            | User can cancel the edit and is redirected to the dashboard                                                         | Pass          |
| 4.6       | (subtest)                                            | User is informed that the edit was successful and that it is pending approval                                       | Pass          |
| 5.0       | As a user I want to log out                          | User can navigate to the "Log out" link in the "User Tools"                                                         | Pass          |
| 5.1       | (subtest)                                            | User is informed they have logged out and are redirected to the main dictionary page                                | Pass          |
| 6.0       | As a user I want to change my password               | User can click on "Change Password" link in the "User Tools"                                                        | Pass          |
| 6.1       | (subtest)                                            | User is directed to the change password page                                                                        | Pass          |
| 6.2       | (subtest)                                            | If user enters an incorrect current password, they are informed that the current password is incorrect              | Pass          |
| 6.3       | (subtest)                                            | If user does not enter matching new passwords, the form validation informs the user that the passwords do not match | Pass          |
| 6.4       | (subtest)                                            | If user enters all information correctly they are informed that their password has changed                          | Pass          |
| 6.5       | (subtest)                                            | If user uses old password, to log back in, they are denied                                                          | Pass          |
| 6.6       | (subtest)                                            | If user uses new password to log back in, they are successfully logged in                                           | Pass          |
# Editor story testing

| Test Case | User Story                                     | Expected Result                                                                                 | Actual Result |
|-----------|------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------|
| 1.0       | As an editor I want to approve submitted word  | When logged into their dashboard, editors can see words submitted by users                      | Pass          |
| 1.1       | (subtest)                                      | Editors can see a button "Quick Approve" on each submitted word                                 | Pass          |
| 1.2       | (subtest)                                      | When the "Quick Approve" button is pressed, editor is informed the word was approved            | Pass          |
| 2.0       | As an editor I want to reject a submitted word | When logged into their dashboard, editors can see words submitted by users                      | Pass          |
| 2.1       | (subtest)                                      | Editors can see a button "Reject" on each submitted word                                        | Pass          |
| 2.2       | (subtest)                                      | When the "Reject" button is pressed, editor is informed that the word was successfully rejected | Pass          |
| 3.0       | As an editor I want to edit words              | Editor can see "Edit" button on any word rendered on any page                                   | Pass          |
| 3.1       | (subtest)                                      | When editor clicks "Edit" they are taken to the edit word page                                  | Pass          |
| 3.2       | (subtest)                                      | All word details are displayed in the edit word form                                            | Pass          |
| 3.3       | (subtest)                                      | Editor can change information in the form                                                       | Pass          |
| 3.4       | (subtest)                                      | Editor is informed that the edit was successful                                                 | Pass          |
| 3.5       | (subtest)                                      | Edited word is now waiting for approval                                                         | Pass          |
| 4.0       | As an editor I want to delete words            | "Delete button is displayed on every word rendered on any page                                  | Pass          |
| 4.1       | (subtest)                                      | When "Delete" button is clicked a modal appears with all word details                           | Pass          |
| 4.2       | (subtest)                                      | Modal asks for confirmation to delete word                                                      | Pass          |
| 4.3       | (subtest)                                      | Editor can cancel delete task and return to the dashboard                                       | Pass          |
| 4.4       | (subtest)                                      | Editor deletes a word and is informed that the word was deleted                                 | Pass          |




# Administrator story testing

| Test Case | User Story                                                    | Expected Result                                                                                                               | Actual Result |
|-----------|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------|
| 1.0       | As an administrator I want to change user types for all users | When administrator logs in to their dashboard they can see "Change User Type" button                                          | Pass          |
| 1.1       | (subtest)                                                     | Clicking "Change User Type" button navigates to admin panel                                                                   | Pass          |
| 1.2       | (subtest)                                                     | Dropdown menu on admin panel shows the names and user type of all registered users                                            | Pass          |
| 1.3       | (subtest)                                                     | Admin can select user and assign a new user type                                                                              | Pass          |
| 1.4       | (subtest)                                                     | If admin assigns a user type which is the current user type for the user, admin is infomed the user is already that user type | Pass          |
| 2.0       | As an admin I don't want to edit my user type by mistake      | If admin tries to change their own user type, they are informed they cannot change their own type                             | Pass          |