# 🐦 TweetApp – A Minimal Django-Based Microblogging Platform

TweetApp is a simple yet functional microblogging web application built with Django. It allows users to register, log in, and share short messages ("tweets") securely. The project demonstrates core features of Django such as authentication, model forms, class-based views, and CRUD operations.

---

## 🚀 Features

- 📝 **Tweet Creation** – Add tweets via standard forms or Django ModelForms.
- 👥 **User Authentication** – Sign up, log in, and log out using Django’s built-in auth system.
- 🔒 **Access Control** – Only logged-in users can post tweets; users can only delete their own tweets.
- 📋 **Tweet Listing** – View all tweets chronologically with creation timestamps.
- 🎨 **Basic Styling** – Bootstrap 5 integrated with custom CSS for styling forms.

---

## 📂 Project Structure

```

django\_tweet/
├── tweetapp/               # Core app containing models, views, forms, templates
│   ├── templates/
│   │   └── tweetapp/       # HTML templates
│   ├── static/
│   │   └── tweetapp/       # Custom CSS
│   ├── models.py           # Tweet model linked to Django's User
│   ├── views.py            # Main views including tweet add/list/delete
│   ├── forms.py            # Form and ModelForm for tweet creation
│   ├── urls.py             # App-level routes
├── db.sqlite3              # Default SQLite database
├── manage.py
├── settings.py, urls.py    # Django project-level config

````

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML, Bootstrap 5, Custom CSS
- **Database**: SQLite (default for development)
- **Authentication**: Django built-in auth system

---

## 🧪 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tweetapp.git
   cd tweetapp
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access the app**
   Go to `http://127.0.0.1:8000/`

---

## ✅ To Do / Future Improvements

* 🌐 Improve UI/UX with more modern design.
* 🧪 Add unit and integration tests.
* 📬 Add support for replies and likes.
* 📦 Dockerize the app for deployment.

---

## 🙋‍♂️ Author

**Sarper Uzun**
MSc Computer Science | Junior Full-Stack Developer
[LinkedIn](https://www.linkedin.com/in/umut-sarper-uzun) | [GitHub](https://github.com/umutsarperuzun)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).


