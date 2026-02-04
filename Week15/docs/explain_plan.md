EXPLAIN ANALYZE
SELECT id, name, email
FROM users
WHERE name ILIKE '%john%'
ORDER BY created_at DESC
LIMIT 10;

Result:
- Index Scan using idx_users_created_at
- Execution Time: reduced from 120ms → 8ms
