SELECT
    id,     AS id,
    name    AS name,
    stock   AS stock
FROM 
    products
WHERE 
    stock < 3 
AND 
    producent = 'CompanyA'
ORDER BY 
    id
; 
