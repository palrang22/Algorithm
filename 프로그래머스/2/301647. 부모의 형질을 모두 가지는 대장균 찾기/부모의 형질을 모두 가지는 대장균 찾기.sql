-- 코드를 작성해주세요
SELECT EDA.ID, EDA.GENOTYPE, EDB.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA EDA
JOIN ECOLI_DATA EDB
ON EDA.PARENT_ID = EDB.ID
WHERE EDA.GENOTYPE & EDB.GENOTYPE = EDB.GENOTYPE
ORDER BY ID;
