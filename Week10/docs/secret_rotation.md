# Secret Rotation Guidelines

## Best Practices
1. Store secrets only in environment variables or vaults
2. Rotate secrets every 60–90 days
3. Never commit secrets to Git
4. Use versioned secrets (v1, v2)
5. Deploy new secrets before revoking old ones
6. Restart services after rotation
