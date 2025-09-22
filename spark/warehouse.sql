-- Back-end to read parquet files and DB for OLAP
-- Front-end @ api/GraphQL: Read

DESCRIBE TABLE file(`./data/warehouse/*.parquet`, Parquet);

SELECT COUNT(*) AS count
FROM file(`./data/warehouse/*.parquet`, Parquet);




INSERT INTO sometable
FROM INFILE './data/warehouse/*.parquet' FORMAT Parquet;



-- Init
CREATE DATABASE IF NOT EXISTS kv6;
ENGINE = Atomic;

USE kv6;
CREATE TABLE IF NOT EXISTS bus
(
    `msg_type` String,
    `dataownercode` String,
    `vehiclenumber` String,
    `rd_x` Float64,
    `rd_y` Float64,
    `ts` DateTime,
    `lineplanningnumber` Int,
    `journeynumber` Int,
    `prev_rd_x` Float64,
    `prev_rd_y` Float64,
    `straight_line_distance` Float64
)
ENGINE = MergeTree()
