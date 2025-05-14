### Demo Lab Explanation

- Have you ever noticed that in some applications, if you're not logged in and try to access their homepage, about page, or contact page, you are redirected to the login page? This happens because you need to log in first before accessing any features of the application.
- Once logged in, you typically won't be asked to log in again while accessing other features; you remain logged in.
- We can replicate this functionality to better understand how sessions work.

[App flow](image-2.png)

### Demo

- If a user tries to access the About or Contact page without logging in, they will be redirected to the login page.
- After a successful login, the user will be taken back to the page they originally tried to access. This is a new concept being introduced.
- If a user visits the login page directly (not via redirection), they will be taken to the homepage after logging in.
- This entire flow relies on sessions. Without storing login information in a session, this behavior wouldn't work.
- When a user tries to access a protected page, the system checks if they're logged in by checking the session. If not logged in, it redirects them and stores the original URL.
- After login, the system reads the stored path from the session and redirects the user to the original page.
