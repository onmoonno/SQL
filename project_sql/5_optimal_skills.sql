/*
5. What are the most optimal skills to learn?
    Optimal: High Demand and High Paying
*/

WITH skills_analysis AS (
    SELECT 
        skills_job_dim.skill_id,
        skills_dim.skills,
        COUNT(*) AS counts,
        ROUND(AVG(salary_year_avg), 0) AS avg_salary
    FROM job_postings_fact
    INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
    INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
    WHERE job_title_short = 'Data Analyst' 
      AND salary_year_avg IS NOT NULL 
      AND job_work_from_home = TRUE
    GROUP BY skills_job_dim.skill_id, skills_dim.skills
)

SELECT
    skill_id,
    skills,
    counts,
    avg_salary
FROM
    skills_analysis
ORDER BY
    avg_salary DESC,
    counts DESC
LIMIT 25
    
