/*
3. What are the most in-demand skills for my role?
4. What are the top skills based on salary for my role?
5. What are the most optimal skills to learn?
6. Optimal: High Demand and High Paying
*/

SELECT 
    COUNT(*) AS counts,
    skills
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE job_title_short = 'Data Analyst' AND
job_work_from_home = TRUE
GROUP BY skills
ORDER BY counts DESC 
LIMIT 8