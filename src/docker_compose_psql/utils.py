import random
import string


def generate_random_user_data() -> tuple[str, str]:
    """
    Generate random user data consisting of a name and an email address.

    The function creates a random name by selecting 8 random ASCII letters
    and generates an email address using the random name in the format
    '<random_name>@example.com'.

    Returns:
      tuple: A tuple containing:
        - random_name (str): A randomly generated string of 8 ASCII letters.
        - random_email (str): A randomly generated email address based on the random name.
    """
    random_name = "".join(random.choices(string.ascii_letters, k=8))
    random_email = f"{random_name.lower()}@example.com"
    return (random_name, random_email)
