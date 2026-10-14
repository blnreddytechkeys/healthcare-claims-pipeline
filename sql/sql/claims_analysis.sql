-- Total claims by status
SELECT status, COUNT(*) AS total_claims, SUM(claim_amount) AS total_amount
FROM claims
GROUP BY status
ORDER BY total_amount DESC;

-- High value claims
SELECT claim_id, member_id, claim_amount, status
FROM claims
WHERE claim_amount > 400
ORDER BY claim_amount DESC;

-- Claims by provider
SELECT provider_id, COUNT(*) AS claim_count, AVG(claim_amount) AS avg_amount
FROM claims
GROUP BY provider_id
ORDER BY claim_count DESC;