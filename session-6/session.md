# Understanding Web Sessions

When we try to design sessions, basically what we mean by this is we will talk about a few techniques that we can use to try and enhance the security of our web sessions. 

Finally, to cap it off, we will try to demonstrate all of the concepts that we learned through code. We will implement a Flask application that will resemble a real-world application. So we’ll talk about that at the very end.

So guys, this is the plan for the class. With that note, let’s get started.

## What is a Web Session?

A **web session** refers to the period of time an end user is active on a web application until they log out. 

Let’s read that again:  
*A web session refers to a period of time that an end user is active on an application until they log out.*

### Example

Let’s take an example — you are a user and you have logged into an application, some web application or website.

- The time that you log in is the **start** of the session.
- From that point until you log out or close the application, that is your **session time period**.

I repeat: the moment you log in until the moment you log out or close the browser, that is your session duration.

During that time, you interact with the application:
- Click buttons
- Enter data
- Perform actions

All of this interaction creates **associated data**, which is stored on the **server side**.

> This interaction with the application and the server-side data storage together is called a **web session**.

## Why Are Web Sessions Useful?

Let me give you a basic analogy.

Imagine being back in school. When the bell rings, the class starts.  
When the next bell rings, the class ends.

So, between the **first bell** and the **second bell** is the class session — the time when the teacher interacts with us.

Now, if we **store** what the teacher is teaching in our minds, it’s useful for us.  
If we don’t, we’ll struggle in future classes.

If we capture and store that data, future learning becomes easier.

> **Similarly, web sessions help improve user experience** by storing relevant information during user interaction — enhancing convenience and smoothness.

## Where Is Session Data Stored?

Earlier, we mentioned that interaction happens between the **user** and the **application**. Naturally, there will be **associated data** generated.

### But where can this data be stored?

There are two places:

- **Client Side**
- **Server Side**

---

### 📍 What is the Client Side?

The **client** refers to the browser — the application running in the user's system.

In the browser, we can store data using **cookies**.

#### 🍪 What Are Cookies?

Cookies are **small pieces of data** stored in the user's browser.

- They capture user interaction with the application.
- When data is stored as cookies, this is referred to as a **client-side session**.

---

### 🗄️ What is the Server Side?

When the data is stored on the **server**, typically within a **database**, this is known as a **server-side session**.

---

### 🔄 Summary

| Storage | Location      | Method     |
|---------|---------------|------------|
| Client  | In browser    | Cookies    |
| Server  | On backend DB | Session DB |

---

## 🧑‍💻 Why Are Web Sessions Important for UX?

Web sessions improve **user experience** in several ways.

### ✅ Example 1: Persistent Login

You log into a website and start clicking on options and navigating pages.

- You **stay logged in** across pages.
- You're **not asked to log in again** after every click.

This happens because:
> Your **login status** is stored — typically at the backend.

---

### 🛒 Example 2: Shopping Cart Memory

You add items to a cart on Amazon, Swiggy, or JioMart.

Then you:
- **Close** the browser or app
- Later **reopen** it

What happens?

- Your **cart still contains items**
- This is possible because:
  > Interaction data is stored on the server

---

### 🎨 Example 3: UI Preferences

Suppose you change appearance settings (e.g., dark mode, font size).

- Next time you open the page, the settings are still applied.
- This is because:
  > Your preferences are stored — and **retained across sessions**

---

## 🧠 Conclusion: What Are Web Sessions?

Web sessions are periods where users interact with a web application, and **related data is stored**.

- 📍 Storage can happen on:
  - The **browser** (client-side cookies)
  - The **server** (backend database)

- 🎯 Goal: To **retain user state** across different interactions and enhance **user convenience**.

---

> Next time your login, cart items, or theme preferences are magically remembered — it's the power of web sessions in action!


# Working of Web Sessions

When a user interacts with a web application (e.g., logging in), some data needs to be stored to maintain the session. This can be done either on the **client side** or the **server side**.

---

## 📍 Client Side

The data can be stored in the browser using:
- **Cookies**: Small data packets stored in the browser.
- Helps retain user preferences or login status across pages.

---

## 📍 Server Side

The data can be stored on the server using:
- **Sessions**: When a user logs in, a session is created.
- The server stores the session data (like user ID) in a database.
- The client receives a **session ID** via response cookies, which it sends in subsequent requests.

---

## 🧠 Example Use Cases

1. **Login Persistence**:
   - After logging into a website, you stay logged in across pages.
   - Session information is stored and passed back to the server with each request.

2. **Shopping Cart**:
   - Items added to the cart remain even after closing and reopening the app.
   - The backend stores the cart data linked to your session or account.

3. **Preferences Retention**:
   - Font settings or themes (like dark mode) remain intact when you revisit.
   - These are saved either in cookies or on the backend linked to your session.

---

## 📌 Summary

A **web session** is a time period during which a user interacts with a web app. Data related to the session can be stored:
- On the **client side** (cookies),
- On the **server side** (sessions in a database).

This improves user experience by maintaining state across requests in otherwise stateless HTTP protocol.

---

[session-explain]](image.png)

[session-steps]](image-1.png)

## Concept 2: Interaction Between Client and Server (HTTP)

### HTTP Protocol

- HTTP (HyperText Transfer Protocol) is the medium through which **clients (like browsers)** interact with **servers**.
- It is a **stateless protocol**, meaning:
  - It does **not retain any information** from previous interactions.
  - Each HTTP request is **independent**.
  - The server does **not remember** who made previous requests.

---

### Stateless Explanation

- If you send a request to retrieve some data (GET) or post some data (POST), HTTP **does not retain any memory** of the request after it's completed.
- It **only handles the current request** and forgets it afterward.
- There is **no memory or session data** stored inherently in HTTP.

---

### Real-life Example: Banking Application

1. **User Login:**
   - You open a banking application.
   - Enter:
     - Username
     - Email address
     - Password
   - Click **Login**.
   - Behind the scenes:
     - A **HTTP request** is sent with your credentials.
     - The **server checks** these credentials against its **database**.
     - If credentials are valid:
       - A **homepage** is returned (response).
     - If invalid:
       - An **error message** is returned.

2. **After Login:**
   - You navigate to **About Page** or **Contact Us Page**.
   - Each time:
     - A new **HTTP request** is sent.
     - The server returns the respective **page as response**.

---

### How Is Login Status Retained If HTTP Is Stateless?

- Even though HTTP is stateless, your **login status persists** on all pages.
- You may even see:  
  *“Logged in as [username]”* on the top of every page.
  
---

### Session Management

- When you **log in**, the server:
  - Stores your **login data**.
  - Generates a **unique session ID**.
- This data is stored in a **session store** on the server:

  ```plaintext
  Session ID: 123456
  Username: john_doe
  Email: john@example.com
  ```

Think of it like a key-value pair:

```json

{
  "123456": {
    "username": "john_doe",
    "email": "john@example.com"
  }
}

```

- This ID is sent back to the client and usually stored in a cookie.

- Every subsequent request from the client includes this session ID, allowing the server to:

 > Identify the user.

 > Serve the correct data.