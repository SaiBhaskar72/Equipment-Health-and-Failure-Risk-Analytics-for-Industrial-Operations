-- ============================================================
-- Predictive Maintenance Analytics
-- Basic SQL Failure Analysis
-- ============================================================

USE predictive_maintenance;


-- ------------------------------------------------------------
-- 1. Check total number of observations
-- ------------------------------------------------------------

SELECT
    COUNT(*) AS total_observations
FROM equipment_data;


-- ------------------------------------------------------------
-- 2. Count failure and non-failure observations
-- ------------------------------------------------------------

SELECT
    `Machine failure`,
    COUNT(*) AS observations
FROM equipment_data
GROUP BY `Machine failure`;


-- ------------------------------------------------------------
-- 3. Overall failure rate
-- ------------------------------------------------------------

SELECT
    COUNT(*) AS total_observations,
    SUM(`Machine failure`) AS failures,
    ROUND(
        AVG(`Machine failure`) * 100,
        2
    ) AS failure_rate_percent
FROM equipment_data;


-- ------------------------------------------------------------
-- 4. Failure rate by product type
-- ------------------------------------------------------------

SELECT
    `Type`,
    COUNT(*) AS observations,
    SUM(`Machine failure`) AS failures,
    ROUND(
        AVG(`Machine failure`) * 100,
        2
    ) AS failure_rate_percent
FROM equipment_data
GROUP BY `Type`
ORDER BY failure_rate_percent DESC;


-- ------------------------------------------------------------
-- 5. Average operating conditions by failure outcome
-- ------------------------------------------------------------

SELECT
    `Machine failure`,
    COUNT(*) AS observations,
    ROUND(AVG(`Torque [Nm]`), 2) AS avg_torque,
    ROUND(
        AVG(`Rotational speed [rpm]`),
        2
    ) AS avg_speed,
    ROUND(
        AVG(`Tool wear [min]`),
        2
    ) AS avg_tool_wear
FROM equipment_data
GROUP BY `Machine failure`;


-- ------------------------------------------------------------
-- 6. Average temperature conditions by failure outcome
-- ------------------------------------------------------------

SELECT
    `Machine failure`,
    ROUND(
        AVG(`Air temperature [K]`),
        2
    ) AS avg_air_temperature,
    ROUND(
        AVG(`Process temperature [K]`),
        2
    ) AS avg_process_temperature,
    ROUND(
        AVG(
            `Process temperature [K]`
            - `Air temperature [K]`
        ),
        2
    ) AS avg_temperature_difference
FROM equipment_data
GROUP BY `Machine failure`;


-- ------------------------------------------------------------
-- 7. Failure-mode counts
-- ------------------------------------------------------------

SELECT
    SUM(TWF) AS tool_wear_failures,
    SUM(HDF) AS heat_dissipation_failures,
    SUM(PWF) AS power_failures,
    SUM(OSF) AS overstrain_failures,
    SUM(RNF) AS random_failures
FROM equipment_data;


-- ------------------------------------------------------------
-- 8. Check label disagreements
-- ------------------------------------------------------------

SELECT
    COUNT(*) AS disagreement_count
FROM equipment_data
WHERE
    (
        `Machine failure` = 0
        AND (TWF + HDF + PWF + OSF + RNF) > 0
    )
    OR
    (
        `Machine failure` = 1
        AND (TWF + HDF + PWF + OSF + RNF) = 0
    );


-- ------------------------------------------------------------
-- 9. View disagreement records
-- ------------------------------------------------------------

SELECT
    UDI,
    `Product ID`,
    `Machine failure`,
    TWF,
    HDF,
    PWF,
    OSF,
    RNF
FROM equipment_data
WHERE
    (
        `Machine failure` = 0
        AND (TWF + HDF + PWF + OSF + RNF) > 0
    )
    OR
    (
        `Machine failure` = 1
        AND (TWF + HDF + PWF + OSF + RNF) = 0
    )
ORDER BY UDI;