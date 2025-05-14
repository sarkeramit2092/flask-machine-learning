# Types of Sessions

## Based on Duration

### 1. Persistent Sessions
- These sessions remain active for a very long period of time.
- They end only when the user manually terminates the session.
- **Examples**: Social media platforms, OTT platforms.

# Persistent Sessions Explained

We have something called **persistent sessions** — you can also refer to them as **permanent sessions**. These sessions remain active for a very long period of time. A persistent session ends only when the user **manually terminates** it.

As long as the user does not terminate the session, it will remain **active**.

## Where is this useful?

Think about when you use any **social media application** like X (formerly Twitter) or Facebook. Even after 2–3 weeks, if you open the app, you'll see that your account is still logged in.

### How is that possible?

That’s because the session created when you first logged in is a **persistent session**. It stays active for a very long time — you remain logged in **until you manually log out**, or for a long period by default.

## Real-life examples

- **Social media platforms** (e.g., Facebook, X)
- **Streaming platforms** like **Amazon Prime** and **Netflix**

You stay logged in, and you’re not frequently asked to re-authenticate unless you manually log out.

---

### 2. Non-persistent Sessions
- These sessions last for a very short period, typically a single application visit.
- The session ends when the application or browser is closed.

## Non-Persistent Sessions

On the flip side, you also have **non-persistent sessions**.

These are the sessions that remain active for only a **very short period of time**. The moment you **close the browser** or if you're **inactive for a short period**, the session will **end automatically**.

### Characteristics:

- Session ends when the **browser is closed**
- Session may also end after a **short period of inactivity**
- Commonly used for **temporary access** or **secure environments** where long sessions are not allowed

These types of sessions are ideal for use cases where security is a concern, or where temporary, one-time access is required.


---

## Based on Security Mechanism

### 1. Authenticated Sessions
- Sessions are created only after the user has been authenticated (via login credentials).

In an **authenticated session**, the session starts **only after successful login**. For example, when you open a website or an application, you are required to **authenticate** yourself — typically by logging in with a username and password, or through another method like OTP, biometrics, etc.

Only after this authentication is successful will the **session begin**.

#### Key Points:
- **Authentication is mandatory** before the session starts
- These sessions ensure a **secure environment**
- Commonly used for **banking, enterprise, or any user-specific applications**

As a rule of thumb:  
> Wherever there is authentication, **there is security**.

### 2. Anonymous Sessions
- Sessions are created even if the user hasn't been authenticated.
- Useful for maintaining state information without authentication (as a "Guest").
- **Example**: Browsing online retail stores.

(Though not covered in your transcript, for completeness you may consider adding this.)

In contrast, an **anonymous session** starts **without authentication**. These are common in public-facing websites or applications where **no login is required**, and users can access general features.

#### Key Points:
- No login or authentication required
- Limited or read-only access
- Used in **public or informational platforms**

---

## Based on Storage Location

> Sessions can also be classified based on **where the session or state information is stored**. 
> There are two main types:

### 1. Client-side
- State information of the sessions is stored within the browser.
- Useful for storing small, insensitive data.
- **Example**: Browser cookies.


In **client-side sessions**, the session data is stored **within the browser**, typically in the form of **cookies**.

#### Key Points:
- Stored on the **client/browser**
- Should only be used for **non-sensitive** or **non-crucial** data
- Not suitable for storing login credentials, passwords, or other secure information
- Advantage: Lightweight and quick to access
- Risk: Less secure than server-side storage

Use this **only** when the data involved is not critical or sensitive.

### 2. Server-side
- State information of the sessions is stored in databases.
- Ideal for large volumes and sensitive data.
- Offers improved security and data integrity.

In **server-side sessions**, all session information is stored entirely on the **server** — typically in the application memory, server filesystem, or a **database**.

#### Key Points:
- Stored on the **server**
- Recommended when dealing with **sensitive or important data** like login credentials
- More **secure** compared to client-side sessions
- Typically used in production environments for applications requiring **data privacy**

#### Why server-side sessions?

> **Databases** and server environments are **designed for security** and data protection.  
> So, when working with sensitive or confidential information, always prefer **server-side sessions** over client-side ones.
