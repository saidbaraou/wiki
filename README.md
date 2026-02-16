
# wiki

A simple wiki built with Django.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-%3E=3.0-green.svg)](https://www.djangoproject.com/)

## 📑Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Development Server](#running-the-development-server)
- [Usage](#usage)
- [Features](#features)
- [Technologies used](#technologies-used)


## 🔍Overview

This project is a basic wiki application developed using the Django web framework. It allows users to create, view, edit, and organize knowledge in a collaborative manner. It's designed to be lightweight and easy to deploy.

## ✨Features

- **Create Pages:** Users can create new wiki pages with rich text formatting.
- **View Pages:** Easily browse and read existing wiki pages.
- **Edit Pages:** Authorized users can modify the content of wiki pages.
- **Basic Navigation:** Simple navigation to browse through different pages.
- **Markdown Support:** Content is written and rendered using Markdown.
- **User Authentication:** Basic user registration and login for content management.
- **Search Functionality:** (Optional - Include if implemented) Search through the wiki content.

## 🚀Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### 🛠️Prerequisites

- **Python:** Make sure you have Python 3.8 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **pip:** Python package installer (should come with your Python installation).
- **Git:** Required for cloning the repository. You can download it from [git-scm.com](https://git-scm.com/downloads).

### ⚙️Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/saidbaraou/wiki.git](https://github.com/saidbaraou/wiki.git)
   cd wiki
   ```
   
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Make migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application.**

## ✨ Features

* **Listings:** Display of active and closed auction listings.
* **Product Page:** Detailed information about each listed item.
* **Create Listing:** Option for logged-in users to create new auction listings.
* **Watchlist:** Ability for users to track items they are interested in.
* **Categories:** View listings from different categories by filtering them.
* **Bidding:** System for placing bids on auction items.
* **Admin Interface:** Django's built-in admin interface for managing the application.

## 🛠️ Technologies Used

![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![image](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
=======
# saidbaraou
