-- create table
CREATE TABLE cpu_usage."kafka_consumer"
(
    cpu_usage_percent                    NUMERIC                        NOT NULL,
    virtual_memory_usage_percent         NUMERIC                        NOT NULL,
    virtual_memory_usage_available_bytes BIGINT                         NOT NULL,
    virtual_memory_usage_used_bytes      BIGINT                         NOT NULL,
    swap_memory_usage_percent            NUMERIC                        NOT NULL,
    swap_memory_usage_free_bytes         BIGINT                         NOT NULL,
    swap_memory_usage_used_bytes         BIGINT                         NOT NULL,
    modified_timestamp                   TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    computer_user                        VARCHAR(255)                   NOT NULL
);
