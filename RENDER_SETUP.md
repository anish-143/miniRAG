# DEPLOYMENT GUIDE FOR RENDER

## Environment Variables to Set in Render Dashboard

Copy these environment variables to your Render service settings:

```
QDRANT_URL=<your_qdrant_url>
QDRANT_API_KEY=<your_qdrant_api_key>
QDRANT_COLLECTION=policylens_chunks
GROQ_API_KEY=<your_groq_api_key>
DEPLOYMENT_MODE=lite
```

## Important Notes

- Set `DEPLOYMENT_MODE=lite` for Render deployment to avoid memory issues
- Never commit actual API keys to the repository
- Use Render's environment variables dashboard to set these values
- The Procfile is already configured for deployment
