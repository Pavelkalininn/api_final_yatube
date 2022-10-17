# yatube_project

«Social network of bloggers»

## Description

Thanks to this project, bloggers can communicate.

## Technologies

    Python 3.7 Django 2.2.19

## Dev-mode run

Install dependencies from the file requirements.txt

    pip install -r requirements.txt

In the file folder manage.py run the command:

    python manage.py runserver

## Request examples

To get an authorization token, follow the link
    
    POST..../api/v1/jwt/create/
    
    {
    "username": "string",
    "password": "string"
    }
    
To update the authorization token, follow the link
    
    POST..../api/v1/jwt/refresh/
    
    {
    "refresh": "string"
    }
    
You can check the token by following the link
    
    POST..../api/v1/jwt/verify/
    
    {
    "token": "string"
    }

The API itself is available at

    GET..../api/v1/

Examples of API requests:

Example of a POST request with Anton Chekhov token: adding a new post:

    POST .../api/v1/posts/

    {
    "text": "Some text",
    "group": 1
    } 

Answer:
    
    {
    "id": 14,
    "text": "Some text",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
    } 

Example of a POST request with Anton Chekhov token: we send a new comment to the post with id=14.

    POST .../api/v1/posts/14/comments/

    {
    "text": "test test"
    }
Answer:

    {
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "test test",
    "created": "2021-06-01T10:14:51.388932Z"
    }

Example of a GET request with Anton Chekhov token: getting information about the group.

    GET .../api/v1/groups/2/
    
Answer:

    {
    "id": 2,
    "title": "Mathematic",
    "slug": "math",
    "description": "Math posts"
    }
    
Example of a GET request with a token to get a list of your own subscriptions.

    GET .../api/v1/follow/
    
Answer:

    [
        {
            "user": "string",
            "following": "string"
        }
    ]
    
You can subscribe to the author by passing his username in a POST request to:

POST .../api/v1/follow/

    {
        "following": "string"
    }
    
The answer will be a dictionary with the user names of the subscriber and the subscriber:

    {
        "user": "string",
        "following": "string"
    }

Author __Pavel Kalinin__
