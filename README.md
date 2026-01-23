# Recipe-Sharing-Blog
 
Project by: Iyeme Salubi 

[View live project](https://our-recipe-app-368893a37080.herokuapp.com/)

This Community Sharing Recipe App is a simple, community-driven web app for discovering and sharing recipes. Browse the latest recipes, use the built-in search to find inspiration, and create an account to add your own recipes and contribute to the collection.

# Table of Contents

1. [Project Overview](#project-overview)
2. [User Stories](#user-stories)
3. [Rationale](#rationale)
   - [Project Purpose](#project-purpose)
   - [Target Audience](#target-audience)  
   - [Motivation and Inspiration](#motivation-and-inspiration)  
   - [Background and Context](#background-and-context)  
   - [Problem Statement](#problem-statement)
   - [Proposed Solution](#proposed-solution)  
   - [Benefits and Advantages](#benefits-and-advantages)  
   - [Project Scope and Limitations](#project-scope-and-limitations)  
   - [Future Improvements](#future-improvements)  
   - [Summary](#summary)  
5. [Design](#design)
   - [Brand Colours](#brand-colours)  
   - [Layout & Structure](#layout-and-structure)  
   - [Wireframes](#wireframes)  
6. [Deployment](#deployment)
7. [Security Features](#security-features)
8. [Testing](#testing)
   - [Browser Testing](#browser-testing)  
   - [Code Validation](#code-validation)  
   - [Lighthouse Test](#lighthouse-test)
9. [Testing Errors and Improvements](#testing-errors-and-improvements)
10. [Technologies Used](#technologies-used)
11. [Credit and Reference](#credit-and-reference)
12. [Author](#author)


# Project Overview
This project is based on developing a community-driven web app for discovering and sharing recipes: visitors can browse the latest recipe feed, search for dishes, and explore recipes by meal type (breakfast, lunch, dinner), then open a detailed recipe page to view information like description, calories, cuisine, ingredients, and step-by-step instructions. Users can also create an account and log in to contribute their own recipes through an authenticated “New recipe” flow, helping build a shared collection of everyday cooking ideas.

---

# User Stories
- View latest recipes
As a visitor, I want to see the latest recipes on the home/feed page so that I can quickly discover new ideas.

- Browse recipes by meal type
As a visitor, I want to browse recipes by meal type (breakfast/lunch/dinner) so that I can find recipes appropriate for that time of day.

- Search for recipes
As a visitor, I want to search for recipes so that I can quickly find a specific dish or ingredient.

- View a recipe’s details
As a visitor, I want to view a recipe’s full details so that I can cook it successfully.

- Create an account
As a new user, I want to sign up so that I can post my own recipes, view and edit past recipes, and also add new recipes

- Responsive browsing experience
As a user, I want the app to work well on smaller screens so that I can browse recipes and use them in my kitchen were i can't access my laptop

---

# Rationale

## Project Purpose

### Primary Goal
The **Community Sharing Recipe App** is designed to make it easy to **discover, browse, and share recipes** in one place—helping users go from “what should I cook?” to a clear set of ingredients and steps quickly.

### What the App Enables
At its core, the app supports these key user needs:
- Browse the **latest recipes** in a simple feed.
- Explore recipes by **meal type** (Breakfast, Lunch, Dinner).
- View **full recipe details** (description, calories, cuisine, ingredients, instructions).
- Create an account and sign in to **contribute recipes** (recipe creation is protected behind authentication).

---

## Target Audience

### Home Cooks and Busy Individuals
This app is ideal for people who cook at home and want quick inspiration without scrolling endlessly through blogs or social media. The latest-recipes feed and meal-type categories help users decide what to cook based on time of day and convenience.

### Beginners Learning to Cook
New cooks benefit from having recipes presented in a consistent structure—clear ingredient lists and step-by-step instructions—so they can follow along confidently without needing to interpret long-form content.

### People Who Cook on Mobile in the Kitchen
Because cooking often happens away from a laptop, this app suits users who rely on phones or tablets while preparing meals. A responsive design supports browsing and following recipes directly from smaller screens.

### Community Contributors
Users who enjoy sharing their own recipes (family meals, cultural dishes, creative experiments) can create accounts and contribute, helping the platform grow into a community-led recipe collection.

---

## Motivation and Inspiration

### Why This Project Exists
Finding recipes online is easy—but **finding the right recipe at the right time**, in a format that’s quick to follow, can be frustrating. Many people bounce between saved posts, screenshots, random browser tabs, and notes. This project was created to provide a **single, consistent place** to:
- discover new meal ideas,
- keep recipe information structured and readable,
- and share recipes with others without extra friction.

### Community-Driven Inspiration
The app is built around the idea that the best recipes often come from other home cooks—so the platform encourages users to **register and share their own meals** with the wider community.

---

## Background and Context

### The “Too Many Sources” Problem
Recipes live everywhere: social media, blogs, family messages, notes apps, and videos. Even when you find something great, it’s often hard to:
- locate it later,
- compare options quickly,
- or follow it cleanly while cooking.

### Cooking Happens Away From the Laptop
Cooking is a hands-on activity—people often use phones or tablets in the kitchen. That’s why a key requirement is a **responsive experience** so users can browse and follow recipes on smaller screens.

---

## Problem Statement

### The Pain Point
The project targets a common inefficiency: **recipe discovery and execution are often slower than they should be** because information is scattered, inconsistent, or not presented in a simple step-by-step format.

### What Needs Improving
This app aims to improve:
- **Discovery speed** (latest feed + meal categories).
- **Decision-making** (clear titles + short descriptions at a glance).
- **Cooking clarity** (ingredients and instructions displayed cleanly on the recipe page).

---

## Proposed Solution

### High-Level Approach
The solution is a simple web app that combines **recipe browsing** with **community contribution**, where recipes follow a consistent structure and users can quickly move from browsing to cooking.

### Key Features Mapped to User Stories

#### View Latest Recipes
As a visitor, I want to see the latest recipes on the home/feed page so that I can quickly discover new ideas.

#### Browse by Meal Type
As a visitor, I want to browse recipes by meal type (breakfast/lunch/dinner) so that I can find recipes appropriate for that time of day.

#### Search for Recipes
As a visitor, I want to search for recipes so that I can quickly find a specific dish or ingredient.

#### View Recipe Details
As a visitor, I want to view a recipe’s full details so that I can cook it successfully.

#### Create an Account
As a new user, I want to sign up so that I can post my own recipes, view and edit past recipes, and also add new recipes.

#### Responsive Browsing Experience
As a user, I want the app to work well on smaller screens so that I can browse recipes and use them in my kitchen where I can’t access my laptop.

---

## Benefits and Advantages

### Benefits for Visitors
- **Fast discovery** through a latest-recipes feed and meal-type entry points.
- **Clear, consistent recipe structure** that’s easy to follow while cooking.

### Benefits for Registered Users
- A simple way to **contribute recipes** and help grow a community collection.

### Why This Is Different
Instead of acting like a generic list of links, the app focuses on:
- structured recipe pages (ingredients + instructions),
- low-friction browsing by meal context,
- and community posting behind a clear authentication flow.

---

## Scope and Limitations

### In Scope
- Viewing latest recipes and opening full recipe pages.
- Browsing by meal type via dedicated navigation links.
- Account registration and login.
- Auth-protected recipe creation entry point (“New”).

### Known Limitations
- Advanced community features (e.g., comments/ratings/follows) are not included in the current scope.
- Editing and managing previously posted recipes may be limited depending on what’s implemented.
- Search depth (title-only vs ingredients vs filters) depends on the backend implementation.

---

## Future Enhancements

### Community & Personalization
- User profiles and “My Recipes”
- Edit/update previously posted recipes
- Favorites / saved recipes

### Discovery Improvements
- Tagging and richer filtering (cuisine, time, difficulty)
- More robust search (ingredients + partial matching)

### Cooking Experience Upgrades
- Servings scaling
- Print-friendly mode
- PWA/offline access for kitchen use

---

## Summary and Impact
This project exists to solve a practical problem: recipes are easy to find but often hard to **organize, rediscover, and follow while cooking**. The Community Sharing Recipe App addresses this by combining a **latest-recipes feed**, **meal-type browsing**, and **clear recipe detail pages**, while enabling registered users to **contribute recipes** through an authenticated flow. The result is a structured, community-driven recipe experience that reduces friction and helps users cook with confidence.

# Design

## Brand Colours
The app uses a clean, food-friendly colour palette that keeps the interface simple and readable while letting recipe content stand out. Colour is primarily used to support navigation, highlight key actions (like browsing categories or creating a recipe), and maintain a consistent visual identity across pages.

## Layout and Structure
The layout is designed for quick discovery and easy reading. Recipes are presented in a clear feed/card format for browsing, with dedicated pages for full recipe details. Navigation supports common user journeys (latest recipes, meal categories, search, authentication), and the structure prioritises scannability—especially for ingredients and step-by-step instructions.

### Overall Information Architecture
The site is organised around a small set of top-level pages that support the main user journeys. A persistent header navigation provides direct access to **Home**, **Recipes**, **New**, **Register**, and **Login**, with a **Search** control available across pages to encourage quick discovery. 

In terms of hierarchy, the experience flows from **discovery** (Home/Recipes) → **selection** (Recipe list) → **execution** (Recipe detail) → **contribution** (Register/Login → New recipe).

---

### Key Pages and Their Structure

#### Home (Discovery + Direction)
The Home page acts as a “starting hub” with a clear headline and a primary call-to-action (“Browse recipes”), immediately steering users into discovery. It also includes a **Browse By Meal Type** section with three prominent options (Breakfast, Lunch, Dinner) to help users jump straight to context-based browsing without extra clicks.

#### Recipes (Latest Feed)
The Recipes page is structured as a **latest-recipes feed**, presenting multiple recipe entries together so visitors can scan quickly and choose what interests them. Beneath the feed, there’s a clear prompt encouraging visitors to register (“Register to Share Yours”), which supports the transition from browsing to contributing.

#### Meal Type Views (Breakfast/Lunch/Dinner)
Meal-type navigation routes users to filtered recipe views using a query parameter (e.g., `?meal_type=breakfast`). This keeps the browsing model consistent—users still view recipes in the same list structure—but with the intent narrowed to the meal category they selected. 

##### Recipe Detail (Cooking Mode)
Each recipe has a dedicated detail page that prioritises cooking clarity. The content is presented with a clear hierarchy:
- Title + author/date metadata
- Short description
- Key metadata (e.g., calories, cuisine)
- **Ingredients** section
- **Instructions** section  
This structure reduces cognitive load while cooking by separating “what you need” (ingredients) from “what you do” (instructions).

##### Authentication + Protected Actions
Account creation and sign-in live on dedicated pages (Register/Login). Importantly, the **New** navigation item is protected: if a user attempts to access recipe creation without being authenticated, they are redirected to the sign-in page with a “next” destination so they can return to the creation flow after logging in. 

---

### How the Layout Answers the User Stories

#### 1) View latest recipes
The **Recipes** page is explicitly labelled “Latest Recipes” and presents recipes in a scannable list/card format, enabling fast browsing and quick selection from multiple options. 

#### 2) Browse recipes by meal type
The Home page includes a dedicated **Browse By Meal Type** section with clear category entry points (Breakfast/Lunch/Dinner). These links route users into a filtered recipe list, supporting the “time-of-day” decision process without requiring a search.

#### 3) Search for recipes
Search is placed in the global header area and appears across pages, making it available at the exact moment a user switches from “explore” to “find something specific.” This placement supports quick, repeated searching without forcing users to return to a single “search page.” 

#### 4) View a recipe’s details
From the Recipes feed, each recipe title links to a dedicated detail page. The detail layout is intentionally broken into **Ingredients** and **Instructions** sections, which aligns with how users follow recipes in real life and makes the page usable as a cooking checklist. 

#### 5) Create an account
Registration and login are first-class navigation items, making account creation easy to find. The Recipes page also reinforces this by prompting visitors to sign up to share recipes, creating a clear conversion path from reader → contributor.

#### 6) Responsive browsing experience
The site’s structure is content-first and modular (hero → category tiles → lists → detail sections), which adapts well to smaller screens by naturally stacking into a single-column reading flow. The most important cooking content (ingredients/instructions) is separated into clear blocks, supporting quick scrolling and “glance-and-cook” use on a phone in the kitchen. 


## Wireframes
Wireframes were used to plan the core screens and user flow before implementation, focusing on essential interactions. This ensured the UI remained consistent, user-focused, and responsive across device sizes.

# Security features considered

## Secret management and environment-based configuration

### Secret key from environment
- `SECRET_KEY` is loaded from an environment variable instead of being hardcoded in the repo:
  ```python
  SECRET_KEY = os.environ.get("SECRET_KEY")
Why it matters: Prevents accidental exposure of a critical secret in GitHub and supports different keys per environment (local vs production).

### Debug controlled by environment
DEBUG is controlled by an environment variable:

python code
DEBUG = os.environ.get("DEBUG", "False") == "True"
Why it matters: Helps ensure production can run with DEBUG=False thi is important because debug pages can leak settings, stack traces, and sensitive info.

## Host header protection
Restricted allowed hosts
ALLOWED_HOSTS is restricted to Heroku domain and local development hosts:

python
ALLOWED_HOSTS = [".herokuapp.com", "127.0.0.1", "our-recipe-app-...herokuapp.com"]
Why it matters: Protects against Host header attacks by preventing Django from serving requests for unexpected domains.

## CSRF protection for forms and admin actions
CSRF middleware enabled
Django’s CSRF middleware is enabled:

python
"django.middleware.csrf.CsrfViewMiddleware"
Why it matters: Blocks cross-site request forgery attempts on POST requests including recipe creation/editing/deleting and Django admin actions.

Trusted origins configured for Heroku
Trusted origins are configured for Heroku:

python
CSRF_TRUSTED_ORIGINS = [
    "https://our-recipe-app-...herokuapp.com",
    "https://*.herokuapp.com",
]
Why it matters: Essential behind a reverse proxy like Heroku so CSRF validation works correctly and requests only from trusted HTTPS origins are accepted.

## Secure deployment behind Heroku’s HTTPS proxy
Proxy SSL header set

python
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
Why it matters: Tells Django to treat requests as HTTPS when Heroku terminates SSL upstream. Helps CSRF and session/cookie behavior stay correct in production.

## Authentication and password security
Using Django auth + allauth
Django’s auth system + allauth used (django.contrib.auth, allauth, allauth.account, etc.).

Why it matters: Provides robust-tested login/session management rather than custom auth.

### Default password validators enabled
Keeps Django’s default password validators:

### similarity check

minimum length

common password check

numeric password check

Why it matters: Reduces weak-password risk significantly.

### Account configuration
Account setup:

python
ACCOUNT_LOGIN_METHODS = {"username", "email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]
ACCOUNT_EMAIL_VERIFICATION = "none"
Why it matters: Provides structured signup fields and uses Django’s password confirmation flow.

## Access control and authorization
View-level protections
App patterns (Create/Update/Delete views + mixins):

- LoginRequiredMixin protects pages like adding/editing/deleting recipes so anonymous users can’t modify data.

- UserPassesTestMixin ensures only the owner of a recipe can edit/delete it (prevents users changing or removing other users’ content).

- handle unauthorized access with a clear 403-style page message.

## Database and data security separation
Production DB via environment variable
Production uses PostgreSQL via DATABASE_URL and dj_database_url.parse(...):

python
if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
Why it matters: Credentials are not stored in code, only in environment variables.

## Static/media storage and file-handling considerations
S3 storage via django-storages
Static and media are stored on S3 via django-storages, with AWS credentials pulled from environment variables.

Why it matters: Keeps files off the ephemeral Heroku filesystem and controls access policies at the bucket level.

## Logging (operational security)
Console logging to Heroku logs
Logging config routes errors to console (Heroku logs).

Why it matters: Helps detect issues quickly without exposing stack traces to users (as long as DEBUG=False in production).

# Deployment to Heroku (Django + Postgres + S3)

## Pre-deployment checks (local)

Activate venv and confirm the project runs locally:

python manage.py check
python manage.py makemigrations --check
python manage.py migrate
python manage.py runserver

Check to ensure a single requirements.txt at the project root is present.

## Install production dependencies

### Install Gunicorn (Heroku web server):
pip install gunicorn~=20.1

### Freeze requirements:
pip freeze > requirements.txt

### Commit the changes:
git add requirements.txt
git commit -m "chore(deploy): add production dependencies"

## Create the Procfile

At the project root (no extension), create Procfile containing:
web: gunicorn main.wsgi:application


Commit:
git add Procfile
git commit -m "chore(deploy): add Procfile for gunicorn"

## Create the Heroku app and connect Git remote

- Create the Heroku app from the dashboard.

- Add the Heroku remote:
heroku git:remote -a recipe-blog

- Check remotes:
git remote -v

## Configure settings.py for production
A) ALLOWED_HOSTS

Add Heroku domain:

ALLOWED_HOSTS = [
  ".herokuapp.com",
  "127.0.0.1",
  "recipe-blog.herokuapp.com",
]

B) Proxy/HTTPS + CSRF config

For Heroku HTTPS:

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_TRUSTED_ORIGINS = [
  "https://recipe-blog.herokuapp.com",
  "https://*.herokuapp.com",
]

C) Database (Postgres)
import dj_database_url

if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

D) DEBUG controlled by env var
DEBUG = os.environ.get("DEBUG", "False") == "True"

Commit:
git add main/settings.py
git commit -m "chore(deploy): configure settings for Heroku"

## Add Heroku config vars (environment variables)

In the Heroku dashboard → Settings → Config Vars add:

SECRET_KEY = your Django secret key
DEBUG = False (production)
(Later) USE_AWS, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

## Add Postgres to Heroku

Create a Postgres addon:
heroku addons:create heroku-postgresql:essential-0 -a recipe-blog
Verify:
heroku config -a recipe-blog

## Deploy to Heroku

Push code:
git push heroku main

To update GitHub:
git push origin main

## Run migrations on Heroku
heroku run -a recipe-app -- python manage.py migrate

## Configure S3 for static + media (storages)
### Install dependencies
pip install django-storages boto3
pip freeze > requirements.txt
git add requirements.txt
git commit 

### Add storages to INSTALLED_APPS
INSTALLED_APPS += ["storages"]

### Add S3 storage settings
AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME
AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY from env vars
STATICFILES_LOCATION = "static"
MEDIAFILES_LOCATION = "media"
STORAGES mapping for default and staticfiles

### Add Heroku config vars for AWS
heroku config:set USE_AWS=True -a recipe-blog
heroku config:set AWS_ACCESS_KEY_ID="..." -a recipe-blog
heroku config:set AWS_SECRET_ACCESS_KEY="..." -a recipe-blog

## Collect static to S3

After deployment:
heroku run -a recipe-blog -- python manage.py collectstatic --noinput

## Open the app + monitor logs
Open:
heroku open -recipe-blog



