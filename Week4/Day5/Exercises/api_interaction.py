import requests


def get_github_user_info(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None


if __name__ == "__main__":
    username = 'your_github_username'
    user_info = get_github_user_info(username)
    if user_info:
        print(f"GitHub User Info for {username}:")
        print(f"Name: {user_info['name']}")
        print(f"Public Repositories: {user_info['public_repos']}")
        print(f"Followers: {user_info['followers']}")
        print(f"Following: {user_info['following']}")
