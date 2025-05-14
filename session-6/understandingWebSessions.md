
# Understanding Web Sessions in Client-Server Architecture

In modern web applications, understanding how sessions work is key to maintaining user state across multiple interactions. Here's a comprehensive breakdown of how sessions function in a client-server setup.

---

## 1. Client-Server Architecture

Any web application operates using the **client-server model**. The client (typically a browser) communicates with a remote server, which processes requests and sends back responses.

---

## 2. HTTP is Stateless

The interaction between the client and server occurs over the **HTTP protocol**.

- HTTP is **stateless**, meaning it does not retain any information about previous requests.
- Every request is treated independently. This means once a request is completed, HTTP "forgets" everything about it.
  
_For example_:  
You may log in to a banking site, and then go to another page. Even though you’re still logged in, HTTP alone doesn’t remember that.

---

## 3. Login Credentials Are Stored in the Server

When you log in (e.g., to a bank application), you enter your **email/username and password**.

- A request is sent to the server with these **login credentials**.
- The server checks these credentials against its database.

---

## 4. Session ID Is Generated

If your credentials are valid:

- The server **generates a unique Session ID** (e.g., `123`) to represent your session.
- It creates a key-value pair like:

  ```json
  {
    "123": {
      "username": "user@example.com",
      "preferences": {...}
    }
  }
  ```

---

## 5. Session Store

All login session data is stored under a unique **Session ID** in the **Session Store**.

This is like a dictionary or hashmap on the server that maps each Session ID to its respective user data.

When the server responds to the login request, it includes the **Session ID as a cookie**.

The client browser saves this cookie.

---

## 6. Maintaining Session Across Interactions

From this point on:

- Every request the client sends will **automatically include the Session ID cookie**.
- The server uses this Session ID to **look up the session data** from the Session Store.
- This is how your:
  - Logged-in status  
  - Shopping cart  
  - Preferences  
  ...are maintained across interactions.

---

## Client-Side vs. Server-Side Sessions

- **Client-side sessions**:  
  Data is stored on the client, often encrypted inside cookies.  
  _Example_: Flask (default behavior)

- **Server-side sessions**:  
  Session data is stored entirely on the server.  
  Requires a library or database for storage.

---

## Summary

| Concept              | Description                                                  |
|----------------------|--------------------------------------------------------------|
| Stateless HTTP       | Each HTTP request is independent.                            |
| Session ID           | Unique identifier sent by server after login.                |
| Session Store        | Server-side storage of session data using Session ID.        |
| Cookie               | Stores Session ID on the client.                             |
| Client Interaction   | Future requests include Session ID for continuity.           |

---

### How Does a Session End?

When the session ends, the **session ID is deleted**. Once that happens, your session is considered **closed**.

At this point, the **server no longer has any idea who you are**. The connection between your identity and the server is lost.

So, the next time you **open the application**, you'll need to **log in again**, because the previous session is gone.

A **new session** will be created, and the same process will repeat — a new session ID will be **generated**, **stored**, and **sent to the client**.

This is what happens **behind the scenes** in applications using **session-based authentication**.

---

## Understanding Client-Side vs. Server-Side Sessions

We’ve established that when a user interacts with a web application, their data is stored in the **Session Store**. In the first response from the server (after login), a **Session ID** is sent to the client.

However, there are **two types of session mechanisms** based on what gets sent to the client:

---

### 1. Client-Side Session

If the **entire session data**, including the session ID and the user data, is sent to the client as a **cookie**, it’s called a **client-side session** (or simply, *client session*).

- **Definition**: A session where the entire session data is sent to the client.
- The data resides on the **client**, typically in cookies (often encrypted).

---

### 2. Server-Side Session

If **only the session ID** is sent to the client (not the session data), then it's a **server-side session** (or *server session*).

- **Definition**: A session where only the session ID is sent to the client.
- The actual data stays securely on the **server**.

---

### Flask and Sessions

- By **default**, **Flask** uses **client-side sessions**.
- That means Flask sends the session data to the client as cookies.
- However, it’s possible to use **server-side sessions** in Flask.
  - To do this, you’ll need to use an **external library** or a **server-side session extension**.

---

> The **main concept** revolves around the generation of a Session ID and sending that ID along with the request. Everything else builds upon the basic client-server architecture.