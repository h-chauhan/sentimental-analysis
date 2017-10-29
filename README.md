# Leave Me Alone - Sentimental Analysis API Service

## API Endpoint

```
leavemealone.tech
```

1. Get sentiment of a statement: POST `\api\is_harassing\`

Request Body
```
{
  "statement": "Hello, how are you?"
}
```

Response
```
{
  "is_harassing": false
}
```

2. Add statements to dataset: POST `\api\add_query\`

Request Body
```
{
  "statement": "Hello, how are you?",
  "is_harassing": false
}
```

Response: `201 CREATED`
