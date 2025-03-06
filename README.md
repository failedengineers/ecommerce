# Ecommerce Developer Website

Welcome to the Ecommerce Developer Website!

## 🌐 Live Demo
[Visit the Website](https://ecommerce-of28.onrender.com/)

## 📌 Project Description
This is an ecommerce developer website built using **Django**. It showcases products and serves as a demonstration project to enhance backend development skills.

## 🔑 Features
- User Authentication (Sign Up, Login, Logout)
- Product Listing
- Product Detail View
- Cart Management
- Checkout Process
- Admin Panel for Product Management

## 🛠️ Technologies Used
- **Backend:** Django 4.x
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **Hosting:** Render

## ⚙️ Installation
### Prerequisites
- Python 3.10+
- Virtual Environment

### Setup Instructions
```bash
# Clone the repository
git clone https://github.com/failedengineers/ecommerce-developer-website.git

# Navigate to the project directory
cd ecommerce-developer-website

# Create Virtual Environment
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run Migrations
python manage.py migrate

# Start Development Server
python manage.py runserver
```

## 🔑 Environment Variables
Create a `.env` file in the root directory to store sensitive information like:
```
SECRET_KEY=your_secret_key
DEBUG=True
```

## 📌 Usage
- Visit the homepage to browse products.
- Sign up or log in to manage the cart.
- Admin panel available at `/admin` (requires admin credentials).

## 🎯 Future Improvements
- Payment Gateway Integration
- Search and Filtering Functionality
- User Reviews
- Email Notifications

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## 📄 License
This project is licensed under the MIT License.

---
### Connect with Me
- LinkedIn: [Kalash Gulati](https://in.linkedin.com/in/kalash-gulati-789815321)
- GitHub: [failedengineers](https://github.com/failedengineers)
