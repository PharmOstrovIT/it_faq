CREATE TABLE public.apteka
(
    id serial NOT NULL,
    name varchar(12) NOT NULL,
    region varchar(200) NOT NULL,
    city_name varchar(200) NOT NULL,
    address varchar(200) NOT NULL,
    phone varchar(200) NOT NULL,
    mobile_phone varchar(200) NOT NULL,
    organization varchar(200) NOT NULL,
    PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.apteka
    OWNER to postgres;