# RentEasy

Welcome to RentEasy, an innovative rental property marketplace designed to streamline the experience for both landlords and renters. RentEasy combines a user-friendly interface with powerful functionality to simplify the process of finding, listing, and managing rental properties.

## Key Features

- **User Registration and Authentication:** Secure sign-up and login functionality for users.
Property Listings Management:** Admins can list properties, and planned features allow hosts to manage their own listings.
- **Advanced Search and Filtering:** Helps users find properties matching their needs.
- **Inquiry and Messaging System:** Allows communication between renters and property managers or hosts.
- **Personalized User Dashboards:** Custom dashboards for renters, hosts, and admins (planned feature).
- **Payment Integration:** Future support for transactions through PayPal and Stripe.
- **Mobile Responsiveness:** Ensures a seamless experience across all devices.

## Technologies Used

- **Frontend:** HTML5, CSS3, TailwindCSS, DaisyUI, JavaScript, AlpineJS
- **Backend:** Django 6.0.2
- **Database:** PostgreSQL
- **Hosting/Deployment:** Railway
- **Version Control:** Git and GitHub
- **Additional Tools:** WhiteNoise for static files, Gunicorn as the HTTP server

## Getting Started

### Prerequisites

Before setting up the project, ensure you have the following installed:

- **Prerequisites:** Python 3.13 or above
- pip (Python package installer)
- Git

### Installation

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/renteasy.git
    cd renteasy
    ```
2. Set up a Python virtual environment (optional but recommended)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install required Python packages
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the PostgreSQL database
    - Ensure PostgreSQL is installed and running on your machine.
    - Create a new database named renteasy.
    - Update the DATABASES configuration in your settings.py to point to your database.
5. Perform database migrations
    ```bash
    python manage.py migrate
    ```
6. Collect static files (if in production)
    ```bash
    python manage.py collectstatic
    ```
7. Create an admin user
    ```bash
    python manage.py createsuperuser
    ```
8. Run the server
    ```bash
    python manage.py runserver
    ```
9. Visit http://127.0.0.1:8000 in your web browser.

## Contributing

We welcome contributions to RentEasy! If you want to contribute, please follow the standard fork-and-pull request workflow. If you plan to propose a major change, please discuss it via an issue first.

## License

This project is licensed under the MIT License.

## Support

For support, email contact@renteasy.com or open an issue on the GitHub repository.
