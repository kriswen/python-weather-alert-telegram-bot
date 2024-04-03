# Weather Alert Telegram Bot

This Python program sends weather alerts via Telegram based on OpenWeatherMap data.

## Setup

1. Install the required dependencies:

    ```bash
    pip install requests python-dotenv
    ```

2. Create a `.env` file in the root directory of the project and add your environment variables:

    ```plaintext
    TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
    TELEGRAM_CHAT_ID=<your_telegram_chat_id>
    OWM_API_KEY=<your_openweathermap_api_key>
    CITY_LATITUDE=<your_city_latitude>
    CITY_LONGITUDE=<your_city_longitude>
    ```

3. Run the `main.py` script to receive weather alerts.

## Description

This program fetches weather data from OpenWeatherMap and checks if there is any possibility of rain in the forecast. If rain is expected, it sends a notification via Telegram to remind the user to bring an umbrella.

## Usage

Run the `main.py` script:

```bash
python main.py
