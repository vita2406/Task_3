import time
import uuid
import requests

from data import API_URL, TEST_NAME, TEST_PASSWORD


class UserAPI:

    @staticmethod
    def _post(url, payload, retries=3):
        last_error = None

        for attempt in range(retries):
            try:
                response = requests.post(
                    url,
                    json=payload,
                    timeout=15
                )

                response.raise_for_status()
                return response

            except requests.RequestException as e:
                last_error = e
                print(f"Attempt {attempt + 1} failed: {e}")

                if attempt < retries - 1:
                    time.sleep(2)

        raise last_error

    @staticmethod
    def create_user():
        email = f"{uuid.uuid4()}@yandex.ru"

        payload = {
            "email": email,
            "password": TEST_PASSWORD,
            "name": TEST_NAME
        }

        print("REGISTER")

        response = UserAPI._post(
            f"{API_URL}/auth/register",
            payload
        )

        print(response.status_code)
        print(response.text)

        print("\nLOGIN")

        login = UserAPI._post(
            f"{API_URL}/auth/login",
            {
                "email": email,
                "password": TEST_PASSWORD
            }
        )

        print(login.status_code)
        print(login.text)

        data = login.json()

        return {
            "email": email,
            "password": TEST_PASSWORD,
            "name": TEST_NAME,
            "access_token": data["accessToken"],
            "refresh_token": data["refreshToken"]
        }

    @staticmethod
    def delete_user(access_token):
        requests.delete(
            f"{API_URL}/auth/user",
            headers={
                "Authorization": access_token
            },
            timeout=15
        )