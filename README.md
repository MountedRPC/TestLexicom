# Решение второго задания
Вариант 1: Использование подзапроса
```sql
UPDATE full_names
SET status = (
    SELECT status
    FROM short_names
    WHERE name || '.mp3' = full_names.name
)
WHERE EXISTS (
    SELECT 1
    FROM short_names
    WHERE name || '.mp3' = full_names.name
)
```

Вариант 2: Использование JOIN-запроса
```sql
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE full_names.name || '.mp3' = short_names.name
```

