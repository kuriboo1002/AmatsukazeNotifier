# Discord Webhook でメッセージを送信する

import requests
class Discord:

    def __init__(self, webhook_url):
        """
        Initializes the Discord webhook sender.
        :param webhook_url: The Discord webhook URL.
        """
        self.webhook_url = webhook_url

    def send_message(self, message):
        """
        Sends a message to the Discord webhook.
        :param message: The text message to send.
        :return: A dictionary containing the response from Discord (usually JSON).
                 In case of network errors or non-JSON responses, a custom dict is returned.
        """
        
        payload_content = {'content': message}
        
        try:
            # Sending text-only (application/json)
            response = requests.post(self.webhook_url, json=payload_content)

            # Attempt to return JSON response.
            # Discord error responses are JSON. Successful (204 No Content) might not be.
            if response.content: # Check if there's any content in the response
                try:
                    return response.json()
                except requests.exceptions.JSONDecodeError:
                    # If response is not JSON but there's content (e.g. plain text error)
                    return {"status_code": response.status_code, "text": response.text}
            else:
                # For 204 No Content or other empty responses from successful requests
                return {"status_code": response.status_code, "message": "Request successful, no content returned."}

        except requests.exceptions.RequestException as e:
            # print(f"Error sending message to Discord: {e}")
            # Construct an error dictionary
            error_response = {"error": "RequestException", "message": str(e)}
            if e.response is not None:
                error_response["status_code"] = e.response.status_code
                try:
                    error_response["details"] = e.response.json() # If error response from Discord is JSON
                except requests.exceptions.JSONDecodeError:
                    error_response["details"] = e.response.text # If error response is not JSON
            return error_response
