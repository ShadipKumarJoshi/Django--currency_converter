![alt text](image.png)
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

# Install Django and requests
pip install django requests

# Install all requirements
pip install -r requirements.txt

# Run
py manage.py runserver

- Tailwind should be properly configured in `settings.py` using [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/).


## Environment Variables

This project uses an [ExchangerateAPI](https://app.exchangerate-api.com/) API key. To run the project, create a `.env` file in the root directory and add the following:

EXCHANGE_API="your_actual_api_key_here"
