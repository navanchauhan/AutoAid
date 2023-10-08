# AutoAid

To auto-build the CSS files:

```
npm install
npx tailwindcss -i ./src/main.css -o ./static/main.css --watch
```

To run the Python code using Poetry

```
poetry install
poetry shell
python app.py
```

## Requirements

1. AWS Credentials with access to `anthropic.claude-instant-v1`
2. The `SERP_API_KEY` environment variable set
