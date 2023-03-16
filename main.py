'''
How to make a website with Python, covering Flask, authentication and database
- Link: https://www.typingdna.com/authentication-api.html
'''

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)