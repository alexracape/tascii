# Design Documentation

## Home Page
For the home page we took inspiration from social media platforms like YikYak which are already popular amongst college students. We had to carefully think about what information we wanted to include in each post, and we ultimately decided on a stripped down card that displays the essential information about each post. Then users can click on it to see more details about the post. 

In our initial prototypes, users found the interface to be confusing and difficult to navigate. We didn't have a clear way to go back to the home page, and it wasn't clear which page was most relevant. We also used conflicting language describe the main page. For example, we used 'post', 'task', and 'request' to refer to the same thing which was confusing for first time users.

We also wanted the feed to appear seamlessly for users that are both logged in and logged out. To do this we render the page dynamically based on whether the user has logged in and been authenticated. If users are not signed in, almost all of the buttons on the page direct them towards the login page. Similarly, the login and signup buttons become replaced with profile and logout buttons once the user is signed in.

We also built in sort and search functionality as this is essential as the number of posts increases. The nice thing is that the search looks through both post titles and the locations, allowing users to filter results with just one search. 

Users gave us feedback in our initial prototypes indicating that the design was a bit boring, so we added a scroll animation to make the experience a bit more engaging. We also chose to accent all of the prominent buttons with color to draw the users eye to the main actions available on the page. In a sense, we are using color as a signifier to highlight affordances within the design. 

## Log In and Sign Up
The login and signup pages are both relatively simple and straightforward. By staying consistent with a layout that is common in other websites, the process is comfortable and familiar. The signup page provides interactive feedback if the input is invalid, and there are little hints below some hints to guide users. 

## Make a Post and Edit Post
We wanted to streamline the posting process as much as possible, so the form only includes the essential information for a post. In our original form there were redundant fields that we were able to eliminate with default values. The first version of the form also made inputing dates extremely difficult. To help with this problem, the form includes a built-in calendar widget which is much more intuitive. Additionally, we changed the time estimate to a drop-down form with a few basic options to increase efficiency.

The form for editing a post mirrors the form for making a post in the first place, but all of the fields are automatically filled to reflect the current state of the post. It also allows users to take down a post, so that they are able to recover from a mistake easily. While this page isn't very flashy, it is essential for error recovery and user control.

## Profile
The profile page displays all personal information associated with the users account. It also presents some summary statistics such as rating, number of tasks completed, and number of tasks posted. It also is updated with a list of tasks you have posted and completed. We explored storing your history, accepted posts, and pending posts in seperate pages in our initial mockup, but users found this confusing. Instead we decided to simplify the number of pages in our design, by moving all personal information and storage into the profile page.

## Post Details
This page offers more information about the post that appears in the main feed. This page allows users to get the information necessary to complete the task, and most importantly, it serves as a confirmation that the user does actually want to accept the post. This is critical for error prevention.



