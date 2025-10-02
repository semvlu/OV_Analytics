-- Back-end to read parquet files and DB for OLAP
-- Front-end @ api/GraphQL: Read

-- Enter ClickHouse CLI: docker exec -it warehouse clickhouse-client

DESCRIBE TABLE file(`warehouse/*.parquet`, Parquet);

SELECT COUNT(*) AS count
FROM file(`warehouse/*.parquet`, Parquet);


CREATE TABLE buses
ENGINE = MergeTree
ORDER BY tuple() AS
SELECT *
FROM file('warehouse/*.parquet', Parquet);

-- Init
CREATE DATABASE IF NOT EXISTS kv6;
ENGINE = Atomic;

USE kv6;


SETTINGS allow_nullable_key = 1;


-- UPSERT: EGNINE = ReplacingMergeTree(journeynumber)

-- Grant API access
CREATE USER api IDENTIFIED WITH plaintext_password BY 'password'

GRANT ALL ON <database>.* TO api